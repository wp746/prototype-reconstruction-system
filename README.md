# Prototype Reconstruction System

> v0.3.1 | 2026-06-02

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

## 三支线速览

复刻 / 重构进入生产时，系统按输入条件和控制目标选择 A/B/C 三条支线：

| 支线 | 什么时候用 | 核心输入 | 主要目标 | 关键风险 |
|---|---|---|---|---|
| A 线：资产直出 | 用户有角色、产品、场景、道具或品牌资产，身份一致性最重要 | 身份资产、环境资产、机制资产、执行态资产、最终 payoff 资产 | 保住指定资产身份，并迁移参考片的方法 DNA | 资产过多、状态图混用、最终态提前、节奏后移 |
| B 线：故事板控制 | 镜头顺序、切点、构图、动作方向最重要 | 资产图 + 干净黑白故事板 / 控制帧 | 锁镜头逻辑和运动方向 | 故事板箭头/编号/UI 污染，草图身份覆盖资产 |
| C 线：纯文本直出 | 用户没有资产和故事板，只要一条 Seedance 提示词快速验证 | 无上传图，只用文本 | 快速验证剧情结构、镜头节奏和因果链 | 身份、道具、细节一致性弱，复杂状态变化不稳定 |

三条支线都必须先完成后台 DNA 拆解，最终模型提示词不得出现“参考片、原片、学习、复制”等源片过程语言。

A 线采用“身份资产 -> 环境资产 -> 道具/机制资产 -> 执行态资产 -> 最终 payoff 资产”的资产职责隔离模型。当前系统把 86/100 作为有资产复刻的最低可用视觉基准，交付提示词按 95/100 自审；若单条 12-15 秒无法同时保住快节奏和复杂状态，应拆段生成再剪辑。

B 线只把干净黑白故事板作为镜头顺序、构图、动作方向和切点节奏参考，不把带标注的故事板上传给 Seedance。C 线使用紧凑因果锁，通常控制在用户要求的字数内，不混入 A/B 线的资产板和故事板负面词。

完整规则见 [复刻重构三支线全局规则](docs/global-three-branch-remake-system.md) 和 [Seedance 2.0 三支线交付协议](docs/seedance-two-branch-delivery-protocol.md)。

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

Agent / Skill 入口：

```text
https://raw.githubusercontent.com/wp746/prototype-reconstruction-system/main/SKILL.md
```

推荐调用方式：

```text
请调用 prototype-reconstruction-system 技能。
参考素材：<本地视频 / 视频链接 / 截图 / 用户资产包>
目标：先做 DNA 拆解与遗漏审核，再按 A/B/C 支线输出可生产提示词。
```

如果你的 agent 工具支持从 GitHub 安装技能，可以直接安装整个仓库；如果只支持单文件入口，就使用根目录 `SKILL.md`。OpenAI / Codex 类工具还会读取 `agents/openai.yaml` 作为列表卡片和默认调用提示。

推荐先看：

- [原型重构多智能体 SOP](docs/prototype-reconstruction-sop.md)
- [复刻需求收集与重构协议](docs/remake-reconstruction-protocol.md)
- [DNA 取证审核系统](docs/dna-forensic-audit-system.md)
- [复刻重构三支线全局规则](docs/global-three-branch-remake-system.md)
- [Seedance 2.0 三支线交付协议](docs/seedance-two-branch-delivery-protocol.md)
- [视频分析模块](docs/video-analysis-module.md)
- [Agent 职责卡](docs/agent-cards.md)
- [角色资产板固定模板 V2](templates/character-asset-board-template-v2.md)
- [场景资产板固定模板 V1](templates/scene-asset-board-template-v1.md)
- [道具资产板固定模板 V1](templates/prop-asset-board-template-v1.md)
- [故事板固定模板 V1](templates/storyboard-asset-board-template-v1.md)
- [复刻重构总控提示词 V1](templates/remake-master-agent-prompt-v1.md)
- [Seedance 明确引用模板 V1](templates/seedance-reference-prompt-template-v1.md)
- [Markdown 交接模板](templates/handoff-template.md)
- [JSON 交接模板](templates/handoff-template.json)
- [JSON Schema](schemas/handoff.schema.json)
- [QA Checklist](checklists/qa-checklist.md)

所有复刻任务必须先完成用户需求收集：确认要复刻镜头节奏、运镜、剧情、角色、场景、风格、台词/旁白、音效、特效、剪辑中的哪些层。用户未确认复刻范围时，只做 DNA 分析，不直接进入资产、故事板或 Seedance 生产。

