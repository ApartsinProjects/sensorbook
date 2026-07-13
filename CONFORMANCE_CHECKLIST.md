# Conformance Checklist — Building Sensory AI

Structural and formatting requirements every section HTML file must satisfy. Enforced by
the book-skills post-generation pass (Controller #42) and the pre-publish gate.

## Structural items (per section file)
- **(A) Header links**: `<header class="chapter-header">` with nav back to book root and part index; correct relative-depth link to `styles/book.css`.
- **(B) Epigraph**: opening epigraph with "A [Adjective] AI Agent" attribution style.
- **(C) Prerequisites**: prose statement of prerequisites with cross-links to the chapters/appendices that supply them (self-containment).
- **(D) Callouts**: use the 15 approved callout classes only; each with its icon; no ad-hoc box styles.
- **(E) Code captions**: every `<pre>` has a unique, specific `<div class="code-caption">` placed BELOW the block.
- **(F) Research frontier**: at least one `research-frontier` callout in [A]/[R] sections naming current SOTA.
- **(G) What's Next**: a "What's Next" section before the bibliography linking to the next chapter.
- **(H) Bibliography**: card layout; annotations complete (no truncation); citations verified with `bibtest`.
- **(I) Navigation footer**: previous/next section and up-to-chapter links.
- **(J) CSS completeness**: links `styles/book.css`; no full inline `<style>` blocks.
- **(K) Responsive**: renders at mobile and desktop widths.
- **(L) Cross-references**: at least 3 inline cross-chapter hyperlinks per section where relevant.
- **(M) Content width**: body content constrained to the book's reading measure.
- **(N) Style rules**: no em-dashes or double-hyphens; no banned phrases (honestly/frankly/etc.); Part>Chapter>Section terminology only.

## Book-specific rules
- **Level tags** `[F]/[C]/[A]/[R]` appear in the chapter header and carry through to section-level tags.
- **Six-verb thread**: each chapter states which of measure/clean/represent/infer/fuse/deploy it advances.
- **Right-Tool pairing**: every from-scratch concept pairs with a `library-shortcut` callout and an explicit line-count reduction.
- **Leakage-safe evaluation** is mentioned wherever a model is trained or evaluated.
- **Named-entity accuracy**: every named model/dataset/standard (e.g. TimesFM, MOMENT, Occ3D, ISO 21448) is verified before print; arXiv IDs and years pass `bibtest`.

## Pre-publish gate (BLOCKING before any EPUB/KDP build)
Run in order from the book root (see book-skills SKILL.md §16):
1. `fix_inline_math.py --apply` (bare `$...$` → `\(...\)` so KaTeX renders it)
2. `fix_svg_label_math.py --apply` (LaTeX in SVG `<text>` → Unicode)
3. `audit_ai_tells.py --css styles/book.css --apply` (strip `data-agent` stamps, tooltip leaks)
4. `audit_kdp_risk.py` (placeholders, em-dashes, broken image `src`, citation conflicts)
5. `detect_duplicates.py` + `bibtest` on extracted references

## Change Log
- 2026-07: Initial checklist created with the scaffold. Structure: 14 parts / 72 chapters (see `BOOK_CONFIG.md`).
