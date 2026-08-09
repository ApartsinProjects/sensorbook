#!/usr/bin/env python3
"""Generate the book landing page (index.html) in the series house cover style.

Reuses the shared cover CSS from the Building Vision AI landing page, then
composes SensorAI-specific content: hero + cover image, the 14-part grid (built
from scripts/book_structure.json and the plan's "Part goal" lines), the teaching
habits, and the Hands-On AI Science series navigation.

index.html is authored by THIS script, not by scaffold.py (which owns toc.html).

Usage: python scripts/gen_landing.py
"""
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VISION_INDEX = Path("E:/Projects/Books/VisionAI/index.html")

TITLE = "Building Sensory AI"
ARC = "Machine Perception of the Physical World"
SUB = ("A practitioner's guide to the full sensing chain: signal processing, state estimation, "
       "deep learning and foundation models for sensor data, multimodal fusion, and trustworthy deployment.")
DOMAIN = "https://sensorbook.icsgen-ai.org"

PROMISE = ("Most AI meets the world through text and pictures. Sensory AI starts earlier, at the device that "
           "measures reality imperfectly. This book is one connected journey through the theories, models, and "
           "engineering practices for systems that perceive the physical world through inertial, vibration, radar, "
           "lidar, depth, thermal, event, RF, tactile, and biomedical sensing. It begins with sensor physics and "
           "measurement models, builds through classical filtering and state estimation into deep learning and "
           "sensor foundation models, then moves into fusion, world models, and edge deployment, before closing "
           "with the evaluation, robustness, safety, and responsible-practice concerns that govern real systems.")

TEACH = [
    ("&#9881;", "Worked Pipelines",
     "Every chapter builds complete, runnable systems (a leakage-safe activity recognizer, a Kalman tracker, a "
     "remaining-useful-life predictor), never isolated snippets."),
    ("&#9889;", "Library Shortcuts",
     "After each from-scratch build, a shortcut callout shows the same task in a few lines of SciPy, filterpy, "
     "sktime, PyTorch, or a pretrained foundation model, and names exactly what the library handles for you."),
    ("&#9707;", "Three Reading Levels",
     "Every chapter and section is tagged foundational, core, advanced, or research frontier, so undergraduates, "
     "graduate students, and working engineers each find their depth in the same book."),
    ("&#9654;", "Exercises &amp; Labs",
     "Each chapter closes with a hands-on lab on public sensor datasets plus level-tagged exercises, from quick "
     "checks to projects you can put in a portfolio."),
    ("&#8634;", "Classical Ideas Return Learned",
     "Filtering becomes the 1D convolution, the Kalman filter becomes a learned state-space model, handcrafted "
     "features become self-supervised representations, and calibration returns as conformal prediction."),
]

SERIES = [
    ("Building Language AI", "From Tokens to Agents.", "https://llmbook.icsgen-ai.org", "https://www.amazon.com/dp/B0H1MQH23D"),
    ("Building Vision AI", "From Pixels to Generative Models.", "https://visionbook.icsgen-ai.org", "https://www.amazon.com/dp/B0H5BT8Y75"),
    ("Building Temporal AI", "From Forecasting to Sequential Decision Making.", "https://temporalbook.icsgen-ai.org", "https://www.amazon.com/dp/B0H5KRJFCD"),
    ("Building Scalable AI", "From Big Data Algorithms to Distributed Intelligence.", "https://scalablebook.icsgen-ai.org", "https://www.amazon.com/dp/B0H5Q1471R"),
    ("Building Embodied AI", "From Perception to Autonomous Action.", "https://embodiedbook.icsgen-ai.org", None),
    ("Building Agentic AI", "From Goals to Autonomous Systems.", "https://agenticbook.icsgen-ai.org", None),
    ("Building Discovery AI", "From Vibe Coding to Autonomous Science.", "https://discoverybook.icsgen-ai.org", None),
    ("Building Neuromorphic AI", "From Spiking Neurons to Edge Intelligence.", "https://neuromorphicbook.icsgen-ai.org", None),
    ("Building Quantum AI", "From Qubits to Quantum Machine Learning.", "https://quantumbook.icsgen-ai.org", None),
    ("Building Sensory AI", "Machine Perception of the Physical World.", None, None),  # you are here
]


def part_goals() -> dict[int, str]:
    """Pull each part's 'Part goal:' line from the plan, keyed by part number."""
    text = (ROOT / "building_sensory_ai_book_plan.md").read_text(encoding="utf-8")
    roman = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12,"XIII":13,"XIV":14}
    goals, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^#\s+Part\s+([IVXL]+)\s+·", line)
        if m:
            cur = roman[m.group(1)]
            continue
        m = re.match(r"^\*\*Part goal:\*\*\s*(.+?)\s*$", line)
        if m and cur:
            goals[cur] = m.group(1).rstrip(".")
            cur = None
    return goals


