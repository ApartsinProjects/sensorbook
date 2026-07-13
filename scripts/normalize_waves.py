#!/usr/bin/env python3
"""Force LF line endings on generated Workflow scripts.

gen_pack_waves.py (run on Windows) writes CRLF, which the Workflow permission
handler rejects as control characters. Run this immediately after generating
pack scripts.

Usage: python scripts/normalize_waves.py
"""
from pathlib import Path

here = Path(__file__).resolve().parent
n = 0
for f in list(here.glob("pack-*.js")) + list(here.glob("*-workflow.js")):
    b = f.read_bytes()
    if b"\r\n" in b:
        f.write_bytes(b.replace(b"\r\n", b"\n"))
        n += 1
print(f"normalized {n} workflow scripts to LF")
