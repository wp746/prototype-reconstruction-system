# Prototype Reconstruction System

> v0.1.0 | 2026-05-29

一个面向 AIGC 短片创作者和内部制作团队的“原型重构”多智能体工作流系统。

它不是简单帮你分析一个视频，也不是把参考片一比一抄成提示词，而是把一个优秀创意短片拆成可迁移的电影方法：

```text
参考片链接 / 本地视频 / 新主题 brief
-> 媒体探测 / 抽帧 / 音频转写 / 音画对齐
-> 逐镜拆解剧情、角色、风格、道具、台词功能、构图、运镜、特效、音效和叙事节奏
-> 保留层 / 变化层 / 合规风险映射
-> 新片剧情、角色、场景、道具和风格迁移
-> Markdown + JSON 生产交接包
-> Image2 + Seedance 2.0 后端提示词工厂
```

系统默认做 **方法复刻**，不是复制原片。它保留镜头语言、节奏结构、情绪曲线、构图逻辑、运镜方法和声音节奏，同时替换原片角色、台词、品牌、音乐、IP 符号和可识别画面表达。

## Quick Start

如果你现在就要把这套系统交给 Codex、OpenClaw、Hermes 或内部多智能体工作流，用下面这组信息就够了。

安装仓库地址：

```text
https://github.com/wp746/prototype-reconstruction-system.git
```

核心 SOP 地址：

```text
https://raw.githubusercontent.com/wp746/prototype-reconstruction-system/main/docs/prototype-reconstruction-sop.md
```

视频分析模块地址：

```text
https://raw.githubusercontent.com/wp746/prototype-reconstruction-system/main/docs/video-analysis-module.md
```

压缩包地址：

```text
https://github.com/wp746/prototype-reconstruction-system/archive/refs/heads/main.zip
```

推荐先看：

- [原型重构多智能体 SOP](docs/prototype-reconstruction-sop.md)
- [视频分析模块](docs/video-analysis-module.md)
- [Agent 职责卡](docs/agent-cards.md)
- [角色资产板固定模板 V2](templates/character-asset-board-template-v2.md)
- [场景资产板固定模板 V1](templates/scene-asset-board-template-v1.md)
    ├── storyboard-asset-board-template-v1.md

- [道具资产板固定模板 V1](templates/prop-asset-board-template-v1.md)
所有故事板类 Image2 提示词必须使用 `WHITE_STORYBOARD_SHEET_TEMPLATE`，模板见 [templates/storyboard-asset-board-template-v1.md](templates/storyboard-asset-board-template-v1.md)。故事板必须包含 10 个固定段落：`[PROJECT CARD]`、`[CONTINUITY HEADER]`、`[SUBJECTS]`、`[SCENE]`、`[STORYBOARD FORMAT]`、`[VISUAL LANGUAGE]`、`[ACTION DNA]`、`[SHOT DESIGN RULES]`、`[PANEL BEAT MAP]`、`[NEGATIVE]`。每格 beat 用"景别 + 动作"一句话，不要长描写。风格包写成一段完整声明而不是关键词堆砌。角色描述必须包含动作语言而不是只有外观。
- [故事板固定模板 V1](templates/storyboard-asset-board-template-v1.md)

- [Markdown 交接模板](templates/handoff-template.md)
- [JSON 交接模板](templates/handoff-template.json)
- [JSON Schema](schemas/handoff.schema.json)
- [QA Checklist](checklists/qa-checklist.md)

## 它解决什么问题

这个系统主要解决参考片反推和 AIGC 复刻生产里的 12 个关键问题：

