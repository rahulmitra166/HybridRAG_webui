"""Local open-source PDF -> LLM-friendly extraction pipeline.

No commercial APIs or cloud services are used. The pipeline uses local Python
libraries plus optional local tools such as Tesseract, GROBID, and pix2tex.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import statistics
import traceback
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd
import pdfplumber
import pypdfium2 as pdfium
from PIL import Image
from pypdf import PdfReader
from tqdm.auto import tqdm

BBox = Tuple[float, float, float, float]  # x0, top, x1, bottom, top-origin page points


@dataclass
class PipelineConfig:
    input_dir: Path = Path("pdfs")
    output_dir: Path = Path("pdf_llm_output")
    recursive: bool = True
    dpi: int = 200
    save_page_images: bool = False
    save_crops: bool = True
    crop_padding_points: float = 8.0
    enable_ocr: bool = True
    ocr_language: str = "eng"
    min_native_words_for_no_ocr: int = 25
    scanned_image_coverage_threshold: float = 0.55
    enable_embedded_image_export: bool = True
    min_figure_area_fraction: float = 0.015
    merge_graphics_margin_points: float = 12.0
    equation_crop_padding_points: float = 10.0
    chunk_chars: int = 3500
    chunk_overlap_chars: int = 350
    table_settings: Dict[str, Any] = field(default_factory=lambda: {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "snap_tolerance": 3,
        "join_tolerance": 3,
        "edge_min_length": 3,
        "min_words_vertical": 3,
        "min_words_horizontal": 1,
        "intersection_tolerance": 3,
        "text_tolerance": 3,
    })


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            h.update(block)
    return h.hexdigest()


def safe_name(name: str, max_len: int = 120) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("._")
    return cleaned[:max_len] or "document"


def clean_text(text: Optional[str]) -> str:
    if not text:
        return ""
    text = str(text).replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def bbox_tuple(obj: Dict[str, Any]) -> Optional[BBox]:
    try:
        x0 = float(obj.get("x0", 0.0))
        x1 = float(obj.get("x1", 0.0))
        top = float(obj.get("top", obj.get("y0", 0.0)))
        bottom = float(obj.get("bottom", obj.get("y1", 0.0)))
        if x1 <= x0 or bottom <= top:
            return None
        return (x0, top, x1, bottom)
    except Exception:
        return None


def bbox_to_dict(b: Optional[BBox]) -> Optional[Dict[str, float]]:
    if b is None:
        return None
    x0, top, x1, bottom = b
    return {
        "x0": round(float(x0), 3),
        "top": round(float(top), 3),
        "x1": round(float(x1), 3),
        "bottom": round(float(bottom), 3),
        "width": round(float(x1 - x0), 3),
        "height": round(float(bottom - top), 3),
    }


def bbox_area(b: Optional[BBox]) -> float:
    if not b:
        return 0.0
    return max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])


def expand_bbox(b: BBox, pad: float, page_width: float, page_height: float) -> BBox:
    return (
        max(0.0, b[0] - pad),
        max(0.0, b[1] - pad),
        min(page_width, b[2] + pad),
        min(page_height, b[3] + pad),
    )


def overlap_area(a: BBox, b: BBox) -> float:
    x0 = max(a[0], b[0])
    top = max(a[1], b[1])
    x1 = min(a[2], b[2])
    bottom = min(a[3], b[3])
    if x1 <= x0 or bottom <= top:
        return 0.0
    return (x1 - x0) * (bottom - top)


def overlap_ratio(a: BBox, b: BBox) -> float:
    denom = min(bbox_area(a), bbox_area(b)) or 1.0
    return overlap_area(a, b) / denom


def boxes_touch_or_overlap(a: BBox, b: BBox, margin: float) -> bool:
    ae = (a[0] - margin, a[1] - margin, a[2] + margin, a[3] + margin)
    return overlap_area(ae, b) > 0


def union_bbox(boxes: Iterable[BBox]) -> BBox:
    box_list = list(boxes)
    return (
        min(b[0] for b in box_list),
        min(b[1] for b in box_list),
        max(b[2] for b in box_list),
        max(b[3] for b in box_list),
    )


def merge_nearby_boxes(boxes: List[BBox], margin: float) -> List[BBox]:
    clusters: List[List[BBox]] = []
    for box in boxes:
        placed = False
        for cluster in clusters:
            if boxes_touch_or_overlap(union_bbox(cluster), box, margin):
                cluster.append(box)
                placed = True
                break
        if not placed:
            clusters.append([box])
    changed = True
    while changed:
        changed = False
        new_clusters: List[List[BBox]] = []
        for cluster in clusters:
            cbox = union_bbox(cluster)
            merged = False
            for existing in new_clusters:
                if boxes_touch_or_overlap(union_bbox(existing), cbox, margin):
                    existing.extend(cluster)
                    changed = True
                    merged = True
                    break
            if not merged:
                new_clusters.append(cluster)
        clusters = new_clusters
    return [union_bbox(c) for c in clusters]


def matrix_to_markdown(matrix: List[List[Any]]) -> str:
    rows = [["" if cell is None else str(cell).replace("\n", " ").strip() for cell in row] for row in matrix if row]
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    col_widths = [max(len(row[i]) for row in rows) for i in range(width)]

    def fmt(row: List[str]) -> str:
        return "| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(width)) + " |"

    header = fmt(rows[0])
    sep = "| " + " | ".join("-" * max(3, col_widths[i]) for i in range(width)) + " |"
    body = [fmt(row) for row in rows[1:]]
    return "\n".join([header, sep] + body)


def write_csv(path: Path, matrix: List[List[Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(matrix)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False), encoding="utf-8")


def relpath(path: Path, start: Path) -> str:
    return str(Path(path).resolve().relative_to(Path(start).resolve())).replace(os.sep, "/")


def discover_pdfs(cfg: PipelineConfig) -> List[Path]:
    pattern = "**/*.pdf" if cfg.recursive else "*.pdf"
    return sorted(p for p in Path(cfg.input_dir).glob(pattern) if p.is_file())


def render_page_to_pil(pdf_path: Path, page_index: int, dpi: int) -> Image.Image:
    pdf = pdfium.PdfDocument(str(pdf_path))
    try:
        page = pdf[page_index]
        bitmap = page.render(scale=dpi / 72.0)
        return bitmap.to_pil()
    finally:
        try:
            pdf.close()
        except Exception:
            pass


def save_bbox_crop(pdf_path: Path, page_index: int, bbox: BBox, page_width: float, page_height: float,
                   out_path: Path, dpi: int, pad_points: float = 6.0) -> Optional[str]:
    try:
        b = expand_bbox(bbox, pad_points, page_width, page_height)
        img = render_page_to_pil(pdf_path, page_index, dpi)
        scale = dpi / 72.0
        crop_box = (
            max(0, int(math.floor(b[0] * scale))),
            max(0, int(math.floor(b[1] * scale))),
            min(img.width, int(math.ceil(b[2] * scale))),
            min(img.height, int(math.ceil(b[3] * scale))),
        )
        if crop_box[2] <= crop_box[0] or crop_box[3] <= crop_box[1]:
            return None
        crop = img.crop(crop_box)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        crop.save(out_path)
        return str(out_path)
    except Exception:
        return None


def extract_pdf_metadata(pdf_path: Path) -> Dict[str, Any]:
    try:
        reader = PdfReader(str(pdf_path))
        metadata = {str(k).lstrip("/"): str(v) for k, v in dict(reader.metadata or {}).items()}
        return {"page_count": len(reader.pages), "pdf_metadata": metadata, "is_encrypted": bool(reader.is_encrypted)}
    except Exception as e:
        return {"page_count": None, "pdf_metadata": {}, "metadata_error": repr(e)}


def extract_embedded_images_with_pypdf(pdf_path: Path, page_index: int, out_dir: Path, rel_root: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    try:
        reader = PdfReader(str(pdf_path))
        images = getattr(reader.pages[page_index], "images", [])
        for i, img in enumerate(images):
            raw_name = getattr(img, "name", f"image_{i}.bin") or f"image_{i}.bin"
            suffix = Path(raw_name).suffix or ".bin"
            out_path = out_dir / f"page_{page_index+1:04d}_embedded_{i:03d}{suffix}"
            data = getattr(img, "data", None)
            if data:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_bytes(data)
                records.append({"id": f"p{page_index+1:04d}_embedded_image_{i:03d}", "source": "pypdf_page_images", "file": relpath(out_path, rel_root), "name": raw_name, "bytes": len(data)})
    except Exception as e:
        records.append({"source": "pypdf_page_images", "error": repr(e)})
    return records


def page_image_coverage(page: pdfplumber.page.Page) -> float:
    page_area = float(page.width * page.height) or 1.0
    total = 0.0
    for img in getattr(page, "images", []) or []:
        b = bbox_tuple(img)
        if b:
            total += bbox_area(b)
    return min(1.0, total / page_area)


def extract_words_and_lines(page: pdfplumber.page.Page) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], str]:
    try:
        words_raw = page.extract_words(x_tolerance=1.5, y_tolerance=3, use_text_flow=True, keep_blank_chars=False, extra_attrs=["fontname", "size"])
    except TypeError:
        words_raw = page.extract_words(x_tolerance=1.5, y_tolerance=3, use_text_flow=True, keep_blank_chars=False)
    words_raw = words_raw or []

    words: List[Dict[str, Any]] = []
    for i, w in enumerate(words_raw):
        b = bbox_tuple(w)
        text = clean_text(w.get("text", ""))
        if text and b:
            words.append({"id": f"w{i:05d}", "text": text, "bbox": bbox_to_dict(b), "fontname": w.get("fontname"), "size": float(w["size"]) if w.get("size") is not None else None})

    sorted_words = sorted(words_raw, key=lambda w: (float(w.get("top", 0)), float(w.get("x0", 0))))
    grouped: List[List[Dict[str, Any]]] = []
    for w in sorted_words:
        b = bbox_tuple(w)
        if not b or not clean_text(w.get("text", "")):
            continue
        for group in grouped:
            gb = union_bbox([bbox_tuple(g) for g in group if bbox_tuple(g)])
            if abs(b[1] - gb[1]) <= 3.0 or overlap_area((0, b[1], page.width, b[3]), (0, gb[1], page.width, gb[3])) > 0:
                group.append(w)
                break
        else:
            grouped.append([w])

    sizes_all = [float(w.get("size")) for w in words_raw if w.get("size") is not None]
    median_size = statistics.median(sizes_all) if sizes_all else None
    caption_re = re.compile(r"^\s*(fig(?:ure)?\.?|table|tab\.?|eq(?:uation)?\.?)\s*\(?\d+[\w.-]*\)?", re.I)
    lines: List[Dict[str, Any]] = []
    for i, group in enumerate(grouped):
        group = sorted(group, key=lambda w: float(w.get("x0", 0)))
        boxes = [bbox_tuple(g) for g in group if bbox_tuple(g)]
        if not boxes:
            continue
        b = union_bbox(boxes)
        text = clean_text(" ".join(g.get("text", "") for g in group))
        if not text:
            continue
        sizes = [float(g.get("size")) for g in group if g.get("size") is not None]
        avg_size = statistics.mean(sizes) if sizes else None
        line_type = "text"
        if caption_re.search(text):
            line_type = "caption"
        elif median_size and avg_size and avg_size >= 1.22 * median_size and len(text) <= 160:
            line_type = "heading"
        elif len(text) <= 90 and text.isupper() and sum(c.isalpha() for c in text) > 4:
            line_type = "heading"
        lines.append({"id": f"line_{i:04d}", "type": line_type, "text": text, "bbox": bbox_to_dict(b), "word_count": len(group), "avg_font_size": round(avg_size, 3) if avg_size else None})

    try:
        plain = clean_text(page.extract_text(layout=True) or "")
    except Exception:
        plain = ""
    if not plain:
        plain = clean_text("\n".join(line["text"] for line in lines))
    return words, lines, plain


def should_ocr_page(page: pdfplumber.page.Page, native_word_count: int, cfg: PipelineConfig) -> Tuple[bool, str, float]:
    coverage = page_image_coverage(page)
    if native_word_count == 0:
        return True, "no_native_words", coverage
    if native_word_count < cfg.min_native_words_for_no_ocr and coverage >= cfg.scanned_image_coverage_threshold:
        return True, "few_native_words_and_high_image_coverage", coverage
    if native_word_count < max(5, cfg.min_native_words_for_no_ocr // 3):
        return True, "very_few_native_words", coverage
    return False, "native_text_sufficient", coverage


def ocr_page_if_needed(pdf_path: Path, page_index: int, page: pdfplumber.page.Page, native_word_count: int, cfg: PipelineConfig) -> Dict[str, Any]:
    needed, reason, coverage = should_ocr_page(page, native_word_count, cfg)
    out = {"needed": needed, "applied": False, "reason": reason, "language": cfg.ocr_language, "image_coverage": round(coverage, 4), "text": "", "words": [], "lines": [], "error": None}
    if not needed or not cfg.enable_ocr:
        return out
    try:
        import pytesseract
        from pytesseract import Output
    except Exception as e:
        out["error"] = f"pytesseract/tesseract not available: {e!r}"
        return out
    try:
        img = render_page_to_pil(pdf_path, page_index, cfg.dpi).convert("RGB")
        data = pytesseract.image_to_data(img, lang=cfg.ocr_language, output_type=Output.DICT)
        scale = cfg.dpi / 72.0
        words: List[Dict[str, Any]] = []
        groups: Dict[Tuple[int, int, int], List[Dict[str, Any]]] = {}
        for i, txt0 in enumerate(data.get("text", [])):
            txt = clean_text(txt0)
            if not txt:
                continue
            try:
                conf = float(data.get("conf", ["-1"])[i])
            except Exception:
                conf = -1.0
            if conf < 0:
                continue
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            b = (x / scale, y / scale, (x + w) / scale, (y + h) / scale)
            rec = {"id": f"ocr_w{i:05d}", "text": txt, "bbox": bbox_to_dict(b), "confidence": round(conf, 3)}
            words.append(rec)
            key = (int(data.get("block_num", [0])[i]), int(data.get("par_num", [0])[i]), int(data.get("line_num", [0])[i]))
            groups.setdefault(key, []).append({"text": txt, "bbox": b, "confidence": conf})
        lines = []
        for j, (_, group) in enumerate(sorted(groups.items())):
            b = union_bbox([g["bbox"] for g in group])
            confs = [g["confidence"] for g in group if g["confidence"] >= 0]
            lines.append({"id": f"ocr_line_{j:04d}", "type": "ocr_text", "text": clean_text(" ".join(g["text"] for g in group)), "bbox": bbox_to_dict(b), "avg_confidence": round(statistics.mean(confs), 3) if confs else None})
        out.update({"applied": True, "text": clean_text("\n".join(line["text"] for line in lines)), "words": words, "lines": lines})
    except Exception as e:
        out["error"] = repr(e)
    return out


MATH_SYMBOL_RE = re.compile(r"(\\[a-zA-Z]+|[=<>≤≥±≈≠∞∑∫√∂∇πθλμσΩαβγδ]|\^|_|\bfrac\b|\bsum\b|\bint\b)")


def is_equation_like(text: str) -> bool:
    t = clean_text(text)
    if not t or len(t) > 220:
        return False
    symbol_hits = len(MATH_SYMBOL_RE.findall(t))
    digits = sum(ch.isdigit() for ch in t)
    spaces = t.count(" ")
    if symbol_hits >= 2 and len(t) <= 160:
        return True
    if symbol_hits >= 1 and digits >= 1 and spaces <= 12 and len(t) <= 120:
        return True
    if re.search(r"\b[A-Za-z]\s*=\s*", t) and len(t) <= 140:
        return True
    return False


def detect_equations(lines: List[Dict[str, Any]], pdf_path: Path, page_index: int, page_width: float, page_height: float, out_dir: Path, rel_root: Path, cfg: PipelineConfig) -> List[Dict[str, Any]]:
    equations = []
    for i, line in enumerate(lines):
        text = line.get("text", "")
        bdict = line.get("bbox")
        if not bdict or not is_equation_like(text):
            continue
        b = (bdict["x0"], bdict["top"], bdict["x1"], bdict["bottom"])
        crop_file = None
        if cfg.save_crops:
            out_path = out_dir / f"page_{page_index+1:04d}_equation_{i:03d}.png"
            crop_abs = save_bbox_crop(pdf_path, page_index, b, page_width, page_height, out_path, cfg.dpi, cfg.equation_crop_padding_points)
            crop_file = relpath(Path(crop_abs), rel_root) if crop_abs else None
        equations.append({"id": f"p{page_index+1:04d}_eq_{i:03d}", "source": "line_math_heuristic", "text": text, "latex": None, "mathml": None, "bbox": bbox_to_dict(b), "crop_file": crop_file, "caption": None, "note": "Candidate equation. Optionally run local pix2tex for image-to-LaTeX."})
    return equations


def extract_tables(page: pdfplumber.page.Page, page_index: int, out_dir: Path, rel_root: Path, cfg: PipelineConfig) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    try:
        tables = page.find_tables(table_settings=cfg.table_settings)
    except Exception:
        tables = []
    for i, table in enumerate(tables or []):
        try:
            matrix = table.extract() or []
        except Exception:
            matrix = []
        matrix = [["" if c is None else str(c).strip() for c in row] for row in matrix if row]
        if not matrix:
            continue
        tid = f"p{page_index+1:04d}_table_{i:03d}"
        csv_path = out_dir / f"page_{page_index+1:04d}_table_{i:03d}.csv"
        md_path = out_dir / f"page_{page_index+1:04d}_table_{i:03d}.md"
        html_path = out_dir / f"page_{page_index+1:04d}_table_{i:03d}.html"
        markdown = matrix_to_markdown(matrix)
        write_csv(csv_path, matrix)
        write_text(md_path, markdown)
        try:
            df = pd.DataFrame(matrix[1:], columns=matrix[0]) if len(matrix) >= 2 else pd.DataFrame(matrix)
            write_text(html_path, df.to_html(index=False, escape=True))
        except Exception:
            write_text(html_path, "<pre>" + markdown.replace("&", "&amp;").replace("<", "&lt;") + "</pre>")
        b = tuple(float(v) for v in table.bbox) if getattr(table, "bbox", None) else None
        records.append({"id": tid, "source": "pdfplumber.find_tables", "bbox": bbox_to_dict(b) if b else None, "row_count": len(matrix), "col_count": max((len(r) for r in matrix), default=0), "matrix": matrix, "markdown": markdown, "files": {"csv": relpath(csv_path, rel_root), "markdown": relpath(md_path, rel_root), "html": relpath(html_path, rel_root)}, "caption": None})
    return records


def extract_links(page: pdfplumber.page.Page) -> List[Dict[str, Any]]:
    links = []
    for i, link in enumerate(getattr(page, "hyperlinks", []) or []):
        links.append({"id": f"link_{i:04d}", "uri": link.get("uri"), "bbox": bbox_to_dict(bbox_tuple(link))})
    return links


def caption_candidates(lines: List[Dict[str, Any]], kind: Optional[str] = None) -> List[Dict[str, Any]]:
    caps = [ln for ln in lines if ln.get("type") == "caption"]
    if kind == "figure":
        return [c for c in caps if re.match(r"^\s*fig", c.get("text", ""), re.I)] or caps
    if kind == "table":
        return [c for c in caps if re.match(r"^\s*(table|tab\.)", c.get("text", ""), re.I)] or caps
    if kind == "equation":
        return [c for c in caps if re.match(r"^\s*eq", c.get("text", ""), re.I)] or caps
    return caps


def attach_nearest_caption(record: Dict[str, Any], lines: List[Dict[str, Any]], kind: str) -> None:
    bdict = record.get("bbox")
    if not bdict:
        return
    b = (bdict["x0"], bdict["top"], bdict["x1"], bdict["bottom"])
    best = None
    best_score = float("inf")
    for cap in caption_candidates(lines, kind=kind):
        cdict = cap.get("bbox")
        if not cdict:
            continue
        c = (cdict["x0"], cdict["top"], cdict["x1"], cdict["bottom"])
        vertical_gap = min(abs(c[1] - b[3]), abs(b[1] - c[3]))
        horizontal_overlap = max(0.0, min(b[2], c[2]) - max(b[0], c[0]))
        horizontal_bonus = horizontal_overlap / max(1.0, min(b[2] - b[0], c[2] - c[0]))
        score = vertical_gap - 25.0 * horizontal_bonus
        if score < best_score and vertical_gap < 140:
            best, best_score = cap, score
    if best:
        record["caption"] = {"text": best.get("text"), "line_id": best.get("id"), "bbox": best.get("bbox")}


def extract_figures_and_graphics(page: pdfplumber.page.Page, pdf_path: Path, page_index: int, table_records: List[Dict[str, Any]], equation_records: List[Dict[str, Any]], lines: List[Dict[str, Any]], out_dir: Path, rel_root: Path, cfg: PipelineConfig) -> List[Dict[str, Any]]:
    page_area = float(page.width * page.height) or 1.0
    exclusion_boxes: List[BBox] = []
    for rec in table_records + equation_records:
        bdict = rec.get("bbox")
        if bdict:
            exclusion_boxes.append((bdict["x0"], bdict["top"], bdict["x1"], bdict["bottom"]))
    boxes: List[BBox] = []
    for img in getattr(page, "images", []) or []:
        b = bbox_tuple(img)
        if b and bbox_area(b) / page_area >= 0.003:
            boxes.append(b)
    for source_name in ["rects", "curves", "lines"]:
        for obj in getattr(page, source_name, []) or []:
            b = bbox_tuple(obj)
            if not b:
                continue
            if b[2] - b[0] < 1.0:
                b = (b[0] - 0.5, b[1], b[2] + 0.5, b[3])
            if b[3] - b[1] < 1.0:
                b = (b[0], b[1] - 0.5, b[2], b[3] + 0.5)
            if bbox_area(b) / page_area >= 0.00002:
                boxes.append(b)
    clusters = merge_nearby_boxes(boxes, cfg.merge_graphics_margin_points) if boxes else []
    records: List[Dict[str, Any]] = []
    min_area = cfg.min_figure_area_fraction * page_area
    for i, b in enumerate(clusters):
        if bbox_area(b) < min_area:
            continue
        if any(overlap_ratio(b, ex) > 0.45 for ex in exclusion_boxes):
            continue
        crop_file = None
        if cfg.save_crops:
            crop_path = out_dir / f"page_{page_index+1:04d}_figure_{i:03d}.png"
            crop_abs = save_bbox_crop(pdf_path, page_index, b, page.width, page.height, crop_path, cfg.dpi, cfg.crop_padding_points)
            crop_file = relpath(Path(crop_abs), rel_root) if crop_abs else None
        rec = {"id": f"p{page_index+1:04d}_figure_{i:03d}", "source": "pdfplumber_graphic_cluster", "bbox": bbox_to_dict(b), "crop_file": crop_file, "caption": None, "note": "Candidate figure/graphic region. May include plots, diagrams, raster images, or vector graphics."}
        attach_nearest_caption(rec, lines, kind="figure")
        records.append(rec)
    return records


def text_units_for_chunking(page_record: Dict[str, Any]) -> List[Dict[str, Any]]:
    units: List[Dict[str, Any]] = []
    pnum = page_record["page_number"]
    for line in page_record.get("lines", []):
        txt = clean_text(line.get("text"))
        if txt:
            units.append({"kind": line.get("type", "text"), "text": txt, "page_numbers": [pnum], "source_ids": [line.get("id")]})
    ocr = page_record.get("ocr", {})
    if ocr.get("applied") and len(page_record.get("words", [])) < 10:
        for line in ocr.get("lines", []):
            txt = clean_text(line.get("text"))
            if txt:
                units.append({"kind": "ocr_text", "text": txt, "page_numbers": [pnum], "source_ids": [line.get("id")]})
    for table in page_record.get("tables", []):
        cap = clean_text((table.get("caption") or {}).get("text", ""))
        md = clean_text(table.get("markdown", ""))
        payload = "\n\n".join(x for x in [cap, md] if x)
        if payload:
            units.append({"kind": "table", "text": payload, "page_numbers": [pnum], "source_ids": [table.get("id")]})
    for eq in page_record.get("equations", []):
        payload = clean_text(eq.get("latex") or eq.get("text") or "")
        if payload:
            units.append({"kind": "equation", "text": payload, "page_numbers": [pnum], "source_ids": [eq.get("id")]})
    for fig in page_record.get("figures", []):
        cap = clean_text((fig.get("caption") or {}).get("text", ""))
        if cap:
            units.append({"kind": "figure_caption", "text": cap, "page_numbers": [pnum], "source_ids": [fig.get("id")]})
    return units


def build_chunks(document: Dict[str, Any], cfg: PipelineConfig) -> List[Dict[str, Any]]:
    units: List[Dict[str, Any]] = []
    for page in document.get("pages", []):
        units.extend(text_units_for_chunking(page))
    chunks: List[Dict[str, Any]] = []
    buffer: List[str] = []
    pages: List[int] = []
    source_ids: List[str] = []
    heading_context = ""

    def flush() -> None:
        nonlocal buffer, pages, source_ids
        text = clean_text("\n".join(buffer))
        if not text:
            buffer, pages, source_ids = [], [], []
            return
        chunks.append({"chunk_id": f"{document['document_id']}_chunk_{len(chunks):05d}", "document_id": document["document_id"], "file_name": document["file_name"], "page_numbers": sorted(set(pages)), "heading_context": heading_context, "text": text, "text_for_embedding": clean_text("\n\n".join([heading_context, text])) if heading_context else text, "source_ids": [sid for sid in source_ids if sid], "char_count": len(text)})
        if cfg.chunk_overlap_chars > 0 and len(text) > cfg.chunk_overlap_chars:
            buffer = [text[-cfg.chunk_overlap_chars:]]
        else:
            buffer = []
        pages, source_ids = [], []

    for unit in units:
        if unit["kind"] == "heading":
            heading_context = unit["text"]
        if sum(len(x) + 1 for x in buffer) + len(unit["text"]) > cfg.chunk_chars and buffer:
            flush()
        buffer.append(f"[{unit['kind']}; page {','.join(map(str, unit['page_numbers']))}]\n{unit['text']}")
        pages.extend(unit["page_numbers"])
        source_ids.extend(unit.get("source_ids", []))
    flush()
    return chunks


def build_llm_markdown(document: Dict[str, Any]) -> str:
    lines = [f"# {document['file_name']}", "", f"- document_id: `{document['document_id']}`", f"- sha256: `{document['sha256']}`", f"- page_count: {document.get('meta', {}).get('page_count')}", ""]
    for page in document.get("pages", []):
        lines.append(f"## Page {page['page_number']}")
        warnings = page.get("quality", {}).get("warnings") or []
        if warnings:
            lines.append("Warnings: " + "; ".join(warnings))
        if clean_text(page.get("text", "")):
            lines.extend(["", clean_text(page.get("text", ""))])
        if page.get("tables"):
            lines.extend(["", "### Tables"])
            for table in page["tables"]:
                cap = (table.get("caption") or {}).get("text")
                if cap:
                    lines.append(f"**{cap}**")
                lines.extend([table.get("markdown", ""), ""])
        if page.get("equations"):
            lines.append("### Equation candidates")
            for eq in page["equations"]:
                lines.append(f"- `{eq['id']}`: {eq.get('latex') or eq.get('text')}")
                if eq.get("crop_file"):
                    lines.append(f"  - crop: `{eq['crop_file']}`")
            lines.append("")
        if page.get("figures"):
            lines.append("### Figure / graphic candidates")
            for fig in page["figures"]:
                cap = (fig.get("caption") or {}).get("text") or "No caption detected"
                lines.append(f"- `{fig['id']}`: {cap}")
                if fig.get("crop_file"):
                    lines.append(f"  - crop: `{fig['crop_file']}`")
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def process_pdf(pdf_path: Path, cfg: PipelineConfig) -> Dict[str, Any]:
    pdf_path = Path(pdf_path)
    file_hash = sha256_file(pdf_path)
    doc_id = file_hash[:16]
    doc_folder = Path(cfg.output_dir) / f"{safe_name(pdf_path.stem)}_{doc_id}"
    assets_dir = doc_folder / "assets"
    tables_dir = assets_dir / "tables"
    figures_dir = assets_dir / "figures"
    equations_dir = assets_dir / "equations"
    embedded_dir = assets_dir / "embedded_images"
    pages_dir = doc_folder / "pages"
    doc_folder.mkdir(parents=True, exist_ok=True)
    document: Dict[str, Any] = {
        "schema_version": "1.0.0-local-open-source",
        "extracted_at": utc_now_iso(),
        "document_id": doc_id,
        "source_path": str(pdf_path.resolve()),
        "file_name": pdf_path.name,
        "sha256": file_hash,
        "meta": extract_pdf_metadata(pdf_path),
        "extraction_policy": {"commercial_apis_used": False, "primary_tools": ["pdfplumber", "pdfminer.six", "pypdf", "pypdfium2"], "optional_local_tools": ["tesseract", "pix2tex", "grobid"], "notes": "All extraction is local. No paid cloud/commercial API calls are made."},
        "pages": [],
        "chunks": [],
        "errors": [],
    }
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            for page_index, page in enumerate(tqdm(pdf.pages, desc=pdf_path.name, leave=False)):
                page_num = page_index + 1
                page_record: Dict[str, Any] = {"page_number": page_num, "width": float(page.width), "height": float(page.height), "rotation": getattr(page, "rotation", None), "text": "", "words": [], "lines": [], "tables": [], "figures": [], "equations": [], "links": [], "embedded_images": [], "ocr": {}, "page_image": None, "quality": {"warnings": []}}
                if cfg.save_page_images:
                    page_png = pages_dir / f"page_{page_num:04d}.png"
                    img = render_page_to_pil(pdf_path, page_index, cfg.dpi)
                    page_png.parent.mkdir(parents=True, exist_ok=True)
                    img.save(page_png)
                    page_record["page_image"] = relpath(page_png, cfg.output_dir)
                words, lines, plain_text = extract_words_and_lines(page)
                page_record["words"] = words
                page_record["lines"] = lines
                page_record["text"] = plain_text
                page_record["ocr"] = ocr_page_if_needed(pdf_path, page_index, page, len(words), cfg)
                if not page_record["text"] and page_record["ocr"].get("text"):
                    page_record["text"] = page_record["ocr"]["text"]
                    page_record["quality"]["warnings"].append("native_text_missing_used_ocr_text")
                page_record["tables"] = extract_tables(page, page_index, tables_dir, cfg.output_dir, cfg)
                page_record["equations"] = detect_equations(lines, pdf_path, page_index, page.width, page.height, equations_dir, cfg.output_dir, cfg)
                for eq in page_record["equations"]:
                    attach_nearest_caption(eq, lines, kind="equation")
                for table in page_record["tables"]:
                    attach_nearest_caption(table, lines, kind="table")
                page_record["figures"] = extract_figures_and_graphics(page, pdf_path, page_index, page_record["tables"], page_record["equations"], lines, figures_dir, cfg.output_dir, cfg)
                page_record["links"] = extract_links(page)
                if cfg.enable_embedded_image_export:
                    page_record["embedded_images"] = extract_embedded_images_with_pypdf(pdf_path, page_index, embedded_dir, cfg.output_dir)
                page_record["quality"].update({"native_word_count": len(words), "native_line_count": len(lines), "table_count": len(page_record["tables"]), "figure_candidate_count": len(page_record["figures"]), "equation_candidate_count": len(page_record["equations"]), "image_coverage": page_record.get("ocr", {}).get("image_coverage"), "ocr_applied": bool(page_record.get("ocr", {}).get("applied"))})
                if len(words) < 5 and not page_record["ocr"].get("applied"):
                    page_record["quality"]["warnings"].append("very_low_text_and_no_ocr")
                document["pages"].append(page_record)
    except Exception as e:
        document["errors"].append({"stage": "process_pdf", "error": repr(e), "traceback": traceback.format_exc()})
    document["chunks"] = build_chunks(document, cfg)
    json_path = doc_folder / "document.json"
    md_path = doc_folder / "document_llm.md"
    chunks_path = doc_folder / "chunks.jsonl"
    write_json(json_path, document)
    write_text(md_path, build_llm_markdown(document))
    with chunks_path.open("w", encoding="utf-8") as f:
        for chunk in document["chunks"]:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    return {"document_id": doc_id, "file_name": pdf_path.name, "source_path": str(pdf_path), "output_folder": str(doc_folder), "document_json": str(json_path), "document_markdown": str(md_path), "chunks_jsonl": str(chunks_path), "page_count": len(document.get("pages", [])), "chunk_count": len(document.get("chunks", [])), "error_count": len(document.get("errors", []))}


def process_folder(cfg: PipelineConfig) -> List[Dict[str, Any]]:
    Path(cfg.input_dir).mkdir(parents=True, exist_ok=True)
    Path(cfg.output_dir).mkdir(parents=True, exist_ok=True)
    pdfs = discover_pdfs(cfg)
    if not pdfs:
        print(f"No PDFs found in {Path(cfg.input_dir).resolve()}")
        return []
    results: List[Dict[str, Any]] = []
    for pdf_path in tqdm(pdfs, desc="PDFs"):
        try:
            results.append(process_pdf(pdf_path, cfg))
        except Exception as e:
            results.append({"file_name": pdf_path.name, "source_path": str(pdf_path), "error": repr(e), "traceback": traceback.format_exc()})
    manifest = {"schema_version": "1.0.0-local-open-source", "created_at": utc_now_iso(), "input_dir": str(Path(cfg.input_dir).resolve()), "output_dir": str(Path(cfg.output_dir).resolve()), "config": {k: str(v) if isinstance(v, Path) else v for k, v in asdict(cfg).items()}, "documents": results}
    write_json(Path(cfg.output_dir) / "manifest.json", manifest)
    with (Path(cfg.output_dir) / "corpus_chunks.jsonl").open("w", encoding="utf-8") as chunks_out, (Path(cfg.output_dir) / "corpus_documents.jsonl").open("w", encoding="utf-8") as docs_out:
        for result in results:
            json_path = result.get("document_json")
            if not json_path or not Path(json_path).exists():
                continue
            doc = json.loads(Path(json_path).read_text(encoding="utf-8"))
            docs_out.write(json.dumps({"document_id": doc["document_id"], "file_name": doc["file_name"], "sha256": doc["sha256"], "page_count": len(doc.get("pages", [])), "chunk_count": len(doc.get("chunks", [])), "document_json": str(Path(json_path)), "document_markdown": result.get("document_markdown")}, ensure_ascii=False) + "\n")
            for chunk in doc.get("chunks", []):
                chunks_out.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    print(f"Processed {len(results)} PDF(s).")
    print("Manifest:", (Path(cfg.output_dir) / "manifest.json").resolve())
    print("Corpus chunks:", (Path(cfg.output_dir) / "corpus_chunks.jsonl").resolve())
    return results


def enrich_with_local_grobid(document_json_path: Path, grobid_url: str = "http://localhost:8070") -> Dict[str, Any]:
    """Optional local-only GROBID call. Assumes GROBID is running locally."""
    try:
        import requests
    except Exception as e:
        return {"ok": False, "error": f"requests not installed: {e!r}"}
    doc = json.loads(Path(document_json_path).read_text(encoding="utf-8"))
    pdf_path = Path(doc["source_path"])
    out_xml = Path(document_json_path).parent / "grobid_fulltext.tei.xml"
    try:
        with pdf_path.open("rb") as f:
            files = {"input": (pdf_path.name, f, "application/pdf")}
            data = {"consolidateHeader": "1", "consolidateCitations": "1", "includeRawCitations": "1", "includeRawAffiliations": "1", "teiCoordinates": "ref,figure,formula,biblStruct"}
            r = requests.post(f"{grobid_url.rstrip('/')}/api/processFulltextDocument", files=files, data=data, timeout=120)
            r.raise_for_status()
            out_xml.write_text(r.text, encoding="utf-8")
        doc.setdefault("enrichments", {})["grobid"] = {"tei_xml": str(out_xml), "grobid_url": grobid_url, "created_at": utc_now_iso()}
        write_json(Path(document_json_path), doc)
        return {"ok": True, "tei_xml": str(out_xml)}
    except Exception as e:
        return {"ok": False, "error": repr(e)}


def run_optional_pix2tex_on_equations(document_json_path: Path, output_root: Optional[Path] = None) -> Dict[str, Any]:
    """Optional heavy local-only equation OCR. Requires pix2tex installed locally."""
    try:
        from pix2tex.cli import LatexOCR
    except Exception as e:
        return {"ok": False, "error": f"pix2tex is not installed or could not import: {e!r}"}
    try:
        model = LatexOCR()
        doc = json.loads(Path(document_json_path).read_text(encoding="utf-8"))
        root = Path(output_root) if output_root else Path(document_json_path).parent.parent
        count = 0
        for page in doc.get("pages", []):
            for eq in page.get("equations", []):
                crop_file = eq.get("crop_file")
                if not crop_file:
                    continue
                path = root / crop_file
                if not path.exists():
                    continue
                try:
                    eq["latex"] = model(Image.open(path))
                    count += 1
                except Exception as e:
                    eq["latex_error"] = repr(e)
        write_json(Path(document_json_path), doc)
        return {"ok": True, "equations_updated": count, "document_json_path": str(document_json_path)}
    except Exception as e:
        return {"ok": False, "error": repr(e)}
