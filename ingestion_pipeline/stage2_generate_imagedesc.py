#!/usr/bin/env python3
"""
stage2_generate_imagedesc.py
----------------------------
STAGE 2: Generate structured descriptions for images extracted in stage 1.

Reads from stage1_out/ and writes vision_results.json in the same format expected
by stage3_assemble.py.

Examples:
    python stage2_generate_imagedesc.py --provider anthropic --input ./stage1_out --domain "stock trading"
    python stage2_generate_imagedesc.py --provider ollama --model llama3.2-vision:latest --input ./stage1_out

Provider notes:
    anthropic: Uses ANTHROPIC_API_KEY, or Anthropic Foundry env vars when no API key is present.
    ollama:    Uses a local Ollama server, default http://localhost:11434.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

if load_dotenv:
    load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))


SYSTEM_PROMPT = """You are a knowledge extraction specialist. Analyze images from
educational or technical documents and extract their knowledge content in structured form.
Respond with valid JSON only; no markdown fences, no preamble."""


DEFAULT_MODELS = {
    "ollama": "llama3.2-vision:latest",
    "gemma4": "gemma4:e4b",
    "gemini": "gemini-3.5-flash",
    "anthropic": "claude-sonnet-4-6",
}

VISION_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "knowledge_type": {
            "type": "string",
            "enum": ["chart", "diagram", "table", "equation", "illustration", "photograph", "other"],
        },
        "key_concepts": {"type": "array", "items": {"type": "string"}},
        "knowledge_claims": {"type": "array", "items": {"type": "string"}},
        "tags": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["title", "description", "knowledge_type", "key_concepts", "knowledge_claims", "tags"],
}

DEFAULT_CONTEXT_BLOCKS = 5
MAX_SURROUNDING_CONTEXT_CHARS = 1600


def build_prompt(domain_hint: str, surrounding_text: str) -> str:
    domain_clause = f"The document is about: {domain_hint}.\n\n" if domain_hint else ""
    context_clause = (
        f"Surrounding text from the document:\n```\n{surrounding_text[:MAX_SURROUNDING_CONTEXT_CHARS]}\n```\n\n"
        if surrounding_text.strip()
        else ""
    )
    return f"""{domain_clause}{context_clause}Analyze this image extracted from a technical PDF.

Return ONLY this JSON structure:
{{
  "title"            : "Short descriptive figure title",
  "description"      : "2-5 sentence description of what this image shows, for someone who cannot see it. Be specific about axes, labels, patterns, values visible.",
  "knowledge_type"   : "chart | diagram | table | equation | illustration | photograph | other",
  "key_concepts"     : ["concept 1", "concept 2"],
  "knowledge_claims" : ["Specific atomic fact or lesson this image conveys", "..."],
  "tags"             : ["#tag1", "#tag2"]
}}

Guidelines:
- key_concepts: 3-8 domain concepts illustrated (be specific to this image)
- knowledge_claims: 2-5 precise, atomic facts a reader should take away
- tags: 4-8 Obsidian hashtags for wiki linking
- Escape newline and tab characters inside string values.
- If the image is decorative with no knowledge value, set knowledge_type to "other" and knowledge_claims to []
- Return ONLY the JSON object. No explanation, no markdown, no extra text.
"""


def strip_markdown_fence(raw: str) -> str:
    raw = raw.strip()
    if not raw.startswith("```"):
        return raw
    parts = raw.split("```")
    if len(parts) < 3:
        return raw.strip("`").strip()
    fenced = parts[1].strip()
    if fenced.lower().startswith("json"):
        fenced = fenced[4:].strip()
    return fenced


def extract_json_object(raw: str) -> str:
    """Return the first balanced JSON object, tolerating preamble/epilogue text."""
    start = raw.find("{")
    if start < 0:
        return raw

    in_string = False
    escaped = False
    depth = 0

    for index in range(start, len(raw)):
        char = raw[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return raw[start:index + 1]

    return raw[start:].strip()


def remove_common_json_trailing_commas(raw: str) -> str:
    return re.sub(r",\s*([}\]])", r"\1", raw)


def strip_json_comments(raw: str) -> str:
    lines = []
    for line in raw.splitlines():
        if re.match(r"^\s*//", line):
            continue
        lines.append(re.sub(r"\s+//.*$", "", line))
    return "\n".join(lines)


def replace_python_literals(raw: str) -> str:
    replacements = {
        "None": "null",
        "True": "true",
        "False": "false",
    }
    for source, target in replacements.items():
        raw = re.sub(rf"(?<![A-Za-z0-9_\"'])\b{source}\b(?![A-Za-z0-9_\"'])", target, raw)
    return raw


def remove_array_placeholders(raw: str) -> str:
    raw = re.sub(r"(?<=\[)\s*\.\.\.\s*,?", "", raw)
    raw = re.sub(r",\s*\.\.\.\s*(?=[,\]])", "", raw)
    return raw


def quote_bare_array_tokens(raw: str) -> str:
    """Quote common unquoted array items emitted by local models, especially #tags."""
    token_pattern = r"#[A-Za-z0-9_./:-]+|[A-Za-z][A-Za-z0-9_./:-]*"
    return re.sub(
        rf"(?<=[\[,])(\s*)({token_pattern})(\s*)(?=[,\]])",
        lambda match: f'{match.group(1)}"{match.group(2)}"{match.group(3)}',
        raw,
    )


