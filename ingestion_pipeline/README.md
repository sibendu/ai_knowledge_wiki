# AI Knowledge Wiki Ingestion

Convert knowledge-heavy PDFs into Obsidian notes while preserving both text and visual knowledge from charts, diagrams, tables, and figures.

The pipeline has three stages:

1. Extract ordered text blocks and images from a PDF.
2. Generate structured image descriptions with a vision model.
3. Assemble text, images, and descriptions into an Obsidian vault note.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

For Anthropic vision, set one of:

```bash
set ANTHROPIC_API_KEY=your_api_key
```

or configure the Anthropic Foundry environment variables used by `stage2_generate_imagedesc.py`.

For Gemini vision, set one of:

```bash
set GEMINI_API_KEY=your_api_key
```

or:

```bash
set GOOGLE_API_KEY=your_api_key
```

For local vision models, start Ollama and make sure the model is available:

```bash
ollama pull llama3.2-vision:latest
ollama pull gemma4:e4b
```

## Stage 1: Extract PDF Content

```bash
python stage1_extract.py input/book.pdf --output ./stage1_out
```

This writes:

```text
stage1_out/
  text_blocks.json
  extraction_result.json
  images/
    fig_p57_002.png
```

After stage 1, you can manually delete unwanted images from `stage1_out/images/`. Later stages treat the images folder as the reviewed source of truth.

## Stage 2: Generate Image Descriptions

Supported providers:

| Provider | Default model | Notes |
| --- | --- | --- |
| `anthropic` | `claude-sonnet-4-6` | Uses Anthropic API key or Foundry env vars |
| `ollama` | `llama3.2-vision:latest` | Uses local Ollama at `http://localhost:11434` |
| `gemma4` | `gemma4:e4b` | Uses local Ollama at `http://localhost:11434` |
| `gemini` | `gemini-3.5-flash` | Uses Gemini API with `GEMINI_API_KEY` or `GOOGLE_API_KEY` |

Examples:

```bash
python stage2_generate_imagedesc.py --provider anthropic --input ./stage1_out --domain "stock trading"
python stage2_generate_imagedesc.py --provider ollama --input ./stage1_out --parallel 5
python stage2_generate_imagedesc.py --provider gemma4 --input ./stage1_out --parallel 5
	
```

Stage 2 is resumable. It loads `vision_results.json`, skips images that already have successful descriptions, and retries images that are missing or have previous failure placeholders.

Console messages are intentionally explicit:

```text
[SKIP] fig_p57_002.png already has a description
[PROCESS 1/146] fig_p60_003.png - generating description (previous attempt failed)
[DONE 1/146] fig_p60_003.png
[FAILED 2/146] fig_p62_005.png
```

`--parallel` controls how many images are actively processed at once. The default is `3`. With `--parallel 5`, the script keeps at most five model calls in flight and starts another only when one finishes.

Results are saved atomically after each completed image, so stopping the program midway should preserve completed descriptions. On the next run, completed images are skipped.

Useful options:

| Option | Default | Description |
| --- | --- | --- |
| `--provider` | required | `anthropic`, `ollama`, `gemma4`, or `gemini` |
| `--input` | `./stage1_out` | Stage 1 output folder |
| `--output` | same as input | Folder for `vision_results.json` |
| `--domain` | empty | Topic hint for sharper image analysis |
| `--model` | provider default | Override the model name |
| `--host` | `http://localhost:11434` | Ollama host |
| `--parallel` | `3` | Number of active image description calls |
| `--delay` | provider-dependent | Delay between submitted calls |
| `--context-blocks` | `5` | Nearby text blocks to include as image context |

## Stage 3: Assemble Obsidian Note

```bash
python stage3_assemble.py --input ./stage1_out --vault ./ai_knowledgewiki_ingestion_vault --title "My Note"
```

This writes:

```text
vault/
  notes/
    my-note.md
  assets/
    my-note/
      fig_p57_002.png
```

If `vision_results.json` exists, each image gets an Obsidian image embed plus a figure callout containing the generated description, knowledge claims, and tags. If stage 2 is skipped, images still embed without AI descriptions.

## Typical Workflow

```bash
python stage1_extract.py input/book.pdf --output ./stage1_out
python stage2_generate_imagedesc.py --provider gemma4 --input ./stage1_out --domain "stock trading" --parallel 5
python stage3_assemble.py --input ./stage1_out --vault ./ai_knowledgewiki_ingestion_vault --title "Trade Like a Stock Market Wizard"
```

If some images fail in stage 2, rerun the same command until the failed count reaches zero.
