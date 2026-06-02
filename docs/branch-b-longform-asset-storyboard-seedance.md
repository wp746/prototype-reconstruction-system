# Branch B Longform Asset + Storyboard + Seedance Protocol

B 线不是单纯的“故事板控切镜”。它是长一点片子里的主生产线：用资产锁统一性，用故事板锁叙事和镜头，用 Seedance 2.0 的全能参考把资产和故事板合并读取，最终在多段视频中保持风格、角色、场景和道具统一。

## 1. 核心目的

```text
资产包
-> 故事板 / 干净控制帧
-> Seedance 2.0 全能参考
-> 多段连续成片
```

B 线要解决的不是单个 12 秒片段，而是更长片子的连续生产问题：

- 角色脸、体型、服装、发型、气质统一。
- 场景空间、光线方向、空间锚点统一。
- 道具形状、材质、持握方式、状态变化统一。
- 故事板控制镜头顺序、切点、构图、动作方向和叙事节拍。
- 多个 Seedance 段落之间保持动作、空间、风格和情绪连续。

## 2. 输入职责

### 资产图负责身份和统一性

- 角色资产：脸、发型、体型、服装、手部、表情、动作语言。
- 场景资产：空间布局、入口出口、光线方向、前中后景、角色区、道具锚点。
- 道具资产：形状、材质、尺度、持握、触发、状态变化。
- 风格资产或风格锁：媒介、色彩、光影、质感、真实/动画/卡通/超现实程度。

### 故事板负责叙事和镜头

- 镜头顺序。
- 切点节奏。
- 构图重心。
- 主体位置。
- 动作方向。
- 运镜意图。
- 每镜的叙事功能和 out-state。

### Seedance 负责融合执行

Seedance 提示词必须明确告诉模型：

- 资产图是身份、场景、道具和风格的最高优先级。
- 故事板只作为镜头、运动、构图、切点、动作方向和叙事节拍参考。
- 如果故事板和资产冲突，以资产为准，只保留故事板的运动和叙事功能。

## 3. 长片拆段规则

长片不能把所有镜头塞进一条 Seedance。

推荐拆法：

- 每段 4-15 秒。
- 每段 1 个主要叙事动作或 1 个完整微事件。
- 每段最多 10 个 storyboard panels。
- 每段必须写 `in_state / action / out_state`。
- 下段的 `in_state` 必须继承上段 `out_state`。

段落交接字段：

```text
SEG##
runtime
story_function
in_state
action_chain
out_state
active_assets
storyboard_board
continuity_to_next
seedance_reference_plan
```

## 4. Storyboard Board Policy

B 线需要两套故事板：

- `S##_ANNOTATED_STORYBOARD`：导演人审版，可以有编号、箭头、构图说明和文字注释。
- `S##_CLEAN_BW_STORYBOARD`：Seedance 输入版，必须干净黑白手稿或干净控制帧。

Seedance 输入版禁止：

- 箭头。
- 编号。
- 框线。
- 标签。
- 文字说明。
- 面板 UI。
- 白底资产板痕迹。
- 精修角色脸。
- 精修服装材质。
- 临时角色、临时场景、临时道具。

如果干净故事板无法保持资产身份，不能直接上传，应改为：

```text
不上传故事板图，只把故事板转译成 SH timing、构图和动作方向文字。
```

## 5. B 线 Seedance Reference Hierarchy

提示词必须显式写优先级：

```text
Priority 1: 资产图锁角色、场景、道具、风格统一性。
Priority 2: 故事板锁镜头顺序、构图、动作方向、切点和叙事节拍。
Priority 3: 文字 timing 锁每镜动作、in/out state、台词/声音和段落交接。
```

中文可复制句：

```text
本次使用 Seedance 2.0 全能参考。请同时读取资产图和干净黑白故事板：资产图优先级最高，用于锁定角色身份、服装、场景空间、道具形状和整体风格；故事板只用于读取 SH01-SH[N] 的镜头顺序、构图重心、动作方向、切点节奏和叙事节拍。若故事板与资产图冲突，以资产图为准，只保留故事板的运动、构图和叙事功能。不要把故事板画成分镜图播放，不要渲染故事板边框、编号、箭头、文字标注或面板布局，最终必须是一条连续成片。
```

## 6. Segment Handoff Template

```text
[VIDEO TASK]
生成一条完整连续的 [runtime] 秒电影级视频，[aspect]，[fps]。这是长片第 [SEG##] 段，承接上一段 out_state，并输出本段 out_state 给下一段。

[REFERENCE HIERARCHY]
本次使用 Seedance 2.0 全能参考。
@图片1 / A01 锁角色身份：[module labels]。
@图片2 / A02 锁场景空间：[module labels]。
@图片3 / A03 锁道具机制：[module labels]。
@图片X / S##_CLEAN_BW_STORYBOARD 只锁 SH01-SH[N] 的镜头顺序、构图、动作方向、切点节奏和叙事节拍。
如果故事板与资产图冲突，以资产图为准。

[SEGMENT STATE]
in_state:
action_chain:
out_state:
continuity_to_next:

[SHOT TIMING]
SH01 / [timecode] / [shot size] / [camera move] / [action + visible result] / active assets: [A01/Mxx, A02/Vxx, A03/Pxx]
SH02 / ...

[VOICE / SFX]
台词/旁白：[功能和节奏，不生成字幕]
无 BGM。SFX：[画内声和后期音效点]

[NEGATIVE]
字幕，画面文字，水印，logo，故事板边框，面板布局，编号，箭头，标签，故事板翻页，临时故事板人物脸，临时服装，临时场景，角色脸漂移，服装漂移，道具变形，场景漂移，风格漂移，多指，坏手。
```

## 7. B 线 QA

交付前必须检查：

- 是否完成资产包。
- 是否完成段落拆分。
- 每段是否有 `in_state / action / out_state`。
- 故事板 panel 是否对应真实镜头或新片镜头功能。
- Seedance 输入版故事板是否干净。
- 资产优先级是否高于故事板。
- 每个镜头是否引用资产模块。
- 多段之间角色、场景、道具和风格是否连续。
- A11 评分是否达到 95/100。
