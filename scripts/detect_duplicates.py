#!/usr/bin/env python
"""Detect near-duplicate text blocks across all built section files in the book.

Extracts callout blocks and paragraphs from every section-*.html file, then
computes pairwise similarity (difflib ratio on normalized token sets). Pairs at
or above the threshold are written to scripts/dedup_report.json for the
deduplication pass to act on.
"""
import json
import os
import re
import sys
from difflib import SequenceMatcher
from html.parser import HTMLParser

THRESHOLD = 0.55


def find_book_root(argv):
    for i, a in enumerate(argv):
        if a == "--book-root" and i + 1 < len(argv):
            return argv[i + 1]
    return os.getcwd()


class BlockExtractor(HTMLParser):
    """Collect visible text grouped by block-level callouts and paragraphs."""

    BLOCK_TAGS = {"p", "li", "h2", "h3", "h4", "blockquote"}

    def __init__(self):
        super().__init__()
        self.blocks = []
        self._buf = []
        self._depth = 0
        self._capture = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK_TAGS:
            self._capture += 1

    def handle_endtag(self, tag):
        if tag in self.BLOCK_TAGS and self._capture > 0:
            self._capture -= 1
            text = " ".join("".join(self._buf).split())
            if len(text) >= 40:
                self.blocks.append(text)
            self._buf = []

    def handle_data(self, data):
        if self._capture > 0:
            self._buf.append(data)


def normalize(text):
    text = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    return " ".join(text.split())


def collect_sections(root):
    sections = {}
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if re.match(r"section-.*\.html$", fn):
                path = os.path.join(dirpath, fn)
                with open(path, encoding="utf-8") as fh:
                    parser = BlockExtractor()
                    parser.feed(fh.read())
                rel = os.path.relpath(path, root).replace("\\", "/")
                sections[rel] = parser.blocks
    return sections


def main():
    root = find_book_root(sys.argv)
    sections = collect_sections(root)
    items = []  # (section, index, normalized_text, raw_text)
    for sec, blocks in sections.items():
        for i, b in enumerate(blocks):
            items.append((sec, i, normalize(b), b))

    pairs = []
    n = len(items)
    for i in range(n):
        si, ii, ni, ri = items[i]
        for j in range(i + 1, n):
            sj, ij, nj, rj = items[j]
            if si == sj:
                continue  # only cross-section duplication is of interest
            if abs(len(ni) - len(nj)) > max(len(ni), len(nj)) * 0.6:
                continue
            ratio = SequenceMatcher(None, ni, nj).ratio()
            if ratio >= THRESHOLD:
                pairs.append(
                    {
                        "similarity": round(ratio, 3),
                        "a": {"section": si, "block": ii, "text": ri[:280]},
                        "b": {"section": sj, "block": ij, "text": rj[:280]},
                    }
                )

    pairs.sort(key=lambda p: p["similarity"], reverse=True)
    report = {
        "threshold": THRESHOLD,
        "sections_scanned": len(sections),
        "blocks_scanned": n,
        "pairs": pairs,
    }
    out = os.path.join(root, "scripts", "dedup_report.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print(f"scanned {len(sections)} sections, {n} blocks")
    print(f"found {len(pairs)} candidate pair(s) at similarity >= {THRESHOLD}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