def quote_bare_object_values(raw: str) -> str:
    keys = "title|description|knowledge_type"
    return re.sub(
        rf'("(?:{keys})"\s*:\s*)([A-Za-z][A-Za-z0-9_ ./:-]*)(\s*[,}}])',
        lambda match: f'{match.group(1)}"{match.group(2).strip()}"{match.group(3)}',
        raw,
    )


def repair_common_json_model_errors(raw: str) -> str:
    repaired = strip_json_comments(raw)
    repaired = replace_python_literals(repaired)
    repaired = remove_array_placeholders(repaired)
    repaired = quote_bare_array_tokens(repaired)
    repaired = quote_bare_object_values(repaired)
    repaired = remove_common_json_trailing_commas(repaired)
    return repaired


def close_truncated_json(raw: str) -> str:
    """Best-effort recovery for model output cut off mid-string or before final braces."""
    stack: list[str] = []
    in_string = False
    escaped = False

    for char in raw:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char in "{[":
            stack.append("}" if char == "{" else "]")
        elif char in "}]":
            if stack and stack[-1] == char:
                stack.pop()

    repaired = raw.rstrip()
    if escaped:
        repaired += "\\"
    if in_string:
        repaired += '"'
    repaired = remove_common_json_trailing_commas(repaired)
    while stack:
        repaired += stack.pop()
    return repaired


def json_error_context(raw: str, exc: json.JSONDecodeError, radius: int = 100) -> str:
    start = max(0, exc.pos - radius)
    end = min(len(raw), exc.pos + radius)
    return raw[start:end].replace("\n", "\\n").replace("\r", "\\r")


def parse_json_response(raw: str) -> dict[str, Any]:
    """Parse model JSON, tolerating common local-model formatting mistakes."""
    candidate = extract_json_object(strip_markdown_fence(raw))
    last_error: json.JSONDecodeError | None = None

    candidates = [
        candidate,
        remove_common_json_trailing_commas(candidate),
        repair_common_json_model_errors(candidate),
        close_truncated_json(repair_common_json_model_errors(candidate)),
    ]
    seen: set[str] = set()

    for candidate_variant in candidates:
        if candidate_variant in seen:
            continue
        seen.add(candidate_variant)
        try:
            return json.loads(candidate_variant, strict=False)
        except json.JSONDecodeError as exc:
            last_error = exc

    if last_error:
        context = json_error_context(candidate, last_error)
        raise json.JSONDecodeError(
            f"{last_error.msg}; nearby text: {context}",
            last_error.doc,
            last_error.pos,
        ) from last_error

    return json.loads(candidate, strict=False)


def get_image_media_type(image_path: Path) -> str:
    suffix = image_path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return "image/jpeg"
    if suffix == ".webp":
        return "image/webp"
    return "image/png"


def parse_page_from_image_filename(image_filename: str) -> int | None:
    """Parse page numbers from filenames like fig_p3_001.png."""
    for part in image_filename.split("_"):
        if part.startswith("p") and part[1:].isdigit():
            return int(part[1:])
    return None


