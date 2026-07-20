export const meta = {
  name: 'draft-part',
  description: 'Draft-only pass: write all unwritten sections of one Part in house convention (no sweep, no illustrations)',
  phases: [{ title: 'Draft' }],
}

const ROOT = 'E:/Projects/Books/SensorAI'
const BOOK = 'Building Sensory AI'
const part = args // { part_roman, part_title, sections:[...], chapter_hrefs:{...} }
const hrefs = part.chapter_hrefs || {}

const WRITE_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    id: { type: 'string' }, path: { type: 'string' },
    words: { type: 'number' }, wrote: { type: 'boolean' },
    callouts: { type: 'array', items: { type: 'string' } },
    cross_refs: { type: 'number' }, notes: { type: 'string' },
  },
  required: ['id', 'path', 'wrote'],
}

function prompt(s) {
  const chmap = Object.entries(hrefs)
    .map(([n, v]) => `  Ch ${n}: ${v.title} ${v.levels}  ->  ${v.href}`).join('\n')
  return `You are a section writer for the textbook "${BOOK}: Machine Perception of the Physical World".
Write ONE complete, self-contained, publication-quality HTML page for Section ${s.sec_id}: "${s.sec_title}".
This is a section of Chapter ${s.ch_num} "${s.ch_title}" (level ${s.levels}) in Part ${s.part_roman}: ${s.part_title}.

WRITE THE FILE with the Write tool to: ${ROOT}/${s.path}
IDEMPOTENT: first check if that file already exists with real <main> content (more than ~400 words). If so, do NOT overwrite; return {wrote:false}. Otherwise write it.

Read ${ROOT}/BOOK_CONFIG.md and ${ROOT}/CONFORMANCE_CHECKLIST.md first for house rules. Skim the Chapter ${s.ch_num} entry in ${ROOT}/building_sensory_ai_book_plan.md for scope.

This chapter's other sections (do NOT cover their material; stay on THIS section's topic):
${s.siblings.map(x => '  ' + x).join('\n')}

EXACT PAGE STRUCTURE (house convention; this file is 2 levels below the book root, so use ../../ for root assets):

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Section ${s.sec_id}: ${s.sec_title}. ${BOOK}." name="description"/>
<title>Section ${s.sec_id}: ${s.sec_title} | ${BOOK}</title>
<link href="../../styles/book.css" rel="stylesheet"/>
<link href="../../styles/pygments.css" rel="stylesheet"/>
<link href="../../vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer src="../../vendor/katex/katex.min.js"></script>
<script defer onload="renderMathInElement(document.body, {delimiters:[{left:'$$',right:'$$',display:true},{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});" src="../../vendor/katex/contrib/auto-render.min.js"></script>
<link href="../../vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer src="../../vendor/prism/prism-bundle.min.js"></script>
<script defer src="../../scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../../index.html">${BOOK}</a>
<a class="toc-link" href="../../toc.html" title="Table of Contents"><span class="toc-icon">&#9776;</span> Contents</a>
</nav>
<div class="part-label"><a href="../index.html">Part ${s.part_roman}: ${s.part_title}</a></div>
<div class="chapter-label"><a href="index.html">Chapter ${s.ch_num}: ${s.ch_title}</a></div>
<h1>${s.sec_title}</h1>
</header>
<main class="content" id="main-content">
... YOUR CONTENT ...
</main>
<footer>
<p class="footer-title">${BOOK}: Machine Perception of the Physical World</p>
<p>&#169; 2026 Alexander Apartsin &amp; Yehudit Aperstein &#183; <a href="../../toc.html">Contents</a></p>
</footer>
</body>
</html>

INSIDE <main>, in order:
- <blockquote class="epigraph"><p>"..."</p><cite>An [Adjective] AI Agent</cite></blockquote> (dry, witty, on-topic; cite has no leading dash, CSS adds it).
${s.first ? '- <div class="prerequisites"><h3>Prerequisites</h3><p>...</p></div> naming what this chapter assumes and where it is developed (Part I / appendices).' : ''}
- Opening <div class="callout big-picture"> framing why this section matters.
- 3 to 5 <h2> subsections of real, specific content. Every concept answers what/why/how/when. Justify claims.
- At least one <div class="callout key-insight">, one <div class="callout practical-example"> (a concrete named-domain mini-story: wearable, industrial, automotive, clinical, robotics), and where you teach a concept a library makes trivial, one <div class="callout library-shortcut"> stating the line-count reduction and what the library handles.
- A small runnable Python code block where it genuinely helps, with a <div class="code-caption"> BELOW the <pre>, referenced in prose. (Optional for purely conceptual [F] sections.)
- One <div class="callout exercise"> and one <div class="callout self-check"> (2-3 questions).
- At least 2 inline cross-reference hyperlinks to OTHER chapters. Use ONLY these exact hrefs (pick chapters whose topics relate to this section):
${chmap}
${s.last ? `- <div class="callout lab"><h3 class="callout-title">Lab ${s.ch_num}</h3><p>${s.lab}</p></div>\n- <section class="bibliography" id="bibliography"><h2 class="bibliography-title">Bibliography</h2> ... 6-10 real hyperlinked references grouped by <p class="bib-category">, each as <div class="bib-entry-card"><p class="bib-ref"><a href="URL">Author (Year). Title. Venue.</a></p><p class="bib-annotation">why it matters</p></div>. Cite only works you are confident exist (landmarks + well-known 2023-2026 models like TimesFM, MOMENT, Google LSM). Do NOT invent arXiv IDs or DOIs.</section>` : ''}
- End with <h2>What's Next</h2><p>In <a class="cross-ref" href="${s.next_link}">${s.next_label}</a>, ...teaser...</p>

HARD RULES:
- NO em-dashes or double hyphens anywhere. Use commas, colons, semicolons, parentheses, separate sentences.
- Do not use the words honestly, frankly, candidly.
- Inline math uses \\(...\\); display math uses $$...$$ or \\[...\\]. Never bare single-$ math.
- Every code block, table, figure, callout must be referenced in prose. Callout titles use <h3 class="callout-title">.
- Target 900 to 1400 words of body prose. Specific, confident, example-driven, one voice with the rest of the book.
- Footer nav is handled by book.js; do NOT add a chapter-nav element.

After writing, return the structured summary.`
}

phase('Draft')
const results = await pipeline(
  part.sections,
  (s) => agent(prompt(s), { schema: WRITE_SCHEMA, label: `draft-${s.sec_id}`, phase: 'Draft', effort: 'high' })
)

const wrote = results.filter(Boolean).filter(r => r.wrote).length
return { part: part.part_roman, requested: part.sections.length, wrote, sections: results.filter(Boolean).map(r => r.path) }
