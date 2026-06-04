# Board Meta Prompt Compiler V1

Compiler code: `BOARD_META_PROMPT_COMPILER_V1`

This meta prompt is the upstream compiler for all Image2 board prompts in this repository. It receives the finished DNA analysis, asset extraction, style decision, and storyboard plan, then emits stable board prompts using the fixed templates below:

- Character boards: `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`
- Scene boards: `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`
- Prop boards: `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`
- Storyboard sheets: `WHITE_STORYBOARD_SHEET_TEMPLATE`

Standalone meta prompts:

- [Character Board Meta Prompt V1](character-board-meta-prompt-v1.md)
- [Scene Board Meta Prompt V1](scene-board-meta-prompt-v1.md)
- [Prop Board Meta Prompt V1](prop-board-meta-prompt-v1.md)
- [Storyboard Board Meta Prompt V1](storyboard-board-meta-prompt-v1.md)

The goal is to prevent random board drift. Every generated prompt must preserve the same design substrate, typography logic, label contract, layout proportions, language mode, and style-lock architecture across the whole project.

## Compiler Inputs

Every board prompt must be compiled from structured source material, not written freehand.

```text
PROJECT_DNA:
- remake_branch: A / B / C / D / A+B / D+B
- medium: cinematic realism / anime / 3D stylized / surreal / other
- visual_style: color, light, texture, rendering, atmosphere
- story_function: what this asset or board does in the film
- invariant_locks: what must not change from shot to shot
- variable_swaps: what has been intentionally redesigned

BOARD_REQUEST:
- board_type: character / scene / prop / storyboard_annotated / storyboard_clean_bw
- language_mode: zh / en
- aspect_ratio: 16:9
- asset_code: A## / CHAR_CODE / SCENE_CODE / PROP_CODE / S##
- board_title: visible title text
- template_code: one of the fixed template codes

ASSET_SOURCE:
- identity_anchors: face, body, silhouette, scale, shape, material, color
- module_requirements: M01-M08 / V01-V09+MAP / P01-P08 / SH01-SH[N]
- continuity_notes: what later Seedance must reference
- forbidden_drift: face, body, wardrobe, prop, geography, light, state, style

STYLE_SOURCE:
- medium_variable
- subject_material_variable
- wardrobe_or_surface_variable
- scene_light_variable
- anti_mismatch_variable
- Image2_overfit_noise_constants

STORYBOARD_SOURCE, only for storyboard boards:
- SEG##, runtime, in_state, action_chain, out_state, continuity_to_next
- shot_count, grid_layout, panel_beats
- active_assets per shot
- camera rhythm and motion direction
```

## Non-Negotiable Output Contract

The compiler must output one bilingual prompt pair per requested board by default: one Chinese Image2 prompt and one English Image2 prompt.

Each language output must include:

1. `TEMPLATE_CODE` line.
2. `BOARD_ID` line.
3. `LANGUAGE_MODE` line.
4. A fixed layout block copied from the matching board template.
5. Project-specific content variables filled from the DNA and asset source.
6. A compiled style lock, not a generic pasted tail.
7. Negative constraints as prompt constraints only, never as visible board modules.
8. A `QA_SELF_CHECK` block at the end for the human/operator, outside the image instruction.

The prompt must not:

- invent a new board layout;
- change background color, typography family, divider logic, or module labels;
- mix Chinese and English label systems in one board;
- render long paragraphs, random text, subtitles, watermarks, logos, or brand text inside the image;
- let storyboard drawings replace asset identity;
- use polished storyboard frames as Seedance control frames;
- put arrows, motion lines, frame boxes, labels, panel numbers, timestamps, title bars, captions, or white storyboard UI into `S##_CLEAN_STORYBOARD_CONTROL`.

Extra scene-board rule: `V01`-`V09` scene image areas must contain no text, arrows, measurement lines, zone circles, camera icons, dashed paths, legends, explanatory notes, or UI markers. All annotations are allowed only in the bottom `MAP` / top-down plan area.

## Global Board Substrate Lock

Use this substrate unless the user explicitly requests another production system:

```text
Canvas: 16:9 landscape, recommended 3840x2160.
Background: white or near-white #FFFFFF / #F8F8F4.
Dividers: thin black #111111, subtle gray guide lines #C8C8C8.
Typography: fixed bold sans-serif.
Cards: no nested cards, no decorative poster frame.
Text: large readable module labels only, no tiny paragraphs.
Language: pure Chinese labels for zh board, pure English labels for en board.
```

