export const meta = {
  name: 'ch01-draft',
  description: 'Draft Chapter 1 "What Is Sensory AI?" — plan, then write 8 conformant section pages',
  phases: [
    { title: 'Plan', detail: 'chapter lead sets objectives, notation, epigraph voice, cross-refs' },
    { title: 'Write', detail: 'one writer per section (1.1-1.8) produces a full HTML page' },
  ],
}

const BOOK = 'Building Sensory AI'
const ROOT = 'E:/Projects/Books/SensorAI'
const CHDIR = ROOT + '/part-01-foundations-of-sensory-ai/chapter-01-what-is-sensory-ai'

const SECTIONS = [
  { id: '1.1', file: 'section-1-1.html', title: 'Sensors as imperfect windows into the world' },
  { id: '1.2', file: 'section-1-2.html', title: 'Physical-world AI vs digital/text AI: why measurement changes everything' },
  { id: '1.3', file: 'section-1-3.html', title: 'Measurement, state, event, action: the four quantities' },
  { id: '1.4', file: 'section-1-4.html', title: 'A taxonomy of modalities and task families' },
  { id: '1.5', file: 'section-1-5.html', title: 'From raw signal to decision: the sensing chain' },
  { id: '1.6', file: 'section-1-6.html', title: 'Sampling, latency, bandwidth, power, cost, and privacy as first-class constraints' },
  { id: '1.7', file: 'section-1-7.html', title: 'The 2023-2026 shift: from bespoke pipelines to foundation models and agentic sensing' },
  { id: '1.8', file: 'section-1-8.html', title: 'Book map: measure, clean, represent, infer, fuse, deploy' },
]

const PLAN_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    chapter_thesis: { type: 'string' },
    learning_objectives: { type: 'array', items: { type: 'string' }, minItems: 4 },
    notation_conventions: { type: 'string' },
    sections: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          id: { type: 'string' },
          angle: { type: 'string', description: 'the distinct one-paragraph angle for this section so pages do not overlap' },
          key_concepts: { type: 'array', items: { type: 'string' } },
          cross_refs: { type: 'array', items: { type: 'string' }, description: 'e.g. "Ch 2 Sensor Physics", "Ch 19 TSFMs"' },
          epigraph_quote: { type: 'string' },
          epigraph_attribution: { type: 'string' },
        },
        required: ['id', 'angle', 'key_concepts', 'epigraph_quote', 'epigraph_attribution'],
      },
    },
  },
  required: ['chapter_thesis', 'learning_objectives', 'sections'],
}

const WRITE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    id: { type: 'string' },
    path: { type: 'string' },
    word_count: { type: 'number' },
    has_epigraph: { type: 'boolean' },
    callouts: { type: 'array', items: { type: 'string' } },
    has_code: { type: 'boolean' },
    cross_ref_count: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['id', 'path', 'word_count', 'callouts'],
}

phase('Plan')
const plan = await agent(
`You are the Chapter Lead for "${BOOK}", planning Chapter 1 "What Is Sensory AI?" (level [F], foundational).

Read these files for context:
- ${ROOT}/BOOK_CONFIG.md (identity, style, chapter map)
- ${ROOT}/CONFORMANCE_CHECKLIST.md (required structure)
- ${ROOT}/CROSS_REFERENCE_MAP.md (progressive-depth concepts)
- ${ROOT}/building_sensory_ai_book_plan.md (find "# Part I" and "## Chapter 1"; also read the Central Thesis, six-verb arc, and "Who This Book Is For")

The chapter has 8 sections, each becoming its own HTML page:
${SECTIONS.map(s => `  ${s.id} ${s.title}`).join('\n')}
and Lab 1: survey a dozen sensor datasets; classify by sampling rate, dimensionality, modality, task, noise source, label cost, deployment constraint.

Produce a coordination plan so the 8 section writers do not overlap and share consistent notation. For EACH section give: a distinct angle (one paragraph), 3-5 key concepts, 1-3 concrete cross-references to other chapters (use the chapter map), and a short witty epigraph with an attribution in the book's "A [Adjective] AI Agent" style (dry, self-aware, never mean, no em-dashes). Also give chapter-level learning objectives, a one-line thesis, and notation conventions (symbols for signal, state, observation, time).

Return ONLY the structured object. Use no em-dashes or double hyphens anywhere.`,
  { schema: PLAN_SCHEMA, label: 'chapter-lead', effort: 'high' }
)

