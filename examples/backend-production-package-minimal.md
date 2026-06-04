# 示例项目 B 线后端生产包

## 0. 使用说明

本文件按 B 线后端生产顺序执行：资产 -> 干净故事板 -> Seedance 2.0 视频。  
绿色上传提醒只给用户操作用，不要复制进 Image2 或 Seedance。

## 0.1 前端交接标准化

```text
FRONTEND_HANDOFF_NORMALIZATION:
input_quality: standard
inferred_fields: none
missing_fields: none
assumptions: none
needs_model_completion: no
user_questions: none
handoff_ready: yes

STYLE_CONTRACT:
source_style_evidence: 前端物料指定为高端 3D 动画电影资产，角色、场景、道具都使用统一 3D 材质和体积光。
render_style: 高端 3D 动画电影
medium: 3D animated film asset and cinematic video
realism_level: stylized cinematic 3D, not photoreal live-action
material_finish: refined 3D surfaces, soft roughness, controlled details, smooth gradients
lighting_language: soft volumetric lighting, cinematic rim light, coherent scene shadows
lens_language: cinematic perspective, spatial depth, no flat illustration layout
color_palette: controlled cool blue and dark metal palette with restrained highlights
forbidden_styles: 二次元、动漫插画、赛璐璐、漫画线稿、真人照片、游戏 UI 立绘、风格混搭
style_source: explicit
```

---

## 1. 阶段一：资产提示词

### 1.1 角色资产 / Character Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有角色图，请上传 @图片1 = A01 / 角色参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
高端 3D 动画电影角色资产，不是二次元，不是动漫插画，不是真人照片，不是游戏 UI 立绘。A01 使用统一 3D 材质、体积光、空间透视、柔和边缘和受控细节。

STYLE_NEGATIVE:
不要二次元、动漫脸、赛璐璐上色、漫画线稿、真人照片、游戏立绘、塑料玩具感、风格混搭。

生成 A01 角色资产板，包含 M01 FACE、M03 COSTUME、M05 BODY SCALE、M06 HAND GESTURE。
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
High-end 3D animated film character asset, not 2D anime, not anime illustration, not live-action photography, not game UI character art. A01 uses unified 3D materials, volumetric lighting, spatial perspective, refined edges, and controlled details.

STYLE_NEGATIVE:
No 2D anime, anime face, cel shading, manga line art, live-action photo, game character splash art, plastic toy look, or mixed styles.

Generate the A01 character asset board with M01 FACE, M03 COSTUME, M05 BODY SCALE, and M06 HAND GESTURE.
```

### 1.2 场景资产 / Scene Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有场景图，请上传 @图片2 = A03 / 场景参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
高端 3D 动画电影场景资产，与 A01 使用同一 3D 材质语言、体积光、电影空间透视和受控色彩系统，不是动漫背景插画。

STYLE_NEGATIVE:
不要二次元背景、赛璐璐上色、漫画线稿、真人照片、游戏 UI 场景、塑料玩具感、风格混搭。

生成 A03 场景资产板，包含 V01 ESTABLISHING、V04 CAMERA A、V05 CAMERA B、MAP。
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
High-end 3D animated film scene asset, matching A01 with the same 3D material language, volumetric lighting, cinematic spatial perspective, and controlled palette. Not anime background illustration.

STYLE_NEGATIVE:
No 2D anime background, cel shading, manga line art, live-action photo, game UI environment, plastic toy look, or mixed styles.

Generate the A03 scene asset board with V01 ESTABLISHING, V04 CAMERA A, V05 CAMERA B, and MAP.
```

### 1.3 道具资产 / Prop Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有道具图，请上传 @图片3 = A05 / 道具参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
高端 3D 动画电影道具资产，与 A01 和 A03 使用同一 3D 材质、能量光效、空间透视和柔和边缘，不是平面图标或动漫道具。

STYLE_NEGATIVE:
不要二次元道具、赛璐璐上色、漫画线稿、真人照片、游戏图标、塑料玩具感、风格混搭。

生成 A05 道具资产板，包含 P01 HERO PROP、P04 ACTIVE STATE、P06 HAND LOGIC、P07 SCENE ANCHOR。
```

#### EN_IMAGE2_PROMPT

```text
STYLE_CONTRACT_LOCK:
High-end 3D animated film prop asset, matching A01 and A03 with the same 3D materials, energy lighting, spatial perspective, and refined edges. Not flat icon art or anime prop art.

STYLE_NEGATIVE:
No 2D anime prop, cel shading, manga line art, live-action photo, game icon, plastic toy look, or mixed styles.

Generate the A05 prop asset board with P01 HERO PROP, P04 ACTIVE STATE, P06 HAND LOGIC, and P07 SCENE ANCHOR.
```

---

## 2. 阶段二：干净故事板提示词

<span style="color:#15803d;font-weight:600;">上传提醒：生成故事板时请参考 @图片1 = A01 角色资产、@图片2 = A03 场景资产、@图片3 = A05 道具资产。此提醒不属于提示词。</span>

### 2.1 ZH_IMAGE2_PROMPT

```text
TEMPLATE_CODE：CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID：S01_CLEAN_STORYBOARD_CONTROL
PART：Part 1 / 00:00-00:15
LAYOUT：4x2 horizontal storyboard, 8 clean panels

