#!/usr/bin/env python3
"""Post-draft check for one Part: repair cross-refs, then validate the drafted
sections (house head, closing tag, no em/en dashes, no data-agent stamps,
substantial body, resolving links). Prints a one-line PASS/FAIL summary.

Run per part after its draft workflow; then `git add <partdir> && commit`.
Full index/section_index regeneration is deferred to a single scaffold run at
the end of the campaign.

Usage: python scripts/finish_part.py <partdir>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import fix_xrefs

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    partdir = ROOT / sys.argv[1]
    files = sorted(partdir.rglob("section-*.html"))
    fixed = sum(fix_xrefs.fix_file(f) for f in files)

    hh = cc = dashes = da = small = broken = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        if "pygments.css" in t and "book.js" in t and " | Building Sensory AI</title>" in t:
            hh += 1
        if t.rstrip().endswith("</html>"):
            cc += 1
        if re.search(r"—|–| -- ", t):
            dashes += 1
        if "data-agent" in t:
            da += 1
        mm = re.search(r"<main.*?</main>", t, re.DOTALL)
        if not mm or len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", mm.group(0)))) < 500:
            small += 1
        for m in re.finditer(r'(?:href|src)="([^"#]+)', t):
            u = m.group(1)
            if u.startswith(("http", "mailto", "data")) or "vendor/" in u or "pagefind/" in u:
                continue
            if not (f.parent / u).resolve().exists():
                broken += 1
    n = len(files)
    ok = (hh == n and cc == n and dashes == 0 and da == 0 and small == 0 and broken == 0)
    print(f"{'PASS' if ok else 'FAIL'} {sys.argv[1]}: {n} files | head {hh} close {cc} "
          f"| dashes {dashes} data-agent {da} small {small} broken {broken} | xref-fixed {fixed}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
