#!/usr/bin/env python3
"""
Review generated prompt files for common quality issues.

Checks:
- missing core sections
- thin implementation or tests blocks
- repeated full boilerplate markers
- ambiguous wording in rendered output
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

DEFAULT_DIR = Path("generated_prompts")

REQUIRED_HEADERS = [
    "GOAL OF THIS PROMPT",
    "SCOPE OF THIS PROMPT",
    "IMPLEMENTATION DETAILS",
    "TESTS",
    "SUCCESS CRITERIA",
]

AMBIGUOUS_PHRASES = [
    "if needed",
    "if practical",
    "or equivalent",
    "as needed",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section_body(text: str, header: str) -> str:
    start = text.find(header)
    if start == -1:
        return ""
    next_start = len(text)
    for other in REQUIRED_HEADERS:
        if other == header:
            continue
        candidate = text.find(other, start + len(header))
        if candidate != -1:
            next_start = min(next_start, candidate)
    return text[start:next_start].strip()


def review_file(path: Path) -> List[str]:
    warnings: List[str] = []
    text = read_text(path)
    lower = text.lower()

    for header in REQUIRED_HEADERS:
        if header not in text:
            warnings.append(f"{path.name}: missing header '{header}'")

    implementation = section_body(text, "IMPLEMENTATION DETAILS")
    tests = section_body(text, "TESTS")

    if len(implementation) < 160:
        warnings.append(f"{path.name}: implementation block looks thin")
    if len(tests) < 80:
        warnings.append(f"{path.name}: tests block looks thin")

    if "Current project state:" in text and "ARCHITECTURE REMINDERS" in text:
        warnings.append(f"{path.name}: uses the full boilerplate template; consider --compact if token cost matters")

    for phrase in AMBIGUOUS_PHRASES:
        if phrase in lower:
            warnings.append(f"{path.name}: contains ambiguous phrase '{phrase}'")

    return warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Review generated KKC prompts")
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR, help="Directory containing generated prompt files")
    args = parser.parse_args()

    if not args.dir.exists():
        raise SystemExit(f"Directory not found: {args.dir}")

    prompt_files = sorted(args.dir.glob("prompt_*.md"))
    if not prompt_files:
        raise SystemExit(f"No generated prompt files found in: {args.dir}")

    all_warnings: List[str] = []
    for path in prompt_files:
        all_warnings.extend(review_file(path))

    print(f"Reviewed {len(prompt_files)} generated prompt files from {args.dir}")
    print()
    if all_warnings:
        print("WARNINGS:")
        for warning in all_warnings:
            print(f"  - {warning}")
    else:
        print("WARNINGS: none")


if __name__ == "__main__":
    main()
