#!/usr/bin/env python3
"""Scaffold the Building Sensory AI book tree from the plan file.

Single source of truth: ``building_sensory_ai_book_plan.md`` in the repo root.
This script PARSES that plan and MATERIALIZES the directory/build structure used
by the book-skills / html2epub / epub2kpf pipeline, matching the series house
convention (as in the Building Vision AI book):

    part-N-slug/
        index.html                      (part landing page)
        module-NN-slug/
            index.html                  (chapter landing page, lists sections)
            section-N.M.html            (section pages, written by the pipeline)

Note: directories use ``module-NN`` (house convention, so the book-skills
``part-*/module-*/section-*.html`` globs match), while prose uses Part > Chapter
> Section. Section files live directly in the module dir (no ``sections/``
subdir) and are named ``section-<id>.html`` with a dot (e.g. section-1.1.html).

Also emits ``scripts/book_structure.json`` and ``scripts/section_index.json``,
refreshes the root ``index.html`` / ``toc.html``, and regenerates the marked
chapter-map block of ``BOOK_CONFIG.md``.

Usage:
    python scripts/scaffold.py            # parse plan, build tree + indexes
    python scripts/scaffold.py --check    # parse only, print a summary
"""
from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "building_sensory_ai_book_plan.md"
BOOK_TITLE = "Building Sensory AI"
BOOK_FULL = "Building Sensory AI: Machine Perception of the Physical World"

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14,
}

PART_RE = re.compile(r"^#\s+Part\s+([IVXL]+)\s+·\s+(.+?)\s*$")
CHAP_RE = re.compile(r"^##\s+Chapter\s+(\d+)\.\s+(.+?)\s*$")
SEC_RE = re.compile(r"^(\d+)\.(\d+)\s+(.+?)\s*$")
LAB_RE = re.compile(r"^\*\*Lab\s+\d+:\*\*\s*(.+?)\s*$")
TAG_RE = re.compile(r"\*\*((?:\[[FCAR]+\])+)\*\*\s*$")


def slugify(text: str, maxlen: int = 48) -> str:
    text = text.lower()
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0]
    return text


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(?:\[[FCAR]+\])+\*\*", "", text)  # level tags
    text = re.sub(r"\s*—\s*\*\*.*?\*\*", "", text)          # trailing bold aside
    text = re.sub(r"\*\((.*?)\)\*", "", text)               # *(verb)* annotation
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def parse_plan() -> dict:
    parts: list[dict] = []
    cur_part = cur_chap = None
    for raw in PLAN.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        m = PART_RE.match(line)
        if m:
            verb = ""
            vm = re.search(r"\*\((.*?)\)\*", line)
            if vm:
                verb = vm.group(1)
            cur_part = {"number": ROMAN[m.group(1)], "roman": m.group(1),
                        "title": strip_md(m.group(2)), "verb": verb, "chapters": []}
            parts.append(cur_part)
            cur_chap = None
            continue
        m = CHAP_RE.match(line)
        if m and cur_part is not None:
            tm = TAG_RE.search(line)
            cur_chap = {"number": int(m.group(1)), "title": strip_md(m.group(2)),
                        "levels": tm.group(1) if tm else "", "sections": [], "lab": ""}
            cur_part["chapters"].append(cur_chap)
            continue
        m = SEC_RE.match(line)
        if m and cur_chap is not None and int(m.group(1)) == cur_chap["number"]:
            cur_chap["sections"].append({"id": f"{m.group(1)}.{m.group(2)}",
                                         "title": strip_md(m.group(3))})
            continue
        m = LAB_RE.match(line)
        if m and cur_chap is not None:
            cur_chap["lab"] = strip_md(m.group(1))
    return {"parts": parts}


def part_dir(part: dict) -> str:
    return f"part-{part['number']}-{slugify(part['title'])}"


def module_dir(chap: dict) -> str:
    return f"module-{chap['number']:02d}-{slugify(chap['title'])}"


def section_file(sec_id: str) -> str:
    return f"section-{sec_id}.html"