所有复刻任务还必须先通过 `DNA_SIGNOFF`。15 秒以内片段要逐帧/逐变化拆解，并显式检查主角变身、道具机制、法术升级、群体反应和终帧前态；0.5 秒接触表只能辅助导航，不能替代 DNA 证据。没有通过 [DNA 取证审核系统](docs/dna-forensic-audit-system.md)，不得进入资产、故事板或 Seedance。

如果用户准备了自己的角色、场景、道具、产品或素材包，系统必须进入 `REFERENCE_PLUS_USER_ASSETS` 分支。用户资产是主资产来源，参考片资产只提供镜头功能、出场方法、构图关系、动作节奏和运镜方法。资产板要基于用户素材做 `Visible / Inferred / Missing` 摄取和保守补全，不得用参考片角色、场景或道具覆盖用户资产身份。

所有故事板类 Image2 提示词必须使用 `WHITE_STORYBOARD_SHEET_TEMPLATE`。故事板必须包含 10 个固定段落：`[PROJECT CARD]`、`[CONTINUITY HEADER]`、`[SUBJECTS]`、`[SCENE]`、`[STORYBOARD FORMAT]`、`[VISUAL LANGUAGE]`、`[ACTION DNA]`、`[SHOT DESIGN RULES]`、`[PANEL BEAT MAP]`、`[NEGATIVE]`。故事板格数必须等于参考片镜头数；超过 10 镜必须拆成多个故事板。每格 beat 必须写清 `SH## / timecode / 景别 / 运镜 / 动作 / active assets`。

Seedance 2.0 后期交付分三条支线：A 线为资产直出 Seedance，不上传故事板，优先保护用户指定角色、场景和道具；B 线为黑白手稿故事板参考 Seedance，只在切镜和构图控制优先且故事板通过身份审核时使用；C 线为无资产文本直出 Seedance，适用于用户没有资产、也没有要求资产/故事板、只要一条 Seedance 2.0 提示词的快速复刻或重构。A/B 线必须使用明确引用写法，例如 `参考 A01 / M03 FACE CLOSE-UP 锁定角色脸部`、`参考 A02 / V04 CAMERA A 锁定场景机位`、`参考 A03 / P06 HAND LOGIC 锁定道具持握`；C 线没有资产引用，必须用短而稳定的文本锚点锁角色、场景、道具和风格。15 秒以内短片必须写成一条完整连续视频，逐镜 timing 只是片内切点，不是拆成多条视频。

三支线全局方法见 [复刻重构三支线全局规则](docs/global-three-branch-remake-system.md)。A 线遵循“身份资产 -> 环境资产 -> 道具/机制资产 -> 执行态资产 -> 最终 payoff 资产”的资产职责隔离模型；B 线只把干净黑白故事板作为镜头顺序、构图、动作方向和切点节奏控制；C 线为无资产纯文本直出，使用紧凑因果锁而不是资产或故事板引用。若单条 12-15 秒生成无法同时保住快节奏和复杂状态，系统应主动建议拆段生成再剪。

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

复刻任务会额外输出 `shot_count_estimate`、切点证据、镜头连贯性说明和故事板布局计划。15 秒以内的片段必须确认真实镜头数量；如果一个 12 秒片段有 8 个镜头，故事板和 Seedance 就按 8 镜头写，而不是压成 4 个宏观段落。

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

所有场景类 Image2 资产提示词必须使用 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`，模板见 [templates/scene-asset-board-template-v1.md](templates/scene-asset-board-template-v1.md)。场景板必须有可见 stable 标签：`V01`-`V09`、`MAP`、`ENTRANCE`、`EXIT`、`CAM_A`、`CAM_B`、`CAM_C`、`CHAR_ZONE`、`PROP_ANCHOR`、`LIGHT_DIR`、`NO_DRIFT`。

所有道具类 Image2 资产提示词必须使用 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`，模板见 [templates/prop-asset-board-template-v1.md](templates/prop-asset-board-template-v1.md)。道具板必须有可见 stable 标签：`P01`-`P08`、`REFERENCE USE`、`@PROP_CODE`、`HAND`、`SCENE_ANCHOR`、`DO_NOT_CHANGE`。

用户自带资产必须先出用户资产板：

```text
Source Asset ID：用户素材编号或文件名
Media DNA：真人摄影 / 二次元 / CG / 插画 / 产品摄影 / 真实场景 / 混合媒介
Visible：原图可见且必须保留
Inferred：可保守补全
Missing：缺失或需要确认
Remake Function：替代参考片里的哪个资产功能
Module Reference Plan：后续 Seedance 引用 A01/M03、A02/V04、A03/P06 等模块
```

