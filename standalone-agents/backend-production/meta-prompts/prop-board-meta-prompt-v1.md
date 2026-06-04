# Prop Board Meta Prompt V1

Meta prompt code: `PROP_BOARD_META_PROMPT_V1`

Use this meta prompt after DNA analysis and prop extraction are complete. It compiles one stable Image2 prop asset board prompt from structured project material.

It must always call the fixed template:

```text
WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE
```

## Input Package

```text
PROJECT_DNA:
- remake_branch:
- medium:
- visual_style:
- prop_story_function:
- invariant_locks:
- variable_swaps:

BOARD_REQUEST:
- language_mode: zh / en
- board_id:
- prop_code:
- prop_name:
- template_code: WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE

PROP_SOURCE:
- prop identity:
- story function:
- user / owner:
- scene anchor:
- shape:
- scale:
- material:
- color:
- glow / text / no-text rule:
- grip logic:
- state changes:
- continuity notes:
- forbidden drift:

STYLE_SOURCE:
- medium_variable:
- prop_identity_variable:
- material_variable:
- usage_or_grip_variable:
- state_change_variable:
- scene_anchor_light_variable:
- anti_mismatch_variable:
- Image2_overfit_noise_constants:
```

## Meta Prompt

```text
You are PROP_BOARD_META_PROMPT_V1.
Compile one bilingual pair of copyable Image2 prop asset board prompts.

Use TEMPLATE_CODE: WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE.
Do not invent a new board design.
Use a 16:9 horizontal white or near-white board.
Canvas substrate: #FFFFFF or #F8F8F4 background, thin black #111111 dividers, subtle gray #C8C8C8 guide lines, fixed bold sans-serif typography.
Deliver both language modes by default. The Chinese prompt uses Chinese in-image labels only. The English prompt uses English in-image labels only. Do not mix Chinese and English labels in the same board.

The board must contain fixed modules P01-P08 plus REFERENCE USE:
- P01 / HERO: largest clean prop identity source.
- P02 / FRONT-SIDE: front and side construction.
- P03 / BACK-TOP-3Q: back, top, or 3/4 construction.
- P04 / MATERIAL: material, wear, texture, glow, edge detail.
- P05 / SCALE: ratio to hand, body, or scene object.
- P06 / HAND LOGIC: left/right hand, fingers, grip point, use posture.
- P07 / STATE: scripted state change; if none, stable state.
- P08 / SCENE ANCHOR: which scene, which character, placement or motion anchor.
- REFERENCE USE: exact later Seedance reference duty: shape, material, hand logic, state change, scene anchor.

Fill the board content from PROJECT_DNA, BOARD_REQUEST, PROP_SOURCE, and STYLE_SOURCE.
One plot-critical hero prop per board by default.
Multi-prop boards are only for secondary props and every prop must have a large visible code.
The same prop must not drift in shape, scale, material, color, readable text rule, hand logic, or state change across modules.

Compile the style lock from the current prop:
medium variable + prop identity variable + material variable + usage/grip variable + state-change variable + scene-anchor light variable + anti-mismatch lockout + Image2 overfitting-noise constants.

Chinese constants:
干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。

English constants:
clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.

Output exactly:
TEMPLATE_CODE:
BOARD_ID:
ZH_IMAGE2_PROMPT:
EN_IMAGE2_PROMPT:
QA_SELF_CHECK:
- P01-P08 plus REFERENCE USE fixed layout present
- one hero prop unless secondary multi-prop is explicitly requested
- hand logic visible
- scripted state changes visible
- scene anchor explicit
- labels use one language only
- style lock is prop-specific
- no poster layout, watermark, logo, subtitle, random text, or prop drift
```

## QA Gate

Do not hand off if below `95/100`.

- Layout consistency: 20
- P01-P08 + REFERENCE USE completeness: 20
- Prop identity fidelity: 20
- Style-lock specificity: 15
- Single-language labels: 10
- Seedance reference usability: 10
- Pollution control: 5