# ---- house head/nav fragments (depth-parameterized) ----

def head(up: str, title: str, desc: str, math: bool = False) -> str:
    katex = ""
    if math:
        katex = (
            f'<link href="{up}vendor/katex/katex.min.css" rel="stylesheet"/>\n'
            f'<script defer src="{up}vendor/katex/katex.min.js"></script>\n'
            f'<script defer onload="renderMathInElement(document.body, {{\n'
            f"  delimiters: [\n"
            f"  {{left: '$$', right: '$$', display: true}},\n"
            f"  {{left: '\\\\[', right: '\\\\]', display: true}},\n"
            f"  {{left: '\\\\(', right: '\\\\)', display: false}}\n"
            f"  ],\n  throwOnError: false\n"
            f'  }});" src="{up}vendor/katex/contrib/auto-render.min.js"></script>\n'
            f'<link href="{up}vendor/prism/prism-theme.css" rel="stylesheet"/>\n'
            f'<script defer src="{up}vendor/prism/prism-bundle.min.js"></script>\n'
        )
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\"/>\n"
        "<meta content=\"width=device-width, initial-scale=1.0\" name=\"viewport\"/>\n"
        f"<meta content=\"{escape(desc)}\" name=\"description\"/>\n"
        f"<title>{escape(title)}</title>\n"
        f"<link href=\"{up}styles/book.css\" rel=\"stylesheet\"/>\n"
        f"<link href=\"{up}styles/pygments.css\" rel=\"stylesheet\"/>\n"
        f"{katex}"
        f"<script defer src=\"{up}scripts/book.js\"></script>\n"
        "</head>\n<body>\n"
        "<a class=\"skip-link\" href=\"#main-content\">Skip to main content</a>\n"
    )


def footer(up: str) -> str:
    return (
        "<footer>\n"
        f"<p class=\"footer-title\">{escape(BOOK_FULL)}</p>\n"
        f"<p>&#169; 2026 Alexander Apartsin &amp; Yehudit Aperstein &#183; <a href=\"{up}toc.html\">Contents</a></p>\n"
        "</footer>\n</body>\n</html>\n"
    )


