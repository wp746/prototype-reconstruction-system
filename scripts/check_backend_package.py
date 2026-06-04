#!/usr/bin/env python3
"""Validate a backend-production Markdown package.

This checker is intentionally structural. It does not judge creative quality,
but it catches the recurring production failures that make the backend handoff
hard to use: missing stages, missing bilingual prompts, upload reminders inside
prompt blocks, missing motion text, missing dynamic style lock, and stale
storyboard-contamination negatives.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 0. 使用说明",
    "## 0.1 前端交接标准化",
    "## 1. 阶段一：资产提示词",
    "## 2. 阶段二：干净故事板提示词",
    "## 3. 阶段三：Seedance 2.0 视频提示词",
    "## 4. QA 自检",
]

REQUIRED_TOKENS = [
    "ZH_IMAGE2_PROMPT",
    "EN_IMAGE2_PROMPT",
    "ZH_SEEDANCE_PROMPT",
    "EN_SEEDANCE_PROMPT",
    "FRONTEND_HANDOFF_NORMALIZATION",
    "SEEDANCE_MOTION_TEXT",
    "REALISTIC CINEMA STYLE LOCK",
    "NEGATIVE PROMPT",
    "BACKEND_PRODUCTION_QA",
]

REFERENCE_TOKENS = [
    "@图片1",
    "@图片2",
    "@图片3",
    "@图片4",
    "A01",
    "A03",
    "A05",
]

STALE_NEGATIVE_TERMS = [
    "蓝色箭头",
    "红色箭头",
    "绿色标签",
    "红色框线",
    "故事板边框",
    "面板编号",
    "时间码文字",
]

GREEN_REMINDER_RE = re.compile(r"<span\s+style=\"color:#15803d;[^>]*>.*?</span>", re.S)
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
CLEAN_STORYBOARD_ID_RE = re.compile(r"S(?:##|\d{2})_CLEAN_STORYBOARD_CONTROL")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def strip_code_fences(text: str) -> str:
    return CODE_FENCE_RE.sub("", text)


def code_fence_spans(text: str) -> list[tuple[int, int]]:
    return [match.span() for match in CODE_FENCE_RE.finditer(text)]


def check_package(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    text = path.read_text(encoding="utf-8")
    code_spans = code_fence_spans(text)
    outside_code = strip_code_fences(text)

    if text.count("```") % 2 != 0:
        errors.append("unbalanced Markdown code fences")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing required section `{section}`")

    for token in REQUIRED_TOKENS:
        if token not in text:
            errors.append(f"missing required token `{token}`")

    for token in REFERENCE_TOKENS:
        if token not in text:
            warnings.append(f"missing common reference token `{token}`")

    if not GREEN_REMINDER_RE.search(outside_code):
        errors.append("missing green upload reminder outside prompt code blocks")

    for match in GREEN_REMINDER_RE.finditer(text):
        in_code = any(start <= match.start() < end for start, end in code_spans)
        if in_code:
            line = line_number(text, match.start())
            errors.append(f"green upload reminder appears inside a code block at line {line}")

    if "handoff_ready:" not in text:
        errors.append("missing `handoff_ready` in frontend normalization")

    if "REALISTIC CINEMA STYLE LOCK" in text:
        style_index = text.find("REALISTIC CINEMA STYLE LOCK")
        style_tail = text[style_index : style_index + 800]
        if "根据当下" in style_tail or "current" in style_tail:
            warnings.append("style lock still appears templated; replace with project-specific drift risks")

    negative_positions = [m.start() for m in re.finditer(r"NEGATIVE PROMPT", text)]
    if negative_positions:
        negative_tail = text[negative_positions[-1] : negative_positions[-1] + 1000]
        stale_terms = [term for term in STALE_NEGATIVE_TERMS if term in negative_tail]
        if stale_terms:
            warnings.append(
                "negative prompt may contain stale storyboard-contamination terms: "
                + ", ".join(stale_terms)
            )

    if not CLEAN_STORYBOARD_ID_RE.search(text):
        errors.append("missing clean storyboard control board code")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Path to backend production Markdown package")
    args = parser.parse_args()

    if not args.package.exists():
        print(f"ERROR: file does not exist: {args.package}")
        return 2

    errors, warnings = check_package(args.package)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASSED: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