1. 看到一个创意短片觉得好，但不知道它到底好在剧情、镜头、节奏、声音还是美术。
2. 想做同类型短片，但不想照搬原片角色、台词、品牌、音乐和 IP 表达。
3. 普通视频分析只给画面描述，缺少可交给 Image2 + Seedance 2.0 的生产字段。
4. 只看截图容易误判运镜和节奏，缺少帧间变化、音频节拍和剪辑点证据。
5. 参考片是动画，新片想改成写实时，缺少风格迁移和材质/表演重写规则。
6. 横屏参考片迁移到 9:16 时，构图、人物关系和运动方向容易硬塞。
7. 台词被错误复写，导致侵权或新片主题不成立。
8. 原音乐、音效、logo、包装、名人脸和 IP 符号没有被单独拦截。
9. 下游后端拿到的是“高级感、电影感”这类空话，无法直接生成资产板和分镜。
10. Seedance 分段没有 in state、action、out state，剪辑接不上。
11. 前端分析、人审确认和后端提示词工厂之间缺少稳定 JSON 契约。
12. 后期迭代时，SOP、模板、schema、校验器和 README 容易不同步。

## 核心能力

### 1. PromptLens 式视频分析前置层

系统吸收了 PromptLens 的有效思路：先把视频变成可分析的帧序列、音频文本和时间线证据，再进入导演拆解。

默认视频分析链路：

```text
Media Probe
-> Frame Sampling
-> Single-Frame Visual Pass
-> Sequence Visual Pass
-> Audio Extraction and Transcription
-> LLM Audio Segmentation
-> Multimodal Sync
-> Shot Candidate Reconciliation
```

这样逐镜拆解不是凭感觉写，而是由抽帧、视觉变化、运镜起止、音频节拍和叙事 beat 共同支撑。

### 2. 多智能体原型重构

系统内置 A0-A11 共 12 个 Agent：

- A0 总控制片 Agent
- A1 输入与版权溯源 Agent
- A2 视频分析与切段 Agent
- A3 逐镜拆解 Agent
- A4 叙事与台词功能 Agent
- A5 风格与资产 Agent
- A6 声音与节奏 Agent
- A7 保留/变化映射 Agent
- A8 新片映射 Agent
- A9 合规与风险 Agent
- A10 后端交接 Agent
- A11 QA Agent

每个 Agent 都有明确输入、输出和通过标准，避免“分析很多，但没人知道下一步怎么做”。

### 3. 方法复刻，不复制原片

系统把参考片拆成两层：

- `Preserve Logic`：镜头语法、景别推进、构图逻辑、运镜路径、剪辑节奏、声音节奏、情绪曲线、角色/产品出场方法。
- `Replace Expression`：角色身份和脸、服装造型、品牌商标、原台词、原字幕、原音乐、可识别场景、IP 符号和具体剧情设定。

每个可识别元素都必须有替换方案、风险等级和新的 prompt 规则。

### 4. 后端可解析交接包

最终输出两份交接物：

- Markdown 人审版：给导演、制片、客户或内部团队审核。
- JSON 机器版：给后端解析并生成 Image2 资产提示词、Image2 Storyboard / Control Board 和 Seedance 2.0 视频提示词。

JSON 顶层结构固定包含：

```text
project_lock
source_lock
reference_summary
media_probe
frame_sampling_plan
frame_observations
audio_transcript
audio_segments
multimodal_sync
shot_ledger
preservation_variation_map
new_production_mapping
asset_matrix
scene_geography
prop_ui_text_matrix
segment_plan
sound_post_duties
compliance_risks
backend_instructions
```

### 5. 资产板固定模板

所有角色类 Image2 资产提示词必须使用 `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`，模板见 [templates/character-asset-board-template-v2.md](templates/character-asset-board-template-v2.md)。

固定版式为：

```text
左侧超大主全身
+ 顶部中间 4 个完整全身转面
+ 右侧脸部特写和表情库
+ 下方动作、手部、道具、服装材质、色卡、连续性标签
```

其中 `M02 / 全身转面` 是硬规则：必须是头顶到鞋底完整可见的四个全身角度，禁止半身、胸像、腰部裁切、只画头肩或只画上半身。后端交付包里的 `CHAR_*` 资产板不得再使用旧式“半身视图条”或松散拼贴版式。