角色图补 M01-M08，场景图补 V01-V09 和 MAP，道具图补 P01-P08。用户资产与参考片镜头方法冲突时，优先保护用户资产身份，再调整镜头调度。

所有故事板类 Image2 提示词必须使用 `WHITE_STORYBOARD_SHEET_TEMPLATE`，模板见 [templates/storyboard-asset-board-template-v1.md](templates/storyboard-asset-board-template-v1.md)。故事板必须根据参考片真实镜头数动态布局：1-4 镜使用 1x4 或 4x1，5-6 镜使用 3x2，7-8 镜使用 4x2，9-10 镜使用 5x2，超过 10 镜拆成多个故事板。故事板仍必须包含 10 个固定段落：`[PROJECT CARD]`、`[CONTINUITY HEADER]`、`[SUBJECTS]`、`[SCENE]`、`[STORYBOARD FORMAT]`、`[VISUAL LANGUAGE]`、`[ACTION DNA]`、`[SHOT DESIGN RULES]`、`[PANEL BEAT MAP]`、`[NEGATIVE]`。如果故事板包含箭头、框线、标签、编号或说明文字，必须另出 `S##_CLEAN_BW_STORYBOARD` 黑白手稿故事板供 Seedance 使用。

这些资产板标签是生产引用标签，不属于随机画面文字。Seedance 提示词应按这些标签引用资产局部，例如 `use @图片2 V04 CAMERA A`、`use @图片3 P06 HAND LOGIC`。

Seedance 2.0 提示词必须使用 `SEEDANCE_EXPLICIT_REFERENCE_TEMPLATE`，模板见 [templates/seedance-reference-prompt-template-v1.md](templates/seedance-reference-prompt-template-v1.md)。每条提示词必须包含资产引用表、干净控制帧引用或纯文字故事板转译、逐镜 timing、镜头连贯性、后期音效点、Do Not Copy 和 Negative Prompt。

### 6. 大师级双层架构风格锁标准 (Master Decoupled Style Lock Standard)

为了实现画面画质控制的绝对稳定，系统已全面引入**双层风格锁架构（Decoupled Style Lock Architecture）**，在所有 `image2` 提示词中强制解耦：
- **不变常量（超高清画质渲染控制）**：固定拼接 `平滑阴影、柔光处理、细节控制、纹理简约、高清晰度、边缘精致、渐变平滑、无噪点、无颗粒感、无人工痕迹、无高频细节、无脏乱纹理、无过度锐化、无斑驳、无杂乱细节`，以强力杜绝 AI 生成中常见的杂色、噪点与过度锐化硬伤。
- **Image2 去除过拟合噪点提示词（鲤鱼老师）**：中文风格锁追加 `干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节`。英文风格锁追加 `clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.`
- **变化变量（触觉与风格特征）**：随资产类型、媒介风格、角色身份、场景空间、道具材质和剧情动作自适应编译物理特性。不能把同一条风格锁机械复制到所有资产上；必须先替换变量，再拼接不变量。
  1. **真人电影写实 (Cinematic Realism)**：商业摄影/影视人像 + 自然柔和光影 + 真实但克制的皮肤质感 + 物理硬材质与衣物粗糙度。
  2. **日式动漫 / 二次元 (Anime / 2D)**：干净手绘平涂 + 扁平大色块背景 + 线条清晰描绘。
  3. **美式卡通 / 三维风格化 (Cartoon / 3D Stylized)**：三维黏土树脂潮玩 + 哑光塑料肌理 + 糖果配色。
  4. **超现实主义 (Surrealism / Dreamcore)**：重力悬浮与时空扭曲 + 渐变光泽 + 梦境色谱天幕。

真人人像额外执行“减法锁”：GPT-image2 真人资产优先使用 `人物主体 + 气质/姿态 + 风格锚点 + 光影质感 + 真实但克制的皮肤质感`。禁止默认堆叠 `ultra realistic`、`photorealistic`、`highly detailed`、`8k`、`masterpiece`、`best quality`、`sharp focus`、`film grain`、`Kodak Portra`、`85mm f/1.2`、`skin pores`、`subsurface scattering` 等词。真人资产提示词应先短、准、统一，再按问题单点加词；详细规则见 [docs/image2-live-action-portrait-overfit-control.md](docs/image2-live-action-portrait-overfit-control.md)。

风格锁编译公式：

