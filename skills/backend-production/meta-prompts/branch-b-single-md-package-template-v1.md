# B 线单文件生产包模板 V1

Template Code: `B_LINE_SINGLE_MD_PACKAGE_TEMPLATE_V1`

用途：把 B 线“资产 + 干净故事板 + Seedance 2.0 全能参考”串成一个最终交付 `.md` 文件。以后 B 线进入生产阶段后，只按顺序给用户输出这一个 Markdown 文件；文件内包含三阶段提示词，所有提示词默认双语。

## 1. 核心原则

1. 最终只输出一个 `.md` 文件，不把资产提示词、故事板提示词和 Seedance 视频提示词拆成多个零散回复。
2. 三阶段顺序固定：
   - 阶段一：资产提示词，角色 / 场景 / 道具。
   - 阶段二：干净故事板提示词，含 `SEEDANCE_MOTION_TEXT`。
   - 阶段三：Seedance 2.0 视频提示词，含动态电影风格锁和动态负面词。
3. 所有生成提示词都必须双语：
   - `ZH_IMAGE2_PROMPT` / `ZH_SEEDANCE_PROMPT`：中文版本。
   - `EN_IMAGE2_PROMPT` / `EN_SEEDANCE_PROMPT`：英文版本。
4. 若某条提示词需要用户上传参考图，必须在提示词前用绿色文字提醒用户上传哪张图；绿色提醒不属于提示词，不能复制进 Image2 或 Seedance。
5. 上传提醒统一使用 HTML 绿色文本：

```html
<span style="color:#15803d;font-weight:600;">上传提醒：@图片1 = A01 / 角色资产图；@图片2 = A03 / 场景资产图；@图片3 = A05 / 道具资产图；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 4x2 干净故事板。</span>
```

6. 资产提示词引用参考图时，绿色提醒放在提示词块外；提示词正文内只写模型要读的内容。
7. 故事板必须是 `S##_CLEAN_STORYBOARD_CONTROL`：无箭头、无运动线、无彩色标注、无编号、无时间码、无文字说明、无图例、无标题栏、无白底 UI。
8. 运镜、动作方向、速度、切点功能不得画在故事板中，必须写入 `SEEDANCE_MOTION_TEXT`。
9. Seedance 视频提示词里的 `[REALISTIC CINEMA STYLE LOCK]` 和 `[NEGATIVE PROMPT]` 必须根据当下片子最容易跑偏的方向动态编写，不套通用废话。
10. 干净故事板已经通过门禁时，Seedance 负面词不再堆砌箭头、红框、绿标、编号、时间码等旧污染项；这些属于故事板阶段 QA。

## 2. B 线单文件输出结构

最终交付文件必须严格使用以下顺序：

# [项目名] B 线生产提示词包

## 0. 使用说明

## 1. 阶段一：资产提示词
### 1.1 角色资产 / Character Asset
### 1.2 场景资产 / Scene Asset
### 1.3 道具资产 / Prop Asset

## 2. 阶段二：干净故事板提示词
### 2.1 故事板上传提醒
### 2.2 中文故事板提示词
### 2.3 English Storyboard Prompt
### 2.4 SEEDANCE_MOTION_TEXT

## 3. 阶段三：Seedance 2.0 视频提示词
### 3.1 视频上传提醒
### 3.2 中文 Seedance 提示词
### 3.3 English Seedance Prompt

## 4. QA 自检
```

## 3. 可复制输出模板

下面是最终 `.md` 文件的可复制骨架。生成实际项目时，替换所有 `[占位符]`。

```markdown
# [项目名] B 线生产提示词包

## 0. 使用说明

本文件按 B 线三阶段生产：先出资产，再出干净故事板，最后出 Seedance 2.0 视频。  
绿色上传提醒只给用户操作用，不属于提示词，不要复制进 Image2 或 Seedance。

---

## 1. 阶段一：资产提示词

### 1.1 角色资产 / Character Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有角色图，请上传 @图片1 = A01 / 角色参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
[填写中文角色资产提示词。必须基于 character-board-meta-prompt-zh-v1.md 编译。]

