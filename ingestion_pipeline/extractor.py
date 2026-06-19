"""
extractor.py
------------
Extracts text blocks and images from a PDF, preserving their reading order
and positional context. Uses PyMuPDF (fitz) for maximum fidelity.

Each page is processed as a unified stream of "blocks" — text paragraphs
and image placeholders — ordered by their vertical position on the page.
This lets the assembler stitch them back together in correct reading order.
"""

import fitz  # PyMuPDF
import base64
import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── Data Structures ──────────────────────────────────────────────────────────

@dataclass
class ImageBlock:
    """A raster or vector image extracted from a PDF page."""
    block_type: str = "image"
    page_num: int = 0
    bbox: tuple = (0, 0, 0, 0)          # (x0, y0, x1, y1) on page
    image_bytes: bytes = b""             # raw PNG bytes
    image_b64: str = ""                  # base64 encoded PNG (for API calls)
    width_px: int = 0
    height_px: int = 0
    xref: int = 0                        # internal PDF cross-reference id
    image_hash: str = ""                 # SHA1 for deduplication
    suggested_filename: str = ""         # e.g. "fig_p3_001.png"

    # Filled in later by the vision stage
    ai_description: str = ""
    ai_concepts: list = field(default_factory=list)
    ai_tags: list = field(default_factory=list)


@dataclass
class TextBlock:
    """A paragraph of text from a PDF page."""
    block_type: str = "text"
    page_num: int = 0
    bbox: tuple = (0, 0, 0, 0)
    text: str = ""


@dataclass
class PageBlock:
    """All content from one page, in reading order."""
    page_num: int
    width: float
    height: float
    blocks: list   # ordered list of TextBlock | ImageBlock


@dataclass
class ExtractionResult:
    """Full extraction output for one PDF."""
    source_pdf: str
    total_pages: int
    pages: list[PageBlock]
    all_images: list[ImageBlock]   # flat list for easy iteration


# ── Constants ────────────────────────────────────────────────────────────────

MIN_IMAGE_WIDTH = 80     # px — ignore tiny icons/decorations
MIN_IMAGE_HEIGHT = 80
MIN_TEXT_LEN = 3         # chars — ignore stray punctuation blocks


# ── Main Extractor ───────────────────────────────────────────────────────────

