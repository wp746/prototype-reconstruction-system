# 视频分析模块

本模块吸收 PromptLens 的有效思路：先把视频变成“可分析的帧序列 + 可检索的音频文本 + 可对齐的时间线”，再交给逐镜拆解 Agent。它不直接生成后端提示词，而是为 `shot_ledger`、`segment_plan` 和 `sound_post_duties` 提供可靠证据。

## 1. 设计原则

- 视频分析先于导演拆解；没有媒体探测、抽帧和音频转写，不进入逐镜复刻。
- 单帧分析回答“画面是什么”，序列分析回答“画面怎么变化”。
- 音频分析回答“说了什么、何时说、声音如何推动节奏”。
- 多模态对齐回答“哪个画面变化对应哪个台词、音效或剪辑点”。
- 所有分析都必须保留 timecode，避免后端拿到没有定位依据的创意描述。
- 复刻任务必须先确认镜头数量和切点。故事板和 Seedance 提示词必须跟真实镜头数量对齐，不能用 4 个宏观段落替代逐镜节奏。
- 复刻任务必须先通过 DNA 取证审核。15 秒以内片段必须做逐帧/逐变化拆解，不能只看 1fps 或 0.5 秒接触表；0.5 秒接触表只是导航图，不是最终证据。

## 2. Video Analysis Pipeline

### V0 Media Probe

目标：确认视频是否可分析，并建立基础参数。

输出 `media_probe`：

- `duration`
- `width`
- `height`
- `fps`
- `codec`
- `has_audio`
- `aspect_ratio_detected`
- `analysis_mode`

默认分析模式：

- `quick_8`: 快速初筛，均匀抽 8 帧。
- `standard_16`: 默认模式，均匀帧 + 段落边界帧。
- `forensic_32`: 精拆模式，均匀帧 + 视觉变化点 + 音频分段边界。

### V1 Frame Sampling

目标：生成可分析帧序列。

输出 `frame_sampling_plan`：

- `strategy`: `uniform`、`scene_boundary`、`audio_aligned`、`manual_markers`。
- `target_frame_count`
- `timestamps`
- `reason`

采样规则：

- 均匀抽帧用于快速理解整体风格和主体。
- 视觉突变点用于发现剪辑点、场景切换、光影变化。
- 音频边界帧用于定位台词、音效和情绪节拍。
- 关键动作前后至少保留 2 帧，避免只看结果不看动作发生。
- 15 秒以内的复刻片段，必须额外生成 0.5 秒级联系表或等效密度抽帧，用来确认快切数量和镜头连续性。
- 15 秒以内片段必须补充逐帧或逐变化帧审计：每一个视觉状态变化都要记录，包括角色形态、服装/甲胄、道具、法术、群体反应、终帧前态。若无法逐帧人工描述全部帧，必须至少对每个连续动作段做前帧/中帧/后帧三点验证，并记录未确认风险。

### V2 Single-Frame Visual Pass

目标：逐帧识别静态画面要素。

输出 `frame_observations[]`：

- `frame_id`
- `timestamp`
- `linked_shot`
- `subject`
- `environment`
- `shot_size`
- `angle`
- `composition`
- `lighting`
- `color_texture`
- `style`
- `mood`
- `visible_text_or_logo`
- `risk_flags`

分析维度固定为：

- 主体：人物、动作、服装、道具。
- 环境：空间类型、前中后景、时段、天气、背景符号。
- 镜头：景别、角度、构图、焦点、景深。
- 光影：光源、方向、光比、色温、特殊光效。
- 美术：风格、色彩、材质、后期质感。
- 情绪：基调、叙事暗示、节奏动态。

### V3 Sequence Visual Pass

目标：识别帧间变化和运镜规律。

输出写回 `shot_ledger` 和 `multimodal_sync`：

- 帧间变化：主体、场景、光影和道具的变化。
- 运动轨迹：人物/物体的路径、方向和速度。
- 镜头运动：推、拉、摇、移、跟、环绕、手持、锁定。
- 起止状态：镜头从哪里开始、停在哪里、为什么停。
- 视觉一致性：哪些元素贯穿全段，哪些元素突然变化。
- 节奏判断：静态、慢速、中速、快速、动荡。
- 镜头数量：输出 `shot_count_estimate`、每个切点的 timecode、每镜预计时长和证据来源。
- 切点证据：视觉突变、构图重心变化、景别变化、运镜方向变化、动作触发、声音/台词点。
- 连贯性判断：镜头是否一气呵成，靠动作、视线、运动方向、线条方向、声音点还是构图重心衔接。
- 状态变化判断：角色是否变身、换装、显形、升级、被托起、法相化；道具是否展开、断裂、发光、变形；群体是否冻结、后仰、跪下、散开或被牵引。任何状态变化都必须单独命名，不能合并成“特效变化”。

