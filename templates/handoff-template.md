# [Project] - Prototype Reconstruction Handoff

## Project Lock

- Project:
- Format:
- Duration:
- Aspect ratio:
- Platform:
- Target model/platform: Image2 + Seedance 2.0
- Remake boundary: method_remake
- Target style:
- Language:
- Delivery target:

## Source / Provenance Lock

| Source | Type | Owner | Permission | Reuse Boundary | Notes |
|---|---|---|---|---|---|
|  | video_link/local_video |  |  | Preserve method only; do not copy identifiable expression. |  |

## User Asset Manifest

Use this section only when `input_mode = REFERENCE_PLUS_USER_ASSETS`.

| Source Asset ID | Asset Type | Media DNA | Replaces Reference Function | Preserve Lock | Missing / Confirm | Module Reference Plan |
|---|---|---|---|---|---|---|
| USER_ASSET_001 | character/scene/prop/product | live-action/anime/CG/illustration/product/real_scene/mixed |  |  |  | A01/M03, A02/V04, A03/P06 |

User-provided assets are the primary asset source. Reference-video assets provide only shot function, staging, rhythm, camera logic, and composition method.

## Reference Summary

- Opening Hook:
- Setup:
- Development:
- Turning Point:
- Payoff:
- Ending Image:

## Media Probe

| Duration | Resolution | FPS | Codec | Has Audio | Detected Aspect Ratio | Analysis Mode |
|---:|---|---:|---|---|---|---|
| 0 |  | 0 |  | yes/no |  | standard_16 |

## Frame Sampling Plan

| Strategy | Target Frame Count | Timestamps | Reason |
|---|---:|---|---|
| uniform + scene_boundary + audio_aligned | 16 |  |  |

## Frame Observations

| Frame ID | Timestamp | Linked Shot | Subject | Environment | Shot Size | Angle | Composition | Lighting | Color / Texture | Style | Mood | Visible Text / Logo | Risk Flags |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| FR_001 | 0 | REF_001 |  |  |  |  |  |  |  |  |  |  |  |

## Audio Transcript

| Start | End | Speaker | Text Summary | Audio Event | Confidence |
|---:|---:|---|---|---|---:|
| 0 | 0 | unknown |  |  | 0 |

## Audio Segments

| Start | End | Summary | Tags | Dialogue Function | Rhythm Function | Confidence |
|---:|---:|---|---|---|---|---|
| 0 | 0 |  |  |  |  | low/medium/high |

## Multimodal Sync

| Timecode | Visual Event | Audio Event | Edit Signal | Narrative Function | Remake Instruction |
|---|---|---|---|---|---|
| 00:00-00:00 |  |  |  |  |  |

## Shot Ledger

| Shot ID | Timecode | Duration | Narrative Function | Shot Size | Angle | Composition | Camera Movement | Action / Blocking | Props | Lighting / Color | VFX | Sound | Edit In / Out | Emotional Function |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| REF_001 | 00:00-00:00 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |

## Preservation / Variation Map

| Reference Element | Preserve Logic | Replace With | Reason | Risk | New Prompt Rule |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## New Production Mapping

| Reference Shot | New Segment | New Beat | New Assets | Style Migration | Dialogue Function | Sound Strategy | Do Not Copy |
|---|---|---|---|---|---|---|---|
| REF_001 | SEG_001 |  |  |  |  |  |  |

## Asset Matrix

| Code | Type | Name | Must Preserve | May Clarify | Forbidden Drift |
|---|---|---|---|---|---|
| CHAR_A | character |  |  |  |  |
| SCENE_01 | scene |  |  |  |  |
| PROP_01 | prop |  |  |  |  |
| UI_TEXT_01 | ui_text |  |  |  |  |
| STYLE_LOOK_SAFE | style |  |  |  | Do not override identity, geography, props, or story facts. |

## Scene Geography

| Code | Location | Fixed Anchors | Light | Entrances / Exits | Camera-Safe Zones |
|---|---|---|---|---|---|
| SCENE_01 |  |  |  |  |  |

## Prop / UI / Text Matrix

| Code | Item | Duty | Exact Text? | Generation Mode | Post Mode |
|---|---|---|---|---|---|
| PROP_01 |  |  | no | image2_asset |  |
| UI_TEXT_01 |  | exact readable text plate | yes | post_or_ui_plate | post |

## Segment Plan

| Segment | Runtime | Beat | Function | References Needed | In State | Action | Out State | Next Handoff | Complexity Risk | Fix |
|---|---:|---|---|---|---|---|---|---|---|---|
| SEG_001 | 8 |  |  | CHAR_A, SCENE_01 |  |  |  | SEG_002 | low |  |

## Sound / Music / Post Duties

| Code | Duty | Timing | Description | Owner | Notes |
|---|---|---|---|---|---|
| POST_SOUND_01 | sound_design | SEG_001 |  | post | Do not copy original music or sound asset. |

## Compliance Risks

| Risk ID | Level | Source Element | Risk Type | Replace With | Prompt Rule | Status |
|---|---|---|---|---|---|---|
| RISK_001 | low/medium/high |  |  |  |  | open/resolved |

## Backend Instructions

```json
{
  "target_pipeline": "image2_seedance_2_0",
  "handoff_mode": "asset_storyboard_seedance_prompt_factory",
  "front_end_boundary": "deconstruction_mapping_compliance_handoff_only",
  "backend_duties": [
    "image2_asset_prompts",
    "image2_storyboard_control_boards",
    "seedance_2_0_video_prompts",
    "generation_review",
    "repair_prompts",
    "postproduction_execution"
  ]
}
```
