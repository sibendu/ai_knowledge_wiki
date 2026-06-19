#!/usr/bin/env python3
"""
PDF Splitter - Splits a PDF into chunks of up to 99 pages each.

Usage:
    python split_pdf.py <input.pdf> [--pages N] [--output-dir DIR]

Arguments:
    input.pdf       Path to the source PDF file
    --pages N       Max pages per chunk (default: 99)
    --output-dir    Directory to save output files (default: same as input)
"""

import argparse
import sys
import os
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Installing required library: pypdf")
    os.system(f"{sys.executable} -m pip install pypdf --quiet")
    from pypdf import PdfReader, PdfWriter


def split_pdf(input_path: str, max_pages: int = 99, output_dir: str = None) -> list[str]:
    """
    Split a PDF file into chunks of up to max_pages pages.

    Args:
        input_path:  Path to the input PDF file.
        max_pages:   Maximum number of pages per output file (default 99).
        output_dir:  Directory for output files. Defaults to the input file's directory.

    Returns:
        List of paths to the created PDF files.
    """
    input_path = Path(input_path).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if not input_path.suffix.lower() == ".pdf":
        raise ValueError(f"Input file must be a PDF: {input_path}")

    # Determine output directory
    out_dir = Path(output_dir).resolve() if output_dir else input_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)

    if total_pages == 0:
        raise ValueError("The PDF has no pages.")

    stem = input_path.stem
    num_chunks = (total_pages + max_pages - 1) // max_pages  # ceiling division
    pad = len(str(num_chunks))  # zero-padding width

    print(f"  Input : {input_path.name}")
    print(f"  Total pages : {total_pages}")
    print(f"  Pages per chunk : {max_pages}")
    print(f"  Chunks to create : {num_chunks}")
    print()

    output_files = []
    for chunk_idx in range(num_chunks):
        start = chunk_idx * max_pages          # 0-based
        end   = min(start + max_pages, total_pages)  # exclusive

        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        chunk_number = str(chunk_idx + 1).zfill(pad)
        out_filename = f"{stem}_part{chunk_number}.pdf"
        out_path = out_dir / out_filename

        with open(out_path, "wb") as f:
            writer.write(f)

        pages_in_chunk = end - start
        print(f"  [{chunk_number}/{num_chunks}]  Pages {start + 1}–{end}  ({pages_in_chunk} pages)  →  {out_filename}")
        output_files.append(str(out_path))

    print(f"\n  Done! {num_chunks} file(s) saved to: {out_dir}")
    return output_files


def parse_args():
    parser = argparse.ArgumentParser(
        description="Split a PDF into chunks of up to N pages (default 99).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--input", "-i", help="Path to the input PDF file")
    parser.add_argument(
        "--pages", "-p",
        type=int,
        default=99,
        metavar="N",
        help="Maximum pages per output file (default: 99)",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default=None,
        metavar="DIR",
        help="Directory to write output files (default: same directory as input)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.pages < 1:
        print("Error: --pages must be at least 1.")
        sys.exit(1)

    try:
        split_pdf(args.input, max_pages=args.pages, output_dir=args.output_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)