# Branch B Longform Asset + Storyboard + Seedance Protocol

B 线不是单纯的“故事板控切镜”。它是长一点片子里的主生产线：用资产锁统一性，用故事板锁叙事和镜头，用 Seedance 2.0 的全能参考把资产和故事板合并读取，最终在多段视频中保持风格、角色、场景和道具统一。

## 1. 核心目的

```text
长片前端 DNA 拆解
-> 段落划分与连续性圣经
-> B_FRONTEND_SIGNOFF
-> 资产包
-> 分段故事板 / 干净控制帧
-> Seedance 2.0 全能参考
-> 多段连续成片
```

B 线的前端拆解必须和 A 线、C 线一样先做多维 DNA 审核。不能因为最终会用故事板控制镜头，就跳过剧情、表演、空间、声音、状态变化和连续性分析。

## 2. B 线前端长片拆解

长片先不要进入资产、故事板或 Seedance。必须先完成：

```text
P0 intake
-> P1 whole-film structure
-> P2 segment DNA ledger
-> P3 cross-segment continuity bible
-> P4 omission audit
-> B_FRONTEND_SIGNOFF
```

### P1 Whole-Film Structure

先把长片拆成可生产段落，而不是直接按秒数切：

- 全片时长、画幅、fps、音频状态。
- 故事段落：开场、设定、推进、转折、高潮、收束。
- 情绪曲线：每段情绪起点、变化、终点。
- 角色出场和状态变化表。
- 场景地理变化表。
- 道具/产品/法术/机制变化表。
- 声音、台词、字幕、BGM 和后期边界。
- 叙事优先级：哪些段落必须复刻，哪些段落可压缩或重组。

### P2 Segment DNA Ledger

每个被选中段落都必须独立做多维拆解：

```text
SEG##
source_timecode
duration
story_function
emotion_in
emotion_out
shot_or_beat_count
continuity_mode
camera_grammar
composition_logic
character_state
performance_beats
scene_geography
prop_mechanism
wardrobe_makeup_state
lighting_color_texture
dialogue_or_vo_function
sfx_function
vfx_state_change
edit_rhythm
in_state
action_chain
out_state
continuity_to_next
asset_needs
storyboard_needs
risk_notes
```

如果一个段落超过 15 秒，继续拆成 4-15 秒的 Seedance 子段；但每个子段仍要保留它在原长片段落里的叙事功能。

### P3 Cross-Segment Continuity Bible

B 线长片最怕“每段都好看，但剪起来断”。所以必须先写连续性圣经：

- 角色连续性：脸、体型、发型、服装、妆容、情绪状态、动作习惯。
- 场景连续性：空间地理、入口出口、光源方向、前中后景、可拍区域。
- 道具连续性：形状、材质、尺度、持握、状态变化和上一段遗留状态。
- 风格连续性：媒介、色彩、光影、镜头质感、颗粒/清晰度、运动风格。
- 声音连续性：环境声、台词/旁白节奏、音效点、BGM 后期边界。
- 剪辑连续性：动作匹配、视线匹配、声音切点、方向匹配、终帧到下段入帧。

### P4 B Line Omission Audit

进入资产和故事板前逐项审核：

| Audit Item | Required Check |
|---|---|
| 全片结构 | 是否知道每段服务哪个叙事功能？ |
| 段落切分 | 是否每段 4-15 秒，且不是机械按秒切？ |
| 镜头/Beat | 是否确认每段镜头数或 beat 数，且连续性模式正确？ |
| 状态链 | 上段 out_state 是否能接下段 in_state？ |
| 角色统一 | 角色状态变化是否能被资产和故事板承接？ |
| 场景统一 | 空间地理和光线方向是否跨段一致？ |
| 道具机制 | 道具/产品/法术状态是否跨段继承？ |
| 叙事节奏 | 哪些段落必须保留，哪些可压缩是否明确？ |
| 声音边界 | BGM、字幕、旁白、环境声、音效是否分清？ |
| 故事板需求 | 每段需要几格故事板，是否超过 10 格需拆板？ |
| 资产需求 | 每段需要哪些角色/场景/道具/执行态/终态资产？ |

### B_FRONTEND_SIGNOFF

没有通过前端签核，不得进入资产包、故事板或 Seedance：

```text
B_FRONTEND_SIGNOFF: PASS / FAIL
whole_film_structure_complete: yes/no
segment_dna_ledgers_complete: yes/no
cross_segment_continuity_bible_complete: yes/no
segment_in_out_states_chain: yes/no
asset_needs_mapped: yes/no
storyboard_needs_mapped: yes/no
sound_post_boundaries_clear: yes/no
omission_audit_passed: yes/no
qa_score: [0-100]
```

任一关键项为 `no`，或 `qa_score < 95`，不得进入后续生产。

## 3. 后端生产主链

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

## 4. 输入职责

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

## 5. 长片拆段规则

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

## 6. Storyboard Board Policy

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

## 7. B 线 Seedance Reference Hierarchy

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

## 8. Segment Handoff Template

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

## 9. B 线 QA

交付前必须检查：

- 是否完成 B 线前端长片拆解。
- 是否通过 `B_FRONTEND_SIGNOFF`。
- 是否完成全片结构表、逐段 DNA ledger 和跨段连续性圣经。
- 是否完成资产包。
- 是否完成段落拆分。
- 每段是否有 `in_state / action / out_state`。
- 故事板 panel 是否对应真实镜头或新片镜头功能。
- Seedance 输入版故事板是否干净。
- 资产优先级是否高于故事板。
- 每个镜头是否引用资产模块。
- 多段之间角色、场景、道具和风格是否连续。
- A11 评分是否达到 95/100。