def main() -> None:
    style = re.search(r"<style>.*?</style>", VISION_INDEX.read_text(encoding="utf-8"), re.DOTALL).group(0)
    struct = json.loads((ROOT / "scripts" / "book_structure.json").read_text(encoding="utf-8"))
    goals = part_goals()

    import scaffold
    cards = []
    for i, p in enumerate(struct["parts"]):
        nch = len(p["chapters"])
        nsec = sum(len(c["sections"]) for c in p["chapters"])
        goal = goals.get(p["number"], "")
        goal = goal[0].upper() + goal[1:] if goal else ""
        cards.append(
            f'<a class="part-card part-{(i % 4) + 1}" href="{scaffold.part_dir(p)}/index.html">\n'
            f'<span class="part-roman">{p["roman"]}</span>\n'
            f'<h3>{escape(p["title"])}</h3>\n'
            f'<p>{escape(goal)}.</p>\n'
            f'<span class="part-count">{nch} chapters &#183; {nsec} sections</span>\n</a>'
        )

    teach = "\n\n".join(
        f'<div class="teach-item">\n<span aria-hidden="true" class="teach-glyph">{g}</span>\n'
        f'<h3>{t}</h3>\n<p>{d}</p>\n</div>' for g, t, d in TEACH
    )

    series = []
    for i, (name, arc, url, kindle) in enumerate(SERIES):
        if url is None:
            links = '<span class="series-here">You are here</span>'
        else:
            links = f'<span class="series-links"><a href="{url}" rel="noopener" target="_blank">Read online</a>'
            if kindle:
                links += f' &#183; <a href="{kindle}" rel="noopener" target="_blank">Kindle</a>'
            links += "</span>"
        series.append(
            f'<div class="part-card series-card part-{(i % 4) + 1}">\n<h3>{name}</h3>\n'
            f'<p class="series-arc">{arc}</p>\n{links}\n</div>'
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="{escape(TITLE)}: {escape(ARC)}. {escape(SUB)}" name="description"/>
<title>{escape(TITLE)}: {escape(ARC)}</title>
<meta content="{escape(TITLE)}: {escape(ARC)}" property="og:title"/>
<meta content="{escape(SUB)}" property="og:description"/>
<meta content="{DOMAIN}/images/book-cover.jpg" property="og:image"/>
<meta content="{DOMAIN}/" property="og:url"/>
<meta content="book" property="og:type"/>
<meta content="summary_large_image" name="twitter:card"/>
<link href="styles/book.css" rel="stylesheet"/>
{style}
<script defer src="scripts/book.js"></script>
</head>
<body class="cover-page">

<div class="cover-wrap">

<header class="hero">
<span class="edition-pill">First Edition &#183; 2026</span>
<div class="cover-image-wrapper"><img alt="Book cover: sensor waveforms, a radar range-Doppler panel and a lidar point cloud rising through a neural network into a reconstructed walking figure and robot, with the title Building Sensory AI, Machine Perception of the Physical World" class="cover-image" height="1600" src="images/book-cover.jpg" width="1000"/></div>
<h1 class="cover-title">{escape(TITLE)}
<span class="title-arc">{escape(ARC)}</span></h1>
<p class="cover-subtitle">{escape(SUB)}</p>
<div aria-hidden="true" class="cover-separator"><span>&#10022;</span></div>
<p class="cover-authors">
<a href="front-matter/about-authors.html">Alexander (Sasha) Apartsin, Ph.D.</a>
<span class="amp">&amp;</span>
<a href="front-matter/about-authors.html">Yehudit Aperstein, Ph.D.</a>
</p>
<p class="cover-promise">{escape(PROMISE)}</p>
<nav aria-label="Primary" class="cover-cta">
<a class="btn-start" href="part-1-foundations-of-sensory-ai/module-01-what-is-sensory-ai/section-1.1.html">Start Reading</a>
<a class="btn-contents" href="toc.html">Contents</a>
</nav>
<div class="cover-meta">
<span>14 parts</span>
<span>72 chapters</span>
<span>505 sections</span>
<span>10 appendices &amp; a capstone</span>
</div>
</header>

<section aria-labelledby="parts-heading" class="parts-section">
<h2 class="cover-section-title" id="parts-heading">The Fourteen-Part Arc</h2>
<p class="cover-section-sub">Six verbs carry the book: measure, clean, represent, infer, fuse, deploy. Each part stands on the one before it.</p>
<div class="part-grid">

{chr(10).join(cards)}

</div>
</section>

<section aria-labelledby="teaches-heading" class="teaches-section">
<h2 class="cover-section-title" id="teaches-heading">How This Book Teaches</h2>
<p class="cover-section-sub">Five habits, kept in every chapter from the first raw sample to the deployed system.</p>
<div class="teach-grid">

{teach}

</div>
</section>

<section aria-labelledby="series-heading" class="series-section">
<h2 class="cover-section-title" id="series-heading">The Hands-On AI Science Series</h2>
<p class="cover-section-sub">Building Sensory AI is one of ten connected books, each a deep, build-it-yourself guide to a major field of AI.</p>
<p class="cover-promise" style="margin-top:0;">Hands-On AI Science is a series of in-depth guides to the major fields of artificial intelligence. Every book goes deep into the theory, models, and internals, covering the classical foundations and the most recent ideas, then shows you how to build each one in Python with the modern libraries and tools that get the job done. The writing stays plain and light (illustrations, analogies, mental models, worked examples, and a little fun) without trading away rigor or coverage. Each volume is self-contained and complete enough to anchor a full course on its subject.</p>
<div class="part-grid">

{chr(10).join(series)}

</div>
<p class="series-cta">Read the full <a href="front-matter/about-the-series.html">About the Hands-On AI Science Series</a> note.</p>
</section>

</div>

<footer class="cover-footer">
<p class="footer-title">{escape(TITLE)}: {escape(ARC)}, First Edition</p>
<p>&#169; 2026 Alexander Apartsin &amp; Yehudit Aperstein &#183; <a href="toc.html">Contents</a></p>
</footer>

</body>
</html>
"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"index.html written: {len(html):,} chars, {len(cards)} part cards, {len(series)} series cards")


if __name__ == "__main__":
    main()