所有场景类 Image2 资产提示词必须使用 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`，模板见 [templates/scene-asset-board-template-v1.md](templates/scene-asset-board-template-v1.md)。场景板必须有可见稳定标签：`V01`-`V09`、`MAP`、`ENTRANCE`、`EXIT`、`CAM_A`、`CAM_B`、`CAM_C`、`CHAR_ZONE`、`PROP_ANCHOR`、`LIGHT_DIR`、`NO_DRIFT`。
    ├── storyboard-asset-board-template-v1.md


所有道具类 Image2 资产提示词必须使用 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`，模板见 [templates/prop-asset-board-template-v1.md](templates/prop-asset-board-template-v1.md)。道具板必须有可见稳定标签：`P01`-`P08`、`REFERENCE USE`、`@PROP_CODE`、`HAND`、`SCENE_ANCHOR`、`DO_NOT_CHANGE`。
- [故事板固定模板 V1](templates/storyboard-asset-board-template-v1.md)


这些资产板标签是生产引用标签，不属于随机画面文字。Seedance 提示词应按这些标签引用资产局部，例如 `use @图片2 V04 CAMERA A`、`use @图片3 P06 HAND LOGIC`。

### 6. 校验脚本和 QA 门禁

内置无依赖 Python 校验脚本：

```bash
python3 scripts/validate_handoff.py templates/handoff-template.json
```

它会检查：

- 顶层字段是否完整
- 逐镜字段是否完整
- 资产编码是否稳定
- 每段 Seedance runtime 是否在 4-15 秒
- 新片映射是否引用有效镜头和资产
- high risk 合规项是否仍处于 open
- 后端目标是否为 `image2_seedance_2_0`

## 标准工作流

默认运行链路：

```text
Reference Intake
-> Video Analysis and Segmentation
-> Shot-by-Shot Deconstruction
-> Preservation / Variation Map
-> New Production Mapping
-> Compliance and Risk Gate
-> Human Approval Gates
-> Backend Handoff
-> QA
```

默认有 4 个人工确认点：

1. 参考片拆解完成，确认镜头与节奏理解准确。
2. 保留/变化边界完成，确认没有复制风险。
3. 新主题、新角色、新风格、新资产完成，确认创意方向。
4. 最终 Markdown + JSON 交接包完成，确认交给后端。

## 后端交接边界

前端只负责：

- 参考片反推
- 视频分析
- 方法迁移
- 合规审查
- Markdown + JSON 交接

后端负责：

- Image2 资产提示词
- Image2 Storyboard / Control Board
- Seedance 2.0 视频提示词
- 生成结果评分
- 失败镜头修复
- 后期拼接与声音执行

## 仓库结构

```text
.
├── README.md
├── CHANGELOG.md
├── checklists/
│   └── qa-checklist.md
├── docs/
│   ├── agent-cards.md
│   ├── prototype-reconstruction-sop.md
│   └── video-analysis-module.md
├── schemas/
│   └── handoff.schema.json
├── scripts/
│   └── validate_handoff.py
└── templates/
    ├── character-asset-board-template-v2.md
    ├── prop-asset-board-template-v1.md
- [故事板固定模板 V1](templates/storyboard-asset-board-template-v1.md)

    ├── scene-asset-board-template-v1.md
    ├── storyboard-asset-board-template-v1.md

    ├── handoff-template.json
    └── handoff-template.md
```

## 迭代维护约定

后续每次优化这套系统时，必须同步更新：

- README：更新版本、能力说明、Quick Start 或使用边界。
- CHANGELOG：记录本次变更原因、影响模块和校验结果。
- SOP / Agent Cards：如果工作流或角色职责变化，必须同步。
- Templates / Schema / Validator：如果交接字段变化，三者必须一起改。
- Asset Board Templates：如果角色、场景或道具资产板版式优化，必须同步模板、SOP、README 和既有提示词包。
- QA Checklist：如果新增风险、字段或后端约束，必须同步检查项。

这条规则是为了保证后期持续迭代时，文档、接口和校验器不会各说各话。
