#!/usr/bin/env python3
"""Validate a prototype reconstruction handoff JSON file.

The validator intentionally uses only the Python standard library so the SOP can
run in a clean production folder without dependency setup.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "project_lock",
    "source_lock",
    "reference_summary",
    "media_probe",
    "frame_sampling_plan",
    "frame_observations",
    "audio_transcript",
    "audio_segments",
    "multimodal_sync",
    "shot_ledger",
    "preservation_variation_map",
    "new_production_mapping",
    "asset_matrix",
    "scene_geography",
    "prop_ui_text_matrix",
    "segment_plan",
    "sound_post_duties",
    "compliance_risks",
    "backend_instructions",
]

REQUIRED_SHOT_FIELDS = [
    "shot_id",
    "timecode",
    "duration",
    "narrative_function",
    "shot_size",
    "angle",
    "composition",
    "camera_movement",
    "action",
    "blocking",
    "props",
    "lighting",
    "color",
    "vfx",
    "sound",
    "edit_in",
    "edit_out",
    "emotional_function",
    "dialogue_function",
]

REQUIRED_SEGMENT_FIELDS = [
    "segment",
    "runtime",
    "beat",
    "function",
    "references_needed",
    "in_state",
    "action",
    "out_state",
    "next_handoff",
    "complexity_risk",
    "fix",
]

ASSET_CODE_RE = re.compile(
    r"^(CHAR_[A-Z]+|SCENE_[0-9]{2}|PROP_[0-9]{2}|UI_TEXT_[0-9]{2}|"
    r"STYLE_LOOK_SAFE|EXTRA_GROUP_[A-Z0-9_]+|PRODUCT_[0-9]{2})$"
)


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def require_fields(obj: dict[str, Any], fields: list[str], path: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj:
            errors.append(f"{path}: missing required field `{field}`")
        elif is_blank(obj[field]):
            errors.append(f"{path}.{field}: value is blank")


def validate_handoff(data: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"$: missing top-level field `{key}`")

    if errors:
        return errors, warnings

    project_lock = data["project_lock"]
    if project_lock.get("remake_boundary") != "method_remake":
        errors.append("project_lock.remake_boundary must be `method_remake`")

    media_probe = data["media_probe"]
    require_fields(
        media_probe,
        [
            "duration",
            "width",
            "height",
            "fps",
            "codec",
            "has_audio",
            "aspect_ratio_detected",
            "analysis_mode",
        ],
        "media_probe",
        errors,
    )
    if media_probe.get("analysis_mode") not in {"quick_8", "standard_16", "forensic_32"}:
        errors.append("media_probe.analysis_mode must be quick_8, standard_16, or forensic_32")

    sampling_plan = data["frame_sampling_plan"]
    require_fields(
        sampling_plan,
        ["strategy", "target_frame_count", "timestamps", "reason"],
        "frame_sampling_plan",
        errors,
    )
    if not isinstance(sampling_plan.get("timestamps"), list) or not sampling_plan.get("timestamps"):
        errors.append("frame_sampling_plan.timestamps must contain at least one timestamp")

    backend = data["backend_instructions"]
    if backend.get("target_pipeline") != "image2_seedance_2_0":
        errors.append("backend_instructions.target_pipeline must be `image2_seedance_2_0`")
    if backend.get("handoff_mode") != "asset_storyboard_seedance_prompt_factory":
        errors.append(
            "backend_instructions.handoff_mode must be "
            "`asset_storyboard_seedance_prompt_factory`"
        )

    source_lock = data["source_lock"]
    if not source_lock.get("sources"):
        errors.append("source_lock.sources must contain at least one source")
    if not source_lock.get("forbidden_copy_items"):
        errors.append("source_lock.forbidden_copy_items must not be empty")

    shot_ids: set[str] = set()
    for index, shot in enumerate(data["shot_ledger"]):
        path = f"shot_ledger[{index}]"
        require_fields(shot, REQUIRED_SHOT_FIELDS, path, errors)
        shot_id = shot.get("shot_id")
        if shot_id:
            if not re.match(r"^REF_[0-9]{3}$", shot_id):
                errors.append(f"{path}.shot_id must match REF_###")
            if shot_id in shot_ids:
                errors.append(f"{path}.shot_id duplicates `{shot_id}`")
            shot_ids.add(shot_id)
        if isinstance(shot.get("duration"), (int, float)) and shot["duration"] <= 0:
            errors.append(f"{path}.duration must be greater than 0")

    for index, frame in enumerate(data["frame_observations"]):
        path = f"frame_observations[{index}]"
        require_fields(
            frame,
            [
                "frame_id",
                "timestamp",
                "linked_shot",
                "subject",
                "environment",
                "shot_size",
                "angle",
                "composition",
                "lighting",
                "color_texture",
                "style",
                "mood",
                "visible_text_or_logo",
            ],
            path,
            errors,
        )
        if "risk_flags" not in frame:
            errors.append(f"{path}: missing required field `risk_flags`")
        if frame.get("linked_shot") not in shot_ids:
            errors.append(f"{path}.linked_shot does not match any shot_ledger shot_id")
        if frame.get("risk_flags") and frame.get("visible_text_or_logo") == "none":
            warnings.append(f"{path}: risk_flags are present but visible_text_or_logo is none")

    if not data["multimodal_sync"]:
        errors.append("multimodal_sync must contain at least one sync record")

    for index, transcript in enumerate(data["audio_transcript"]):
        path = f"audio_transcript[{index}]"
        require_fields(transcript, ["start", "end", "speaker", "confidence", "audio_event"], path, errors)
        if transcript.get("confidence", 1) < 0.7:
            warnings.append(f"{path}: low ASR confidence needs human review")

    for index, segment in enumerate(data["audio_segments"]):
        path = f"audio_segments[{index}]"
        require_fields(
            segment,
            ["start", "end", "summary", "tags", "dialogue_function", "rhythm_function", "confidence"],
            path,
            errors,
        )
        if segment.get("confidence") == "low":
            warnings.append(f"{path}: low confidence audio segment needs human review")

    asset_codes: set[str] = set()
    for index, asset in enumerate(data["asset_matrix"]):
        path = f"asset_matrix[{index}]"
        require_fields(
            asset,
            ["code", "type", "name", "must_preserve", "may_clarify", "forbidden_drift"],
            path,
            errors,
        )
        code = asset.get("code")
        if code:
            if not ASSET_CODE_RE.match(code):
                errors.append(f"{path}.code `{code}` is not an approved asset code")
            if code in asset_codes:
                errors.append(f"{path}.code duplicates `{code}`")
            asset_codes.add(code)

    segment_ids: set[str] = set()
    for index, segment in enumerate(data["segment_plan"]):
        path = f"segment_plan[{index}]"
        require_fields(segment, REQUIRED_SEGMENT_FIELDS, path, errors)
        segment_id = segment.get("segment")
        if segment_id:
            if not re.match(r"^SEG_[0-9]{3}$", segment_id):
                errors.append(f"{path}.segment must match SEG_###")
            if segment_id in segment_ids:
                errors.append(f"{path}.segment duplicates `{segment_id}`")
            segment_ids.add(segment_id)

        runtime = segment.get("runtime")
        if isinstance(runtime, (int, float)):
            if runtime < 4 or runtime > 15:
                errors.append(f"{path}.runtime must be between 4 and 15 seconds")
        else:
            errors.append(f"{path}.runtime must be a number")

        for ref in segment.get("references_needed", []):
            if ref not in asset_codes:
                warnings.append(f"{path}.references_needed contains unknown asset `{ref}`")

    for index, mapping in enumerate(data["new_production_mapping"]):
        path = f"new_production_mapping[{index}]"
        require_fields(
            mapping,
            [
                "reference_shot",
                "new_segment",
                "new_beat",
                "new_assets",
                "style_migration",
                "dialogue_function",
                "sound_strategy",
                "do_not_copy",
            ],
            path,
            errors,
        )
        if mapping.get("reference_shot") not in shot_ids:
            errors.append(f"{path}.reference_shot does not match any shot_ledger shot_id")
        if mapping.get("new_segment") not in segment_ids:
            errors.append(f"{path}.new_segment does not match any segment_plan segment")
        for asset in mapping.get("new_assets", []):
            if asset not in asset_codes:
                warnings.append(f"{path}.new_assets contains unknown asset `{asset}`")
        if "do not copy" not in str(mapping.get("do_not_copy", "")).lower():
            warnings.append(f"{path}.do_not_copy should explicitly include a do-not-copy rule")

    for index, risk in enumerate(data["compliance_risks"]):
        path = f"compliance_risks[{index}]"
        require_fields(
            risk,
            ["risk_id", "level", "source_element", "risk_type", "replace_with", "prompt_rule", "status"],
            path,
            errors,
        )
        if risk.get("level") == "high" and risk.get("status") == "open":
            errors.append(f"{path}: high risk item cannot remain open")

    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate_handoff.py path/to/handoff.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("ERROR: handoff root must be a JSON object", file=sys.stderr)
        return 1

    errors, warnings = validate_handoff(data)

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