15 秒以内片段建议输出：

```text
shot_count_estimate:
SH01 00:00.0-00:01.2 / evidence: high wide to rear pressure cut
SH02 00:01.2-00:02.1 / evidence: composition center and camera angle change
...
```

### V4 Audio Extraction and Transcription

目标：把音频变成可对齐文本和声音事件。

输出 `audio_transcript[]`：

- `start`
- `end`
- `speaker`
- `text`
- `confidence`
- `audio_event`

音频处理规则：

- 优先提取 16kHz mono WAV 供 ASR 使用。
- 识别对白、旁白、音乐、环境声、静默、冲击音效。
- 原台词只进入分析层，后续只能保留台词功能，不能复制原句。
- 原音乐和音效素材不得进入后端生成或后期复用。

### V5 LLM Audio Segmentation

目标：把转写文本转成逻辑段落。

输出 `audio_segments[]`：

- `start`
- `end`
- `summary`
- `tags`
- `dialogue_function`
- `rhythm_function`

分段原则：

- 优先按话题、情绪转折、信息释放和声音事件切段。
- 如果 LLM 分段失败，退回固定时长分段，但必须标记 `confidence: low`。
- 每段摘要只描述内容功能，不复写完整台词。

### V6 Multimodal Sync

目标：合并视觉和音频，形成可复刻的证据链。

输出 `multimodal_sync[]`：

- `timecode`
- `visual_event`
- `audio_event`
- `edit_signal`
- `narrative_function`
- `remake_instruction`

对齐规则：

- 如果视觉剪辑点和音频节拍重合，标记为强剪辑点。
- 如果台词信息点触发镜头切换，记录为台词驱动剪辑。
- 如果静默制造悬念，记录为声音节奏方法，而不是空缺。
- 如果音画不一致，记录为反讽、悬念或信息错位。

### V7 Shot Candidate Reconciliation

目标：把抽帧分析、音频分段和视觉突变合并为最终镜头。

输出最终 `shot_ledger`：

- 每个 shot 必须由至少一种证据支持：视觉突变、运镜起止、音频节拍、叙事 beat。
- 如果一个镜头内部变化过大，拆成多个 shot 或多个 Seedance segment。
- 如果多个抽帧属于同一连续运镜，合并为一个 shot，并记录起止状态。
- 最终 `shot_ledger` 的镜头数量必须被写入故事板计划：`storyboard_count`、`panels_per_board`、`layout`。
- 如果镜头数不超过 10，故事板 panel 数必须等于镜头数。
- 如果镜头数超过 10，必须拆成多个故事板，每板最多 10 镜。

### V8 DNA Forensic Audit

目标：在生产前审核是否真正拿到原片 DNA。

读取并执行 [DNA Forensic Audit System](dna-forensic-audit-system.md)。

输出：

- `frame_ledger`
- `shot_ledger`
- `dna_invariant_ledger`
- `omission_audit`
- `DNA_SIGNOFF`

硬性规则：

- `DNA_SIGNOFF` 未通过，不得进入资产、故事板或 Seedance 提示词。
- 如果发现角色变身、法术升级、道具机制、群体反应或终帧前态漏项，必须回退到 V1-V3 重新拆。
- 生产提示词不能写“参考原片/学习原片”等后台措辞；审核结论要转成新片自身的镜头动作和状态变化。

## 3. Failure Handling

- 视频不可解析：要求用户补交可访问文件、截图序列或关键帧。
- 音频不可用：继续做视觉分析，但 `audio_transcript` 标记为空，声音策略进入人工补充。
- 抽帧过少：不得生成最终交接包，只能输出粗分析。
- ASR 低置信：台词功能必须标记为待人工确认。
- 多模态冲突：保留冲突说明，不强行编造成一致叙事。

## 4. Human Review Points

- Review 1：抽帧是否覆盖关键段落。
- Review 2：音频转写是否准确，台词功能是否正确。
- Review 3：视觉分段与音频分段是否对齐。
- Review 4：最终 shot ledger 是否能支撑逐镜复刻。
- Review 5：DNA 审核是否检查了变身/状态变化、道具机制、法术升级、群体反应和终帧前态；没有通过不得生产。
