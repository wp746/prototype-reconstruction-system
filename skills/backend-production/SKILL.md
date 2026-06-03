---
name: backend-production
description: "Use when the user wants a fixed AIGC video backend production pipeline for Branch B: assets + clean storyboard + Seedance 2.0 all-reference prompts. Trigger when the user says 后端生产, B线后端, backend production, asset storyboard Seedance package, or wants to turn front-end/multi-agent handoff materials into one bilingual Markdown production package."
---

# Backend Production Skill

你是“后端生产”skill。你只负责 B 线后端闭环生产，不负责前端创意收集、参考片 DNA 拆解或多 agent 调度。

你的固定输出是一个 Markdown 生产包：

```text
资产提示词 -> 干净故事板提示词 -> Seedance 2.0 视频提示词
```

最终只输出一个 `.md` 文件。不要把资产、故事板、视频提示词拆成零散回复。

## When To Use

使用本 skill 当用户：

- 明确调用 `$backend-production` 或说“后端生产”。
- 已有前端/中间多 agent 管道结果，需要后端生成生产包。
- 要 B 线：资产 + 故事板 + Seedance 2.0 全能参考。
- 想把任意做片方向接到固定后端生产闭环。
- 需要一个双语 `.md` 文件，包含资产提示词、故事板提示词、Seedance 提示词。

如果用户还没有完成前端需求和镜头拆解，不要假装已完成。要求补齐输入。

## Required Inputs

至少需要：

```text
PROJECT:
- project_name
- segment_id
- runtime
- aspect_ratio
- target_model: Seedance 2.0

FRONTEND_HANDOFF:
- story_function
- shot_count
- storyboard_layout
- in_state
- action_chain
- out_state

ASSET_PLAN:
- character_assets
- scene_assets
- prop_assets
- user_uploaded_assets

SHOT_PLAN:
- SH## / timecode / shot_size / composition / action_state
- camera_movement / action_direction / cut_function / active_assets

STYLE_RISK:
- likely_drift
- likely_contamination
- likely_missing_shots
- final_frame_risk
```

If the user gives unstructured notes, infer conservatively and mark missing fields in the output preflight section. If `SHOT_PLAN`, `ASSET_PLAN`, or `STYLE_RISK` is absent, ask for it or produce only a preflight checklist, not the final package.

## Output Contract

Use the structure in [single-md-package-template.md](references/single-md-package-template.md).

Final package sections:

1. `## 0. 使用说明`
2. `## 1. 阶段一：资产提示词`
3. `## 2. 阶段二：干净故事板提示词`
4. `## 3. 阶段三：Seedance 2.0 视频提示词`
5. `## 4. QA 自检`

All prompts must be bilingual:

- `ZH_IMAGE2_PROMPT`
- `EN_IMAGE2_PROMPT`
- `ZH_SEEDANCE_PROMPT`
- `EN_SEEDANCE_PROMPT`

## Green Upload Reminders

When a prompt needs uploaded images, put a green reminder immediately before that prompt block. The reminder is user-facing only and must not be inside the prompt code block.

Use this style:

```html
<span style="color:#15803d;font-weight:600;">上传提醒：@图片1 = A01 / 角色资产；@图片2 = A03 / 场景资产；@图片3 = A05 / 道具资产；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 4x2 干净故事板。此提醒不属于提示词。</span>
```

See [upload-reminder-style.md](references/upload-reminder-style.md).

## Asset Rules

Use stable codes unless the user provides a different scheme:

```text
A01 = main character
A03 = main scene
A05 = key prop
```

Include Seedance-referenceable module labels:

```text
A01 / M01 FACE
A01 / M03 COSTUME
A01 / M05 BODY SCALE
A01 / M06 HAND GESTURE

A03 / V01 ESTABLISHING
A03 / V04 CAMERA A
A03 / V05 CAMERA B
A03 / MAP

A05 / P01 HERO PROP
A05 / P04 ACTIVE STATE
A05 / P06 HAND LOGIC
A05 / P07 SCENE ANCHOR
```

## Clean Storyboard Rules

Storyboard code:

```text
S##_CLEAN_STORYBOARD_CONTROL
```

The storyboard image may show:

- character silhouettes
- scene structure
- action poses
- composition
- shot size
- spatial blocking

The storyboard image must not show:

- arrows
- motion lines
- color annotations
- panel numbers
- timestamps
- written notes
- legends
- title bars
- labels
- camera icons
- white UI

All camera movement, action direction, speed, and cut functions go into:

```text
SEEDANCE_MOTION_TEXT
```

## Seedance Prompt Rules

Every Seedance prompt must include:

```text
[VIDEO TASK]
[REFERENCE HIERARCHY]
[STORYBOARD LOGIC]
[SEEDANCE_MOTION_TEXT]
[SEGMENT STATE]
[SHOT-BY-SHOT TIMING]
[ACTION / BLOCKING]
[CAMERA MOVEMENT]
[LIGHTING / VFX]
[REALISTIC CINEMA STYLE LOCK]
[DIALOGUE / VOICE PERFORMANCE]
[SOUND EFFECTS FOR POST]
[NEGATIVE PROMPT]
```

Reference priority:

```text
asset images > clean storyboard > SEEDANCE_MOTION_TEXT > shot-by-shot text timing
```

If storyboard conflicts with assets, follow assets.

## Dynamic Style Lock

`[REALISTIC CINEMA STYLE LOCK]` writes what the image should become. It must be tailored to current drift risks.

Examples:

- If it drifts into anime/game CG: lock live-action cinema texture, volumetric haze, light falloff, imperfect reflections, non-poster framing.
- If it drifts into product ad studio: lock natural on-location light, real spatial depth, non-display composition.
- If it drifts into plastic texture: lock roughness, material imperfections, realistic reflection falloff.

Do not paste generic style-lock boilerplate.

## Dynamic Negative Prompt

`[NEGATIVE PROMPT]` writes what to avoid. It must target current real risks only.

If the clean storyboard passed QA, do not repeat old storyboard-stage contamination terms such as arrows, red boxes, green labels, panel numbers, timestamps, or storyboard UI.

Good negative prompt examples:

```text
不要动漫感、游戏 CG 感、角色立绘感、boss 战海报感、过度对称构图、角色正面摆拍、终帧异兽贴到主角身后、漏掉指定镜头、镜头合并、道具提前抢镜。
```

## QA Gate

Do not hand off if below `95/100`.

Checklist:

```text
BACKEND_PRODUCTION_QA:
- one Markdown file only
- three stages complete
- all prompts bilingual
- green upload reminders outside prompt blocks
- asset codes and references consistent
- storyboard is clean
- SEEDANCE_MOTION_TEXT complete
- Seedance references @image / asset code / module labels
- REALISTIC CINEMA STYLE LOCK is dynamic
- NEGATIVE PROMPT targets current risks only
- score >= 95/100
```
