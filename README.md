# Building Sensory AI: Machine Perception of the Physical World

A comprehensive, self-contained textbook and field manual on AI systems that perceive the
physical world through the full spectrum of sensing: inertial, vibration, radar, lidar, depth,
thermal, event, RF/Wi-Fi, tactile, biosignals, and industrial telemetry.

Written for three audiences at once (undergraduates, graduate students, and
researchers/engineers) via explicit level tags (`[F]/[C]/[A]/[R]`) and reading paths.

**14 parts · 72 chapters · 505 sections · 72 labs · capstone.**

## Status

All **505 sections drafted** in house style (validated: house head on every page, zero
em-dashes, zero machine-authored tells, all internal links resolve). **Chapter 1** is
fully finished (43-agent quality sweep + 7 illustrations + pre-publish gate + `bibtest`);
**Chapters 2–72 are first drafts** awaiting the sweep and illustrations. Next: build the
EPUB (`html2epub`), and run the pack-wave sweep (see `WAVE_PLAN.md`) chapter by chapter.

## Repository layout

```
building_sensory_ai_book_plan.md   Plan of record (single source of truth for structure)
BOOK_CONFIG.md                     Book identity + chapter map (generated from the plan)
CONFORMANCE_CHECKLIST.md           Structural/formatting requirements + pre-publish gate
CROSS_REFERENCE_MAP.md             Progressive-depth concept cross-references
index.html                         Generated table of contents
book.json                          Book metadata (single source of truth)
html2epub.toml                     EPUB build config
styles/book.css, styles/pygments.css   Shared stylesheets (house style, from the series)
scripts/book.js                    Client-side book chrome (nav, search)
vendor/                            KaTeX + Prism (installed locally; see vendor/README.md)
front-matter/, appendices/, capstone/  Non-chapter content
images/                            Illustrations (raster PNG)
scripts/scaffold.py                Parses the plan and materializes the tree
scripts/book_structure.json        Machine-readable chapter/section map (generated)
part-N-slug/
    index.html                     Part landing page
    module-NN-slug/                (directory says "module"; prose says "Chapter")
        index.html                 Chapter landing page (lists sections)
        section-N.M.html           Section pages (written by the book-skills pipeline)
```

Layout follows the series house convention (as in the Building Vision AI book), so the
book-skills `part-*/module-*/section-*.html` globs work out of the box.

## Regenerating structure

The plan file is authoritative. After editing it, rebuild the tree, `BOOK_CONFIG.md`
chapter map, and TOC:

```bash
python scripts/scaffold.py --check   # parse only, print a summary
python scripts/scaffold.py           # materialize/refresh the tree + indexes
```

## Publishing pipeline

1. **Write** — `book-skills` produces per-chapter HTML into `sections/`.
2. **Build** — `html2epub` turns the HTML tree into a validated EPUB 3.
3. **Ship** — `epub2kpf` produces a KDP-ready KPF.

Run the pre-publish gate in `CONFORMANCE_CHECKLIST.md` before any EPUB/KDP build.

See [`building_sensory_ai_book_plan.md`](building_sensory_ai_book_plan.md) for the full plan.