## Bilingual Paired Delivery Rule

Always deliver both prompt versions for asset boards and storyboard boards:

- `ZH_IMAGE2_PROMPT`: Chinese prompt, Chinese in-image labels only. Stable codes such as `A01`, `CHAR_CODE`, `SCENE_CODE`, `PROP_CODE`, `M01`, `V01`, `P01`, `SH01`, and `CAM_A` may remain as production codes.
- `EN_IMAGE2_PROMPT`: English prompt, English in-image labels only. Do not render Chinese labels in the English board.
- The Chinese and English prompts must describe the same layout, same asset identity, same modules, same storyboard beats, same style lock logic, and same QA gate.
- Do not mix Chinese descriptive labels into the English prompt. Do not mix English descriptive labels into the Chinese prompt except stable production codes.
- If the user explicitly asks for only one language, keep the other language internally compiled for QA, but only display the requested one.

## Style Lock Compiler

Do not paste the same style lock into every board. Compile it using the current subject.

Formula:

```text
style_lock =
medium_variable
+ current subject material variables
+ wardrobe / surface / prop / geography variables
+ scene-light variables
+ anti-mismatch lockout
+ Image2 overfitting-noise constants
```

Chinese constants:

```text
干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。
```

English constants:

```text
clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.
```

## Character Board Meta Prompt

Use when `board_type = character`.

```text
You are BOARD_META_PROMPT_COMPILER_V1.
Compile one Image2 character asset board prompt from the source material below.

Use TEMPLATE_CODE: WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE.
Do not invent a new board design.
Use the global board substrate lock.
Use language_mode: [zh/en].
The board must be a 16:9 white or near-white character asset board with fixed modules M01-M08.
M01 must be a huge complete front full body.
M02 must be four equal complete head-to-toe full-body turnaround views.
M03-M08 must preserve face identity, expression range, action-hand-prop logic, wardrobe material, color palette, and continuity notes.

Fill all variables from:
[PROJECT_DNA]
[BOARD_REQUEST]
[ASSET_SOURCE]
[STYLE_SOURCE]

Compile the style lock from the current character's medium, body language, wardrobe materials, prop relationship, and scene light. Append the Image2 overfitting-noise constants in the matching language.

Output exactly:
TEMPLATE_CODE:
BOARD_ID:
ZH_IMAGE2_PROMPT:
EN_IMAGE2_PROMPT:
QA_SELF_CHECK:
- layout uses M01-M08 fixed template
- M02 complete head-to-toe x4
- labels are single-language
- identity anchors preserved
- style lock is subject-specific
- no random text, watermark, logo, poster design, or crop errors
```

## Scene Board Meta Prompt

Use when `board_type = scene`.

```text
You are BOARD_META_PROMPT_COMPILER_V1.
Compile one Image2 scene asset board prompt from the source material below.

Use TEMPLATE_CODE: WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE.
Do not invent a new board design.
Use the global board substrate lock.
Use language_mode: [zh/en].
The board must be a 16:9 white or near-white scene asset board with V01-V09 plus MAP.
Every view must belong to the same geography.
Use faceless silhouettes or position markers only; do not generate clear main-character faces.
The MAP strip must include ENTRANCE, EXIT, CAM_A, CAM_B, CAM_C, CHAR_ZONE, PROP_ANCHOR, LIGHT_DIR, and NO_DRIFT.

Fill all variables from:
[PROJECT_DNA]
[BOARD_REQUEST]
[ASSET_SOURCE]
[STYLE_SOURCE]

Compile the style lock from the current space type, architecture or terrain material, time/weather/light, shootable zones, and anti-mismatch lockout. Append the Image2 overfitting-noise constants in the matching language.

Output exactly:
TEMPLATE_CODE:
BOARD_ID:
ZH_IMAGE2_PROMPT:
EN_IMAGE2_PROMPT:
QA_SELF_CHECK:
- layout uses V01-V09 plus MAP
- one stable geography only
- camera and prop anchors visible
- no clear character identity created
- labels are single-language
- style lock is scene-specific
- no random text, watermark, logo, poster design, or geography drift
```

