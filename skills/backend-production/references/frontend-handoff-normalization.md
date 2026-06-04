# Frontend Handoff Normalization

Use this reference when frontend input is vague, incomplete, or not formatted for the backend production skill.

## Goal

Convert messy frontend notes into the standard backend handoff. Do not invent high-risk story facts. Infer conservative production details when the user intent is clear. Mark uncertain fields.

## Normalization Output

```text
FRONTEND_HANDOFF_NORMALIZATION:
input_quality: standard / usable_but_incomplete / vague / blocked
inferred_fields:
missing_fields:
assumptions:
needs_model_completion: yes / no
user_questions:
handoff_ready: yes / no
```

## Standard Backend Handoff

```text
PROJECT:
- project_name:
- segment_id:
- runtime:
- aspect_ratio:
- target_model: Seedance 2.0

FRONTEND_HANDOFF:
- story_function:
- shot_count:
- storyboard_layout:
- continuity_mode:
- in_state:
- action_chain:
- out_state:
- continuity_to_next:

ASSET_PLAN:
- character_assets:
- scene_assets:
- prop_assets:
- user_uploaded_assets:

SHOT_PLAN:
- SH01:
  - timecode:
  - shot_size:
  - composition:
  - action_state:
  - camera_movement:
  - action_direction:
  - cut_function:
  - active_assets:

STYLE_RISK:
- likely_drift:
- likely_contamination:
- likely_missing_shots:
- final_frame_risk:

STYLE_CONTRACT:
- source_style_evidence:
- render_style:
- medium:
- realism_level:
- material_finish:
- lighting_language:
- lens_language:
- color_palette:
- forbidden_styles:
- style_source: explicit / inferred_from_assets / inferred_from_reference / needs_user
```

## Completion Rules

### Style Contract Is A Hard Gate

Do not enter backend production until `STYLE_CONTRACT` is present.

`STYLE_RISK` describes what may go wrong. `STYLE_CONTRACT` defines what every asset, storyboard, and video prompt must look like.

If the frontend says the style directly, use it:

```text
3D / live-action / photoreal / anime / cartoon / clay / ink / pixel / documentary / surreal / product render
```

If the frontend does not say style directly, infer conservatively from:

- uploaded assets or their descriptions.
- reference stills.
- scene material language.
- character design language.
- platform/model output the user is testing.

Record the evidence:

```text
style_source: inferred_from_assets
source_style_evidence: "角色和场景均为 3D 体积光、圆润材质、动画电影比例"
```

If evidence is insufficient or contradictory, block production and ask only the minimum question:

```text
这个项目最终统一成哪种风格：3D 动画电影、真人电影感、动漫、卡通，还是其他？
```

### Safe To Infer

- `segment_id` if only one segment exists: use `SEG01`.
- `target_model` if the user asks B line / Seedance: use `Seedance 2.0`.
- `storyboard_layout` from shot count: 1-4 shots `1x4/4x1`; 5-6 shots `3x2`; 7-8 shots `4x2`; 9-10 shots `5x2`; over 10 split segments.
- `timecode` from runtime and shot count when rhythm is not specified, but mark as estimated.
- asset codes from the backend standard: `A01` main character, `A03` main scene, `A05` key prop.
- style contract from strong visual evidence, but mark `style_source` and `source_style_evidence`.
- style risks from genre and prior failures, but mark as inferred.

### Do Not Infer Without Evidence

- exact character identity if user says they have a specific uploaded character.
- exact brand/product claims.
- exact dialogue.
- final frame if the story payoff is unknown.
- visual style when no assets, no reference, and no style words are provided.
- shot count when the user explicitly says the reference has a specific number but does not provide it.

### Ask User When Missing

Ask only the minimum questions needed:

```text
需要补齐：
1. 这段时长和画幅是多少？
2. 是否已有角色/场景/道具资产？如果有，请告诉我对应图片。
3. 你希望故事板按几个镜头控制？
4. 最终统一风格是什么？例如 3D 动画电影、真人电影感、动漫、卡通、超现实。
```

## Model Completion Prompt

Use this when the user permits model completion:

```text
请把以下模糊前端材料整理成 B 线后端生产可用 handoff。能保守推断的字段请补齐并标记 inferred；不能推断的字段列入 missing_fields。不要进入资产、故事板或 Seedance 生产，只输出标准 handoff。

[RAW_FRONTEND_INPUT]
...

[OUTPUT_FORMAT]
FRONTEND_HANDOFF_NORMALIZATION:
input_quality:
inferred_fields:
missing_fields:
assumptions:
needs_model_completion:
user_questions:
handoff_ready:

PROJECT:
...

FRONTEND_HANDOFF:
...

ASSET_PLAN:
...

SHOT_PLAN:
...

STYLE_RISK:
...

STYLE_CONTRACT:
...
```

## Backend Entry Gate

Only enter backend production when:

```text
handoff_ready: yes
shot_count: known
storyboard_layout: known
asset_plan: known or intentionally none
shot_plan: complete enough for every SH
style_risk: present
style_contract: present and not contradictory
```
