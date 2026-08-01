#!/usr/bin/env python3
"""Precompute per-section enhance specs (Plan B lean sweep) grouped by part.

Covers chapters 6-72 EXCEPT the flagship chapters (which get the full 10-pack
pipeline) and skips chapters 1-5 (Ch1 done, Ch2-5 pilot). Emits
scripts/enhance_specs.json with a global chapter-href map plus per-part section
lists. Each section already exists and is house-styled; enhance edits in place.

Usage: python scripts/gen_enhance_specs.py
"""
from __future__ import annotations

import json
from pathlib import Path

import scaffold

ROOT = Path(__file__).resolve().parent.parent

# flagship chapters -> full 10-pack sweep (handled separately, not enhanced here)
FLAGSHIP = {9, 19, 29, 43, 68, 72}
SKIP_DONE = set(range(1, 6))  # Ch1 done, Ch2-5 pilot


def main() -> None:
    structure = scaffold.parse_plan()
    chapter_hrefs = {}
    for part in structure["parts"]:
        for chap in part["chapters"]:
            href = f"../../{scaffold.part_dir(part)}/{scaffold.module_dir(chap)}/index.html"
            chapter_hrefs[str(chap["number"])] = {"href": href, "title": chap["title"], "levels": chap["levels"]}

    by_part, total = {}, 0
    for part in structure["parts"]:
        pd = scaffold.part_dir(part)
        for chap in part["chapters"]:
            n = chap["number"]
            if n in FLAGSHIP or n in SKIP_DONE:
                continue
            md = scaffold.module_dir(chap)
            for s in chap["sections"]:
                rel = f"{pd}/{md}/{scaffold.section_file(s['id'])}"
                if not (ROOT / rel).exists():
                    continue
                key = f"part-{part['number']:02d}"
                by_part.setdefault(key, {"part_roman": part["roman"], "part_title": part["title"], "sections": []})
                by_part[key]["sections"].append({
                    "path": rel, "sec_id": s["id"], "sec_title": s["title"],
                    "ch_num": n, "ch_title": chap["title"], "levels": chap["levels"],
                })
                total += 1

    (ROOT / "scripts" / "enhance_specs.json").write_text(
        json.dumps({"chapter_hrefs": chapter_hrefs, "parts": by_part}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    print(f"enhance_specs.json: {total} sections to lean-enhance across {len(by_part)} parts")
    print(f"flagship chapters (full 10-pack, excluded here): {sorted(FLAGSHIP)}")
    for k in sorted(by_part):
        print(f"  {k}: {len(by_part[k]['sections'])} sections")


if __name__ == "__main__":
    main()