## Prop Board Meta Prompt

Use when `board_type = prop`.

```text
You are BOARD_META_PROMPT_COMPILER_V1.
Compile one Image2 prop asset board prompt from the source material below.

Use TEMPLATE_CODE: WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE.
Do not invent a new board design.
Use the global board substrate lock.
Use language_mode: [zh/en].
The board must be a 16:9 white or near-white prop asset board with P01-P08 and REFERENCE USE.
One plot-critical hero prop per board by default.
The prop must preserve shape, scale, material, color, hand logic, state changes, and scene anchor across all modules.

Fill all variables from:
[PROJECT_DNA]
[BOARD_REQUEST]
[ASSET_SOURCE]
[STYLE_SOURCE]

Compile the style lock from the current prop identity, material, grip/usage logic, state-change requirement, scene-anchor light, and anti-mismatch lockout. Append the Image2 overfitting-noise constants in the matching language.

Output exactly:
TEMPLATE_CODE:
BOARD_ID:
ZH_IMAGE2_PROMPT:
EN_IMAGE2_PROMPT:
QA_SELF_CHECK:
- layout uses P01-P08 plus REFERENCE USE
- one hero prop unless secondary multi-prop is explicitly requested
- hand logic and state changes are visible
- scene anchor is explicit
- labels are single-language
- style lock is prop-specific
- no random text, watermark, logo, poster design, or prop drift
```

## Storyboard Board Meta Prompt

Use when `board_type = storyboard_seedance_v4`.

```text
You are BOARD_META_PROMPT_COMPILER_V1.
Compile one bilingual pair of Image2 storyboard prompts using STORYBOARD_BOARD_META_PROMPT_V1 / Storyboard Meta Prompt Generator V4: Seedance 2.0 Dedicated Edition.

Use TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE.
One storyboard Part must never exceed 15 seconds.
If the plot exceeds 15 seconds, automatically split it into Part 1 (00:00-00:15), Part 2 (00:15-00:30), etc.
Every Panel timestamp must be written in prompt text, formatted as [00:00s - 00:02s], but must not appear in the storyboard image.
Shot timing must follow action rhythm, emotional progression, and cinematic breathing. Do not divide time mechanically.
Chinese prompt text must be Chinese. English prompt text must be English. Stable production codes are allowed.
The storyboard image must be clean grayscale visual control: no arrows, motion lines, labels, panel numbers, timestamps, captions, legends, title bars, or white UI.
Transfer camera movement, action direction, speed, and cut function into SEEDANCE_MOTION_TEXT instead of drawing them.

Fill all variables from:
[PROJECT_DNA]
[BOARD_REQUEST]
[ASSET_SOURCE]
[STYLE_SOURCE]
[STORYBOARD_SOURCE]

Each Panel line must include SH ID, timestamp, shot size, composition, character position, action state, and active assets.
Character identity, wardrobe, prop shape, and scene identity come from asset boards. Storyboard controls shot order, action state, composition, spatial distance, and rhythm preview. Motion direction and camera movement go into SEEDANCE_MOTION_TEXT.
Compile the style packet from the current segment's medium, previs drawing, rhythm, action density, camera direction, readable geography, and silhouettes. Append the Image2 overfitting-noise constants in the matching language.

Output exactly:
TEMPLATE_CODE:
BOARD_ID:
PARTS:
ZH_IMAGE2_PROMPT:
EN_IMAGE2_PROMPT:
QA_SELF_CHECK:
- each Part is no longer than 15 seconds
- every Panel timestamp is written in prompt text
- timestamps follow cinematic breathing, not mechanical division
- final storyboard image has no arrows, annotations, panel numbers, timestamps, or text
- Chinese and English prompt language are fully isolated
- character and scene consistency anchors are explicit
- every Panel has action or state change
- SEEDANCE_MOTION_TEXT is complete
- asset identity overrides temporary storyboard drawing
```

## Project-Level QA Gate

Before any board prompt is handed to the user, the compiler must internally score it.

Pass threshold: `95/100`.

Scoring:

- Layout and typography consistency: 20
- Module completeness: 20
- DNA and asset-variable fidelity: 20
- Style-lock specificity: 15
- Single-language label discipline: 10
- Seedance reference usability: 10
- Negative/pollution control: 5

If score is below 95, revise internally and do not hand off the prompt.