const planById = Object.fromEntries((plan.sections || []).map(s => [s.id, s]))

const SPEC = (s, idx) => {
  const p = planById[s.id] || {}
  const isFirst = idx === 0
  const isLast = idx === SECTIONS.length - 1
  const next = SECTIONS[idx + 1]
  const prev = SECTIONS[idx - 1]
  const nextLink = isLast
    ? '../../chapter-02-sensor-physics-and-measurement-models/sections/section-2-1.html'
    : (next ? next.file : 'index.html')
  const nextLabel = isLast ? 'Chapter 2, Section 2.1' : (next ? `Section ${next.id}` : 'Chapter 1')
  const prevLink = isFirst ? '../index.html' : (prev ? prev.file : '../index.html')
  const prevLabel = isFirst ? `Chapter 1` : (prev ? `Section ${prev.id}` : 'Chapter 1')

  return `You are a section writer for the textbook "${BOOK}: Machine Perception of the Physical World".
Write a complete, self-contained, publication-quality HTML page for Section ${s.id}: "${s.title}".
This is a foundational [F] section of Chapter 1, aimed at readers ranging from advanced undergraduates to practicing engineers.

WRITE THE FILE DIRECTLY with the Write tool to:
  ${CHDIR}/sections/${s.file}

Coordination plan for this section (from the Chapter Lead):
- Angle: ${p.angle || s.title}
- Key concepts: ${(p.key_concepts || []).join('; ')}
- Cross-references to weave in: ${(p.cross_refs || []).join('; ') || 'link to at least 2 relevant later chapters using the chapter map in BOOK_CONFIG.md'}
- Epigraph: "${p.epigraph_quote || ''}" -- ${p.epigraph_attribution || 'An AI Agent'}
Chapter thesis: ${plan.chapter_thesis || ''}
Notation to use consistently: ${plan.notation_conventions || 'signal x(t), hidden state s, observation y, time t'}

Read ${ROOT}/BOOK_CONFIG.md and ${ROOT}/CONFORMANCE_CHECKLIST.md first. Also skim the Chapter 1 entry in ${ROOT}/building_sensory_ai_book_plan.md.

REQUIRED PAGE STRUCTURE (exact head/header/footer; correct relative depth for a file 3 levels below root):
1. Start with <!DOCTYPE html><html lang="en"><head> containing:
   - <meta charset="UTF-8">, viewport meta, a <meta name="description">, and <title>Section ${s.id}: ${s.title} — ${BOOK}</title>
   - <link rel="stylesheet" href="../../../styles/book.css">
   - KaTeX: <link rel="stylesheet" href="../../../vendor/katex/katex.min.css"> ; defer scripts katex.min.js and auto-render.min.js with an onload that renders delimiters for \\(...\\) (inline), \\[...\\] (display), and $$...$$ (display). Do NOT enable single-$ as a delimiter.
   - Prism: <link rel="stylesheet" href="../../../vendor/prism/prism.css"> ; <script defer src="../../../vendor/prism/prism.js"></script>
2. <body> with <header class="chapter-header"> containing:
   - <nav class="header-nav"><a href="../../../index.html" class="book-title-link">${BOOK}</a><a href="../../../toc.html" class="toc-link"><span class="toc-icon">&#9776;</span> Contents</a></nav>
   - <div class="part-label"><a href="../../index.html">Part I: Foundations of Sensory AI</a></div>
   - <div class="chapter-label"><a href="../index.html">Chapter 1: What Is Sensory AI?</a></div>
   - <h1>${s.title}</h1>
3. <main class="content"> containing, in order:
   - <blockquote class="epigraph"><p>"..."</p><cite>...</cite></blockquote> (use the coordination epigraph; cite has no leading dash, CSS adds it)
   ${isFirst ? '- A <div class="prerequisites"><h3>Prerequisites</h3><p>...</p></div> stating this chapter assumes only basic Python, calculus, and probability, all developed in Part I and Appendices A-B.' : ''}
   - An opening <div class="callout big-picture"> that frames why this section matters.
   - 3 to 5 <h2> subsections of real content developing the angle. Every concept answers what/why/how/when. Justify claims; no hand-waving.
   - At least one <div class="callout key-insight">, one <div class="callout practical-example"> (a concrete real-world mini-story with a named domain: wearable, industrial, automotive, or clinical), and at most one <div class="callout fun-note"> (dry wit, on-topic).
   - Where you teach a concept from scratch that a library makes trivial, add a <div class="callout library-shortcut"> showing the few-line modern equivalent and stating the line-count reduction and what the library handles internally.
   ${(idx >= 3 && idx <= 5) ? '- Include ONE small runnable Python code block (realistic, current libraries) with a <div class="code-caption"> placed BELOW the <pre>, and a following <div class="code-output"> showing expected output. Reference the code in prose.' : '- Include a code block only if it genuinely helps; if you do, caption goes BELOW the <pre> and must be referenced in prose.'}
   - You may include ONE inline <svg> diagram (with a <figcaption> and a prose reference). Do NOT reference any raster <img> files (none exist yet).
   - One <div class="callout exercise"> and one <div class="callout self-check"> (2-3 questions).
   - At least 2 inline cross-reference hyperlinks to other chapters using paths relative to this file (e.g. ../../chapter-02-sensor-physics-and-measurement-models/index.html, or ../../../part-05-foundation-models-and-agentic-sensing/chapter-19-time-series-foundation-models/index.html). Verify the part/chapter slugs against the directory names.
   ${isLast ? '- A <div class="callout lab"><h3 class="callout-title">Lab 1</h3><p>...</p></div> describing Lab 1 (survey a dozen sensor datasets; classify by sampling rate, dimensionality, modality, task, noise source, label cost, deployment constraint) as a concrete graded exercise.\n   - A <section class="bibliography" id="bibliography"><h2>Bibliography</h2> ... </section> with 6-10 real, hyperlinked references (arXiv/DOI/official docs) grouped by category, each with a one-sentence annotation. Only cite works you are confident exist; prefer well-known landmarks (Kalman 1960; foundational sensing/DL texts; named 2023-2026 models like TimesFM, MOMENT, Google LSM). Do not invent arXiv IDs.' : ''}
   - End <main> with <h2>What's Next</h2><p>In <a class="cross-ref" href="${nextLink}">${nextLabel}</a>, ...teaser...</p>
4. <footer> with:
   - <nav class="chapter-nav"><a href="${prevLink}" class="prev">&larr; ${prevLabel}</a><a href="../index.html" class="up">&uarr; Chapter 1</a><a href="${nextLink}" class="next">${nextLabel} &rarr;</a></nav>
   - <p class="footer-title">${BOOK}</p><p>&copy; 2026 Alexander Apartsin &middot; <a href="../../../toc.html">Contents</a></p>
5. Close </body></html>.

HARD RULES:
- NO em-dashes or double hyphens anywhere. Use commas, colons, semicolons, parentheses, or separate sentences.
- Do not use the words honestly, frankly, candidly.
- Inline math uses \\(...\\); display math uses $$...$$ or \\[...\\]. Never bare single-$ math.
- Every code block, table, figure, and callout must be referenced in the prose.
- Use only the approved callout classes. Callout titles use <h3 class="callout-title">.
- Target 900-1500 words of body prose for this section. Substantive, specific, non-generic.
- Write it so it reads as one voice with the rest of the book: concrete, confident, example-driven.

After writing the file, return the structured summary.`
}

phase('Write')
const results = await parallel(
  SECTIONS.map((s, idx) => () =>
    agent(SPEC(s, idx), { schema: WRITE_SCHEMA, label: `write-${s.id}`, phase: 'Write', effort: 'high' })
  )
)

return { plan_objectives: plan.learning_objectives, sections: results.filter(Boolean) }
