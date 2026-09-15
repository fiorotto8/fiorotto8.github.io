#!/usr/bin/env python3
"""Create the selected web photographs; optional Pillow tooling, not a build step."""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / 'docs/PHOTO_SOURCES.json').read_text())
destination = ROOT / 'images/public'
destination.mkdir(parents=True, exist_ok=True)
photos = {}
for entry in sources:
    if not entry['widths']:
        continue
    source = ROOT / entry['source']
    if hashlib.sha256(source.read_bytes()).hexdigest() != entry['sha256']:
        raise SystemExit(f'Source changed; review and update provenance first: {source}')
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert('RGB')
        variants = []
        for width in entry['widths']:
            if width > image.width:
                raise SystemExit(f'Do not upscale {source} to {width}px')
            height = round(image.height * width / image.width)
            output = destination / entry['area'] / f'{entry["key"]}-{width}.webp'
            output.parent.mkdir(parents=True, exist_ok=True)
            image.resize((width, height), Image.Resampling.LANCZOS).save(
                output, 'WEBP', quality=84, method=6, lossless=entry['lossless'])
            variants.append({'src': '/' + output.relative_to(ROOT).as_posix(),
                             'width': width, 'height': height})
        photos[entry['key']] = {**variants[-1], 'variants': variants}
(ROOT / '_data/photos.json').write_text(json.dumps(photos, indent=2) + '\n')
print(f'Prepared {len(photos)} images; {sum(p.stat().st_size for p in destination.rglob("*.webp")) // 1024} KiB across all sizes.')
