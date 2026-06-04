# Scene Board Meta Prompt V1

Meta prompt code: `SCENE_BOARD_META_PROMPT_V1`

Use this meta prompt after DNA analysis and scene extraction are complete. It compiles one stable Image2 scene asset board prompt from structured project material.

It must always call the fixed template:

```text
WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE
```

## Input Package

```text
PROJECT_DNA:
- remake_branch:
- medium:
- visual_style:
- scene_story_function:
- invariant_locks:
- variable_swaps:

BOARD_REQUEST:
- language_mode: zh / en
- board_id:
- scene_code:
- scene_name:
- template_code: WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE

SCENE_SOURCE:
- space identity:
- era / style:
- time / weather:
- entrance:
- exit:
- main direction:
- foreground / midground / background:
- fixed props:
- character zones:
- prop anchors:
- camera-safe zones:
- light direction:
- forbidden drift:

STYLE_SOURCE:
- medium_variable:
- space_type_variable:
- architecture_or_terrain_material_variable:
- weather_light_variable:
- shootable_zone_variable:
- anti_mismatch_variable:
- Image2_overfit_noise_constants:
```

## Meta Prompt

```text
You are SCENE_BOARD_META_PROMPT_V1.
Compile one bilingual pair of copyable Image2 scene asset board prompts.

Use TEMPLATE_CODE: WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE.
Do not invent a new board design.
Use a 16:9 horizontal white or near-white board.
Canvas substrate: #FFFFFF or #F8F8F4 background, thin black #111111 dividers, subtle gray #C8C8C8 guide lines, fixed bold sans-serif typography.
Deliver both language modes by default. The Chinese prompt uses Chinese in-image labels only. The English prompt uses English in-image labels only. Do not mix Chinese and English labels in the same board.

The board must contain fixed modules V01-V09 plus MAP:
- V01 / ESTABLISHING: full space identity and horizon/direction.
- V02 / ENTRANCE: entry route or arrival direction.
- V03 / EXIT/REVERSE: exit or reverse direction.
- V04 / CAMERA A: primary shooting angle.
- V05 / CAMERA B: reverse angle.
- V06 / CAMERA C: side or diagonal angle.
- V07 / KEY DETAIL: fixed spatial identity object.
- V08 / LIGHT: clean visual lighting view only; do not draw arrows, text, light labels, or explanatory marks inside the scene image.
- V09 / SCALE: faceless gray silhouettes or clean scale placeholders only; do not write measurements, zone names, dashed lines, arrows, or explanatory text inside the scene image.
- MAP: top-down geography plan with ENTRANCE, EXIT, CAM_A, CAM_B, CAM_C, CHAR_ZONE, PROP_ANCHOR, LIGHT_DIR, NO_DRIFT.

Fill the board content from PROJECT_DNA, BOARD_REQUEST, SCENE_SOURCE, and STYLE_SOURCE.
All nine views must belong to one stable geography.
Do not mix unrelated locations.
Do not create clear main-character faces; use faceless silhouettes, backs, or position markers only.
Doors, platforms, pillars, roads, light direction, prop anchors, and camera directions must not drift between panels.
V01-V09 must be clean scene-view panels: no in-image text, arrows, measurement lines, zone circles, camera icons, dashed lines, legends, explanatory marks, or UI markers inside the scene images. Module titles may sit outside each image in the white title strip, but must not be printed over the scene view. All arrows, camera markers, zones, measurements, legends, and no-drift annotations are allowed only in the bottom MAP / top-down plan.

Compile the style lock from the current scene:
medium variable + space type variable + architecture or terrain material variable + weather/light variable + shootable-zone variable + anti-mismatch lockout + Image2 overfitting-noise constants.

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
- V01-V09 plus MAP fixed layout present
- one stable geography only
- ENTRANCE / EXIT / CAM_A / CAM_B / CAM_C / CHAR_ZONE / PROP_ANCHOR / LIGHT_DIR / NO_DRIFT visible
- V01-V09 contain no in-image text, arrows, measurement lines, zone circles, or camera icons
- no clear main-character face created
- labels use one language only
- style lock is scene-specific
- no poster layout, watermark, logo, subtitle, random text, or geography drift
```

## QA Gate

Do not hand off if below `95/100`.

- Layout consistency: 20
- V01-V09 + MAP completeness: 20
- Geography fidelity: 20
- Style-lock specificity: 15
- Single-language labels: 10
- Seedance reference usability: 10
- Pollution control: 5
