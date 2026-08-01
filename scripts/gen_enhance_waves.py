#!/usr/bin/env python3
"""Emit one self-contained enhance workflow per part from enhance_specs.json,
reusing the exact logic in enhance_part.js (only the data source changes:
`const part = args` becomes the part's baked-in object).

Usage: python scripts/gen_enhance_waves.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
specs = json.loads((HERE / "enhance_specs.json").read_text(encoding="utf-8"))
template = (HERE / "enhance_part.js").read_text(encoding="utf-8")
anchor = "const part = args // { part_roman, part_title, sections:[{path,sec_id,sec_title,ch_num,ch_title,levels}], chapter_hrefs:{...} }"
assert anchor in template, "anchor not found in enhance_part.js"

hrefs = specs["chapter_hrefs"]
written = []
for key in sorted(specs["parts"]):
    p = specs["parts"][key]
    obj = {"part_roman": p["part_roman"], "part_title": p["part_title"],
           "sections": p["sections"], "chapter_hrefs": hrefs}
    script = template.replace(anchor, "const part = " + json.dumps(obj, ensure_ascii=False))
    script = script.replace("name: 'enhance-part',", f"name: 'enhance-{key}',")
    out = HERE / f"enhance-{key}.js"
    out.write_bytes(script.replace("\r\n", "\n").encode("utf-8"))
    written.append((out.name, len(p["sections"]), len(script)))

for name, n, size in written:
    print(f"  {name}: {n} sections, {size:,} chars, under 512k: {size < 524288}")
print(f"generated {len(written)} enhance scripts")
