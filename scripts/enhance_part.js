export const meta = {
  name: 'enhance-part',
  description: 'Plan B lean sweep: one combined enhance+polish pass per section (all high-value agents folded into one read+write)',
  phases: [{ title: 'Enhance' }],
}

const ROOT = 'E:/Projects/Books/SensorAI'
const BOOK = 'Building Sensory AI'
const part = args // { part_roman, part_title, sections:[{path,sec_id,sec_title,ch_num,ch_title,levels}], chapter_hrefs:{...} }
const hrefs = part.chapter_hrefs || {}

const SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: { path: { type: 'string' }, wrote: { type: 'boolean' }, added: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } },
  required: ['path', 'wrote'],
}

function prompt(s) {
  const chmap = Object.entries(hrefs).map(([n, v]) => `  Ch ${n}: ${v.title} ${v.levels} -> ${v.href}`).join('\n')
  const frontier = /\[A\]|\[R\]/.test(s.levels)
  return `You are enhancing ONE already-drafted, already-house-styled section of the textbook "${BOOK}: Machine Perception of the Physical World".
Section ${s.sec_id}: "${s.sec_title}" (Chapter ${s.ch_num} "${s.ch_title}", level ${s.levels}).

File: ${ROOT}/${s.path}
Read it ONCE, improve the content inside <main> in place, then write the file ONCE. This is a single combined pass that folds many editorial roles together. Do NOT rewrite from scratch; raise the existing draft to publication quality.

PRESERVE EXACTLY (do not touch): the <head>, the <header> block, the <footer>, the opening <blockquote class="epigraph">, and the closing <h2>What's Next</h2> paragraph. Keep the same head/nav/footer bytes.

APPLY ALL OF THE FOLLOWING IN THIS ONE PASS, then write:
1. Depth: find the single most surface-level concept and deepen it to answer what / why / how / when (2-4 sentences), justified not asserted.
2. Misconception: if a common reader misconception applies and none is flagged, add one <div class="callout warning"> after the relevant paragraph.
3. Research frontier: ${frontier ? 'ensure exactly one <div class="callout research-frontier"> naming current (2023-2026) SOTA models/methods relevant to this section.' : 'add a short <div class="callout research-frontier"> only if there is a genuinely active research angle; otherwise skip.'}
4. Ensure the section has at least one <div class="callout key-insight"> and one <div class="callout practical-example"> (a concrete named-domain mini-story: wearable, industrial, automotive, clinical, robotics). Add whichever is missing.
5. Library shortcut: where the section teaches a concept from scratch that a modern library makes trivial, add or sharpen one <div class="callout library-shortcut"> that states the line-count reduction and what the library handles. Skip only if truly not applicable.
6. Memorability: sharpen ONE sentence into a crisp, memorable statement of the section's core idea (inline, no new box needed).
7. Ensure one <div class="callout exercise"> and one <div class="callout self-check"> (2-3 questions) exist; add if missing.
8. Cross-references: ensure at least 2 inline hyperlinks to OTHER chapters, using ONLY these exact hrefs:
${chmap}
9. Prose polish: tighten dense or awkward passages for clarity and pacing. Do NOT bloat; net length should stay similar (aim under ~1800 words of body prose).
10. Integrity: fix any obvious factual slip, keep terminology consistent, and ensure every code block has a <div class="code-caption"> placed BELOW the <pre> (not above), referenced in prose.

IDEMPOTENT: if a callout type already exists, improve it rather than add a duplicate (at most: 2 key-insight, 2 warning, 1 research-frontier, 3 practical-example, 2 library-shortcut, 1 exercise, 1 self-check).

HARD RULES:
- NO em-dashes or double hyphens. Use commas, colons, semicolons, parentheses, separate sentences.
- Do not use the words honestly, frankly, candidly.
- Inline math \\(...\\); display $$...$$ or \\[...\\]; never bare single-$.
- Approved callout classes only; titles use <h3 class="callout-title">.
- Do NOT add any data-agent attributes or authoring-comment tooltips.
- Every figure, table, code block, callout must be referenced in prose.

After writing, return the structured summary (which items you added or improved).`
}

phase('Enhance')
const results = await pipeline(
  part.sections,
  (s) => agent(prompt(s), { schema: SCHEMA, label: `enh-${s.sec_id}`, phase: 'Enhance', model: 'sonnet', effort: 'high' })
)

return { part: part.part_roman, requested: part.sections.length, wrote: results.filter(Boolean).filter(r => r.wrote !== false).length, sections: results.filter(Boolean).map(r => r.path) }
