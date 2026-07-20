# Vendored front-end libraries

These are **committed** so the published site (https://sensorbook.apartsin.com) renders math
and syntax-highlighted code. The `html2epub` build does its own KaTeX pass at build time, so
these files serve the web version only.

## KaTeX — `vendor/katex/`
Math rendering. Section pages load `katex.min.css`, `katex.min.js`, and
`contrib/auto-render.min.js`, configured for `\(...\)` (inline), `\[...\]` and `$$...$$`
(display). Single `$` is deliberately **not** a delimiter, so prose containing dollar amounts
is not mangled. `fonts/` is required by `katex.min.css`.

## Prism — `vendor/prism/`
Syntax highlighting. Pages load `prism-theme.css` and `prism-bundle.min.js` (bundle covers
Python, Bash, JSON, YAML, SQL, TOML, JS, CSS, markup, diff).

Both were taken from the sibling Building Vision AI book so versions stay consistent across
the series. To upgrade, replace the files here and keep the same filenames, since every
section page references them by name.