def build(structure: dict) -> None:
    toc_parts = []
    for part in structure["parts"]:
        pdir = ROOT / part_dir(part)
        pdir.mkdir(exist_ok=True)
        verb = f" &#183; <em>{escape(part['verb'])}</em>" if part["verb"] else ""

        cards, toc_chaps = [], []
        for chap in part["chapters"]:
            mdir = pdir / module_dir(chap)
            mdir.mkdir(exist_ok=True)
            rel = f"{module_dir(chap)}/index.html"
            levels = f' <span class="levels">{escape(chap["levels"])}</span>' if chap["levels"] else ""
            cards.append(
                f'<a class="section-card" href="{rel}">'
                f'<span class="card-num">Ch {chap["number"]}</span>'
                f'<span class="card-title">{escape(chap["title"])}</span>{levels}</a>'
            )
            sec_items = []
            for s in chap["sections"]:
                fname = section_file(s["id"])
                exists = (mdir / fname).exists()
                label = f'<span class="sec-id">{escape(s["id"])}</span> {escape(s["title"])}'
                sec_items.append(
                    f'<li><a href="{fname}">{label}</a></li>' if exists else f"<li>{label}</li>"
                )
            (mdir / "index.html").write_text(
                head("../../", f"Chapter {chap['number']}. {chap['title']} | {BOOK_TITLE}",
                     f"Chapter {chap['number']}: {chap['title']}. {BOOK_TITLE}.")
                + '<header class="chapter-header">\n<nav class="header-nav">\n'
                f'<a class="book-title-link" href="../../index.html">{escape(BOOK_TITLE)}</a>\n'
                '<a class="toc-link" href="../../toc.html" title="Table of Contents">'
                '<span class="toc-icon">&#9776;</span> Contents</a>\n</nav>\n'
                f'<div class="part-label"><a href="../index.html">Part {part["roman"]}: {escape(part["title"])}</a></div>\n'
                f'<div class="chapter-label">Chapter {chap["number"]}'
                + (f' &nbsp;<span class="levels">{escape(chap["levels"])}</span>' if chap["levels"] else "")
                + f'</div>\n<h1>{escape(chap["title"])}</h1>\n</header>\n'
                '<main class="content" id="main-content">\n'
                '<p class="status-note">Placeholder chapter page. Sections are produced by the book-skills pipeline.</p>\n'
                "<h2>Sections</h2>\n<ol class=\"section-list\">\n" + "\n".join(sec_items) + "\n</ol>\n"
                f'<div class="callout lab"><h3 class="callout-title">Lab {chap["number"]}</h3><p>{escape(chap["lab"] or "TBD")}</p></div>\n'
                "</main>\n" + footer("../../"),
                encoding="utf-8",
            )
            toc_chaps.append(
                f'<li><a href="{part_dir(part)}/{rel}">Ch {chap["number"]}. '
                f'{escape(chap["title"])}</a> {escape(chap["levels"])}</li>'
            )

        (pdir / "index.html").write_text(
            head("../", f"Part {part['roman']}: {part['title']} | {BOOK_TITLE}",
                 f"Part {part['roman']}: {part['title']}. {BOOK_TITLE}.")
            + '<header class="chapter-header">\n<nav class="header-nav">\n'
            f'<a class="book-title-link" href="../index.html">{escape(BOOK_TITLE)}</a>\n'
            '<a class="toc-link" href="../toc.html" title="Table of Contents">'
            '<span class="toc-icon">&#9776;</span> Contents</a>\n</nav>\n'
            f'<div class="part-label">Part {part["roman"]}{verb}</div>\n<h1>{escape(part["title"])}</h1>\n</header>\n'
            '<main class="content" id="main-content">\n<h2>Chapters</h2>\n'
            '<div class="section-card-grid">\n' + "\n".join(cards) + "\n</div>\n</main>\n" + footer("../"),
            encoding="utf-8",
        )
        toc_parts.append(
            f'<h2><a href="{part_dir(part)}/index.html">Part {part["roman"]}. {escape(part["title"])}</a></h2>\n'
            '<ul class="toc-chapter-list">\n' + "\n".join(toc_chaps) + "\n</ul>"
        )

    front_block = (
        '<h2>Front Matter</h2>\n<ul class="toc-chapter-list">\n'
        '<li><a href="front-matter/foreword.html">Foreword</a></li>\n'
        '<li><a href="front-matter/fm-what-this-book-covers.html">What This Book Covers</a></li>\n'
        '<li><a href="front-matter/fm-who-should-read.html">Who Should Read This Book</a></li>\n'
        '<li><a href="front-matter/fm-how-to-use.html">How to Use This Book</a></li>\n'
        '<li><a href="front-matter/about-authors.html">About the Authors</a></li>\n'
        '<li><a href="front-matter/about-the-series.html">About the Series</a></li>\n'
        '<li><a href="front-matter/copyright.html">Copyright</a></li>\n</ul>'
    )
    appx = [
        ("a-math-reference", "A. Mathematical and Signal-Processing Reference"),
        ("b-deep-learning-refresher", "B. Deep Learning Refresher for Sequences and Tensors"),
        ("c-sensor-hardware", "C. Sensor Hardware Guide"),
        ("d-toolchain", "D. The Sensory AI Toolchain"),
        ("e-datasets-benchmarks", "E. Sensor Datasets and Benchmarks"),
        ("f-evaluation-metrics", "F. Evaluation Metrics Reference"),
        ("g-synthetic-data", "G. Synthetic Data and Simulation Resources"),
        ("h-course-syllabi", "H. Course Syllabi"),
        ("i-solutions", "I. Solutions to Selected Exercises"),
        ("j-notation-glossary", "J. Notation and Glossary"),
    ]
    appx_block = (
        '<h2><a href="appendices/index.html">Appendices</a></h2>\n<ul class="toc-chapter-list">\n'
        + "\n".join(f'<li><a href="appendices/appendix-{slug}/index.html">Appendix {title}</a></li>' for slug, title in appx)
        + "\n</ul>"
    )
    capstone_block = (
        '<h2><a href="capstone/index.html">Capstone</a></h2>\n<ul class="toc-chapter-list">\n'
        '<li><a href="capstone/index.html">End-to-End Sensory AI System</a></li>\n</ul>'
    )
    toc_body = front_block + "\n" + "\n".join(toc_parts) + "\n" + appx_block + "\n" + capstone_block
    # NOTE: index.html is the house-style landing page, authored by
    # scripts/gen_landing.py. This script owns toc.html only and must never
    # overwrite the landing page.
    (ROOT / "toc.html").write_text(
        head("", f"Contents | {BOOK_TITLE}", f"Table of contents. {BOOK_TITLE}.")
        + '<header class="chapter-header">\n<nav class="header-nav">\n'
        f'<a class="book-title-link" href="index.html">{escape(BOOK_TITLE)}</a>\n</nav>\n'
        '<div class="part-label">Table of Contents</div>\n'
        f'<h1>{escape(BOOK_TITLE)}</h1>\n<p class="chapter-subtitle">Machine Perception of the Physical World</p>\n</header>\n'
        '<main class="content" id="main-content">\n' + toc_body + "\n</main>\n" + footer(""),
        encoding="utf-8",
    )

    (ROOT / "scripts" / "book_structure.json").write_text(
        json.dumps(structure, indent=2, ensure_ascii=False), encoding="utf-8")
    write_section_index(structure)
    refresh_book_config(structure)