def normalize_block_type(block: dict[str, Any]) -> str:
    block_type = block.get("type") or block.get("block_type")
    if block_type:
        return str(block_type)
    if block.get("filename"):
        return "image"
    return "text"


def bbox_position(block: dict[str, Any]) -> tuple[float, float]:
    bbox = block.get("bbox") or (0, 0, 0, 0)
    try:
        return float(bbox[1]), float(bbox[0])
    except (IndexError, TypeError, ValueError):
        return 0.0, 0.0


def looks_like_section_break(text: str) -> bool:
    """Heuristic section-heading detector for limiting image context."""
    text = re.sub(r"\s+", " ", text.strip())
    if not text or len(text) > 120:
        return False
    words = text.split()
    if len(words) > 14:
        return False
    if re.match(r"^(chapter|part|section|appendix)\b", text, re.IGNORECASE):
        return True
    if re.match(r"^\d+(\.\d+)*\s+\S+", text) and len(words) <= 12:
        return True
    letters = re.sub(r"[^A-Za-z]", "", text)
    if len(letters) >= 4 and text.upper() == text:
        return True
    if len(words) >= 2 and text == text.title() and not text.endswith((".", "?", "!")):
        return True
    return False


def build_ordered_context_blocks(text_blocks: list[dict[str, Any]], summary: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Build a document-level stream of text and image blocks.

    New stage-1 output contains image placeholders in text_blocks.json. For older
    output, insert virtual image blocks from extraction_result.json so nearby text
    still works without rerunning stage 1.
    """
    ordered_blocks: list[dict[str, Any]] = []
    image_names_in_text_blocks: set[str] = set()

    for page in text_blocks:
        page_num = page.get("page")
        for order, block in enumerate(page.get("blocks", [])):
            block_type = normalize_block_type(block)
            base = {
                "type": block_type,
                "page": page_num,
                "bbox": block.get("bbox") or (0, 0, 0, 0),
                "order": order,
            }
            if block_type == "image":
                filename = block.get("filename")
                if not filename:
                    continue
                image_names_in_text_blocks.add(filename)
                base["filename"] = filename
                ordered_blocks.append(base)
            else:
                text = block.get("text", "").strip()
                if not text:
                    continue
                base["text"] = text
                base["is_section_break"] = looks_like_section_break(text)
                ordered_blocks.append(base)

    next_order = len(ordered_blocks)
    for image in summary.get("images", []):
        filename = image.get("filename")
        if not filename or filename in image_names_in_text_blocks:
            continue
        ordered_blocks.append({
            "type": "image",
            "page": image.get("page") or parse_page_from_image_filename(filename),
            "bbox": image.get("bbox") or (0, 0, 0, 0),
            "filename": filename,
            "order": next_order,
        })
        next_order += 1

    def sort_key(block: dict[str, Any]) -> tuple[int, int, float, float, int]:
        page_num = block.get("page") or 0
        y_pos, x_pos = bbox_position(block)
        # Coarsen y slightly to match stage-1 reading order's tolerance.
        return int(page_num), round(y_pos / 10), y_pos, x_pos, int(block.get("order", 0))

    return sorted(ordered_blocks, key=sort_key)


def collect_previous_text(blocks: list[dict[str, Any]], image_index: int, limit: int) -> list[str]:
    collected: list[dict[str, Any]] = []
    text_count = 0

    for block in reversed(blocks[:image_index]):
        if block.get("type") != "text":
            continue
        collected.append(block)
        if block.get("is_section_break"):
            break
        text_count += 1
        if text_count >= limit:
            break

    return [block["text"] for block in reversed(collected)]


def collect_next_text(blocks: list[dict[str, Any]], image_index: int, limit: int) -> list[str]:
    collected: list[str] = []

    for block in blocks[image_index + 1:]:
        if block.get("type") != "text":
            continue
        if block.get("is_section_break"):
            break
        collected.append(block["text"])
        if len(collected) >= limit:
            break

    return collected


def get_surrounding_text(
    image_filename: str,
    text_blocks: list[dict[str, Any]],
    summary: dict[str, Any],
    context_blocks: int = DEFAULT_CONTEXT_BLOCKS,
) -> str:
    """Find nearby text before and after an image in document reading order."""
    context_blocks = max(0, context_blocks)
    blocks = build_ordered_context_blocks(text_blocks, summary)
    image_index = next(
        (
            index
            for index, block in enumerate(blocks)
            if block.get("type") == "image" and block.get("filename") == image_filename
        ),
        None,
    )

    if image_index is None:
        return ""

    previous_text = collect_previous_text(blocks, image_index, context_blocks)
    next_text = collect_next_text(blocks, image_index, context_blocks)

    sections = []
    if previous_text:
        sections.append("Previous nearby text:\n" + "\n".join(previous_text))
    if next_text:
        sections.append("Next nearby text:\n" + "\n".join(next_text))

    return "\n\n".join(sections)


def normalize_result(filename: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "filename": filename,
        "title": data.get("title", filename),
        "description": data.get("description", ""),
        "knowledge_type": data.get("knowledge_type", "other"),
        "key_concepts": data.get("key_concepts", []),
        "knowledge_claims": data.get("knowledge_claims", []),
        "tags": data.get("tags", []),
    }


def fallback_result(filename: str, reason: str) -> dict[str, Any]:
    return {
        "filename": filename,
        "title": filename,
        "description": f"Vision analysis failed: {reason}. Manual review needed.",
        "knowledge_type": "other",
        "key_concepts": [],
        "knowledge_claims": [],
        "tags": ["#needs-review"],
    }


def is_failed_result(result: Any) -> bool:
    if not isinstance(result, dict):
        return True
    description = str(result.get("description", "")).strip()
    if not description:
        return True
    if description.startswith("Vision analysis failed:"):
        return True
    tags = result.get("tags", [])
    return isinstance(tags, list) and "#needs-review" in tags


def pending_reason(filename: str, results: dict[str, Any]) -> str:
    if filename not in results:
        return "missing description"
    if is_failed_result(results[filename]):
        return "previous attempt failed"
    return "unknown"


def load_existing_results(vision_path: Path) -> dict[str, Any]:
    if not vision_path.exists():
        return {}
    try:
        data = json.loads(vision_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        print(f"[WARN] Existing vision_results.json could not be parsed: {exc}")
        print("       Starting with no previous image descriptions.")
        return {}
    if not isinstance(data, dict):
        print("[WARN] Existing vision_results.json is not a JSON object.")
        print("       Starting with no previous image descriptions.")
        return {}
    return data


def reconcile_existing_results(
    results: dict[str, Any],
    valid_filenames: set[str],
) -> tuple[dict[str, Any], list[str]]:
    stale_filenames = sorted(filename for filename in results if filename not in valid_filenames)
    if stale_filenames:
        results = {
            filename: result
            for filename, result in results.items()
            if filename in valid_filenames
        }
    return results, stale_filenames


def count_successful_results(results: dict[str, Any], image_files: list[Path]) -> int:
    return sum(
        1
        for image_path in image_files
        if image_path.name in results and not is_failed_result(results[image_path.name])
    )


def order_results_by_stage1(results: dict[str, Any], image_files: list[Path]) -> dict[str, Any]:
    ordered: dict[str, Any] = {}
    for image_path in image_files:
        if image_path.name in results:
            ordered[image_path.name] = results[image_path.name]
    return ordered


def save_results_atomic(vision_path: Path, results: dict[str, Any], image_files: list[Path]) -> None:
    vision_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = vision_path.with_name(f"{vision_path.name}.tmp")
    tmp_path.write_text(
        json.dumps(order_results_by_stage1(results, image_files), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    tmp_path.replace(vision_path)


def analyze_pending_image(
    provider: "ImageDescriptionProvider",
    image_path: Path,
    domain: str,
    surrounding_text: str,
) -> tuple[str, dict[str, Any], list[str]]:
    messages: list[str] = []

    try:
        data = provider.analyze_image(image_path, domain, surrounding_text)
        result = normalize_result(image_path.name, data)
        messages.append(f"       Type   : {result['knowledge_type']}")
        messages.append(f"       Title  : {result['title']}")
        messages.append(f"       Claims : {len(result['knowledge_claims'])} extracted")
        messages.append(f"       Tags   : {' '.join(result['tags'][:4])}")
        return image_path.name, result, messages

    except json.JSONDecodeError as exc:
        messages.append(f"       [WARN] JSON parse failed: {exc}")
        messages.append("              The model may have returned non-JSON text.")
        return image_path.name, fallback_result(image_path.name, "JSON parse error"), messages

    except Exception as exc:
        messages.append(f"       [ERROR] {exc}")
        return image_path.name, fallback_result(image_path.name, str(exc)), messages


class ImageDescriptionProvider(ABC):
    """Provider boundary for adding future vision backends."""

    name: str

    def __init__(self, model: str) -> None:
        self.model = model

    def prepare(self) -> None:
        """Optional startup validation for provider-specific dependencies."""

    @abstractmethod
    def analyze_image(self, image_path: Path, domain_hint: str, surrounding_text: str) -> dict[str, Any]:
        """Return a parsed JSON description for one image."""

    def display_model(self) -> str:
        return self.model


class AnthropicProvider(ImageDescriptionProvider):
    name = "anthropic"

    def __init__(self, model: str) -> None:
        super().__init__(model)
        self.client = None

    def prepare(self) -> None:
        try:
            from anthropic import Anthropic, AnthropicFoundry
            from azure.identity import DefaultAzureCredential, get_bearer_token_provider
        except ImportError as exc:
            raise RuntimeError(
                "Anthropic provider dependencies are missing. Install anthropic and azure-identity."
            ) from exc

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key:
            self.client = Anthropic(api_key=api_key)
            return

        base_url = os.environ.get("ANTHROPIC_FOUNDRY_BASE_URL")
        scope = os.environ.get("ANTHROPIC_AZURE_AD_SCOPE")
        if not base_url or not scope:
            raise RuntimeError(
                "Set ANTHROPIC_API_KEY, or set ANTHROPIC_FOUNDRY_BASE_URL and ANTHROPIC_AZURE_AD_SCOPE."
            )

        token_provider = get_bearer_token_provider(DefaultAzureCredential(), scope)
        self.client = AnthropicFoundry(
            base_url=base_url,
            azure_ad_token_provider=token_provider,
        )

    def analyze_image(self, image_path: Path, domain_hint: str, surrounding_text: str) -> dict[str, Any]:
        image_bytes = image_path.read_bytes()
        image_b64 = base64.b64encode(image_bytes).decode()

        print(f"{image_path} surrounding text of ''{surrounding_text[:100]}''  to ''{surrounding_text[-100:]}''")    

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": get_image_media_type(image_path),
                                "data": image_b64,
                            },
                        },
                        {
                            "type": "text",
                            "text": build_prompt(domain_hint, surrounding_text),
                        },
                    ],
                }
            ],
        )

        raw = response.content[0].text
        return parse_json_response(raw)


class OllamaProvider(ImageDescriptionProvider):
    name = "ollama"

    def __init__(self, model: str, host: str) -> None:
        super().__init__(model)
        self.host = host.rstrip("/")

    def prepare(self) -> None:
        self._get_tags()
        self._warn_if_model_missing()

    def _get_tags(self) -> dict[str, Any]:
        try:
            req = urllib.request.Request(f"{self.host}/api/tags")
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Cannot reach Ollama at {self.host}. Start Ollama, then pull a vision model with: ollama pull {self.model}"
            ) from exc

    def _warn_if_model_missing(self) -> None:
        try:
            data = self._get_tags()
        except RuntimeError:
            raise
        except Exception:
            return

        available = [model.get("name", "") for model in data.get("models", [])]
        exact_match = self.model in available
        family_match = any(self.model.split(":", 1)[0] in model for model in available)
        if not exact_match and not family_match:
            print(f"\n[WARN] Model '{self.model}' not found locally.")
            print(f"       Available models: {available or '(none)'}")
            print(f"       Pull it with: ollama pull {self.model}")
            print("       Continuing anyway; Ollama may attempt to pull it on first use.\n")

    def analyze_image(self, image_path: Path, domain_hint: str, surrounding_text: str) -> dict[str, Any]:
        image_bytes = image_path.read_bytes()
        image_b64 = base64.b64encode(image_bytes).decode()

        print(f"{image_path} is has surrounding text of ''{surrounding_text[:100]}''  to ''{surrounding_text[-100:]}''")    


        full_prompt = f"{SYSTEM_PROMPT}\n\n{build_prompt(domain_hint, surrounding_text)}"

        payload = json.dumps(
            {
                "model": self.model,
                "prompt": full_prompt,
                "images": [image_b64],
                "format": "json",
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 2000,
                },
            }
        ).encode()

        req = urllib.request.Request(
            f"{self.host}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            body = exc.read().decode(errors="replace")
            raise RuntimeError(f"Ollama HTTP {exc.code}: {body}") from exc

        return parse_json_response(data.get("response", ""))

    def display_model(self) -> str:
        return f"{self.model} @ {self.host}"


class GeminiProvider(ImageDescriptionProvider):
    name = "gemini"

    def __init__(self, model: str) -> None:
        super().__init__(model)
        self.client = None
        self.types = None

    def prepare(self) -> None:
        try:
            from google import genai
            from google.genai import types
        except ImportError as exc:
            raise RuntimeError(
                "Gemini provider dependencies are missing. Install google-genai."
            ) from exc

        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key) if api_key else genai.Client()
        self.types = types

    def analyze_image(self, image_path: Path, domain_hint: str, surrounding_text: str) -> dict[str, Any]:
        image_bytes = image_path.read_bytes()
        prompt = f"{SYSTEM_PROMPT}\n\n{build_prompt(domain_hint, surrounding_text)}"

        image_part = self.types.Part.from_bytes(
            data=image_bytes,
            mime_type=get_image_media_type(image_path),
        )

        response = self.client.models.generate_content(
            model=self.model,
            contents=[image_part, prompt],
            config={
                "response_mime_type": "application/json",
                "response_schema": VISION_RESULT_SCHEMA,
                "temperature": 0.1,
                "max_output_tokens": 2000,
            },
        )

        return parse_json_response(response.text or "")


def create_provider(provider_name: str, model: str | None, host: str) -> ImageDescriptionProvider:
    provider_model = model or DEFAULT_MODELS[provider_name]
    providers = {
        "anthropic": lambda: AnthropicProvider(provider_model),
        "ollama": lambda: OllamaProvider(provider_model, host),
        "gemma4": lambda: OllamaProvider(provider_model, host),
        "gemini": lambda: GeminiProvider(provider_model),
    }
    return providers[provider_name]()


def reconcile_image_metadata(summary_file: Path, images_dir: Path) -> tuple[dict[str, Any], list[str], list[str]]:
    """
    Treat images_dir as the manually reviewed source of truth.
    Remove extraction_result.json entries for images deleted after stage 1.
    """
    summary = json.loads(summary_file.read_text(encoding="utf-8"))
    image_entries = summary.get("images", [])
    existing_files = {path.name for path in images_dir.glob("*.png")}

    kept_entries = [entry for entry in image_entries if entry.get("filename") in existing_files]
    removed_files = [entry.get("filename", "") for entry in image_entries if entry.get("filename") not in existing_files]
    tracked_files = {entry.get("filename") for entry in kept_entries}
    untracked_files = sorted(existing_files - tracked_files)

    if removed_files:
        summary["images"] = kept_entries
        summary["total_images"] = len(kept_entries)
        summary_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    return summary, removed_files, untracked_files


def reconcile_text_block_image_refs(
    text_file: Path,
    text_blocks: list[dict[str, Any]],
    valid_image_filenames: set[str],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Remove image placeholder blocks for files deleted after stage 1."""
    stale_refs: list[str] = []
    changed = False

    for page in text_blocks:
        kept_blocks = []
        for block in page.get("blocks", []):
            if normalize_block_type(block) == "image":
                filename = block.get("filename")
                if not filename or filename not in valid_image_filenames:
                    if filename:
                        stale_refs.append(filename)
                    changed = True
                    continue
            kept_blocks.append(block)
        page["blocks"] = kept_blocks

    if changed:
        text_file.write_text(json.dumps(text_blocks, indent=2, ensure_ascii=False), encoding="utf-8")

    return text_blocks, stale_refs


def load_stage1_data(in_dir: Path) -> tuple[Path, list[dict[str, Any]], list[Path], dict[str, Any], list[str], list[str], list[str]]:
    images_dir = in_dir / "images"
    text_file = in_dir / "text_blocks.json"
    summary_file = in_dir / "extraction_result.json"

    for path in [in_dir, images_dir, text_file, summary_file]:
        if not path.exists():
            print(f"[ERROR] Not found: {path}")
            print("        Did you run stage1_extract.py first?")
            sys.exit(1)

    summary, removed_files, untracked_files = reconcile_image_metadata(summary_file, images_dir)
    text_blocks = json.loads(text_file.read_text(encoding="utf-8"))
    valid_image_filenames = {
        image.get("filename")
        for image in summary.get("images", [])
        if image.get("filename")
    }
    text_blocks, stale_text_refs = reconcile_text_block_image_refs(text_file, text_blocks, valid_image_filenames)
    image_files = [
        images_dir / image["filename"]
        for image in summary.get("images", [])
        if image.get("filename")
    ]

    return images_dir, text_blocks, image_files, summary, removed_files, untracked_files, stale_text_refs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stage 2: Generate image descriptions with a selectable vision provider"
    )
    parser.add_argument("--provider", choices=sorted(DEFAULT_MODELS), required=True, help="Vision provider to use")
    parser.add_argument("--input", default="./stage1_out", help="Stage 1 output folder")
    parser.add_argument("--output", default=None, help="Output folder (default: same as --input)")
    parser.add_argument("--domain", default="", help="Topic domain hint for sharper analysis")
    parser.add_argument("--model", default=None, help="Provider model name. Defaults depend on --provider.")
    parser.add_argument("--delay", type=float, default=None, help="Seconds between calls. Defaults depend on provider.")
    parser.add_argument("--parallel", type=int, default=3, help="Number of images to process in parallel (default: 3)")
    parser.add_argument("--host", default="http://localhost:11434", help="Ollama host URL")
    parser.add_argument(
        "--context-blocks",
        type=int,
        default=DEFAULT_CONTEXT_BLOCKS,
        help=f"Text blocks before/after each image to include as context (default: {DEFAULT_CONTEXT_BLOCKS})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    in_dir = Path(args.input)
    out_dir = Path(args.output) if args.output else in_dir
    delay = args.delay if args.delay is not None else (0.0 if args.provider == "ollama" else 0.5)
    parallel_workers = max(1, args.parallel)

    _, text_blocks, image_files, summary, removed_files, untracked_files, stale_text_refs = load_stage1_data(in_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    vision_path = out_dir / "vision_results.json"

    if removed_files:
        print(f"[INFO] Removed {len(removed_files)} deleted image reference(s) from extraction_result.json.")
        for filename in removed_files[:10]:
            print(f"       Skipped deleted image: {filename}")
        if len(removed_files) > 10:
            print(f"       ...and {len(removed_files) - 10} more")

    if stale_text_refs:
        print(f"[INFO] Removed {len(stale_text_refs)} deleted image block(s) from text_blocks.json.")

    if untracked_files:
        print(f"[WARN] Found {len(untracked_files)} PNG file(s) not listed in extraction_result.json.")
        print("       They will not be processed because stage 3 needs page metadata from extraction_result.json.")

    if not image_files:
        vision_path.write_text("{}", encoding="utf-8")
        print("[INFO] No remaining reviewed images found. Wrote empty vision_results.json.")
        print(f"       Check: {vision_path}")
        return

    valid_filenames = {image_path.name for image_path in image_files}
    results = load_existing_results(vision_path)
    results, stale_result_refs = reconcile_existing_results(results, valid_filenames)
    if stale_result_refs:
        print(f"[INFO] Removed {len(stale_result_refs)} stale image description(s) from vision_results.json.")

    pending_image_files = [
        image_path
        for image_path in image_files
        if image_path.name not in results or is_failed_result(results[image_path.name])
    ]
    already_described = count_successful_results(results, image_files)
    already_failed = len(image_files) - already_described
    skipped_image_files = [
        image_path
        for image_path in image_files
        if image_path.name in results and not is_failed_result(results[image_path.name])
    ]

    if results or stale_result_refs:
        save_results_atomic(vision_path, results, image_files)

    for image_path in skipped_image_files:
        print(f"[SKIP] {image_path.name} already has a description")

    if not pending_image_files:
        print(f"\n{'=' * 55}")
        print("  STAGE 2 - Image Description Generation")
        print(f"  Input:    {in_dir}")
        print(f"  Images:   {len(image_files)}")
        print(f"  Existing: {already_described} description(s)")
        print(f"{'=' * 55}")
        print("  Nothing to do; every image already has a description.")
        print(f"  Skipped existing descriptions: {already_described}")
        print(f"  Images with descriptions: {already_described}/{len(image_files)}")
        print(f"  Failed/missing images:     {already_failed}")
        print(f"  Check: {vision_path}")
        print(f"{'=' * 55}\n")
        return

    provider = create_provider(args.provider, args.model, args.host)

    try:
        provider.prepare()
    except Exception as exc:
        print(f"[ERROR] {exc}")
        sys.exit(1)

    print(f"\n{'=' * 55}")
    print("  STAGE 2 - Image Description Generation")
    print(f"  Provider: {provider.name}")
    print(f"  Input:    {in_dir}")
    print(f"  Images:   {len(image_files)}")
    print(f"  Existing: {already_described} description(s)")
    print(f"  Pending:  {len(pending_image_files)} image(s)")
    print(f"  Parallel: {parallel_workers} worker(s)")
    print(f"  Domain:   {args.domain or '(none)'}")
    print(f"  Model:    {provider.display_model()}")
    print(f"{'=' * 55}\n")

    total = len(pending_image_files)
    worker_count = min(parallel_workers, total)
    futures: dict[Future[tuple[str, dict[str, Any], list[str]]], tuple[int, Path]] = {}

    try:
        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            next_image_index = 0

            def submit_next_image() -> bool:
                nonlocal next_image_index
                if next_image_index >= total:
                    return False
                image_path = pending_image_files[next_image_index]
                index = next_image_index + 1
                next_image_index += 1
                reason = pending_reason(image_path.name, results)
                print(f"[PROCESS {index}/{total}] {image_path.name} - generating description ({reason})")

                surrounding = get_surrounding_text(image_path.name, text_blocks, summary, args.context_blocks)
                if surrounding:
                    print(f'       Context: "{surrounding[:80]}..."')

                future = executor.submit(analyze_pending_image, provider, image_path, args.domain, surrounding)
                futures[future] = (index, image_path)

                if next_image_index < total and delay > 0:
                    time.sleep(delay)
                return True

            for _ in range(worker_count):
                submit_next_image()

            while futures:
                completed_future = next(as_completed(list(futures)))
                index, image_path = futures.pop(completed_future)
                try:
                    filename, result, messages = completed_future.result()
                except Exception as exc:
                    filename = image_path.name
                    result = fallback_result(filename, f"worker error: {exc}")
                    messages = [f"       [ERROR] Worker failed: {exc}"]

                results[filename] = result
                status = "FAILED" if is_failed_result(result) else "DONE"
                print(f"[{status} {index}/{total}] {filename}")
                for message in messages:
                    print(message)
                save_results_atomic(vision_path, results, image_files)
                print()
                submit_next_image()

    except KeyboardInterrupt:
        for future in futures:
            future.cancel()
        save_results_atomic(vision_path, results, image_files)
        print("\n[INFO] Interrupted. Completed image descriptions have been saved.")
        sys.exit(130)

    described = count_successful_results(results, image_files)
    failed = len(image_files) - described

    print(f"{'=' * 55}")
    print(f"  Stage 2 done. {total} pending image(s) processed this run.")
    print(f"  Skipped existing descriptions: {already_described}")
    print(f"  Images with descriptions: {described}/{len(image_files)}")
    print(f"  Failed/missing images:     {failed}")
    print(f"  Check: {vision_path}")
    print("         Open this file and verify descriptions look correct.")
    print("         You can manually edit any entry before stage 3.")
    print("\n  Next step:")
    print(f'    python stage3_assemble.py --input {in_dir} --vault /path/to/vault --title "My Note"')
    print(f"{'=' * 55}\n")


if __name__ == "__main__":
    main()
