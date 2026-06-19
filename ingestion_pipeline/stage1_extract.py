#!/usr/bin/env python3
"""
stage1_extract.py
-----------------
STAGE 1: Extract text blocks and images from a PDF.

Saves everything to an --output folder so you can inspect before moving on.

Output:
  output_dir/
    text_blocks.json      ← ordered text and image placeholder blocks, page by page
    images/
      fig_p1_001_vec.png  ← every extracted image
    extraction_result.json ← full metadata summary

Run:
    python stage1_extract.py your-file.pdf --output ./stage1_out
"""

import sys
import json
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent))
from extractor import PDFExtractor

def main():
    parser = argparse.ArgumentParser(description="Stage 1: Extract text and images from PDF")
    parser.add_argument("pdf", help="Input PDF file path")
    parser.add_argument("--output", default="./stage1_out", help="Output folder (default: ./stage1_out)")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    out_dir = Path(args.output)
    images_dir = out_dir / "images"

    if not pdf_path.exists():
        print(f"[ERROR] PDF not found: {pdf_path}")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  STAGE 1 — Extract")
    print(f"  Input:  {pdf_path}")
    print(f"  Output: {out_dir}")
    print(f"{'='*55}\n")

    # ── Run extraction ────────────────────────────────────────
    print("Extracting...")
    extractor = PDFExtractor(pdf_path)
    result = extractor.extract()

    print(f"  Pages    : {result.total_pages}")
    print(f"  Images   : {len(result.all_images)}")

    # ── Save images to disk ───────────────────────────────────
    print(f"\nSaving images to {images_dir}/")
    saved_images = []
    for img in result.all_images:
        img_path = images_dir / img.suggested_filename
        img_path.write_bytes(img.image_bytes)
        saved_images.append({
            "filename"  : img.suggested_filename,
            "page"      : img.page_num,
            "size_px"   : f"{img.width_px}x{img.height_px}",
            "hash"      : img.image_hash,
            "bbox"      : img.bbox,
        })
        print(f"  Saved: {img.suggested_filename}  ({img.width_px}x{img.height_px}px, page {img.page_num})")

    # ── Save text blocks ──────────────────────────────────────
    print(f"\nSaving ordered content blocks...")
    text_data = []
    for page in result.pages:
        page_blocks = []
        for block in page.blocks:
            if block.block_type == "text":
                page_blocks.append({
                    "type": "text",
                    "text": block.text,
                    "bbox": block.bbox,
                })
            elif block.block_type == "image":
                page_blocks.append({
                    "type": "image",
                    "text": "",
                    "filename": block.suggested_filename,
                    "bbox": block.bbox,
                    "size_px": f"{block.width_px}x{block.height_px}",
                    "hash": block.image_hash,
                })
        text_data.append({
            "page"   : page.page_num,
            "blocks" : page_blocks,
        })

    text_path = out_dir / "text_blocks.json"
    text_path.write_text(
        json.dumps(text_data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    total_text_blocks = sum(
        1
        for page in text_data
        for block in page["blocks"]
        if block.get("type") == "text"
    )
    total_image_refs = sum(
        1
        for page in text_data
        for block in page["blocks"]
        if block.get("type") == "image"
    )
    print(
        "  Saved: text_blocks.json  "
        f"({total_text_blocks} text blocks, {total_image_refs} image refs across {result.total_pages} pages)"
    )

    # ── Save extraction summary ───────────────────────────────
    summary = {
        "source_pdf"   : result.source_pdf,
        "total_pages"  : result.total_pages,
        "total_images" : len(result.all_images),
        "images"       : saved_images,
    }
    summary_path = out_dir / "extraction_result.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # ── Print reading-order preview ───────────────────────────
    print(f"\n--- Reading-order preview (first 2 pages) ---")
    for page in result.pages[:2]:
        print(f"\n  [Page {page.page_num}]")
        for block in page.blocks:
            if block.block_type == "text":
                preview = block.text[:80].replace("\n", " ")
                print(f"    TEXT : {preview}{'...' if len(block.text) > 80 else ''}")
            else:
                print(f"    IMAGE: {block.suggested_filename}  ({block.width_px}x{block.height_px}px)")

    print(f"\n{'='*55}")
    print(f"  Stage 1 done.")
    print(f"  Check: {out_dir}/images/      ← open PNGs to verify charts extracted")
    print(f"  Check: {out_dir}/text_blocks.json  ← verify text content")
    print(f"\n  Next step:")
    print(f"    python stage2_vision.py --input {out_dir} --domain \"your domain\"")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
