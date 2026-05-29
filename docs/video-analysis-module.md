# 视频分析模块

本模块吸收 PromptLens 的有效思路：先把视频变成“可分析的帧序列 + 可检索的音频文本 + 可对齐的时间线”，再交给逐镜拆解 Agent。它不直接生成后端提示词，而是为 `shot_ledger`、`segment_plan` 和 `sound_post_duties` 提供可靠证据。

## 1. 设计原则

- 视频分析先于导演拆解；没有媒体探测、抽帧和音频转写，不进入逐镜复刻。
- 单帧分析回答“画面是什么”，序列分析回答“画面怎么变化”。
- 音频分析回答“说了什么、何时说、声音如何推动节奏”。
- 多模态对齐回答“哪个画面变化对应哪个台词、音效或剪辑点”。
- 所有分析都必须保留 timecode，避免后端拿到没有定位依据的创意描述。

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
