#!/usr/bin/env python3
"""Emit one self-contained draft workflow per Part from draft_specs.json,
reusing the exact writer logic in draft_part.js (only the data source changes:
`const part = args` becomes the part's baked-in object). Writes
scripts/draft-part-NN.js for every part that has unwritten sections.

Usage: python scripts/gen_draft_waves.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
specs = json.loads((HERE / "draft_specs.json").read_text(encoding="utf-8"))
template = (HERE / "draft_part.js").read_text(encoding="utf-8")
anchor = "const part = args // { part_roman, part_title, sections:[...], chapter_hrefs:{...} }"
assert anchor in template, "anchor line not found in draft_part.js"

hrefs = specs["chapter_hrefs"]
written = []
for key in sorted(specs["parts"]):
    p = specs["parts"][key]
    part_obj = {
        "part_roman": p["part_roman"],
        "part_title": p["part_title"],
        "sections": p["sections"],
        "chapter_hrefs": hrefs,
    }
    embedded = "const part = " + json.dumps(part_obj, ensure_ascii=False)
    script = template.replace(anchor, embedded)
    # unique meta name per part
    script = script.replace("name: 'draft-part',", f"name: 'draft-{key}',")
    out = HERE / f"draft-{key}.js"
    out.write_bytes(script.replace("\r\n", "\n").encode("utf-8"))
    written.append((out.name, len(p["sections"]), len(script)))

for name, n, size in written:
    print(f"  {name}: {n} sections, {size:,} chars, under 512k: {size < 524288}")
print(f"generated {len(written)} draft scripts")