要求：
- 输出角色资产板。
- 明确资产编号：A01。
- 明确可被后续 Seedance 引用的模块标签：M01 FACE、M03 COSTUME、M05 BODY SCALE、M06 HAND GESTURE 等。
- 中文板只使用中文标签，生产代码 A01/M01/M03 可保留。
- 风格锁根据当下角色和片子风险动态编写。
```

#### EN_IMAGE2_PROMPT

```text
[Fill the English character asset prompt. Compile from character-board-meta-prompt-v1.md.]

Requirements:
- Generate the character asset board.
- Asset code: A01.
- Include stable module labels for later Seedance reference: M01 FACE, M03 COSTUME, M05 BODY SCALE, M06 HAND GESTURE, etc.
- English board uses English labels only. Production codes A01/M01/M03 may remain.
- Style lock is tailored to the current character and current drift risks.
```

---

### 1.2 场景资产 / Scene Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有场景图，请上传 @图片2 = A03 / 场景参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
[填写中文场景资产提示词。必须基于 scene-board-meta-prompt-zh-v1.md 编译。]

要求：
- 输出场景资产板。
- 明确资产编号：A03。
- V01-V09 场景画面必须干净，不得在画面内部出现文字、箭头、尺寸线、区域圈、机位图标、虚线、图例或说明标注。
- 所有标注只允许出现在底部 MAP / 俯视图区域。
- 中文板只使用中文标签，生产代码 A03/V01/V04/MAP 可保留。
```

#### EN_IMAGE2_PROMPT

```text
[Fill the English scene asset prompt. Compile from scene-board-meta-prompt-v1.md.]

Requirements:
- Generate the scene asset board.
- Asset code: A03.
- V01-V09 scene views must be clean. No text, arrows, measurement lines, zone circles, camera icons, dashed paths, legends, or explanatory notes inside scene images.
- All annotations are allowed only in the bottom MAP / top-down plan.
- English board uses English labels only. Production codes A03/V01/V04/MAP may remain.
```

---

### 1.3 道具资产 / Prop Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考用户已有道具图，请上传 @图片3 = A05 / 道具参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
[填写中文道具资产提示词。必须基于 prop-board-meta-prompt-zh-v1.md 编译。]

要求：
- 输出道具资产板。
- 明确资产编号：A05。
- 明确可被后续 Seedance 引用的模块标签：P01 HERO PROP、P04 ACTIVE STATE、P06 HAND LOGIC、P07 SCENE ANCHOR 等。
- 中文板只使用中文标签，生产代码 A05/P01/P04/P06 可保留。
- 道具状态变化和持握逻辑必须清晰。
```

#### EN_IMAGE2_PROMPT

```text
[Fill the English prop asset prompt. Compile from prop-board-meta-prompt-v1.md.]

Requirements:
- Generate the prop asset board.
- Asset code: A05.
- Include stable module labels for later Seedance reference: P01 HERO PROP, P04 ACTIVE STATE, P06 HAND LOGIC, P07 SCENE ANCHOR, etc.
- English board uses English labels only. Production codes A05/P01/P04/P06 may remain.
- Prop state changes and hand logic must be clear.
```

---

## 2. 阶段二：干净故事板提示词

### 2.1 故事板上传提醒

<span style="color:#15803d;font-weight:600;">上传提醒：生成故事板时请参考已完成资产。建议上传 @图片1 = A01 角色资产、@图片2 = A03 场景资产、@图片3 = A05 道具资产。此提醒不属于提示词。</span>

### 2.2 中文故事板提示词

```text
TEMPLATE_CODE：CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID：S01_CLEAN_STORYBOARD_CONTROL
PART：[Part 编号 / 00:00-00:15]
LAYOUT：[例如 4x2 horizontal storyboard, 8 clean panels, read left to right, top to bottom]

[填写中文故事板提示词。必须基于 storyboard-board-meta-prompt-zh-v1.md 编译。]

硬规则：
- 故事板图像必须是干净黑白手稿 / 灰阶预演图。
- 只画角色剪影、场景结构、动作姿态、构图、景别和空间关系。
- 不得出现箭头、运动线、彩色标注、编号、时间码、文字说明、图例、标题栏、标签、机位图标、白底 UI。
- 时间码只写在提示词文本里，不画进画面。
- 运镜、动作方向、速度和切点功能写入 SEEDANCE_MOTION_TEXT。
```

### 2.3 English Storyboard Prompt

```text
TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID: S01_CLEAN_STORYBOARD_CONTROL
PART: [Part ID / 00:00-00:15]
LAYOUT: [for example 4x2 horizontal storyboard, 8 clean panels, read left to right, top to bottom]

