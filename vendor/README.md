# Vendored front-end libraries

Browser-preview dependencies for the HTML book. These are **not committed** (see
`.gitignore`); install them locally before opening pages in a browser. The `html2epub`
build has its own KaTeX pass, so these are only needed for local preview.

## KaTeX (math rendering) → `vendor/katex/`
Download a KaTeX release (CSS + JS + `contrib/auto-render.min.js`) from
https://github.com/KaTeX/KaTeX/releases and extract into `vendor/katex/` so that
`vendor/katex/katex.min.css` and `vendor/katex/katex.min.js` exist.

## Prism (syntax highlighting) → `vendor/prism/`
Build a bundle at https://prismjs.com/download.html (languages: Python, Bash, JSON, YAML)
and place `prism.css` + `prism.js` in `vendor/prism/`.

Pages link these with a relative path adjusted for their depth, e.g. from a section file:
`../../../vendor/katex/katex.min.css`.
