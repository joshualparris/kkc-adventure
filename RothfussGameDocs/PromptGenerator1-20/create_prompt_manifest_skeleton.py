#!/usr/bin/env python3
"""Generate a placeholder prompt manifest for a numeric prompt range."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

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


def build_placeholder_entry(number: int) -> Dict[str, Any]:
    return {
        "number": number,
        "title": f"Prompt {number} Placeholder Title",
        "phase_role": (
            "Write a placeholder phase/role description for this prompt so the manifest "
            "is structurally valid and ready to be replaced with real prompt guidance."
        ),
        "goal": "Define the core goal of this prompt in a clear, succinct sentence.",
        "goal_detail": (
            "Provide a short clarification of the goal with enough detail to make the intent "
            "clear without being specific to any implementation details."
        ),
        "scope": [
            "Add or modify the minimal files needed for this prompt.",
            "Keep the implementation constrained and deterministic.",
        ],
        "out_of_scope": [
            "Large new systems or unrelated features.",
            "Major architecture rewrites.",
        ],
        "new_files": [
            f"src/engine/placeholder{number}.ts",
            f"tests/placeholder{number}.test.ts",
        ],
        "modified_files": [
            "src/engine/state.ts",
            "src/narration/renderLocation.ts",
        ],
        "implementation_sections": (
            "Write the required implementation details and structure here so a developer "
            "can implement the feature in a deterministic way."
        ),
        "tests": (
            "Describe the expected tests for this prompt, including at least one positive "
            "and one negative case."
        ),
        "success_criteria": [
            "The prompt is implemented in a small, readable way.",
            "The new behavior is covered by tests.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a placeholder JSON prompt manifest for a numeric prompt range."
    )
    parser.add_argument("--start", type=int, required=True, help="First prompt number to scaffold")
    parser.add_argument("--end", type=int, required=True, help="Last prompt number to scaffold")
    parser.add_argument("--output", type=Path, default=Path("prompt_manifest_41_100.json"), help="Output manifest path")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing manifest file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.start <= 0 or args.end < args.start:
        raise SystemExit("Invalid range: --start must be positive and --end must be >= --start")

    if args.output.exists() and not args.force:
        raise SystemExit(f"Output manifest already exists: {args.output} (use --force to overwrite)")

    entries: List[Dict[str, Any]] = [build_placeholder_entry(n) for n in range(args.start, args.end + 1)]
    args.output.write_text(json.dumps(entries, indent=2), encoding="utf-8")
    print(f"Wrote {args.output} with {len(entries)} placeholder entries")


if __name__ == "__main__":
    main()
