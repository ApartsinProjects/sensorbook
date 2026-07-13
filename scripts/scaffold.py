#!/usr/bin/env python3
"""Scaffold the Building Sensory AI book tree from the plan file.

Single source of truth: ``building_sensory_ai_book_plan.md`` in the repo root.
This script PARSES that plan and MATERIALIZES the directory/build structure the
book-skills / html2epub / epub2kpf pipeline expects:

    part-NN-slug/
        index.html                      (part landing page)
        chapter-NN-slug/
            index.html                  (chapter landing page, lists sections)
            sections/                    (section-N-M.html files, written later)

It also emits ``scripts/book_structure.json`` (machine-readable chapter map used
by the build pipeline) and refreshes the root ``index.html`` table of contents.

Idempotent: re-running updates index pages and adds any new parts/chapters
without clobbering existing section HTML.

Usage:
    python scripts/scaffold.py            # parse plan, build tree + indexes
    python scripts/scaffold.py --check    # parse only, print a summary, write no files
"""
from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "building_sensory_ai_book_plan.md"

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
    # drop the modern-core / verb annotations and markdown emphasis
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0]
    return text


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(?:\[[FCAR]+\])+\*\*", "", text)  # level tags
    text = re.sub(r"\s*—\s*\*\*.*?\*\*", "", text)      # trailing bold aside
    text = re.sub(r"\*\((.*?)\)\*", "", text)           # *(verb)* annotation
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def parse_plan() -> dict:
    parts: list[dict] = []
    cur_part: dict | None = None
    cur_chap: dict | None = None

    for raw in PLAN.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()

        m = PART_RE.match(line)
        if m:
            verb = ""
            vm = re.search(r"\*\((.*?)\)\*", line)
            if vm:
                verb = vm.group(1)
            cur_part = {
                "number": ROMAN[m.group(1)],
                "roman": m.group(1),
                "title": strip_md(m.group(2)),
                "verb": verb,
                "chapters": [],
            }
            parts.append(cur_part)
            cur_chap = None
            continue

        m = CHAP_RE.match(line)
        if m and cur_part is not None:
            tags = ""
            tm = TAG_RE.search(line)
            if tm:
                tags = tm.group(1)
            cur_chap = {
                "number": int(m.group(1)),
                "title": strip_md(m.group(2)),
                "levels": tags,
                "sections": [],
                "lab": "",
            }
            cur_part["chapters"].append(cur_chap)
            continue

        m = SEC_RE.match(line)
        if m and cur_chap is not None and int(m.group(1)) == cur_chap["number"]:
            cur_chap["sections"].append({
                "id": f"{m.group(1)}.{m.group(2)}",
                "title": strip_md(m.group(3)),
            })
            continue

        m = LAB_RE.match(line)
        if m and cur_chap is not None:
            cur_chap["lab"] = strip_md(m.group(1))
            continue

    return {"parts": parts}


def part_dir(part: dict) -> str:
    return f"part-{part['number']:02d}-{slugify(part['title'])}"


def chap_dir(chap: dict) -> str:
    return f"chapter-{chap['number']:02d}-{slugify(chap['title'])}"


PART_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Part {num}: {title}. Building Sensory AI.">
    <title>Part {num}. {title} — Building Sensory AI</title>
    <link rel="stylesheet" href="../styles/book.css">
</head>
<body class="index-page">
<header class="chapter-header">
    <nav class="header-nav">
        <a href="../index.html" class="book-title-link">Building Sensory AI</a>
    </nav>
    <div class="part-label">Part {num}{verb}</div>
    <h1>{title}</h1>
</header>
<main class="content">
    <h2>Chapters</h2>
    <div class="section-card-grid">
{cards}
    </div>
</main>
</body>
</html>
"""

CHAP_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Chapter {num}: {title}. Building Sensory AI.">
    <title>Chapter {num}. {title} — Building Sensory AI</title>
    <link rel="stylesheet" href="../../styles/book.css">
</head>
<body class="index-page">
<header class="chapter-header">
    <nav class="header-nav">
        <a href="../../index.html" class="book-title-link">Building Sensory AI</a>
        <a href="../index.html" class="toc-link">Part {part_num}</a>
    </nav>
    <div class="part-label">Chapter {num}{levels}</div>
    <h1>{title}</h1>
</header>
<main class="content">
    <p class="status-note">Placeholder chapter page. Sections are produced by the
    book-skills pipeline into <code>sections/</code>.</p>
    <h2>Sections</h2>
    <ol class="section-list">
{sections}
    </ol>
    <div class="callout lab"><strong>Lab {num}.</strong> {lab}</div>
</main>
</body>
</html>
"""

ROOT_INDEX_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Building Sensory AI: Machine Perception of the Physical World.">
    <title>Building Sensory AI</title>
    <link rel="stylesheet" href="styles/book.css">
</head>
<body class="index-page">
<header class="chapter-header">
    <div class="part-label">Hands-On AI Science Series</div>
    <h1>Building Sensory AI</h1>
    <p class="chapter-subtitle">Machine Perception of the Physical World</p>
</header>
<main class="content">
    <p>14 parts · 72 chapters. This is the generated table of contents; run
    <code>python scripts/scaffold.py</code> to regenerate it from the plan.</p>
