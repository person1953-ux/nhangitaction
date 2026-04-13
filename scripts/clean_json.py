#!/usr/bin/env python3
"""
Clean "messy" JSON into valid JSON.

Handles:
- JSON Lines (one JSON object per line)
- Leading BOM
- Trailing commas before } or ]
- Comments (#, //, /* ... */) (best-effort)
- Single quotes -> double quotes (best-effort)
- Python literals: True/False/None -> true/false/null (best-effort)

Usage:
  python scripts/clean_json.py input.json output.json
  python scripts/clean_json.py input.jsonl output.jsonl --jsonl
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


_RE_TRAILING_COMMA = re.compile(r",(\s*[}\]])")
_RE_PY_LITERALS = re.compile(r"\b(True|False|None)\b")
_RE_LINE_COMMENT = re.compile(r"(^|[^:])//.*?$", re.M)  # avoid stripping http://
_RE_HASH_COMMENT = re.compile(r"^\s*#.*?$", re.M)
_RE_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)


def _strip_comments(text: str) -> str:
    text = _RE_BLOCK_COMMENT.sub("", text)
    text = _RE_HASH_COMMENT.sub("", text)
    text = _RE_LINE_COMMENT.sub(r"\1", text)
    return text


def _normalize(text: str) -> str:
    # remove UTF-8 BOM if present
    text = text.lstrip("\ufeff")

    text = _strip_comments(text)
    text = _RE_TRAILING_COMMA.sub(r"\1", text)
    text = _RE_PY_LITERALS.sub(lambda m: {"True": "true", "False": "false", "None": "null"}[m.group(1)], text)

    # best-effort single-quote conversion (not perfect for all edge cases)
    if "'" in text and '"' not in text:
        text = text.replace("'", '"')

    return text


def clean_json_text(text: str):
    normalized = _normalize(text)
    return json.loads(normalized)


def clean_jsonl_lines(text: str):
    out = []
    for i, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            out.append(clean_json_text(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON on line {i}: {e}") from e
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--jsonl", action="store_true", help="Treat input as JSON Lines and output as JSON Lines.")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON output (non-JSONL).")
    args = p.parse_args()

    raw = args.input.read_text(encoding="utf-8", errors="replace")

    if args.jsonl:
        records = clean_jsonl_lines(raw)
        with args.output.open("w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    else:
        obj = clean_json_text(raw)
        args.output.write_text(
            json.dumps(obj, ensure_ascii=False, indent=2 if args.pretty else None),
            encoding="utf-8",
        )

    print(f"Wrote cleaned JSON to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())