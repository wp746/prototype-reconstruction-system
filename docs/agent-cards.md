# Agent Cards

## A0 总控制片 Agent

- 职责：管理项目状态、调用子 Agent、判断是否进入下一阶段，并在复刻任务开始前完成需求收集。
- 输入：用户 brief、参考片、当前交接包状态。
- 输出：阶段路由、缺失项列表、确认点、用户选择的复刻范围和变化范围。
- 通过标准：每个阶段都有明确 owner、输入、输出和阻塞项；如果用户没有选择复刻范围，只允许进入分析，不允许直接生产资产、故事板或 Seedance 提示词。

## A1 输入与版权溯源 Agent

- 职责：记录来源、权限、复用边界、目标平台、禁止复制项和用户自带资产状态。
- 输入：视频链接或本地路径、新主题、目标风格、目标时长、画幅、平台、用户提供的角色/场景/道具/产品素材。
- 输出：`source_lock`、`input_mode`、`user_asset_manifest`。
- 通过标准：来源可追踪；禁止复制项明确；无法访问的参考片被标记为 blocked；如果存在用户自带资产，必须标记 `REFERENCE_PLUS_USER_ASSETS` 并记录每个素材的类型、文件名、用途和保留级别。

## A2 视频切段 Agent

- 职责：运行视频分析模块，把参考片拆成可验证的叙事段落和镜头。
- 输入：参考片。
- 输出：`media_probe`、`frame_sampling_plan`、`frame_observations`、`multimodal_sync`、`reference_summary`、`shot_count_estimate`、`shot_ledger` 基础时间线。
- 通过标准：每个镜头有 `shot_id`、`timecode`、`duration`，且至少有抽帧、视觉变化、运镜起止或音频节拍证据；15 秒以内复刻片段必须确认镜头数量和切点证据。

## A3 逐镜拆解 Agent

- 职责：基于单帧观察和序列观察，分析每镜的剧情、画面、构图、运镜、表演、台词/旁白功能、光影、VFX、音效、剪辑和节奏。
- 输入：`shot_ledger` 基础时间线、`frame_observations`、`multimodal_sync`。
- 输出：补全后的 `shot_ledger`。
- 通过标准：每镜都能解释叙事功能、情绪功能、切点原因和与前后镜头的连贯关系。

## A4 叙事与台词功能 Agent

- 职责：提炼信息释放、台词功能、情绪转折和节奏结构。
- 输入：逐镜拆解、`audio_transcript`、`audio_segments`。
- 输出：每镜 `dialogue_function`、`narrative_function`、`emotional_function`，以及待人工确认的低置信台词。
- 通过标准：不复制原台词，只保留台词在剧情中的功能。

## A5 风格与资产 Agent

- 职责：提取角色类型、场景结构、道具系统、服化道、视觉风格，并在用户提供资产时执行资产摄取和补全。
- 输入：逐镜拆解、新片 brief、用户自带资产清单。
- 输出：`asset_matrix`、`scene_geography`、`prop_ui_text_matrix`。
- 通过标准：所有复用资产都有稳定资产码；所有 `CHAR_*` 角色资产必须声明使用 `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`；所有 `SCENE_*` 场景资产必须声明使用 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`；所有 `PROP_*` 道具资产必须声明使用 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`；如果用户提供资产，必须先做 `Visible / Inferred / Missing`，可见项一比一保留，缺失项只保守补全。
- 角色资产硬规则：`M02 / 全身转面` 必须是 4 个头顶到鞋底完整可见的全身角度，禁止半身、胸像、腰部裁切和只画头肩。
- 场景资产硬规则：必须有 `V01`-`V09`、`MAP`、`CAM_A/B/C`、`CHAR_ZONE`、`PROP_ANCHOR`、`LIGHT_DIR`、`NO_DRIFT` 等可见稳定标签。
- 道具资产硬规则：必须有 `P01`-`P08`、`REFERENCE USE`、`@PROP_CODE`、`HAND`、`SCENE_ANCHOR`、`DO_NOT_CHANGE` 等可见稳定标签。
- 故事板硬规则：必须使用 `WHITE_STORYBOARD_SHEET_TEMPLATE`，包含 10 个固定段落，每格 beat 用"景别 + 动作"一句话，角色带动作语言，风格包写成完整声明。
- 用户资产硬规则：用户自带角色、场景、道具和产品是主资产来源；参考片只提供资产功能、镜头位置和动作方法，不得覆盖用户资产的脸、体型、服装、空间地理、道具形状、媒介 DNA 和材质。

## A6 声音与节奏 Agent

- 职责：拆解音乐、环境声、音效、静默、节拍密度和剪辑韵律。
- 输入：参考片音轨、`audio_transcript`、`audio_segments`、逐镜时间线。
- 输出：`sound_post_duties` 和每段声音策略。
- 通过标准：原音乐不被复用；如果用户说明 BGM 是后期添加且不需要分析，A6 只输出原创音效、静默、冲击点和后期声音任务；声音功能被转译为新片可执行策略。

## A7 保留/变化映射 Agent

- 职责：把参考片拆为可保留方法和必须替换表达。
- 输入：逐镜拆解、资产分析、合规初筛。
- 输出：`preservation_variation_map`。
- 通过标准：每个高风险元素都有替换方案和新 prompt 规则。

## A8 新片映射 Agent

- 职责：把参考片镜头方法迁移到新主题、新角色、新场景、新道具和新风格。
- 输入：`preservation_variation_map`、新片 brief、资产矩阵。
- 输出：`new_production_mapping`、`segment_plan`、`storyboard_plan`。
- 通过标准：每个新片镜头或 segment 都有 in state、action、out state 和资产绑定；如果用户选择镜头节奏复刻，故事板 panel 数必须等于参考镜头数，超过 10 镜必须拆板；如果用户提供资产，每个新片镜头必须绑定用户资产模块并说明它替代参考片里的哪个资产功能。

## A9 合规与风险 Agent

- 职责：拦截版权、肖像、品牌、IP、音乐和过度相似风险。
- 输入：完整交接包草稿。
- 输出：`compliance_risks`、替换建议、风险等级。
- 通过标准：没有未处理的 high risk 项。

## A10 后端交接 Agent

- 职责：生成 Markdown 人审版和 JSON 机器版。
- 输入：通过 A9 的交接包。
- 输出：`handoff.md`、`handoff.json`。
- 通过标准：JSON 符合 schema；Markdown 结构完整；后端指令明确；角色类 Image2 提示词已套用 [角色资产板固定模板 V2](../templates/character-asset-board-template-v2.md)，场景、道具和故事板类 Image2 提示词已套用固定标签模板；Seedance 提示词必须写清 `A01 / M03`、`A02 / V04`、`A03 / P06` 等图号和模块标签，并明确把几乘几故事板制作成流畅电影级动画视频。

## A11 QA Agent

- 职责：检查完整性、可生产性、Seedance 分段、资产绑定和后端字段。
- 输入：Markdown + JSON 交接包。
- 输出：QA 报告。
- 通过标准：视频分析字段完整；用户复刻范围已记录；镜头数量和故事板格数一致；Seedance 资产引用写到图号和标签；所有 error 被修复；warning 有明确接受理由。