"""

ROOT_INDEX_FOOT = """</main>
</body>
</html>
"""

TOC_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Table of contents. Building Sensory AI.">
    <title>Contents · Building Sensory AI</title>
    <link rel="stylesheet" href="styles/book.css">
</head>
<body class="index-page">
<header class="chapter-header">
    <nav class="header-nav">
        <a href="index.html" class="book-title-link">Building Sensory AI</a>
    </nav>
    <div class="part-label">Table of Contents</div>
    <h1>Building Sensory AI</h1>
    <p class="chapter-subtitle">Machine Perception of the Physical World</p>
</header>
<main class="content">
"""


def build(structure: dict) -> None:
    toc_parts = []
    for part in structure["parts"]:
        pdir = ROOT / part_dir(part)
        pdir.mkdir(exist_ok=True)
        verb = f" · <em>{escape(part['verb'])}</em>" if part["verb"] else ""

        cards = []
        toc_chaps = []
        for chap in part["chapters"]:
            cdir = pdir / chap_dir(chap)
            (cdir / "sections").mkdir(parents=True, exist_ok=True)
            rel = f"{chap_dir(chap)}/index.html"
            levels = f" <span class=\"levels\">{escape(chap['levels'])}</span>" if chap["levels"] else ""
            cards.append(
                f'        <a class="section-card" href="{rel}">'
                f'<span class="card-num">Ch {chap["number"]}</span>'
                f'<span class="card-title">{escape(chap["title"])}</span>{levels}</a>'
            )
            sec_items = []
            for s in chap["sections"]:
                fname = f"section-{s['id'].replace('.', '-')}.html"
                exists = (cdir / "sections" / fname).exists()
                label = f'<span class="sec-id">{escape(s["id"])}</span> {escape(s["title"])}'
                if exists:
                    sec_items.append(f'        <li><a href="sections/{fname}">{label}</a></li>')
                else:
                    sec_items.append(f'        <li>{label}</li>')
            secs = "\n".join(sec_items)
            (cdir / "index.html").write_text(
                CHAP_INDEX.format(
                    num=chap["number"],
                    part_num=part["number"],
                    title=escape(chap["title"]),
                    levels=f" &nbsp;{escape(chap['levels'])}" if chap["levels"] else "",
                    sections=secs,
                    lab=escape(chap["lab"] or "TBD"),
                ),
                encoding="utf-8",
            )
            toc_chaps.append(
                f'    <li><a href="{part_dir(part)}/{rel}">Ch {chap["number"]}. '
                f'{escape(chap["title"])}</a> {escape(chap["levels"])}</li>'
            )

        (pdir / "index.html").write_text(
            PART_INDEX.format(
                num=part["roman"],
                verb=verb,
                title=escape(part["title"]),
                cards="\n".join(cards),
            ),
            encoding="utf-8",
        )

        toc_parts.append(
            f'    <h2><a href="{part_dir(part)}/index.html">Part {part["roman"]}. '
            f'{escape(part["title"])}</a></h2>\n    <ul class="toc-chapter-list">\n'
            + "\n".join(toc_chaps) + "\n    </ul>"
        )

    (ROOT / "index.html").write_text(
        ROOT_INDEX_HEAD + "\n".join(toc_parts) + "\n" + ROOT_INDEX_FOOT,
        encoding="utf-8",
    )
    (ROOT / "toc.html").write_text(
        TOC_HEAD + "\n".join(toc_parts) + "\n" + ROOT_INDEX_FOOT,
        encoding="utf-8",
    )
    (ROOT / "scripts" / "book_structure.json").write_text(
        json.dumps(structure, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_section_index(structure)
    refresh_book_config(structure)


def write_section_index(structure: dict) -> None:
    """Emit scripts/section_index.json listing every section whose HTML file
    exists on disk (the wave pipeline operates on written sections only).
    Schema: [{sec, title, path}] with path relative to the book root."""
    index = []
    for part in structure["parts"]:
        pdir = part_dir(part)
        for chap in part["chapters"]:
            cdir = chap_dir(chap)
            for s in chap["sections"]:
                fname = f"section-{s['id'].replace('.', '-')}.html"
                rel = f"{pdir}/{cdir}/sections/{fname}"
                if (ROOT / rel).exists():
                    index.append({"sec": s["id"], "title": s["title"], "path": rel})
    (ROOT / "scripts" / "section_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"section_index.json: {len(index)} written sections")


def refresh_book_config(structure: dict) -> None:
    """Regenerate only the marked chapter-map block of BOOK_CONFIG.md, leaving
    the hand-authored identity/style sections untouched."""
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
        first = p["chapters"][0]["number"]
        last = p["chapters"][-1]["number"]
        rows.append(f"### Part {p['roman']}: {p['title']} (Ch {first}-{last}){verb}")
        for c in p["chapters"]:
            lvl = f"  `{c['levels']}`" if c["levels"] else ""
            rows.append(f"- Chapter {c['number']}: {c['title']}{lvl}")
        rows.append("")
    rows.append(end)
    block = "\n".join(rows)
    new = re.sub(re.escape(start) + r".*?" + re.escape(end), block, text, flags=re.DOTALL)
    cfg.write_text(new, encoding="utf-8")


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
