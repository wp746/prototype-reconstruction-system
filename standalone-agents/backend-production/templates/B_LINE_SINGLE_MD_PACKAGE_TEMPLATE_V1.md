# B 线后端生产单文件模板 V1

Template Code: `B_LINE_SINGLE_MD_PACKAGE_TEMPLATE_V1`

最终只输出一个 Markdown 文件。所有提示词双语。绿色上传提醒不属于提示词。

# [项目名] B 线后端生产包

## 0. 使用说明

本文件按 B 线后端生产顺序执行：资产 -> 干净故事板 -> Seedance 2.0 视频。  
绿色上传提醒只给用户操作用，不要复制进 Image2 或 Seedance。

## 0.1 前端交接标准化

```text
FRONTEND_HANDOFF_NORMALIZATION:
input_quality:
inferred_fields:
missing_fields:
assumptions:
needs_model_completion:
user_questions:
handoff_ready:

STYLE_CONTRACT:
source_style_evidence:
render_style:
medium:
realism_level:
material_finish:
lighting_language:
lens_language:
color_palette:
forbidden_styles:
style_source:
```

---

## 1. 阶段一：资产提示词

### 1.1 角色资产 / Character Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有角色图，请上传 @图片1 = A01 / 角色参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[中文风格合同锁：明确 render_style / medium / realism_level / material_finish / lighting_language / lens_language / color_palette。若是 3D，必须写明高端 3D 动画电影资产，不是二次元，不是动漫插画，不是真人照片。]

STYLE_NEGATIVE:
[中文风格负面：只写当前风格最容易跑偏的方向，例如不要动漫脸、赛璐璐上色、真人照片、游戏立绘、塑料玩具感、风格混搭。]

[中文角色资产提示词]
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[English style contract lock: define render_style / medium / realism_level / material_finish / lighting_language / lens_language / color_palette. For 3D, state high-end 3D animated film asset, not 2D anime, not anime illustration, not live-action photography.]

STYLE_NEGATIVE:
[English style negative: only current drift risks, such as no anime face, cel shading, live-action photo, game splash art, plastic toy look, or mixed styles.]

[English character asset prompt]
```

---

### 1.2 场景资产 / Scene Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有场景图，请上传 @图片2 = A03 / 场景参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[中文风格合同锁：必须与角色资产同一风格、同一材质语言、同一光线和色彩系统。]

STYLE_NEGATIVE:
[中文风格负面：禁止与 STYLE_CONTRACT 冲突的风格。]

[中文场景资产提示词]
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[English style contract lock: must match the character asset style, material language, lighting system, and palette.]

STYLE_NEGATIVE:
[English style negative: forbid styles that conflict with STYLE_CONTRACT.]

[English scene asset prompt]
```

---

### 1.3 道具资产 / Prop Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有道具图，请上传 @图片3 = A05 / 道具参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[中文风格合同锁：必须与角色和场景资产同一风格、同一材质语言、同一光效逻辑。]

STYLE_NEGATIVE:
[中文风格负面：禁止与 STYLE_CONTRACT 冲突的风格。]

[中文道具资产提示词]
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
[English style contract lock: must match the character and scene asset style, material language, and lighting logic.]

STYLE_NEGATIVE:
[English style negative: forbid styles that conflict with STYLE_CONTRACT.]

[English prop asset prompt]
```

---

## 2. 阶段二：干净故事板提示词

<span style="color:#15803d;font-weight:600;">上传提醒：生成故事板时请参考 @图片1 = A01 角色资产、@图片2 = A03 场景资产、@图片3 = A05 道具资产。此提醒不属于提示词。</span>

### 2.1 ZH_IMAGE2_PROMPT

```text
TEMPLATE_CODE：CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID：S01_CLEAN_STORYBOARD_CONTROL
PART：[Part 编号 / 00:00-00:15]
LAYOUT：[例如 4x2 horizontal storyboard, 8 clean panels]

[中文干净故事板提示词]
```

### 2.2 EN_IMAGE2_PROMPT

```text
TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID: S01_CLEAN_STORYBOARD_CONTROL
PART: [Part ID / 00:00-00:15]
LAYOUT: [for example 4x2 horizontal storyboard, 8 clean panels]

[English clean storyboard prompt]
```

### 2.3 SEEDANCE_MOTION_TEXT

#### 中文

```text
SH01：[运镜、动作方向、速度、切点功能]
SH02：[运镜、动作方向、速度、切点功能]
...
```

#### English

```text
SH01: [camera movement, action direction, speed, cut function]
SH02: [camera movement, action direction, speed, cut function]
...
```

---

## 3. 阶段三：Seedance 2.0 视频提示词

<span style="color:#15803d;font-weight:600;">上传提醒：Seedance 2.0 全能参考请按顺序上传：@图片1 = A01 / 角色资产；@图片2 = A03 / 场景资产；@图片3 = A05 / 道具资产；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 干净故事板。此提醒不属于提示词。</span>

### 3.1 ZH_SEEDANCE_PROMPT

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
[必须继承 STYLE_CONTRACT，不得改写为另一个风格。]

[DIALOGUE / VOICE PERFORMANCE]

[SOUND EFFECTS FOR POST]

[NEGATIVE PROMPT]
```

### 3.2 EN_SEEDANCE_PROMPT

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
[Must inherit STYLE_CONTRACT and must not rewrite the project into another style.]

[DIALOGUE / VOICE PERFORMANCE]

[SOUND EFFECTS FOR POST]

[NEGATIVE PROMPT]
```

---

## 4. QA 自检

```text
BACKEND_PRODUCTION_QA:
- 是否只输出一个 .md 文件：是 / 否
- 前端交接是否已标准化或确认标准：是 / 否
- 缺失字段是否已补齐，或已明确阻塞：是 / 否
- STYLE_CONTRACT 是否已明确或可靠推断：是 / 否
- 资产提示词是否全部包含 STYLE_CONTRACT_LOCK：是 / 否
- 是否三阶段顺序完整：是 / 否
- 是否全部双语：是 / 否
- 绿色上传提醒是否在提示词外：是 / 否
- 资产编号是否统一：是 / 否
- 故事板是否干净：是 / 否
- SEEDANCE_MOTION_TEXT 是否完整：是 / 否
- Seedance 是否明确引用 @图片编号 / 资产编号 / 模块标签：是 / 否
- REALISTIC CINEMA STYLE LOCK 是否动态贴合当前风险：是 / 否
- NEGATIVE PROMPT 是否只写当前真实风险：是 / 否
- 评分是否达到 95/100：是 / 否
```
