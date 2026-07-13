# Wave Plan — Full-Agent Pass (book-skills)

Applies **all 43 book-skills agents** to the written sections via the token-efficient
**combined pack-wave** sweep. Scope = every section listed in `scripts/section_index.json`
(currently Chapter 1, sections 1.1–1.8; regenerate the index with
`python scripts/scaffold.py` after new chapters are drafted).

Regenerate the pack scripts any time the index changes:
```
python C:/Users/apart/.claude/skills/book-skills/scripts/gen_pack_waves.py \
  --book-root E:/Projects/Books/SensorAI --index scripts/section_index.json --out-dir scripts
python scripts/normalize_waves.py   # force LF (CRLF breaks the Workflow handler)
```

## Agent coverage

`#00` (chapter-lead orchestrator) = me, the main context. `#31` (illustrator) runs as the
3-phase split below. The other **41 agents** run inside the 11 packs; each per-section pack
reads a section once, runs all its agents in sequence, and writes once.

| # | Pack | Phase | Agents | What it does | Mode |
|---|------|-------|--------|--------------|------|
| 1 | p0-plan | Illus-plan | #31a | Identify raster-illustration opportunities; write Gemini prompts to `scripts/illustration_queue.json` | per-section (read-only) |
| — | **shell** | gen | — | `gemini_batch_generate.py` calls Gemini Imagen, saves PNGs to `images/` | main thread (blocking) |
| 2 | p0-embed | Illus-embed | #31b | Insert `<figure><img><figcaption>` + prose reference for each generated PNG | per-section |
| 3 | p1a | Depth | #02 #06 #10 #18 #23 | what/why/how/when, analogies, misconceptions, research frontier, projects | per-section |
| 4 | p1b | Enrich | #07 #26 #33 #34 #41 | exercises, demos, application examples, fun notes, labs | per-section |
| 5 | p2 | Integrity | #11 #12 #20 | fact-check, terminology consistency, content currency | per-section |
| 6 | p3 | Navigation | #13 #14 #22 | cross-reference links, narrative transitions, opening hook | per-section |
| 7 | p4a | Prose-rewrite | #15 #17 #29 #30 | clarity, voice, pacing, senior edit (destructive rewrite) | per-section |
| 8 | p4b | Prose-add | #16 #24 #27 | engagement, aha-moments, memorability (additive) | per-section |
| 9 | p5 | Visual+code | #08 #09 #21 #25 #39 #40 | code pedagogy, SVG diagrams, self-containment, visual identity, figure facts, code captions | per-section |
| 10 | p6 | QA | #01 #03 #04 #05 #28 | curriculum alignment, teaching flow, student advocate, cognitive load, skeptical reader | per-section |
| 11 | p7 | Publish | #19 #32 #35 #36 #37 #38 #42 | structural review, epigraphs, bibliography, meta-audit, controller, pub-QA, dedup | book-level |

**Ordering rationale** (baked into the pack split): p4a (rewrites prose) runs before p4b
(adds inline hooks) so additions are not clobbered; p7 is book-level and runs last because
dedup and structural review need the full section set.

## Launch order

Run each as a **separate top-level Workflow call**, waiting for the completion notification
before the next (hard gate). After each pack, persist the run id to
`scripts/.wave_state.json` and run the conflict check.

```
1.  Workflow({ scriptPath: 'E:/Projects/Books/SensorAI/scripts/pack-p0-plan-workflow.js' })
    → then shell:  python C:/Users/apart/.claude/skills/book-skills/scripts/gemini_batch_generate.py \
                     --book-root E:/Projects/Books/SensorAI \
                     --queue scripts/illustration_queue.json --out-dir images --batch-size 20 \
                     --style "technical flat editorial, muted palette"
2.  Workflow({ scriptPath: '.../pack-p0-embed-workflow.js' })
3.  Workflow({ scriptPath: '.../pack-p1a-workflow.js' })
4.  Workflow({ scriptPath: '.../pack-p1b-workflow.js' })
5.  Workflow({ scriptPath: '.../pack-p2-workflow.js' })
6.  Workflow({ scriptPath: '.../pack-p3-workflow.js' })
7.  Workflow({ scriptPath: '.../pack-p4a-workflow.js' })
8.  Workflow({ scriptPath: '.../pack-p4b-workflow.js' })
9.  Workflow({ scriptPath: '.../pack-p5-workflow.js' })
10. Workflow({ scriptPath: '.../pack-p6-workflow.js' })
11. Workflow({ scriptPath: '.../pack-p7-workflow.js' })
```

Between packs:
```
git add -A && git diff --cached --stat      # confirm expected files changed
```
Commit after every 2–3 packs so a mid-sweep interruption is cheap to resume.

## Concurrency and rate limits

Each per-section pack launches 8 agents (one per section) — within the safe cap
(~6–8 concurrent). No chunking needed at this scale. If a bigger chapter set pushes the
index past ~16 sections, the Workflow engine queues automatically; if the server throttles
("temporarily limiting requests"), resume with `resumeFromRunId` so cached agents replay.

## Illustrator 3-phase (Gemini)

Requires `GEMINI_API_KEY` and the `gemini-imagegen` skill. Targets 5–8 images for the
chapter (1 opener, 1–2 mental-model, 1 system-as-ecosystem, 1–2 analogy, 1 failure-mode).
Images land in `part-01-.../chapter-01-.../images/` (per the embed pack), referenced from
sections as `../images/NAME.png`. If `GEMINI_API_KEY` is unset, mark the run **BLOCKED on
Illustrator raster generation** rather than claiming a full pass.

## Pre-publish gate (BLOCKING before any EPUB build)

After the sweep, before html2epub:
```
python C:/Users/apart/.claude/skills/book-skills/scripts/fix/fix_inline_math.py --book-root . --apply
python C:/Users/apart/.claude/skills/book-skills/scripts/fix/fix_svg_label_math.py --book-root . --apply
python C:/Users/apart/.claude/skills/book-skills/scripts/audit_ai_tells.py --book-root . --css styles/book.css --apply
python C:/Users/apart/.claude/skills/book-skills/scripts/audit_kdp_risk.py --book-root .
python C:/Users/apart/.claude/skills/book-skills/scripts/detect_duplicates.py --book-root .
```
Then run the `bibtest` skill on the extracted bibliography (section 1.8) to catch
hallucinated or wrong-year citations.

> Note: several book-skills fix/audit scripts default to a `part-*/module-*/section-*.html`
> glob. Our layout is `part-*/chapter-*/sections/section-*.html`; pass an explicit
> `--section-glob` where the script supports it, or the wave-edited files (which the packs
> located via `section_index.json`) are still correct on disk regardless.

## Cost and wall-clock (agent execution, not human)

- 10 per-section packs × 8 agents + 1 book-level = **81 agent runs**, plus ~8–16 Gemini images.
- Rough agent wall-clock at 6–8 concurrency: **~30–60 minutes** across the 11 packs.
- Token cost: a few million output tokens (single chapter). Gemini image cost ≈ **$0.30–0.60**.
- This scales linearly with the section count as more chapters are drafted.

## Resume

The Workflow engine caches each agent by (prompt, opts). If a pack is interrupted, relaunch
the same `scriptPath` with `resumeFromRunId` (persisted in `scripts/.wave_state.json`);
completed agents replay instantly. Regenerating the pack scripts after adding sections is
safe — unchanged sections' agents still cache-hit.