class PDFExtractor:
    """
    Extracts text and images from a PDF in unified reading order.

    Usage:
        extractor = PDFExtractor("my_book.pdf")
        result = extractor.extract()
    """

    def __init__(self, pdf_path: str | Path, dpi: int = 150):
        self.pdf_path = Path(pdf_path)
        self.dpi = dpi
        self._seen_hashes: set[str] = set()

    def extract(self) -> ExtractionResult:
        doc = fitz.open(self.pdf_path)
        pages = []
        all_images = []
        image_counter = [0]   # mutable counter shared across pages

        for page_num in range(len(doc)):
            page = doc[page_num]
            page_block = self._process_page(page, page_num + 1, image_counter)
            pages.append(page_block)

            imgs = [b for b in page_block.blocks if b.block_type == "image"]
            all_images.extend(imgs)

        doc.close()

        return ExtractionResult(
            source_pdf=self.pdf_path.name,
            total_pages=len(pages),
            pages=pages,
            all_images=all_images,
        )

    # ── Private Methods ───────────────────────────────────────────────────────

    def _process_page(self, page: fitz.Page, page_num: int, counter: list) -> PageBlock:
        """
        Build a list of TextBlock and ImageBlock objects for one page,
        sorted top-to-bottom (primary) then left-to-right (secondary).
        """
        blocks = []

        # 1. Get all text blocks with their bounding boxes
        text_dict = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
        for block in text_dict.get("blocks", []):
            if block["type"] == 0:   # 0 = text
                text = self._clean_text(block)
                if len(text) >= MIN_TEXT_LEN:
                    blocks.append(TextBlock(
                        page_num=page_num,
                        bbox=tuple(block["bbox"]),
                        text=text,
                    ))

        # 2. Extract embedded raster images
        doc = page.parent
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            img_block = self._extract_raster_image(doc, page, xref, page_num, counter)
            if img_block:
                blocks.append(img_block)

        # 3. Detect vector graphics as page-rendered crops
        vector_blocks = self._detect_vector_graphics(page, page_num, counter, blocks)
        blocks.extend(vector_blocks)

        # 4. Sort all blocks top→bottom, then left→right
        blocks.sort(key=lambda b: (round(b.bbox[1] / 10) * 10, b.bbox[0]))

        return PageBlock(
            page_num=page_num,
            width=page.rect.width,
            height=page.rect.height,
            blocks=blocks,
        )

    def _clean_text(self, block: dict) -> str:
        """Flatten a PyMuPDF text block into a clean string."""
        lines = []
        for line in block.get("spans", []) or []:
            # block["spans"] is flat only in some modes; handle both shapes
            if isinstance(line, dict) and "text" in line:
                lines.append(line["text"])
        if not lines:
            # Fallback: iterate lines → spans
            for ln in block.get("lines", []):
                for span in ln.get("spans", []):
                    lines.append(span.get("text", ""))
        return " ".join(lines).strip()

    def _extract_raster_image(
        self,
        doc: fitz.Document,
        page: fitz.Page,
        xref: int,
        page_num: int,
        counter: list,
    ) -> Optional[ImageBlock]:
        """Extract a raster image by xref, convert to PNG, deduplicate."""
        try:
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image.get("ext", "png")

            # Convert non-PNG to PNG via pixmap
            if ext.lower() not in ("png", "jpg", "jpeg"):
                pix = fitz.Pixmap(doc, xref)
                if pix.n > 4:  # CMYK → RGB
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                image_bytes = pix.tobytes("png")

            width = base_image.get("width", 0)
            height = base_image.get("height", 0)

            if width < MIN_IMAGE_WIDTH or height < MIN_IMAGE_HEIGHT:
                return None

            # Deduplication
            img_hash = hashlib.sha1(image_bytes).hexdigest()[:12]
            if img_hash in self._seen_hashes:
                return None
            self._seen_hashes.add(img_hash)

            # Get bounding box on page
            bbox = self._get_image_bbox(page, xref)

            counter[0] += 1
            filename = f"fig_p{page_num}_{counter[0]:03d}.png"

            return ImageBlock(
                page_num=page_num,
                bbox=bbox,
                image_bytes=image_bytes,
                image_b64=base64.b64encode(image_bytes).decode(),
                width_px=width,
                height_px=height,
                xref=xref,
                image_hash=img_hash,
                suggested_filename=filename,
            )
        except Exception:
            return None

    def _get_image_bbox(self, page: fitz.Page, xref: int) -> tuple:
        """Find the bounding box of an image on the page."""
        try:
            rects = page.get_image_rects(xref)
            if rects:
                return tuple(rects[0])
        except Exception:
            pass

        for item in page.get_image_info(xrefs=True):
            if item.get("xref") == xref:
                r = item.get("bbox") or item.get("rect", (0, 0, 100, 100))
                return tuple(r)
        return (0, 0, page.rect.width, page.rect.height)

    def _detect_vector_graphics(
        self,
        page: fitz.Page,
        page_num: int,
        counter: list,
        existing_blocks: list,
    ) -> list[ImageBlock]:
        """
        Detect regions that look like charts/diagrams but are drawn as
        vector paths (not embedded raster images). We rasterize those
        regions specifically.
        
        Strategy: look for page areas with many drawing commands but no
        text — these are likely charts, diagrams, or figures.
        """
        vector_blocks = []

        # Get drawing paths
        drawings = page.get_drawings()
        if len(drawings) < 8:   # Not enough drawings to constitute a figure
            return []

        # Cluster drawings into regions
        regions = self._cluster_drawings(drawings, page)

        # Covered by existing raster images?
        covered_bboxes = [b.bbox for b in existing_blocks if b.block_type == "image"]

        for region_bbox in regions:
            if self._is_covered(region_bbox, covered_bboxes):
                continue

            # Rasterize just that region
            clip = fitz.Rect(region_bbox)
            mat = fitz.Matrix(self.dpi / 72, self.dpi / 72)
            pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
            image_bytes = pix.tobytes("png")

            if pix.width < MIN_IMAGE_WIDTH or pix.height < MIN_IMAGE_HEIGHT:
                continue

            img_hash = hashlib.sha1(image_bytes).hexdigest()[:12]
            if img_hash in self._seen_hashes:
                continue
            self._seen_hashes.add(img_hash)

            counter[0] += 1
            filename = f"fig_p{page_num}_{counter[0]:03d}_vec.png"

            vector_blocks.append(ImageBlock(
                page_num=page_num,
                bbox=region_bbox,
                image_bytes=image_bytes,
                image_b64=base64.b64encode(image_bytes).decode(),
                width_px=pix.width,
                height_px=pix.height,
                xref=-1,
                image_hash=img_hash,
                suggested_filename=filename,
            ))

        return vector_blocks

    def _cluster_drawings(self, drawings: list, page: fitz.Page) -> list[tuple]:
        """
        Simple bounding-box clustering: merge drawing rects that are
        within 30pt of each other into a unified region.
        """
        if not drawings:
            return []

        rects = []
        for d in drawings:
            r = d.get("rect")
            if r and r.width > 20 and r.height > 20:
                rects.append(list(r))

        if not rects:
            return []

        # Greedy merge
        merged = [rects[0]]
        for r in rects[1:]:
            absorbed = False
            for m in merged:
                if self._rects_close(r, m, threshold=40):
                    m[0] = min(m[0], r[0])
                    m[1] = min(m[1], r[1])
                    m[2] = max(m[2], r[2])
                    m[3] = max(m[3], r[3])
                    absorbed = True
                    break
            if not absorbed:
                merged.append(r)

        # Filter: keep only regions big enough to be figures
        page_area = page.rect.width * page.rect.height
        result = []
        for m in merged:
            w, h = m[2] - m[0], m[3] - m[1]
            area = w * h
            if w > 80 and h > 80 and area > 0.01 * page_area:
                # Add small padding
                pad = 6
                result.append((
                    max(0, m[0] - pad),
                    max(0, m[1] - pad),
                    min(page.rect.width, m[2] + pad),
                    min(page.rect.height, m[3] + pad),
                ))
        return result

    def _rects_close(self, a: list, b: list, threshold: float) -> bool:
        """True if two rects are within `threshold` points of each other."""
        return (
            a[0] < b[2] + threshold and a[2] > b[0] - threshold and
            a[1] < b[3] + threshold and a[3] > b[1] - threshold
        )

    def _is_covered(self, bbox: tuple, existing: list[tuple], overlap_thresh=0.6) -> bool:
        """True if bbox significantly overlaps any existing image bbox."""
        x0, y0, x1, y1 = bbox
        area = max(1, (x1 - x0) * (y1 - y0))
        for ex in existing:
            ix = max(x0, ex[0]);  iy = max(y0, ex[1])
            ax = min(x1, ex[2]);  ay = min(y1, ex[3])
            if ax > ix and ay > iy:
                inter = (ax - ix) * (ay - iy)
                if inter / area >= overlap_thresh:
                    return True
        return False
