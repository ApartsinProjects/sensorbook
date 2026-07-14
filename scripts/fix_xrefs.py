#!/usr/bin/env python3
"""Repair broken cross-chapter links in drafted sections.

Agents occasionally construct a cross-reference href with the wrong part dir
(e.g. chapter 6 under part-1 instead of part-2). Any href pointing at a
`.../module-NN-.../index.html` that does not resolve is replaced with the
authoritative href for chapter NN (computed from the plan via scaffold).

Usage: python scripts/fix_xrefs.py <glob-or-dir> [...]
       python scripts/fix_xrefs.py part-1-foundations-of-sensory-ai
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import scaffold

ROOT = Path(__file__).resolve().parent.parent

# chapter number -> authoritative repo-relative module index path
CH_INDEX = {}
for part in scaffold.parse_plan()["parts"]:
    for chap in part["chapters"]:
        CH_INDEX[chap["number"]] = f"{scaffold.part_dir(part)}/{scaffold.module_dir(chap)}/index.html"

HREF_RE = re.compile(r'(href=")([^"]*?module-(\d+)-[^"]*?/index\.html)(")')


def fix_file(f: Path) -> int:
    text = f.read_text(encoding="utf-8")
    fixed = 0

    def repl(m):
        nonlocal fixed
        pre, url, num, post = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        if (f.parent / url).resolve().exists():
            return m.group(0)  # already valid
        target = CH_INDEX.get(num)
        if not target:
            return m.group(0)
        # relative path from this file's dir to the authoritative target
        from posixpath import relpath
        rel = relpath(target, str(f.parent.relative_to(ROOT)).replace("\\", "/"))
        fixed += 1
        return f"{pre}{rel}{post}"

    new = HREF_RE.sub(repl, text)
    if fixed:
        f.write_text(new, encoding="utf-8")
    return fixed


def main() -> None:
    targets = sys.argv[1:] or ["."]
    files = []
    for t in targets:
        p = ROOT / t
        if p.is_dir():
            files += list(p.rglob("section-*.html"))
        else:
            files += [ROOT / x for x in Path(".").glob(t)]
    total = sum(fix_file(f) for f in files)
    print(f"fixed {total} broken cross-chapter links across {len(files)} files")


if __name__ == "__main__":
    main()
