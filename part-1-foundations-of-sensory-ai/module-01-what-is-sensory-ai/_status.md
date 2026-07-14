# Chapter 1 Status — What Is Sensory AI?

Level: [F] foundational · 8 sections · Lab 1

## Per-file status

| Section | Draft | Epigraph | Callouts | Code | Cross-refs | Bib | Notes |
|---|---|---|---|---|---|---|---|
| 1.1 | done | yes | big-picture, key-insight, practical-example, library-shortcut, fun-note, exercise, self-check | yes | 6 | — | inline SVG (forward/inverse loop) |
| 1.2 | done | yes | big-picture, library-shortcut, key-insight, practical-example, fun-note, exercise, self-check | yes | 4 | — | pipeline-contrast SVG; scoped SVG-label style block |
| 1.3 | done | yes | big-picture, key-insight, practical-example, library-shortcut, fun-note, exercise, self-check | yes | 7 | — | notation table; perceive-act loop SVG |
| 1.4 | done | yes | big-picture, key-insight, practical-example, fun-note, library-shortcut, exercise, self-check | yes (2) | 5 | — | modality-by-task matrix table |
| 1.5 | done | yes | full set | yes (2) | ok | — | sensing-chain stages mapped to six verbs |
| 1.6 | done | yes | full set | yes (2) | ok | — | constraint tradeoffs |
| 1.7 | done | yes | full set | yes | ok | — | 2023-2026 foundation-model + agentic shift |
| 1.8 | done | yes | full set + lab | yes | ok | yes (12) | book-map; Lab 1 callout; bibliography |

## Completed checks (initial draft, 2026-07)
- Structural conformance: header/nav/footer at correct 3-level depth; epigraph; What's Next on every section.
- Style: zero em-dashes / double-hyphens / banned phrases in prose and titles.
- Links: all internal cross-references resolve (verified by scripts/scaffold.py tree + link checker).
- AI-tells: no `data-agent` stamps.
- Math: inline `\(...\)`, display `$$...$$`/`\[...\]`; single-`$` not enabled as a delimiter.

## Deferred / not yet done
- **Illustrations (Illustrator #36)**: no raster PNGs yet. Sections use inline SVG diagrams only. Generate 5-8 chapter illustrations via `gemini-imagegen` from the main context, then embed.
- **Full 46-agent pass**: this is the essential-agent initial draft, not the complete pipeline. Remaining agents (misconception, aha-moment, memorability, skeptical reader, dedup, pub-QA, meta) not yet run.
- **bibtest**: run on section 1.8 references before publication to catch any wrong-year/misattributed citation.
- **Browser render QA**: in-app preview was unresponsive this session; verify rendering (math + Prism need vendor/ installed locally).

## Full-agent wave sweep (2026-07)
All 43 book-skills agents applied via the 11 combined pack waves (81 section-agent runs across p1a-p6, p0-plan/embed, p7; 0 errors). Adds per section: deep-explanation, misconception, analogy, research-frontier, project (p1a); exercises, demos, application examples, fun notes, labs (p1b); fact-check, terminology, currency (p2); cross-refs, transitions, hooks (p3); clarity/voice/pacing rewrite (p4a); engagement, aha-moments, memorability (p4b); code pedagogy, SVG, self-containment, visual identity, captions (p5); curriculum, teaching-flow, student-advocate, cognitive-load, skeptic (p6); structural review, epigraph, bibliography, dedup, meta, pub-QA (p7).

**Illustrations**: 7 raster diagrams generated via gemini-imagegen (key at ~/.gemini-imagegen.json) and embedded in sections 1.1-1.6, 1.8 (1.7 keeps its inline SVG).

**Pre-publish gate**: fix_inline_math (1 file), fix_svg_label_math (2 SVG labels), audit_ai_tells stripped 296 data-agent stamps + 2 CSS tooltip leaks, audit_kdp_risk (fixed a forward Section 2.1 ref + an end-to-end variant). detect_duplicates: 0 duplicate pairs. Final: 0 em-dashes, 0 broken images, 0 dangling refs, 0 terminology clashes.

**bibtest**: all 9 real citations valid (Kalman 1960 DOI; TimesFM/MOMENT/LSM/Conformal/Foundation-Models arXiv IDs; 3 textbooks). No hallucinations or wrong years. (bibtest also flags 9 "not_found" that are the house bib-annotation/category paragraphs, a known markup-vs-parser artifact, not citation errors.)

## Audit History
- 2026-07: Initial draft of all 8 sections via `scripts/ch01_draft.js` workflow (run wf_81937da5-49e, 9 agents, 0 errors). Fixed title em-dash separators and 3 cross-ref path bugs; generated `toc.html`; linked sections from chapter index.
- 2026-07: Migrated to the series house convention (VisionAI parity): `part-1/module-01/section-1.N.html`, 2-level depth. Adopted house `book.css` (4833 lines) + `pygments.css` + `book.js`; rewrote every section head/header/footer to the house template (skip-link, pagefind-less, KaTeX contrib/auto-render, prism-bundle, title ` | Building Sensory AI`); rewrote all in-body cross-refs to `module-NN` paths. Added `book.json`, `html2epub.toml`, front-matter/appendices/capstone stubs. All internal links verified; no old-convention leftovers.
