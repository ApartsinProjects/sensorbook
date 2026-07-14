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

from posixpath import relpath

# any local href that targets a chapter's module dir or a section file
HREF_RE = re.compile(r'(href=")([^"]*?(?:module-\d+-[^"]*?/(?:index\.html|section-[0-9.]+\.html)|section-\d+\.[0-9.]+\.html))(")')


def _chapter_of(url: str) -> int | None:
    m = re.search(r"module-(\d+)-", url)
    if m:
        return int(m.group(1))
    m = re.search(r"section-(\d+)\.[0-9.]+\.html$", url)
    if m:
        return int(m.group(1))
    return None


def fix_file(f: Path) -> int:
    text = f.read_text(encoding="utf-8")
    fixed = 0
    here = str(f.parent.relative_to(ROOT)).replace("\\", "/")

    def repl(m):
        nonlocal fixed
        pre, url, post = m.group(1), m.group(2), m.group(3)
        if (f.parent / url).resolve().exists():
            return m.group(0)  # already valid, leave it
        num = _chapter_of(url)
        target = CH_INDEX.get(num) if num else None
        if not target:
            return m.group(0)
        fixed += 1
        return f"{pre}{relpath(target, here)}{post}"

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
