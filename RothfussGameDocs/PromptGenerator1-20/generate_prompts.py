#!/usr/bin/env python3
"""
Generate KKC prompt files from a JSON manifest and a markdown template.

No third-party dependencies required.
Uses:
- prompt_template.md
- prompt_manifest_21_40.json
- optional project_state.md
- optional hard_bans.md
- optional architecture_rule.md
- optional architecture_reminders.md

Outputs one .md file per prompt into ./generated_prompts by default.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

ROOT = Path(".")
DEFAULT_TEMPLATE = ROOT / "prompt_template.md"
DEFAULT_COMPACT_TEMPLATE = ROOT / "prompt_template_compact.md"
DEFAULT_MANIFEST = ROOT / "prompt_manifest_21_40.json"
DEFAULT_OUTPUT_DIR = ROOT / "generated_prompts"

OPTIONAL_CONTEXT_FILES = {
    "project_state": ROOT / "project_state.md",
    "hard_bans": ROOT / "hard_bans.md",
    "architecture_rule": ROOT / "architecture_rule.md",
    "architecture_reminders": ROOT / "architecture_reminders.md",
}

REQUIRED_FIELDS = [
    "number",
    "title",
    "phase_role",
    "goal",
    "goal_detail",
    "scope",
    "out_of_scope",
    "new_files",
    "modified_files",
    "implementation_sections",
    "tests",
    "success_criteria",
]


def read_text(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else default


def normalise_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def format_bullets(items: Iterable[str], indent: str = "  - ") -> str:
    items = [str(x).strip() for x in items if str(x).strip()]
    return "\n".join(f"{indent}{item}" for item in items) if items else f"{indent}(none)"


def format_numbered(items: Iterable[str], indent: str = "  ") -> str:
    items = [str(x).strip() for x in items if str(x).strip()]
    return "\n".join(f"{indent}{i + 1}. {item}" for i, item in enumerate(items)) if items else f"{indent}1. (none)"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def validate_prompt_entry(entry: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(f"Missing required field: {field}")

    if "number" in entry and not isinstance(entry["number"], int):
        errors.append("Field 'number' must be an integer")

    list_fields = [
        "scope",
        "out_of_scope",
        "new_files",
        "modified_files",
        "success_criteria",
    ]
    for field in list_fields:
        if field in entry and not isinstance(entry[field], list):
            errors.append(f"Field '{field}' must be a list")

    string_fields = [
        "title",
        "phase_role",
        "goal",
        "goal_detail",
        "implementation_sections",
        "tests",
    ]
    for field in string_fields:
        if field in entry and not isinstance(entry[field], str):
            errors.append(f"Field '{field}' must be a string")

    return errors


def load_manifest(path: Path) -> List[Dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Manifest not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Manifest is not valid JSON: {exc}")

    if not isinstance(data, list):
        raise SystemExit("Manifest root must be a JSON array")

    errors: List[str] = []
    seen_numbers = set()

    for idx, entry in enumerate(data):
        if not isinstance(entry, dict):
            errors.append(f"Entry {idx} is not an object")
            continue

        entry_errors = validate_prompt_entry(entry)
        if entry_errors:
            errors.extend([f"Entry {idx}: {msg}" for msg in entry_errors])

        number = entry.get("number")
        if isinstance(number, int):
            if number in seen_numbers:
                errors.append(f"Duplicate prompt number: {number}")
            seen_numbers.add(number)

    if errors:
        joined = "\n".join(f"- {e}" for e in errors)
        raise SystemExit(f"Manifest validation failed:\n{joined}")

    return data


def render_template(template: str, values: Dict[str, str]) -> str:
    missing = []

    def replacer(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            missing.append(key)
            return match.group(0)
        return values[key]

    rendered = re.sub(r"\{\{([a-zA-Z0-9_]+)\}\}", replacer, template)

    if missing:
        missing_list = ", ".join(sorted(set(missing)))
        raise SystemExit(f"Template contains unresolved placeholders: {missing_list}")

    return rendered.strip() + "\n"


def build_values(
    entry: Dict[str, Any],
    global_context: Dict[str, str],
) -> Dict[str, str]:
    number = entry["number"]
    previous_prompt = str(number - 1)

    title = str(entry["title"]).strip()
    filename_slug = slugify(title)

    values: Dict[str, str] = {
        "number": str(number),
        "previous_prompt": previous_prompt,
        "title": title,
        "phase_role": str(entry["phase_role"]).strip(),
        "goal": str(entry["goal"]).strip(),
        "goal_detail": normalise_newlines(str(entry["goal_detail"])),
        "scope": format_numbered(entry["scope"]),
        "out_of_scope": format_bullets(entry["out_of_scope"]),
        "new_files": format_bullets(entry["new_files"]),
        "modified_files": format_bullets(entry["modified_files"]),
        "implementation_sections": normalise_newlines(str(entry["implementation_sections"])),
        "tests": normalise_newlines(str(entry["tests"])),
        "success_criteria": format_bullets(entry["success_criteria"]),
        "hard_bans": global_context["hard_bans"],
        "architecture_rule": global_context["architecture_rule"],
        "architecture_reminders": global_context["architecture_reminders"],
        "project_state": global_context["project_state"],
        "filename_slug": filename_slug,
    }

    return values


def select_entries(
    manifest: List[Dict[str, Any]],
    start: Optional[int],
    end: Optional[int],
    only: Optional[List[int]],
) -> List[Dict[str, Any]]:
    entries = manifest

    if only:
        wanted = set(only)
        entries = [e for e in entries if e["number"] in wanted]

    if start is not None:
        entries = [e for e in entries if e["number"] >= start]

    if end is not None:
        entries = [e for e in entries if e["number"] <= end]

    entries = sorted(entries, key=lambda e: e["number"])

    if not entries:
        raise SystemExit("No prompt entries selected")

    return entries


def parse_only_list(value: Optional[str]) -> Optional[List[int]]:
    if not value:
        return None
    nums = []
    for chunk in value.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            nums.append(int(chunk))
        except ValueError:
            raise SystemExit(f"Invalid prompt number in --only: {chunk}")
    return nums or None


def build_global_context() -> Dict[str, str]:
    return {
        "project_state": normalise_newlines(read_text(OPTIONAL_CONTEXT_FILES["project_state"], "")),
        "hard_bans": normalise_newlines(read_text(OPTIONAL_CONTEXT_FILES["hard_bans"], "HARD BANS — UNCHANGED")),
        "architecture_rule": normalise_newlines(read_text(OPTIONAL_CONTEXT_FILES["architecture_rule"], "ARCHITECTURE RULE — STILL ABSOLUTE")),
        "architecture_reminders": normalise_newlines(read_text(OPTIONAL_CONTEXT_FILES["architecture_reminders"], "These rules from Prompt 1 still apply.")),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate KKC prompt markdown files from a manifest.")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="Path to prompt template markdown")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Path to JSON manifest")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory")
    parser.add_argument("--start", type=int, help="First prompt number to generate")
    parser.add_argument("--end", type=int, help="Last prompt number to generate")
    parser.add_argument("--only", type=str, help="Comma-separated prompt numbers to generate, e.g. 21,22,25")
    parser.add_argument("--compact", action="store_true", help="Use the compact template to reduce repeated boilerplate")
    parser.add_argument("--dry-run", action="store_true", help="Print generated prompts instead of writing files")
    args = parser.parse_args()

    if args.compact:
        args.template = DEFAULT_COMPACT_TEMPLATE

    template = read_text(args.template)
    if not template:
        raise SystemExit(f"Template not found or empty: {args.template}")

    manifest = load_manifest(args.manifest)
    only = parse_only_list(args.only)
    entries = select_entries(manifest, args.start, args.end, only)
    global_context = build_global_context()

    if not args.dry_run:
        args.out.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        values = build_values(entry, global_context)
        rendered = render_template(template, values)

        filename = f"prompt_{entry['number']:02}_{values['filename_slug']}.md"
        output_path = args.out / filename

        if args.dry_run:
            divider = "=" * 80
            print(divider)
            print(filename)
            print(divider)
            print(rendered)
        else:
            output_path.write_text(rendered, encoding="utf-8")
            print(f"Wrote {output_path}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
