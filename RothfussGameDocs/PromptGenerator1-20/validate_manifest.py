#!/usr/bin/env python3
"""
Validate KKC prompt manifest quality before generation.

No third-party dependencies.
Checks:
- required fields
- field types
- duplicate prompt numbers/titles
- empty/thin sections
- suspicious scope drift phrases
- duplicate new_files across prompts
- optional expected prompt range (e.g. 21-40)

Usage:
  python3 validate_manifest.py
  python3 validate_manifest.py --manifest prompt_manifest_21_40.json
  python3 validate_manifest.py --start 21 --end 40
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

DEFAULT_MANIFEST = Path("prompt_manifest_21_40.json")

REQUIRED_FIELDS = {
    "number": int,
    "title": str,
    "phase_role": str,
    "goal": str,
    "goal_detail": str,
    "scope": list,
    "out_of_scope": list,
    "new_files": list,
    "modified_files": list,
    "implementation_sections": str,
    "tests": str,
    "success_criteria": list,
}

SUSPICIOUS_PHRASES = [
    "major refactor",
    "rewrite the architecture",
    "replace the architecture",
    "new web app",
    "frontend rewrite",
    "replace the engine",
    "switch frameworks",
    "new ai provider",
    "anthropic",
    "openai",
    "web server",
    "gui",
    "full natural-language parser",
    "randomly generate",
    "large-scale social simulation",
]

AMBIGUOUS_PHRASES = [
    "if needed",
    "if practical",
    "or equivalent",
    "or existing persistence structure",
    "small flavour variations based on state",
    "if approval tracking exists",
    "as needed",
    "documentation only if needed",
]

THIN_STRING_FIELDS = {
    "goal": 20,
    "goal_detail": 30,
    "implementation_sections": 80,
    "tests": 20,
}

THIN_LIST_FIELDS = {
    "scope": 2,
    "out_of_scope": 2,
    "new_files": 1,
    "modified_files": 1,
    "success_criteria": 2,
}

PROMPT_SPECIFIC_GUARDRAILS = {
    21: {
        "should_include": ["threshold", "band", "trigger"],
    },
    22: {
        "should_include": ["apply_on_day", "queue"],
    },
    23: {
        "should_include": ["approval", "re'lar"],
        "should_not_include": ["research mechanics", "full archives browsing"],
    },
    28: {
        "should_include": ["flag", "world state", "helper"],
    },
    29: {
        "should_include": ["stage", "escalation"],
    },
}


def load_manifest(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Manifest is not valid JSON: {exc}")
    if not isinstance(data, list):
        raise SystemExit("Manifest root must be a JSON array")
    return data


def norm_text(value: str) -> str:
    return " ".join(value.strip().split()).lower()


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def validate_required_fields(entry: Dict[str, Any], idx: int) -> List[str]:
    errors: List[str] = []

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(f"Entry {idx}: missing required field '{field}'")
            continue

        value = entry[field]
        if not isinstance(value, expected_type):
            errors.append(
                f"Entry {idx} prompt {entry.get('number', '?')}: field '{field}' "
                f"must be {expected_type.__name__}"
            )
            continue

        if expected_type is str and not value.strip():
            errors.append(
                f"Entry {idx} prompt {entry.get('number', '?')}: field '{field}' is empty"
            )

        if expected_type is list and len(value) == 0:
            errors.append(
                f"Entry {idx} prompt {entry.get('number', '?')}: field '{field}' is empty"
            )

    return errors


def validate_content_quality(entry: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    number = entry.get("number", "?")
    warnings: List[str] = []
    errors: List[str] = []

    for field, min_len in THIN_STRING_FIELDS.items():
        value = entry.get(field)
        if isinstance(value, str):
            stripped = value.strip()
            if len(stripped) < min_len:
                warnings.append(
                    f"Prompt {number}: field '{field}' looks thin ({len(stripped)} chars)"
                )

    for field, min_items in THIN_LIST_FIELDS.items():
        value = entry.get(field)
        if isinstance(value, list) and len(value) < min_items:
            warnings.append(
                f"Prompt {number}: field '{field}' looks thin ({len(value)} items)"
            )

    for field in ("scope", "out_of_scope", "new_files", "modified_files", "success_criteria"):
        value = entry.get(field)
        if isinstance(value, list):
            for i, item in enumerate(value):
                if not is_nonempty_string(item):
                    errors.append(
                        f"Prompt {number}: field '{field}[{i}]' must be a non-empty string"
                    )

    blob_parts = []
    for key in ("title", "phase_role", "goal", "goal_detail", "implementation_sections", "tests"):
        value = entry.get(key)
        if isinstance(value, str):
            blob_parts.append(value.lower())
    for key in ("scope", "out_of_scope", "new_files", "modified_files", "success_criteria"):
        value = entry.get(key)
        if isinstance(value, list):
            blob_parts.extend(str(v).lower() for v in value)

    blob = "\n".join(blob_parts)

    for phrase in SUSPICIOUS_PHRASES:
        if phrase in blob:
            warnings.append(
                f"Prompt {number}: suspicious phrase found -> '{phrase}'"
            )

    for phrase in AMBIGUOUS_PHRASES:
        if phrase in blob:
            warnings.append(
                f"Prompt {number}: ambiguous phrase found -> '{phrase}'"
            )

    if isinstance(entry.get("tests"), str) and "test" not in entry["tests"].lower():
        warnings.append(f"Prompt {number}: tests section may be too vague")

    if isinstance(entry.get("success_criteria"), list):
        joined = " ".join(str(x).lower() for x in entry["success_criteria"])
        if "test" not in joined and "pass" not in joined:
            warnings.append(
                f"Prompt {number}: success_criteria do not explicitly mention tests"
            )

    guide = PROMPT_SPECIFIC_GUARDRAILS.get(number)
    if guide:
        implementation_text = str(entry.get("implementation_sections", "")).lower()
        for keyword in guide.get("should_include", []):
            if keyword not in implementation_text:
                warnings.append(
                    f"Prompt {number}: implementation_sections may be missing expected keyword '{keyword}'"
                )
        for keyword in guide.get("should_not_include", []):
            if keyword in implementation_text:
                warnings.append(
                    f"Prompt {number}: implementation_sections may be drifting into '{keyword}'"
                )

    return warnings, errors


def validate_duplicates(entries: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    seen_numbers: Dict[int, int] = {}
    seen_titles: Dict[str, int] = {}
    new_file_owners: Dict[str, List[int]] = defaultdict(list)

    for entry in entries:
        number = entry.get("number")
        title = entry.get("title", "").strip()
        if isinstance(number, int):
            if number in seen_numbers:
                errors.append(f"Duplicate prompt number: {number}")
            seen_numbers[number] = 1

        title_key = norm_text(title)
        if title_key:
            if title_key in seen_titles:
                warnings.append(f"Duplicate or near-duplicate title: '{title}'")
            seen_titles[title_key] = 1

        for path in entry.get("new_files", []):
            if isinstance(path, str) and path.strip():
                new_file_owners[path.strip()].append(number)

    for path, owners in sorted(new_file_owners.items()):
        if len(owners) > 1:
            warnings.append(
                f"new_files path reused across prompts {owners}: {path}"
            )

    return warnings, errors


def validate_range(entries: List[Dict[str, Any]], start: int | None, end: int | None) -> List[str]:
    warnings: List[str] = []
    numbers = sorted(e["number"] for e in entries if isinstance(e.get("number"), int))

    if start is not None and end is not None:
        expected = list(range(start, end + 1))
        missing = [n for n in expected if n not in numbers]
        extra = [n for n in numbers if n < start or n > end]

        if missing:
            warnings.append(f"Missing prompt numbers in expected range: {missing}")
        if extra:
            warnings.append(f"Prompt numbers outside expected range: {extra}")

    for a, b in zip(numbers, numbers[1:]):
        if b != a + 1:
            warnings.append(f"Gap detected between prompt {a} and {b}")

    return warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate KKC prompt manifest")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Path to manifest JSON")
    parser.add_argument("--start", type=int, help="Expected first prompt number")
    parser.add_argument("--end", type=int, help="Expected last prompt number")
    args = parser.parse_args()

    entries = load_manifest(args.manifest)

    all_errors: List[str] = []
    all_warnings: List[str] = []

    for idx, entry in enumerate(entries):
        all_errors.extend(validate_required_fields(entry, idx))
        warnings, errors = validate_content_quality(entry)
        all_warnings.extend(warnings)
        all_errors.extend(errors)

    dup_warnings, dup_errors = validate_duplicates(entries)
    all_warnings.extend(dup_warnings)
    all_errors.extend(dup_errors)

    all_warnings.extend(validate_range(entries, args.start, args.end))

    print(f"Validated {len(entries)} prompt entries from {args.manifest}")
    print()

    if all_errors:
        print("ERRORS:")
        for err in all_errors:
            print(f"  - {err}")
        print()
    else:
        print("ERRORS: none")
        print()

    if all_warnings:
        print("WARNINGS:")
        for warning in all_warnings:
            print(f"  - {warning}")
        print()
    else:
        print("WARNINGS: none")
        print()

    if all_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