[Fill the English storyboard prompt. Compile from storyboard-board-meta-prompt-v1.md.]

Hard rules:
- The storyboard image must be a clean black-and-white sketch / grayscale previs board.
- Show only character silhouettes, scene structure, action poses, composition, shot size, and spatial blocking.
- No arrows, motion lines, color annotations, panel numbers, timestamps, written notes, legends, title bars, labels, camera icons, or white UI.
- Timestamps are prompt text only and must not appear in the image.
- Camera movement, action direction, speed, and cut function go into SEEDANCE_MOTION_TEXT.
```

### 2.4 SEEDANCE_MOTION_TEXT

#### 中文

```text
SH01：[运镜、动作方向、速度、切点功能]
SH02：[运镜、动作方向、速度、切点功能]
SH03：[运镜、动作方向、速度、切点功能]
...
SH##：[运镜、动作方向、速度、切点功能]
```

#### English

```text
SH01: [camera movement, action direction, speed, cut function]
SH02: [camera movement, action direction, speed, cut function]
SH03: [camera movement, action direction, speed, cut function]
...
SH##: [camera movement, action direction, speed, cut function]
```

---

## 3. 阶段三：Seedance 2.0 视频提示词

### 3.1 视频上传提醒

<span style="color:#15803d;font-weight:600;">上传提醒：Seedance 2.0 全能参考请按顺序上传：@图片1 = A01 / 角色资产；@图片2 = A03 / 场景资产；@图片3 = A05 / 道具资产；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 干净故事板。此提醒不属于提示词。</span>

### 3.2 中文 Seedance 提示词

```text
[VIDEO TASK]
[填写中文视频任务。只描述新片，不写参考片、原片、学习过程。]

[REFERENCE HIERARCHY]
本次使用 Seedance 2.0 全能参考。
@图片1 / A01 / [角色资产名] 是最高优先级角色身份源，锁定 [脸、发型、服装、比例、手势等]。
@图片2 / A03 / [场景资产名] 是最高优先级场景源，锁定 [空间、光线、地理、关键锚点等]。
@图片3 / A05 / [道具资产名] 是最高优先级道具源，锁定 [形状、材质、尺度、持握、状态变化等]。
@图片4 / S01_CLEAN_STORYBOARD_CONTROL / [布局] 只锁 SH01-SH## 的镜头顺序、构图重心、角色站位、动作状态、空间距离和连续关系。
优先级：资产图 > 干净故事板 > SEEDANCE_MOTION_TEXT > 逐镜文字 timing。若故事板与资产图冲突，以资产图为准。

[STORYBOARD LOGIC]
将提供的 @图片4 / S01_CLEAN_STORYBOARD_CONTROL / [布局] 干净故事板视觉控制板制作成一段流畅的电影级动画视频。按从左到右、从上到下读取 SH01-SH##。严格保持 SH01-SH## 的镜头顺序、构图重心、角色站位、动作状态、空间距离和镜头连贯性。故事板只作为镜头顺序、构图和动作状态参考，最终必须是一条连续成片。

[SEEDANCE_MOTION_TEXT]
[粘贴阶段二中文 SEEDANCE_MOTION_TEXT]

[SEGMENT STATE]
入场状态：
中段状态变化：
结尾状态：

[SHOT-BY-SHOT TIMING]
SH01 / [timecode]：[景别、动作、可见结果、active assets]
SH02 / [timecode]：[景别、动作、可见结果、active assets]
...

[ACTION / BLOCKING]
[写清角色、场景、道具、空间调度、因果链和终帧 payoff。]

[CAMERA MOVEMENT]
[写清当下片子的运镜组合，避免泛泛而谈。]

[LIGHTING / VFX]
[写清光线、材质、特效触发、特效发展和特效边界。]

[REALISTIC CINEMA STYLE LOCK]
[根据当下片子最容易跑偏的方向动态编写。只写必要内容。例如：如果容易动漫化，就锁真实电影质感、体积雾、光效衰减、材质不完美、非海报式构图；如果容易广告棚拍，就锁自然现场感；如果容易塑料质感，就锁材质粗糙度和真实反射。]

[DIALOGUE / VOICE PERFORMANCE]
[台词、旁白或无台词；不生成字幕。]

