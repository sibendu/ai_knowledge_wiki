#!/usr/bin/env python3
"""
stage3_assemble.py
------------------
STAGE 3: Stitch text, images, and AI descriptions into an Obsidian note.

Reads:
  stage1_out/text_blocks.json        ← text content from stage 1
  stage1_out/extraction_result.json  ← page/image metadata from stage 1
  stage1_out/images/*.png            ← extracted images from stage 1
  stage1_out/vision_results.json     ← AI descriptions from stage 2

Writes:
  vault/notes/<title>.md             ← final Obsidian note
  vault/assets/<title>/*.png         ← images copied into vault

Run:
    python stage3_assemble.py --input ./stage1_out --vault ~/my-vault --title "My Book"

If you skipped stage 2 (no vision), it still works — images embed without descriptions.
"""

import sys
import json
import re
import shutil
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80]


def looks_like_heading(text: str) -> bool:
    if len(text) > 100 or "\n" in text:
        return False
    words = text.split()
    if len(words) < 2 or len(words) > 10:
        return False
    if text.upper() == text and text.replace(" ", "").isalpha():
        return True
    if text == text.title() and not text.endswith("."):
        return True
    return False


def render_text_block(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    if looks_like_heading(text):
        level = 2 if len(text) < 40 else 3
        return f"\n{'#' * level} {text}\n"
    return f"\n{text}\n"


def render_image_block(filename: str, slug: str, vision: dict) -> str:
    """
    Dual-track block:
      ![[vault-embed]]          ← for Obsidian to render visually
      > [!figure] callout       ← for LLM retrieval (description + claims + tags)
    """
    lines = [f"\n![[{slug}/{filename}]]\n"]

    if not vision:
        return "\n".join(lines)

    desc  = vision.get("description", "").strip()
    title = vision.get("title", filename).strip()
    claims = vision.get("knowledge_claims", [])
    tags   = vision.get("tags", [])
    ktype  = vision.get("knowledge_type", "")

    # Skip decorative images with no real knowledge content
    if ktype == "other" and not desc:
        return "\n".join(lines)

    lines.append("> [!figure]")
    lines.append(f"> **{title}**")

    if desc:
        lines.append(f">")
        lines.append(f"> {desc}")

    if claims:
        lines.append(f">")
        lines.append(f"> **Key insights:**")
        for claim in claims:
            lines.append(f"> - {claim}")

    if tags:
        lines.append(f">")
        lines.append(f"> {' '.join(tags)}")

    lines.append("")
    return "\n".join(lines)


def reconcile_stage1_images(summary: dict, summary_file: Path, images_dir: Path) -> tuple[dict, list[Path], list[str], list[str]]:
    """
    Treat images_dir as the reviewed source of truth.
    Remove stage-1 metadata entries for images deleted before assembly.
    """
    image_paths_by_name = {path.name: path for path in images_dir.glob("*.png")}
    kept_entries = []
    removed_files = []

    for image in summary.get("images", []):
        filename = image.get("filename")
        if filename in image_paths_by_name:
            kept_entries.append(image)
        else:
            removed_files.append(filename or "(missing filename)")

    kept_names = {image.get("filename") for image in kept_entries}
    untracked_files = sorted(set(image_paths_by_name) - kept_names)

    if removed_files:
        summary["images"] = kept_entries
        summary["total_images"] = len(kept_entries)
        summary_file.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    image_files = [image_paths_by_name[image["filename"]] for image in kept_entries]
    return summary, image_files, removed_files, untracked_files


def reconcile_vision_results(vision_results: dict, vision_file: Path, valid_filenames: set[str]) -> tuple[dict, list[str]]:
    """Remove stale descriptions for images no longer present in stage-1 metadata."""
    stale_filenames = sorted(filename for filename in vision_results if filename not in valid_filenames)
    if stale_filenames:
        vision_results = {
            filename: result
            for filename, result in vision_results.items()
            if filename in valid_filenames
        }
        vision_file.write_text(json.dumps(vision_results, indent=2, ensure_ascii=False), encoding="utf-8")
    return vision_results, stale_filenames


def build_frontmatter(title: str, summary: dict, vision_results: dict, domain: str, source_pdf: str) -> str:
    all_tags = set()
    for v in vision_results.values():
        for t in v.get("tags", []):
            all_tags.add(t.lstrip("#"))

    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f'source: "{source_pdf}"')
    lines.append(f'pages: {summary["total_pages"]}')
    lines.append(f'images_extracted: {summary["total_images"]}')
    if domain:
        lines.append(f'domain: "{domain}"')
    if all_tags:
        lines.append("tags:")
        for t in sorted(all_tags):
            lines.append(f"  - {t}")
    lines.append("---\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Stage 3: Assemble Obsidian note from extracted content")
    parser.add_argument("--input",  default="./stage1_out",   help="Folder containing stage 1 and 2 outputs")
    parser.add_argument("--vault",  required=True,            help="Obsidian vault root path")
    parser.add_argument("--title",  default=None,             help="Note title (default: source PDF name)")
    parser.add_argument("--domain", default="",               help="Domain hint (carried into frontmatter)")
    parser.add_argument("--notes-dir",  default="notes",      help="Notes subfolder in vault (default: notes)")
    parser.add_argument("--assets-dir", default="assets",     help="Assets subfolder in vault (default: assets)")
    args = parser.parse_args()

    in_dir     = Path(args.input)
    vault_root = Path(args.vault).expanduser().resolve()

    # ── Validate inputs ───────────────────────────────────────
    text_file    = in_dir / "text_blocks.json"
    summary_file = in_dir / "extraction_result.json"
    images_dir   = in_dir / "images"
    vision_file  = in_dir / "vision_results.json"

    for p in [text_file, summary_file, images_dir]:
        if not p.exists():
            print(f"[ERROR] Not found: {p}")
            print(f"        Did you run stage1_extract.py first?")
            sys.exit(1)

    if not vault_root.exists():
        print(f"[ERROR] Vault path does not exist: {vault_root}")
        sys.exit(1)

    # ── Load data ─────────────────────────────────────────────
    summary     = json.loads(summary_file.read_text(encoding="utf-8-sig"))
    text_blocks = json.loads(text_file.read_text(encoding="utf-8-sig"))   # list of {page, blocks:[{text,bbox}]}
    summary, png_files, removed_files, untracked_files = reconcile_stage1_images(summary, summary_file, images_dir)

    if removed_files:
        print(f"  [INFO] Removed {len(removed_files)} deleted image reference(s) from extraction_result.json")
        for filename in removed_files[:10]:
            print(f"         Skipped deleted image: {filename}")
        if len(removed_files) > 10:
            print(f"         ...and {len(removed_files) - 10} more")

    if untracked_files:
        print(f"  [WARN] Found {len(untracked_files)} PNG file(s) not listed in extraction_result.json")
        print(f"         These files will not be copied or embedded: {', '.join(untracked_files[:5])}")
        if len(untracked_files) > 5:
            print(f"         ...and {len(untracked_files) - 5} more")

    vision_results = {}
    if vision_file.exists():
        vision_results = json.loads(vision_file.read_text(encoding="utf-8-sig"))
        valid_filenames = {image["filename"] for image in summary.get("images", [])}
        vision_results, stale_vision = reconcile_vision_results(vision_results, vision_file, valid_filenames)
        if stale_vision:
            print(f"  [INFO] Removed {len(stale_vision)} stale image description(s) from vision_results.json")
        print(f"  Loaded vision_results.json  ({len(vision_results)} image descriptions)")
    else:
        print(f"  [INFO] No vision_results.json found — images will embed without descriptions")
        print(f"         (Run stage2_vision.py first if you want AI descriptions)")

    title = args.title or Path(summary["source_pdf"]).stem
    slug  = slugify(title)

    # ── Set up vault paths ────────────────────────────────────
    notes_dir  = vault_root / args.notes_dir
    assets_dir = vault_root / args.assets_dir / slug
    note_path  = notes_dir / f"{slug}.md"

    notes_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  STAGE 3 — Assemble")
    print(f"  Input:  {in_dir}")
    print(f"  Note:   {note_path}")
    print(f"  Assets: {assets_dir}")
    print(f"{'='*55}\n")

    # ── Copy images into vault ────────────────────────────────
    print("Copying images into vault...")
    for img_path in png_files:
        dest = assets_dir / img_path.name
        shutil.copy2(img_path, dest)
        print(f"  Copied: {img_path.name}")

    # ── Build a page → image map ──────────────────────────────
    # summary["images"] = [{filename, page, size_px, hash, bbox}, ...]
    page_to_images: dict[int, list[str]] = {}
    for img_meta in summary["images"]:
        pg = img_meta["page"]
        page_to_images.setdefault(pg, []).append(img_meta["filename"])

    # ── Assemble markdown ─────────────────────────────────────
    print("\nAssembling note...")
    lines = []

    # Frontmatter
    lines.append(build_frontmatter(title, summary, vision_results, args.domain, summary["source_pdf"]))

    # Title heading
    lines.append(f"# {title}\n")

    # Walk pages in order
    for page_data in text_blocks:
        page_num    = page_data["page"]
        text_blocks_on_page = page_data["blocks"]
        images_on_page      = page_to_images.get(page_num, [])

        lines.append(f"\n<!-- Page {page_num} -->\n")

        # Interleave text then images per page.
        # Strategy: emit all text first, then images at end of page.
        # (Stage 1 already captured reading order; a future enhancement
        #  could use bbox Y positions to interleave more precisely.)

        for block in text_blocks_on_page:
            rendered = render_text_block(block["text"])
            if rendered:
                lines.append(rendered)

        for filename in images_on_page:
            vision = vision_results.get(filename, {})
            lines.append(render_image_block(filename, slug, vision))

    # ── Post-process and write ────────────────────────────────
    content = "\n".join(lines)
    content = re.sub(r"\n{3,}", "\n\n", content)   # collapse excess blank lines
    content = content.strip() + "\n"

    note_path.write_text(content, encoding="utf-8")

    # ── Summary ───────────────────────────────────────────────
    described = sum(1 for f in [i["filename"] for i in summary["images"]] if f in vision_results)
    print(f"\n{'='*55}")
    print(f"  Stage 3 done.")
    print(f"")
    print(f"  Note    : {note_path}")
    print(f"  Assets  : {assets_dir}  ({len(png_files)} images)")
    print(f"  Images with AI descriptions : {described}/{len(summary['images'])}")
    print(f"")
    print(f"  Open Obsidian → load vault → find '{slug}.md'")
    print(f"  If images don't render: Settings → Files & Links")
    print(f"    → set 'New link format' to 'Relative path to file'")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
