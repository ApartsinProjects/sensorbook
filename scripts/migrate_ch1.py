#!/usr/bin/env python3
"""One-shot migration of the Chapter 1 draft from the old scaffold convention
(part-01/chapter-01/sections/section-1-N.html, 3 levels deep) to the house
convention (part-1/module-01/section-1.N.html, 2 levels deep).

For each old section it: extracts the <main> content, rewrites in-body cross
-reference hrefs to the new convention, and rebuilds the page with the house
head/header/footer. Writes rebuilt pages to --out (default: scratchpad), so the
old tree can be wiped before the new scaffold runs.

Usage: python scripts/migrate_ch1.py --out <dir>
"""
from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path
from posixpath import normpath, relpath

import scaffold  # reuse slugify / naming / head / footer

ROOT = Path(__file__).resolve().parent.parent
OLD_DIR = ROOT / "part-01-foundations-of-sensory-ai" / "chapter-01-what-is-sensory-ai" / "sections"


def new_target(old_rel: str) -> str:
    """Map an old-convention repo-relative path to the new convention."""
    t = re.sub(r"^part-0*(\d+)-", lambda m: f"part-{int(m.group(1))}-", old_rel)
    t = re.sub(r"/chapter-(\d+)-", r"/module-\1-", t)
    t = re.sub(r"/sections/section-(\d+)-(\d+)\.html", r"/section-\1.\2.html", t)
    return t


def rewrite_href(url: str, old_file_rel: str, new_file_rel: str) -> str:
    if url.startswith(("http://", "https://", "mailto:", "data:", "#")):
        return url
    frag = ""
    if "#" in url:
        url, frag = url.split("#", 1)
        frag = "#" + frag
    old_dir = old_file_rel.rsplit("/", 1)[0]
    target_old = normpath(f"{old_dir}/{url}")           # repo-relative (old)
    target_new = new_target(target_old)                  # repo-relative (new)
    new_dir = new_file_rel.rsplit("/", 1)[0]
    return relpath(target_new, new_dir) + frag


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    structure = json.loads((ROOT / "scripts" / "book_structure.json").read_text(encoding="utf-8"))
    part = structure["parts"][0]
    chap = part["chapters"][0]
    sec_title = {s["id"]: s["title"] for s in chap["sections"]}
    new_mod_rel = f"{scaffold.part_dir(part)}/{scaffold.module_dir(chap)}"

    for s in chap["sections"]:
        sid = s["id"]                      # "1.1"
        old_name = f"section-{sid.replace('.', '-')}.html"
        old_path = OLD_DIR / old_name
        if not old_path.exists():
            print(f"SKIP missing {old_name}")
            continue
        old_file_rel = f"part-01-foundations-of-sensory-ai/chapter-01-what-is-sensory-ai/sections/{old_name}"
        new_file_rel = f"{new_mod_rel}/section-{sid}.html"

        html = old_path.read_text(encoding="utf-8")
        m = re.search(r"<main\b[^>]*>(.*)</main>", html, re.DOTALL)
        inner = m.group(1) if m else ""

        # rewrite every href/src in the body to the new convention
        def _sub(mo):
            attr, q, url = mo.group(1), mo.group(2), mo.group(3)
            return f'{attr}={q}{rewrite_href(url, old_file_rel, new_file_rel)}{q}'
        inner = re.sub(r'(href|src)=(["\'])([^"\']*)\2', _sub, inner)

        title = sec_title[sid]
        desc = f"Section {sid}: {title}. {scaffold.BOOK_TITLE}."
        page = (
            scaffold.head("../../", f"Section {sid}: {title} | {scaffold.BOOK_TITLE}", desc, math=True)
            + '<header class="chapter-header">\n<nav class="header-nav">\n'
            f'<a class="book-title-link" href="../../index.html">{escape(scaffold.BOOK_TITLE)}</a>\n'
            '<a class="toc-link" href="../../toc.html" title="Table of Contents">'
            '<span class="toc-icon">&#9776;</span> Contents</a>\n</nav>\n'
            f'<div class="part-label"><a href="../index.html">Part {part["roman"]}: {escape(part["title"])}</a></div>\n'
            f'<div class="chapter-label"><a href="index.html">Chapter {chap["number"]}: {escape(chap["title"])}</a></div>\n'
            f'<h1>{escape(title)}</h1>\n</header>\n'
            '<main class="content" id="main-content">'
            + inner +
            "</main>\n" + scaffold.footer("../../")
        )
        (out / f"section-{sid}.html").write_text(page, encoding="utf-8")
        print(f"rebuilt section-{sid}.html")


if __name__ == "__main__":
    main()
