# -*- coding: utf-8 -*-
"""Pixelate faces in site photos (excludes hero range-ai.png and snow.jpg)."""
from __future__ import annotations

import shutil
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BACKUP = ROOT / "tools" / "_photo_backup"
MODEL = Path(__file__).resolve().parent / "face_detection_yunet_2023mar.onnx"

# Exclude: top/join hero + winter camp
SKIP = {"range-ai.png", "snow.jpg", "logo.png"}

# Photos known to show people (used on site + related)
TARGETS = [
    "bbq.jpg",
    "clean-group.jpg",
    "bunkasai.jpg",
    "range-real.jpg",
    "horse.jpg",
    "clean-break.jpg",
    "clean-daily.jpg",
]


def detect_faces(img: np.ndarray) -> list[tuple[int, int, int, int]]:
    h, w = img.shape[:2]
    boxes: list[tuple[int, int, int, int]] = []

    detector = cv2.FaceDetectorYN.create(str(MODEL), "", (w, h), 0.35, 0.3, 5000)
    detector.setInputSize((w, h))
    _, faces = detector.detect(img)
    if faces is not None:
        for f in faces:
            x, y, bw, bh = [int(v) for v in f[:4]]
            boxes.append((x, y, bw, bh))

    # Second pass at larger / smaller scales helps group shots
    for scale in (0.6, 1.4):
        sw, sh = max(32, int(w * scale)), max(32, int(h * scale))
        resized = cv2.resize(img, (sw, sh))
        detector.setInputSize((sw, sh))
        _, faces2 = detector.detect(resized)
        if faces2 is None:
            continue
        for f in faces2:
            x, y, bw, bh = [float(v) for v in f[:4]]
            x = int(x / scale)
            y = int(y / scale)
            bw = int(bw / scale)
            bh = int(bh / scale)
            boxes.append((x, y, bw, bh))

    return merge_boxes(boxes, img.shape[1], img.shape[0])


def merge_boxes(
    boxes: list[tuple[int, int, int, int]], w: int, h: int, iou_thresh: float = 0.35
) -> list[tuple[int, int, int, int]]:
    cleaned = []
    for x, y, bw, bh in boxes:
        if bw < 8 or bh < 8:
            continue
        x = max(0, x)
        y = max(0, y)
        bw = min(bw, w - x)
        bh = min(bh, h - y)
        if bw < 8 or bh < 8:
            continue
        cleaned.append((x, y, bw, bh))

    cleaned.sort(key=lambda b: b[2] * b[3], reverse=True)
    kept: list[tuple[int, int, int, int]] = []
    for box in cleaned:
        if any(iou(box, k) > iou_thresh for k in kept):
            continue
        kept.append(box)
    return kept


def iou(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> float:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    x1, y1 = max(ax, bx), max(ay, by)
    x2, y2 = min(ax + aw, bx + bw), min(ay + ah, by + bh)
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    if inter == 0:
        return 0.0
    return inter / float(aw * ah + bw * bh - inter)


def apply_mosaic(img: np.ndarray, boxes: list[tuple[int, int, int, int]]) -> np.ndarray:
    out = img.copy()
    h, w = out.shape[:2]
    for x, y, bw, bh in boxes:
        pad = int(max(bw, bh) * 0.42)
        x0 = max(0, x - pad)
        y0 = max(0, y - pad)
        x1 = min(w, x + bw + pad)
        y1 = min(h, y + bh + pad)
        rw, rh = x1 - x0, y1 - y0
        if rw < 4 or rh < 4:
            continue
        # Very coarse blocks so faces are unrecognizable
        blocks = max(3, min(7, min(rw, rh) // 28))
        roi = out[y0:y1, x0:x1]
        small = cv2.resize(roi, (blocks, blocks), interpolation=cv2.INTER_LINEAR)
        mosaic = cv2.resize(small, (rw, rh), interpolation=cv2.INTER_NEAREST)
        out[y0:y1, x0:x1] = mosaic
    return out


def process(name: str) -> None:
    src = ASSETS / name
    if not src.exists() or name in SKIP:
        print(f"skip {name}")
        return
    BACKUP.mkdir(parents=True, exist_ok=True)
    bak = BACKUP / name
    if not bak.exists():
        shutil.copy2(src, bak)

    # Always process from original backup
    data = np.fromfile(str(bak), dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        raise SystemExit(f"failed to read {bak}")

    boxes = detect_faces(img)
    print(f"{name}: {len(boxes)} faces")
    if not boxes:
        print(f"  WARNING: no faces detected in {name}")
        return

    out = apply_mosaic(img, boxes)
    ext = src.suffix.lower()
    if ext in {".jpg", ".jpeg"}:
        ok, buf = cv2.imencode(".jpg", out, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    else:
        ok, buf = cv2.imencode(".png", out)
    if not ok:
        raise SystemExit(f"encode failed {name}")
    tmp = src.with_suffix(src.suffix + ".tmp")
    buf.tofile(str(tmp))
    tmp.replace(src)
    print(f"  wrote {src}")


def main() -> None:
    for name in TARGETS:
        process(name)


if __name__ == "__main__":
    main()