```text
角色风格锁 = 媒介变量 + 角色身体/身份变量 + 服化道材质变量 + 场景光变量 + 抗错风格排斥变量 + Image2 抗过拟合不变量
场景风格锁 = 媒介变量 + 空间类型变量 + 建筑/地貌材质变量 + 天气/时间/光源变量 + 可拍区域变量 + Image2 抗过拟合不变量
道具风格锁 = 媒介变量 + 道具身份变量 + 主材质变量 + 使用/持握变量 + 状态变化变量 + 场景锚点光变量 + Image2 抗过拟合不变量
故事板风格包 = 媒介变量 + 预演绘制方式变量 + 镜头节奏变量 + 动作线/运动箭头变量 + 场景可读变量 + 角色剪影变量 + Image2 抗过拟合不变量；如果要进入 Seedance，还必须另编译无箭头、无标签、无框线、无文字的干净控制帧风格包
```

例如，同样使用抗过拟合不变量，古战场真人角色要写商业影视人像、克制真实肤感、湿发、氧化青铜、泥水和冷灰天光；二次元校园角色要写手绘平涂、发丝分组、校服布料和窗光；三维卡通机器人要写亚光塑料、软橡胶、圆润关节和糖果色棚拍光；超现实神祇要写半透明薄纱、发光矿物皮肤、漂浮衣摆和梦境渐变天幕。

### 7. Seedance 2.0 逐镜节奏协议

对于下游视频模型提示词，优先按参考片真实镜头数、切点和运镜逻辑写 Seedance。比如 12 秒片段如果有 8 个镜头，就写成 `SH01-SH08` 的逐镜 timing、角色/场景/道具锚点和镜头连贯性；如果 15 秒片段有 10 个镜头，就写成 `SH01-SH10`。这些逐镜不是分开生成，而是一条连续成片中的片内剪辑节奏。

只有当用户没有要求镜头节奏复刻，或参考片没有可用镜头证据时，才使用 12 秒四阶兜底协议：

- `0:00-0:03`：大景慢前推，建立空间和规则。
- `0:03-0:06`：手部/眼部/道具特写，触发动作或信息。
- `0:06-0:09`：中景/中近景推进主体动作或变化。
- `0:09-0:12`：宽景或中近景终帧，最后 0.8 秒稳定锁帧。

不管使用逐镜协议还是四阶兜底协议，都必须禁止字幕、水印、乱码、故事板边框和随机文字进入画面。A/B 线必须明确引用资产图号和模块标签；C 线没有资产图时必须用稳定文本锚点替代资产引用。参考片文字若承担台词、咒语或旁白功能，只重写为新片原创声音/表演节奏，不做画面字幕。

### 8. 校验脚本和 QA 门禁

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

仓库级健康检查脚本：

```bash
python3 scripts/check_project.py
```

它会检查：

- 必需文档、模板、schema 和脚本是否存在
- Markdown 本地链接是否失效
- `templates/handoff-template.json` 是否通过交接校验
- 如果本地存在 `outputs/`，同步校验其中所有 `*handoff*.json`

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
│   ├── remake-reconstruction-protocol.md
│   └── video-analysis-module.md
├── schemas/
│   └── handoff.schema.json
├── scripts/
│   ├── check_project.py
│   └── validate_handoff.py
└── templates/
    ├── character-asset-board-template-v2.md
    ├── prop-asset-board-template-v1.md
    ├── remake-master-agent-prompt-v1.md
    ├── scene-asset-board-template-v1.md
    ├── seedance-reference-prompt-template-v1.md
    ├── storyboard-asset-board-template-v1.md
    ├── handoff-template.json
    └── handoff-template.md
```

`outputs/` 用于本地样例产物和真实项目交付包，默认被 `.gitignore` 忽略。需要发布样例时，建议先脱敏并只提交精选的 Markdown / JSON / contact sheet。

## 迭代维护约定

后续每次优化这套系统时，必须同步更新：

- README：更新版本、能力说明、Quick Start 或使用边界。
- CHANGELOG：记录本次变更原因、影响模块和校验结果。
- SOP / Agent Cards：如果工作流或角色职责变化，必须同步。
- Templates / Schema / Validator：如果交接字段变化，三者必须一起改。
- Asset Board Templates：如果角色、场景或道具资产板版式优化，必须同步模板、SOP、README 和既有提示词包。
- QA Checklist：如果新增风险、字段或后端约束，必须同步检查项。
- Project Check：每次发布前运行 `python3 scripts/check_project.py`，确保文档链接、handoff 模板和本地样例交付包没有断裂。

这条规则是为了保证后期持续迭代时，文档、接口和校验器不会各说各话。
