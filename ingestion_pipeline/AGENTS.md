# Agent Notes

This repository is a local PDF-to-Obsidian ingestion pipeline. Keep changes scoped and avoid editing generated outputs unless the user explicitly asks.

## Important Files

- `stage1_extract.py`: extracts ordered text blocks and images from a PDF into a stage output folder.
- `stage2_generate_imagedesc.py`: generates structured image descriptions and writes `vision_results.json`.
- `stage3_assemble.py`: assembles stage output into an Obsidian vault note.
- `extractor.py`: lower-level PDF extraction logic.
- `stage1_out/`: generated/intermediate output for the current run.
- `ai_knowledgewiki_ingestion_vault/`: generated Obsidian vault output.
- `old/`: historical scripts/docs; do not treat as the current pipeline unless the user asks.

## Current Stage 2 Behavior

`stage2_generate_imagedesc.py` supports these providers:

- `anthropic`: default model `claude-sonnet-4-6`
- `ollama`: default model `llama3.2-vision:latest`
- `gemma4`: default model `gemma4:e4b`, served through local Ollama
- `gemini`: default model `gemini-3.5-flash`, served through the Gemini API with `google-genai`

Stage 2 is resumable:

- It reads existing `vision_results.json`.
- It skips entries that already have a successful description.
- It retries missing entries and failure placeholders such as `Vision analysis failed: ...` or `#needs-review`.
- It saves results atomically after each completed image.
- It supports `--parallel`, default `3`, to bound concurrent image description calls.

Expected console labels:

- `[SKIP] ... already has a description`
- `[PROCESS n/total] ... - generating description (missing description)`
- `[PROCESS n/total] ... - generating description (previous attempt failed)`
- `[DONE n/total] ...`
- `[FAILED n/total] ...`

With `--parallel 5`, only five images should be actively in flight. Do not change this back to submitting the entire pending queue at once.

## Editing Guidance

- Do not modify code when the user asks only for docs.
- Use `apply_patch` for file edits.
- Prefer `rg` and targeted file reads for inspection.
- Avoid changing generated files in `stage1_out/`, `outputs/`, `work/`, or `ai_knowledgewiki_ingestion_vault/` unless requested.
- Preserve resumable behavior in stage 2; it protects long-running image analysis work.
- Preserve provider defaults unless the user asks to change them.
- Gemini uses `GEMINI_API_KEY` or `GOOGLE_API_KEY`; local Ollama providers do not use these keys.

## Quick Checks

After editing Python code, run:

```bash
python -m py_compile stage1_extract.py stage2_generate_imagedesc.py stage3_assemble.py
```

After editing stage 2 provider or CLI behavior, also check:

```bash
python stage2_generate_imagedesc.py --help
```
