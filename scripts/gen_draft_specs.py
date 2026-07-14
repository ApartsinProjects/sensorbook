#!/usr/bin/env python3
"""Precompute per-section draft specs for every UNWRITTEN section, grouped by
part, for the draft-only pass. Writes scripts/draft_specs.json.

Each spec carries everything a section-writer agent needs to produce a
house-convention page (part-N/module-NN/section-N.M.html) without re-deriving
paths: routing links, neighbor labels, lab text (last section), and sibling
section titles (for anti-overlap). Sections whose file already exists are
skipped, so re-runs only fill gaps.

Usage: python scripts/gen_draft_specs.py
"""
from __future__ import annotations

import json
from pathlib import Path

import scaffold

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    structure = scaffold.parse_plan()
    # global ordered chapter list for cross-chapter "next" links
    chapters = []
    for part in structure["parts"]:
        for chap in part["chapters"]:
            chapters.append((part, chap))

    # global map: chapter number -> {href from any section (depth ../../), title, levels}
    chapter_hrefs = {}
    for part, chap in chapters:
        href = f"../../{scaffold.part_dir(part)}/{scaffold.module_dir(chap)}/index.html"
        chapter_hrefs[str(chap["number"])] = {"href": href, "title": chap["title"], "levels": chap["levels"]}

    by_part: dict[str, dict] = {}
    total = skipped = 0
    for gi, (part, chap) in enumerate(chapters):
        pdir = scaffold.part_dir(part)
        mdir = scaffold.module_dir(chap)
        secs = chap["sections"]
        sibs = [f'{s["id"]} {s["title"]}' for s in secs]
        # next chapter (global order) for last-section link
        nxt = chapters[gi + 1] if gi + 1 < len(chapters) else None
        for si, s in enumerate(secs):
            rel = f"{pdir}/{mdir}/{scaffold.section_file(s['id'])}"
            if (ROOT / rel).exists():
                skipped += 1
                continue
            first = si == 0
            last = si == len(secs) - 1
            if first:
                prev_link, prev_label = "index.html", f"Chapter {chap['number']}"
            else:
                pid = secs[si - 1]["id"]
                prev_link, prev_label = f"section-{pid}.html", f"Section {pid}"
            if last:
                if nxt:
                    np, nc = nxt
                    prev_p, prev_m = scaffold.part_dir(np), scaffold.module_dir(nc)
                    next_link = f"../../{prev_p}/{prev_m}/index.html"
                    next_label = f"Chapter {nc['number']}"
                else:
                    next_link, next_label = "../../toc.html", "Contents"
            else:
                nid = secs[si + 1]["id"]
                next_link, next_label = f"section-{nid}.html", f"Section {nid}"
            spec = {
                "path": rel,
                "part_roman": part["roman"], "part_title": part["title"],
                "ch_num": chap["number"], "ch_title": chap["title"], "levels": chap["levels"],
                "sec_id": s["id"], "sec_title": s["title"],
                "first": first, "last": last,
                "prev_link": prev_link, "prev_label": prev_label,
                "next_link": next_link, "next_label": next_label,
                "lab": chap["lab"] if last else "",
                "siblings": sibs,
            }
            key = f"part-{part['number']:02d}"
            by_part.setdefault(key, {"part_roman": part["roman"], "part_title": part["title"], "sections": []})
            by_part[key]["sections"].append(spec)
            total += 1

    (ROOT / "scripts" / "draft_specs.json").write_text(
        json.dumps({"chapter_hrefs": chapter_hrefs, "parts": by_part}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    print(f"draft_specs.json: {total} sections to draft, {skipped} already written")
    for k in sorted(by_part):
        v = by_part[k]
        print(f"  {k} (Part {v['part_roman']}): {len(v['sections'])} sections")


if __name__ == "__main__":
    main()