def write_section_index(structure: dict) -> None:
    index = []
    for part in structure["parts"]:
        pd = part_dir(part)
        for chap in part["chapters"]:
            md = module_dir(chap)
            for s in chap["sections"]:
                rel = f"{pd}/{md}/{section_file(s['id'])}"
                if (ROOT / rel).exists():
                    index.append({"sec": s["id"], "title": s["title"], "path": rel})
    (ROOT / "scripts" / "section_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"section_index.json: {len(index)} written sections")


def refresh_book_config(structure: dict) -> None:
    cfg = ROOT / "BOOK_CONFIG.md"
    if not cfg.exists():
        return
    start = "<!-- CHAPTER-MAP:START (generated by scripts/scaffold.py — do not edit by hand) -->"
    end = "<!-- CHAPTER-MAP:END -->"
    text = cfg.read_text(encoding="utf-8")
    if start not in text or end not in text:
        return
    rows = [start, ""]
    for p in structure["parts"]:
        verb = f"  *({p['verb']})*" if p["verb"] else ""
        rows.append(f"### Part {p['roman']}: {p['title']} (Ch {p['chapters'][0]['number']}-{p['chapters'][-1]['number']}){verb}")
        for c in p["chapters"]:
            rows.append(f"- Chapter {c['number']}: {c['title']}" + (f"  `{c['levels']}`" if c["levels"] else ""))
        rows.append("")
    rows.append(end)
    cfg.write_text(re.sub(re.escape(start) + r".*?" + re.escape(end), "\n".join(rows), text, flags=re.DOTALL),
                   encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="parse only, write nothing")
    args = ap.parse_args()
    structure = parse_plan()
    nparts = len(structure["parts"])
    nchaps = sum(len(p["chapters"]) for p in structure["parts"])
    nsecs = sum(len(c["sections"]) for p in structure["parts"] for c in p["chapters"])
    print(f"Parsed {nparts} parts, {nchaps} chapters, {nsecs} sections.")
    if args.check:
        for p in structure["parts"]:
            print(f"  Part {p['roman']:>4}  {p['title']}  ({len(p['chapters'])} ch)")
        return
    build(structure)
    print(f"Scaffolded tree under {ROOT}")


if __name__ == "__main__":
    main()
