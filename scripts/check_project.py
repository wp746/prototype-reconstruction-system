#!/usr/bin/env python3
"""Run repository-level checks for the prototype reconstruction system."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validate_handoff import validate_handoff


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXCLUDED_LINK_PREFIXES = ("http://", "https://", "mailto:", "#")


def iter_handoff_json_files() -> list[Path]:
    files: set[Path] = set()
    files.add(ROOT / "templates" / "handoff-template.json")

    outputs = ROOT / "outputs"
    if outputs.exists():
        files.update(outputs.rglob("*handoff*.json"))

    return sorted(path for path in files if path.exists())


def validate_handoff_files() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in iter_handoff_json_files():
        rel = path.relative_to(ROOT)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{rel}: handoff root must be a JSON object")
            continue

        file_errors, file_warnings = validate_handoff(data)
        errors.extend(f"{rel}: {item}" for item in file_errors)
        warnings.extend(f"{rel}: {item}" for item in file_warnings)

    return errors, warnings


def markdown_files() -> list[Path]:
    ignored_roots = {".git", "outputs"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored_roots for part in path.relative_to(ROOT).parts)
    )


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.split("#", 1)[0]


def check_markdown_links() -> list[str]:
    errors: list[str] = []

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = normalize_link_target(match.group(1))
            if not target or target.startswith(EXCLUDED_LINK_PREFIXES):
                continue

            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue

            if not target_path.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: missing link target `{target}`")

    return errors


def check_required_files() -> list[str]:
    required = [
        "SKILL.md",
        "README.md",
        "CHANGELOG.md",
        "agents/openai.yaml",
        "docs/prototype-reconstruction-sop.md",
        "docs/video-analysis-module.md",
        "docs/agent-cards.md",
        "templates/character-asset-board-template-v2.md",
        "templates/scene-asset-board-template-v1.md",
        "templates/prop-asset-board-template-v1.md",
        "templates/storyboard-asset-board-template-v1.md",
        "templates/handoff-template.md",
        "templates/handoff-template.json",
        "schemas/handoff.schema.json",
        "checklists/qa-checklist.md",
        "scripts/validate_handoff.py",
    ]
    return [f"missing required file `{item}`" for item in required if not (ROOT / item).exists()]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required_errors = check_required_files()
    link_errors = check_markdown_links()
    handoff_errors, handoff_warnings = validate_handoff_files()

    errors.extend(required_errors)
    errors.extend(link_errors)
    errors.extend(handoff_errors)
    warnings.extend(handoff_warnings)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    checked_handoffs = len(iter_handoff_json_files())
    checked_markdown = len(markdown_files())
    if errors:
        print(
            "FAILED: "
            f"{len(errors)} error(s), {len(warnings)} warning(s), "
            f"{checked_handoffs} handoff JSON file(s), {checked_markdown} markdown file(s)"
        )
        return 1

    print(
        "PASSED: "
        f"0 errors, {len(warnings)} warning(s), "
        f"{checked_handoffs} handoff JSON file(s), {checked_markdown} markdown file(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