生成干净黑白故事板视觉控制板，不要箭头、编号、时间码或文字说明。
```

### 2.2 EN_IMAGE2_PROMPT

```text
TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID: S01_CLEAN_STORYBOARD_CONTROL
PART: Part 1 / 00:00-00:15
LAYOUT: 4x2 horizontal storyboard, 8 clean panels

Generate a clean black-and-white storyboard visual control board with no arrows, numbers, timestamps, or written notes.
```

### 2.3 SEEDANCE_MOTION_TEXT

#### 中文

```text
SH01：低机位快速推近。
SH02：过肩跟拍。
SH03：低机位宽景停顿。
SH04：切角色中近景。
SH05：异兽砸地冲击。
SH06：手部道具启动。
SH07：贴地跟随能量扩散。
SH08：稳定宽景终帧。
```

#### English

```text
SH01: low-angle fast push-in.
SH02: over-the-shoulder tracking.
SH03: low-angle wide hold.
SH04: cut to character medium close-up.
SH05: creature ground impact.
SH06: hand-held prop activation.
SH07: ground-level energy spread.
SH08: stable wide final frame.
```

---

## 3. 阶段三：Seedance 2.0 视频提示词

<span style="color:#15803d;font-weight:600;">上传提醒：Seedance 2.0 全能参考请按顺序上传：@图片1 = A01 / 角色资产；@图片2 = A03 / 场景资产；@图片3 = A05 / 道具资产；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 干净故事板。此提醒不属于提示词。</span>

### 3.1 ZH_SEEDANCE_PROMPT

```text
[VIDEO TASK]
生成 15 秒电影级视频。

[REFERENCE HIERARCHY]
@图片1 / A01 锁角色身份。@图片2 / A03 锁场景。@图片3 / A05 锁道具。@图片4 / S01_CLEAN_STORYBOARD_CONTROL 锁镜头顺序和构图。

[STORYBOARD LOGIC]
按从左到右、从上到下读取 SH01-SH08。

[SEEDANCE_MOTION_TEXT]
使用阶段二中文 SEEDANCE_MOTION_TEXT。

[SEGMENT STATE]
入场状态、状态变化、结尾状态清楚。

[SHOT-BY-SHOT TIMING]
SH01-SH08 完整。

[ACTION / BLOCKING]
保持角色、场景、道具和终帧 payoff。

[CAMERA MOVEMENT]
按 SH01-SH08 执行。

[LIGHTING / VFX]
按项目设定执行。

[REALISTIC CINEMA STYLE LOCK]
保持真实电影质感、真实镜头运动、真实材质反射和克制特效。避免动漫感、游戏 CG 感、塑料皮肤、过度锐化、假胶片颗粒和终帧主体错位。

[DIALOGUE / VOICE PERFORMANCE]
无字幕。

[SOUND EFFECTS FOR POST]
无 BGM。

[NEGATIVE PROMPT]
不要当前项目的真实风险，例如镜头合并、资产漂移、终帧错误。
```

### 3.2 EN_SEEDANCE_PROMPT

```text
[VIDEO TASK]
Generate a 15-second cinematic video.

[REFERENCE HIERARCHY]
@image1 / A01 locks character identity. @image2 / A03 locks the scene. @image3 / A05 locks the prop. @image4 / S01_CLEAN_STORYBOARD_CONTROL locks shot order and composition.

[STORYBOARD LOGIC]
Read SH01-SH08 from left to right and top to bottom.

[SEEDANCE_MOTION_TEXT]
Use the English SEEDANCE_MOTION_TEXT from Stage 2.

[SEGMENT STATE]
Opening state, state change, and ending state are clear.

[SHOT-BY-SHOT TIMING]
SH01-SH08 are complete.

[ACTION / BLOCKING]
Preserve character, scene, prop, and final payoff.

[CAMERA MOVEMENT]
Follow SH01-SH08.

[LIGHTING / VFX]
Follow the project setting.

[REALISTIC CINEMA STYLE LOCK]
Preserve cinematic realism, physical camera movement, real material reflections, and restrained VFX. Avoid anime style, game-CG style, plastic skin, oversharpening, fake film grain, and a misplaced final-frame subject.

[DIALOGUE / VOICE PERFORMANCE]
No subtitles.

[SOUND EFFECTS FOR POST]
No BGM.

[NEGATIVE PROMPT]
Avoid current real risks such as shot merging, asset drift, and wrong final frame.
```

---

## 4. QA 自检

```text
BACKEND_PRODUCTION_QA:
- 是否只输出一个 .md 文件：是
- 前端交接是否已标准化或确认标准：是
- 缺失字段是否已补齐，或已明确阻塞：是
- 是否三阶段顺序完整：是
- 是否全部双语：是
- 绿色上传提醒是否在提示词外：是
- 资产编号是否统一：是
- 故事板是否干净：是
- SEEDANCE_MOTION_TEXT 是否完整：是
- Seedance 是否明确引用 @图片编号 / 资产编号 / 模块标签：是
- REALISTIC CINEMA STYLE LOCK 是否动态贴合当前风险：是
- NEGATIVE PROMPT 是否只写当前真实风险：是
- 评分是否达到 95/100：是
```
