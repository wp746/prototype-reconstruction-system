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

如果用户还没有完成前端需求和镜头拆解，先执行“前端交接标准化层”。能保守补齐的字段由你补齐；不能补齐的字段列成缺失项；如果用户允许，让大模型先按 [frontend-handoff-normalization.md](references/frontend-handoff-normalization.md) 规范化，再进入后端生产。

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

STYLE_CONTRACT:
- source_style_evidence
- render_style
- medium
- realism_level
- material_finish
- lighting_language
- lens_language
- color_palette
- forbidden_styles
- style_source: explicit / inferred_from_assets / inferred_from_reference / needs_user
```

## Frontend Handoff Normalization

Before generating the final package, run this preflight:

```text
FRONTEND_HANDOFF_NORMALIZATION:
- input_quality: standard / usable_but_incomplete / vague / blocked
- inferred_fields:
- missing_fields:
- assumptions:
- needs_model_completion: yes / no
- user_questions:
- handoff_ready: yes / no
```

Style is a hard entry gate. Before any asset prompt is written, normalize or obtain:

```text
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

Rules:

1. If the frontend clearly says `3D`, `live-action`, `anime`, `cartoon`, `clay`, `pixel`, `ink`, `documentary`, or another visual medium, lock that as `render_style`.
2. If the frontend does not explicitly name style but provides assets, screenshots, boards, or reference-frame descriptions, infer the closest style from the material and mark `style_source: inferred_from_assets` or `inferred_from_reference`.
3. If style evidence conflicts, for example reference is 3D but the user asks anime, ask the user which style wins before production.
4. If style cannot be inferred with confidence, set `handoff_ready: no` and ask for the minimum style input. Do not enter asset production.
5. `STYLE_RISK` is not enough by itself. It describes possible failure. `STYLE_CONTRACT` defines what all assets, storyboards, and Seedance prompts must become.

Use these rules:

1. If input is standard, proceed directly.
2. If input is usable but incomplete, infer conservatively and mark assumptions.
3. If input is vague but contains enough story/asset/shot clues, normalize it into the required schema before production.
4. If required fields are absent and cannot be inferred, stop and ask for the minimum missing fields.
5. If the user asks you to proceed despite fuzzy input, first generate a normalized handoff using [frontend-handoff-normalization.md](references/frontend-handoff-normalization.md), then continue only if `handoff_ready = yes`.

Minimum quality standard for backend comfort:

```text
BACKEND_READY_STANDARD:
- project/runtime/aspect/model known
- at least one character, one scene, and one prop/mechanism defined or intentionally marked none
- shot_count and storyboard_layout known
- every SH has timecode or estimated duration
- every SH has shot_size, composition, action_state, camera_movement, action_direction, cut_function
- in_state/action_chain/out_state are clear
- style_contract includes render_style, medium, realism_level, material_finish, lighting_language, lens_language, color_palette, and forbidden_styles
- style_risk includes likely drift and final_frame_risk
```

If the user gives unstructured notes, infer conservatively and mark missing fields in the output preflight section. If `SHOT_PLAN`, `ASSET_PLAN`, `STYLE_CONTRACT`, or `STYLE_RISK` is absent and cannot be inferred, ask for it or produce only a preflight checklist, not the final package.

## Output Contract

Use the structure in [single-md-package-template.md](references/single-md-package-template.md).

Final package sections:

1. `## 0. 使用说明`
2. `## 0.1 前端交接标准化`
3. `## 1. 阶段一：资产提示词`
4. `## 2. 阶段二：干净故事板提示词`
5. `## 3. 阶段三：Seedance 2.0 视频提示词`
6. `## 4. QA 自检`

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

## Asset Style Contract Rules

Every `ZH_IMAGE2_PROMPT` and `EN_IMAGE2_PROMPT` for character, scene, and prop assets must include a visible `STYLE_CONTRACT_LOCK` block near the top of the prompt.

The asset style lock must state:

- exact render style and medium, for example `high-end 3D animated film`, `live-action cinematic realism`, `2D anime`, `cartoon`, `clay stop-motion`, or `surreal photoreal`.
- material and surface behavior.
- lighting language.
- lens / perspective language.
- color palette.
- forbidden styles.

If the intended style is 3D, asset prompts must explicitly say:

```text
STYLE_CONTRACT_LOCK:
高端 3D 动画电影资产，不是二次元，不是动漫插画，不是真人照片，不是游戏 UI 立绘。角色、场景、道具都使用同一套 3D 材质、体积光、空间透视、柔和边缘和受控细节。
```

English version:

```text
STYLE_CONTRACT_LOCK:
High-end 3D animated film asset, not 2D anime, not anime illustration, not live-action photography, not game UI character art. Character, scene, and prop share the same 3D materials, volumetric lighting, spatial perspective, refined edges, and controlled details.
```

If the intended style is not 3D, replace the variable parts with the current style. Do not reuse the 3D lock for anime, cartoon, photoreal, documentary, ink, clay, or surreal projects.

Asset prompts must also include a short style-specific negative line. Example for 3D:

```text
STYLE_NEGATIVE:
不要二次元、动漫脸、赛璐璐上色、漫画线稿、真人照片、游戏立绘、塑料玩具感、风格混搭。
```

English:

```text
STYLE_NEGATIVE:
No 2D anime, anime face, cel shading, manga line art, live-action photo, game character splash art, plastic toy look, or mixed styles.
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

The clean storyboard can be black-and-white, but it must still inherit the project `STYLE_CONTRACT` at the design level. For a 3D project, write the storyboard prompt as clean grayscale cinematic layout for 3D blocking and spatial composition, not anime manga panels.

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

It must inherit `STYLE_CONTRACT`. If the project is 3D, this section is not allowed to drift into generic live-action realism or anime terms. If the project is live-action, do not use 3D animation terms. If the project is anime/cartoon, do not use photoreal texture language unless the user explicitly requested hybrid style.

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
- frontend handoff normalized or confirmed standard
- missing fields resolved or explicitly blocked
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

If script execution is available, run the structural package checker before handoff:

```bash
python3 scripts/check_backend_package.py /path/to/final-backend-package.md
```

Required result:

```text
PASSED: 0 errors, 0 warning(s)
```

This checker only validates the production-package structure. It does not replace creative QA, shot DNA QA, asset continuity QA, or the `95/100` handoff gate. If the checker fails, do not deliver the final package; fix the package first.