[SOUND EFFECTS FOR POST]
[无 BGM / 有 BGM；画内音效和后期音效点。]

[NEGATIVE PROMPT]
[只写当前真实风险。不要堆旧污染项。干净故事板通过后，不再写箭头、红框、绿标、编号、时间码等故事板阶段问题。]
```

### 3.3 English Seedance Prompt

```text
[VIDEO TASK]
[Fill the English video task. Describe only the new film. Do not mention source film, original prompt, analysis, or learning process.]

[REFERENCE HIERARCHY]
Use Seedance 2.0 all-reference mode.
@image1 / A01 / [character asset name] is the highest-priority character identity source, locking [face, hairstyle, wardrobe, body scale, gesture, etc.].
@image2 / A03 / [scene asset name] is the highest-priority scene source, locking [space, lighting, geography, key anchors, etc.].
@image3 / A05 / [prop asset name] is the highest-priority prop source, locking [shape, material, scale, hand logic, state change, etc.].
@image4 / S01_CLEAN_STORYBOARD_CONTROL / [layout] locks only SH01-SH## shot order, composition center, character blocking, action state, spatial distance, and continuity.
Priority: asset images > clean storyboard > SEEDANCE_MOTION_TEXT > shot-by-shot text timing. If storyboard conflicts with assets, follow the assets.

[STORYBOARD LOGIC]
Convert the provided @image4 / S01_CLEAN_STORYBOARD_CONTROL / [layout] clean storyboard visual control board into a smooth cinematic animated video. Read SH01-SH## from left to right and top to bottom. Strictly preserve shot order, composition center, character blocking, action state, spatial distance, and shot continuity. Use the storyboard only as shot order, composition, and action-state reference. The final result must be one continuous film clip.

[SEEDANCE_MOTION_TEXT]
[Paste the English SEEDANCE_MOTION_TEXT from Stage 2.]

[SEGMENT STATE]
Opening state:
Mid-segment state change:
Ending state:

[SHOT-BY-SHOT TIMING]
SH01 / [timecode]: [shot size, action, visible result, active assets]
SH02 / [timecode]: [shot size, action, visible result, active assets]
...

[ACTION / BLOCKING]
[Define character blocking, scene geography, prop causality, action chain, and final payoff.]

[CAMERA MOVEMENT]
[Define the current film's camera grammar precisely.]

[LIGHTING / VFX]
[Define lighting, material behavior, VFX trigger, VFX development, and VFX boundaries.]

[REALISTIC CINEMA STYLE LOCK]
[Write this dynamically for the current film's drift risk. For example: if it tends to become anime/game CG, lock live-action cinematic texture, volumetric haze, light falloff, imperfect reflections, and non-poster framing.]

[DIALOGUE / VOICE PERFORMANCE]
[Dialogue, voiceover, or no dialogue. Do not generate subtitles.]

[SOUND EFFECTS FOR POST]
[No BGM / BGM. On-screen sound and post sound effect points.]

[NEGATIVE PROMPT]
[Write only current real risks. Do not pile up old contamination terms. If the clean storyboard passed QA, do not repeat arrows, red boxes, green labels, panel numbers, timestamps, or other storyboard-stage problems.]
```

---

## 4. QA 自检

```text
B_LINE_SINGLE_MD_PACKAGE_QA:
- 是否只输出一个 .md 文件：是 / 否
- 三阶段顺序是否为资产 -> 干净故事板 -> Seedance 视频：是 / 否
- 所有提示词是否双语：是 / 否
- 所有上传提醒是否为绿色文字，且不在提示词块内：是 / 否
- 资产编号与后续引用是否一致：是 / 否
- 故事板是否为 S##_CLEAN_STORYBOARD_CONTROL：是 / 否
- 故事板是否无箭头、无运动线、无编号、无时间码、无文字说明：是 / 否
- SEEDANCE_MOTION_TEXT 是否完整承接运镜、动作方向、速度和切点功能：是 / 否
- Seedance 是否明确资产优先级高于故事板：是 / 否
- REALISTIC CINEMA STYLE LOCK 是否根据当下跑偏风险动态编写：是 / 否
- NEGATIVE PROMPT 是否只写当前风险，没有堆砌旧污染项：是 / 否
- 低于 95/100 是否已拒绝交付并回退修正：是 / 否
```
