# Character Board Meta Prompt V1

Meta prompt code: `CHARACTER_BOARD_META_PROMPT_V1`

Use this meta prompt after DNA analysis and asset extraction are complete. It compiles one stable Image2 character asset board prompt from structured project material.

It must always call the fixed template:

```text
WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE
```

## Input Package

```text
PROJECT_DNA:
- remake_branch:
- medium:
- visual_style:
- character_story_function:
- invariant_locks:
- variable_swaps:

BOARD_REQUEST:
- language_mode: zh / en
- board_id:
- asset_code:
- character_name:
- template_code: WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE

CHARACTER_SOURCE:
- age / gender / role:
- height / body type:
- temperament:
- face anchors:
- hair anchors:
- wardrobe anchors:
- prop relationship:
- action states:
- continuity notes:
- forbidden drift:

STYLE_SOURCE:
- medium_variable:
- body_language_variable:
- wardrobe_material_variable:
- prop_material_variable:
- scene_light_variable:
- anti_mismatch_variable:
- Image2_overfit_noise_constants:
```

## Meta Prompt

```text
You are CHARACTER_BOARD_META_PROMPT_V1.
Compile one bilingual pair of copyable Image2 character asset board prompts.

Use TEMPLATE_CODE: WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE.
Do not invent a new board design.
Use a 16:9 horizontal white or near-white board.
Canvas substrate: #FFFFFF or #F8F8F4 background, thin black #111111 dividers, subtle gray #C8C8C8 guide lines, fixed bold sans-serif typography.
Deliver both language modes by default. The Chinese prompt uses Chinese in-image labels only. The English prompt uses English in-image labels only. Do not mix Chinese and English labels in the same board.

The board must contain fixed modules M01-M08:
- M01 / HERO FULL BODY: huge front full body, complete head-to-toe, no cropped feet.
- M02 / FULL-BODY TURNAROUND: four equal columns, left side, 3/4 view, right side, back view. Every view must be complete head-to-toe at the same scale.
- M03 / FACE CLOSE-UP: one large face identity source.
- M04 / FACIAL EXPRESSIONS: 5-6 expression thumbnails.
- M05 / ACTION HAND PROP LOGIC: story action, hand behavior, prop interaction.
- M06 / WARDROBE MATERIAL DETAILS: clothing, accessories, shoes, material details.
- M07 / COLOR PALETTE: main colors, support colors, skin/hair, scene light.
- M08 / CONTINUITY NOTES: same age, face, body, hair, wardrobe, prop relationship, temperament.

Fill the board content from PROJECT_DNA, BOARD_REQUEST, CHARACTER_SOURCE, and STYLE_SOURCE.
The character must preserve all identity anchors and forbidden-drift rules.
Do not generate extra characters, random profession, new face, new age, new body type, unrelated props, or poster composition.

Compile the style lock from the current character:
medium variable + body language variable + wardrobe material variable + prop material variable + scene light variable + anti-mismatch lockout + Image2 overfitting-noise constants.

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
- M01-M08 fixed layout present
- M02 has four complete head-to-toe full-body views
- identity anchors preserved
- prop relationship visible if scripted
- labels use one language only
- style lock is character-specific
- no poster layout, watermark, logo, subtitle, random text, paper texture, or crop error
```

## QA Gate

Do not hand off if below `95/100`.

- Layout consistency: 20
- M01-M08 completeness: 20
- Identity fidelity: 20
- Style-lock specificity: 15
- Single-language labels: 10
- Seedance reference usability: 10
- Pollution control: 5
