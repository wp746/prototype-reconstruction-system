# 原型重构多智能体工作流 SOP

## 1. 系统定位

原型重构系统用于把一个参考短片反推为可迁移的 AIGC 生产方法。用户输入参考片链接或本地视频，并给出新主题、新风格、目标画幅和目标平台；系统逐剧情、逐角色、逐风格、逐道具、逐台词功能、逐构图、逐运镜、逐特效、逐音效、逐节奏拆解参考片，再输出给 `Image2 + Seedance 2.0` 后端的生产交接包。

默认复刻边界是“方法复刻”：

- 保留：镜头语法、景别推进、构图逻辑、运镜路径、剪辑节奏、声音节奏、情绪曲线、角色或产品出场方法。
- 替换：原片人物身份和脸、服装造型、品牌商标、原台词、原字幕、原音乐、可识别场景、IP 符号和具体剧情设定。

## 2. 输入与输出

### 输入

- 参考片：公开视频链接或本地视频文件。
- 新片 brief：新主题、目标风格、受众、平台、画幅、目标时长。
- 可选资产：已有角色图、场景图、产品图、品牌规范、音乐或声音方向。
- 复刻强度：默认 `method_remake`，只复刻方法，不复制可识别表达。

### 输出

- Markdown 人审版：用于导演、制片、客户或内部团队审核。
- JSON 机器版：用于后端解析并生成 Image2 / Seedance 提示词。

最终前端交付不是 Seedance 完整提示词，而是足够明确的生产交接包。后端不需要重新做创意判断，只需要执行资产、分镜和视频提示词生产。

角色类 Image2 资产提示词必须使用 `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`，固定模板见 [templates/character-asset-board-template-v2.md](../templates/character-asset-board-template-v2.md)。后端或提示词工厂不得再输出松散拼贴式角色板、半身视图条或缺脚的转面图。

场景类 Image2 资产提示词必须使用 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`，固定模板见 [templates/scene-asset-board-template-v1.md](../templates/scene-asset-board-template-v1.md)。道具类 Image2 资产提示词必须使用 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`，固定模板见 [templates/prop-asset-board-template-v1.md](../templates/prop-asset-board-template-v1.md)。场景和道具资产板必须显示稳定标签，供 Seedance 2.0 后续按剧情引用局部资产。

## 3. 主流程

### P0 Remake Requirement Intake

A0 在分析和生产前必须先做需求收集。详细规则见 [remake-reconstruction-protocol.md](remake-reconstruction-protocol.md)。

必须询问用户要复刻或重构哪些部分，可多选：

- 镜头数量、切点、景别推进和剪辑节奏
- 运镜语言和镜头速度曲线
- 剧情结构和信息释放顺序
- 角色出场方式和动作语言
- 场景空间调度和视觉压力
- 光影、色彩、材质和整体风格
- 台词/旁白功能
- 音效、静默和声音节奏
- 特效触发逻辑和画面功能
- 全部方法层复刻

同时确认变量范围：新主题、新角色、新场景、新道具、新台词、新风格、新画幅、新时长和新平台。

如果用户提供自己的角色图、场景图、道具图、产品图或素材包，A0 必须标记为 `REFERENCE_PLUS_USER_ASSETS`，并确认：

- 用户资产类型：角色、场景、道具、产品或混合资产。
- 用户资产用途：替换参考片主角、配角、场景、道具、产品、特效核心物或风格来源。
- 用户资产保护级别：一比一保留、允许保守补全、允许风格化改写。
- 用户资产缺失视角：正面、侧面、背面、表情、手部、材质、尺度、场景地图、道具持握和状态变化。

通过标准：用户已明确复刻范围和变化范围；如果用户只给参考片但未说明目标，系统只进入 DNA 分析，不直接生成资产、故事板或 Seedance 提示词。

### P1 Reference Intake

A1 接收参考片和新片 brief，生成 `source_lock`：

- 来源类型：`video_link` 或 `local_video`。
- 权限与复用边界。
- 禁止复制项：原台词、音乐、logo、人物脸、IP 符号、可识别场景。
- 目标平台、画幅、时长、模型后端。

通过标准：来源、目标和复用边界明确；无法访问的视频必须要求补充文件、截图序列或人工描述。

### P2 Video Analysis and Segmentation

A2 先运行视频分析模块，再把参考片拆成段落和镜头。详细规则见 [video-analysis-module.md](video-analysis-module.md)。

视频分析必须先输出：

- `media_probe`：时长、分辨率、fps、codec、音频状态、画幅和分析模式。
- `frame_sampling_plan`：抽帧策略、帧数、时间点和采样理由。
- `frame_observations`：单帧画面观察。
- `audio_transcript`：带 timecode 的对白、旁白、声音事件。
- `audio_segments`：由文本和声音节奏生成的逻辑段落。
- `multimodal_sync`：视觉事件、音频事件、剪辑信号和叙事功能的对齐表。

A2 再把参考片拆成段落和镜头：

- 先按叙事段落：Opening Hook、Setup、Development、Turning Point、Payoff、Ending Image。
- 再按镜头输出 `shot_id`、`timecode`、`duration`。

通过标准：每个镜头有唯一 ID、起止时间和时长；每个镜头至少被抽帧、视觉变化、运镜起止或音频节拍中的一种证据支持；没有视频分析证据不得进入下一步。

### P3 Shot-by-Shot Deconstruction

A3-A6 逐镜拆解：

- 剧情：每镜改变了观众什么认知，承担开场、设定、发展、转折、爆点还是收束。
- 单帧观察：主体、环境、景别、角度、构图、光影、色彩、风格、情绪、可见文字/logo。
- 序列观察：帧间变化、运动轨迹、镜头起止、视觉突变、节奏速度。
- 剧情功能：这一镜改变了观众什么认知。
- 景别角度：景别、垂直角度、水平角度。
- 构图：主体位置、前后景、视觉引导线、负空间、安全区。
- 运镜：推拉摇移跟、手持、锁定、旋转、升降、速度曲线。
- 表演调度：人物站位、视线、动作、道具接触点。
- 台词/旁白：只拆功能，不复写原句。
- 美术风格：场景、服装、道具、材质、光影、色彩。
- VFX：特效类型、触发点、与实拍画面的关系。
- 声音：音乐、环境声、音效、静默、对白功能。
- 剪辑：入点、出点、动作剪辑、声音剪辑、情绪剪辑。
- 节奏：镜头时长分布、快切位置、停顿位置、终帧锁定位置。

通过标准：每一镜都解释“为什么放在这里”，不能只写高级、电影感、节奏好。

### P4 Preservation / Variation Map

A7 把参考片拆成保留层和变化层。

保留层只能是方法：

- Shot size progression
- Camera height and movement direction
- Composition logic
- Blocking logic
- Edit rhythm
- Sound rhythm
- Emotional arc
- Lighting motivation
- Reveal structure

变化层必须替换：

- 原片角色身份、脸、服装造型
- 品牌、商标、包装、广告语
- 原台词、字幕、片名、文案
- 可识别 IP、场景、道具
- 原创音乐、声音素材

通过标准：每个可识别元素都必须有替换方案和风险说明。

### P5 New Production Mapping

A8 把参考片方法映射为新片：

- 每个参考镜头对应一个新片镜头或 Seedance 分段。
- 每个新片镜头绑定新角色、新场景、新道具、新声音策略。
- 参考台词只转为“台词功能”，再生成新台词方向。
- 如果参考片是动画而新片是写实，必须迁移材质、表演和摄影逻辑，而不是保留动画造型。
- 如果用户选择 `shot_rhythm` 或 `camera_language`，新片镜头数量、切点顺序和运镜逻辑必须对齐参考片，除非用户明确要求改节奏。
- 如果参考片镜头数不超过 10，故事板必须一格对应一镜；如果超过 10，按每板最多 10 镜拆成 `S01`、`S02`。
- 如果用户提供自带资产，新片映射必须优先绑定用户资产：参考片只提供镜头功能和动作位置，用户资产保留脸、体型、服装、场景地理、道具形状、媒介风格和材质。

通过标准：后端能从映射表直接知道每段要生成什么，不需要补创意。

### P5A User Asset Ingestion

当项目类型为 `REFERENCE_PLUS_USER_ASSETS` 时，P5 后必须插入 P5A，先做用户资产摄取，再进入故事板和 Seedance。

A5 负责把用户提供的资产转成可复刻生产用资产板：

- 角色图：补成 `A##_USER_CHAR` 角色资产板，包含 M01-M08；可见脸、体型、发型、服装和媒介风格必须保留。
- 场景图：补成 `A##_USER_SCENE` 场景九视角板，包含 V01-V09 和 MAP；原空间地理、建筑轮廓、光线方向必须保留。
- 道具图：补成 `A##_USER_PROP` 道具资产板，包含 P01-P08；原形状、材质、比例、使用方式必须保留。

每个用户资产必须输出：

- `source_asset_id`：用户素材编号或文件名。
- `asset_type`：character / scene / prop / product / mixed。
- `media_dna`：live-action photoreal / anime / CG/3D / illustration / product photography / real scene / mixed。
- `visible_lock`：原图可见且必须保留。
- `inferred_fill`：可保守补全。
- `missing_or_confirm`：缺失或需要用户确认。
- `remake_function`：替代参考片里的哪个资产功能。
- `module_reference_plan`：后续 Seedance 引用的模块，例如 `A01/M03`、`A02/V04`、`A03/P06`。

通过标准：用户资产没有被参考片资产覆盖；缺失视角已补全或标记确认；每个用户资产都能被故事板和 Seedance 按模块引用。

### P6 Human Approval Gates

默认有 4 个确认点：

- Gate 1：参考片拆解完成，确认镜头与节奏理解准确。
- Gate 2：保留/变化边界完成，确认没有复制风险。
- Gate 3：新主题、新角色、新风格、新资产完成，确认创意方向。
- Gate 4：最终 Markdown + JSON 交接包完成，确认交给后端。

任一 Gate 被退回，只修改受影响模块，并重新跑 A9 和 A11。

### P7 Compliance and Risk Gate

A9 拦截以下风险：

- 明星、网红、真实个人肖像复刻。
- 品牌 logo、包装、商标和广告语复刻。
- 原台词、字幕、片名、文案复刻。
- 原音乐、音效素材复刻。
- 可识别 IP 角色、服装、武器、场景复刻。
- 与原片过度相似的关键构图或结尾画面。

通过标准：所有风险都有 `risk_level`、`replace_with` 和 `prompt_rule`。

### P8 Backend Handoff

A10 输出两份交接物：

- Markdown：给人审核，保留表格、注释和导演判断。
- JSON：给后端解析，字段必须符合 [schemas/handoff.schema.json](../schemas/handoff.schema.json)。

如果输出 Seedance 2.0 提示词，必须写清：

- 参考哪个资产图编号：例如 `A01`、`A02`、`A03`。
- 锁定哪个模块标签：例如 `A01 / M03 FACE CLOSE-UP`、`A02 / V04 CAMERA A`、`A03 / P06 HAND LOGIC`。
- 选择哪条 Seedance 交付支线：A 线资产直出，或 B 线黑白手稿故事板参考。
- A 线不上传故事板，直接用资产图和 SH01-SH[N] 文字 timing 控制成片。
- B 线使用哪个黑白手稿故事板：例如 `S01_CLEAN_BW_STORYBOARD / 4x2`。带箭头、框线、标签、编号或说明文字的 `S01_ANNOTATED_STORYBOARD` 只供导演审片，不得作为 Seedance 图片输入。
- B 线明确要求：将提供的黑白手稿故事板制作成流畅电影级动画视频，保持镜头顺序、切点节奏、构图重心、动作方向和镜头连贯性；角色身份、服装、道具和场景以资产图为准。

后端指令固定为：

```json
{
  "target_pipeline": "image2_seedance_2_0",
  "handoff_mode": "asset_storyboard_seedance_prompt_factory"
}
```

### P9 QA

A11 检查：

- 媒体探测、抽帧计划、帧观察、音频转写和多模态对齐存在。
- 抽帧覆盖关键视觉变化、音频分段边界和关键动作前后状态。
- 每个镜头有完整拆解字段。
- 每个新片镜头有资产绑定。
- 每个 Seedance segment 为 4-15 秒。
- 精确文字和 UI 进入 `UI_TEXT_*` 或 post duties。
- 风格参考不会覆盖角色身份、场景地理和剧情事实。
- 所有风险被替换或降级。

通过标准：QA 清单全通过，JSON 校验脚本无 error。

## 4. 竖屏迁移规则

横屏参考片迁移到 9:16 时：

- 宽构图改为纵深构图。
- 横向多人关系改为前后景、过肩、反打。
- 横向运动改为靠近、远离、纵深跟随。
- 大场景使用门框、窗户、走廊、高楼、楼梯等竖向引导线。
- 角色脸、产品、关键道具必须位于竖屏中心安全区。

## 5. 后端职责边界

前端交接包必须明确：

- `asset_matrix`：角色、场景、道具、UI/text、style-safe look。
- `scene_geography`：空间锚点、入口出口、光源和可拍区域。
- `segment_plan`：每个 Seedance 单元的 in state、action、out state。
- `sound_post_duties`：字幕、标题、UI、音乐、音效、VFX、调色和剪辑。

后端负责：

- Image2 asset prompt
- Image2 storyboard/control-board prompt
- Seedance 2.0 prompt
- 生成评分
- 修复提示词
- 后期执行清单

## 6. 角色资产板生成规则

所有 `CHAR_*` 角色资产板必须套用 `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`：

- 16:9 横向白底或近白底。
- 顶部 5-7% 为标题栏。
- 左侧 26-30% 宽、70-76% 高为 `M01 / 主全身`，必须是一张超大正面全身，头顶到鞋底完整可见。
- 顶部中间 44-48% 宽、34-40% 高为 `M02 / 全身转面`，必须分成 4 个等宽竖列：左侧面、三分之二、右侧面、背面。
- `M02` 每列都必须是完整全身体，脚、鞋、裤脚、衣摆、包带和背部轮廓必须完整出现。
- 右上为 `M03 / 脸部特写`，下方为 `M04 / 表情库`。
- 中下为 `M05 / 动作手部道具`，右下为 `M06 / 服装材质细节`。
- 底部为 `M07 / 色卡` 和 `M08 / 连续性标签`。

角色资产板禁止：

- 半身图、胸像、腰部裁切、只画头肩、只画上半身。
- 纸纹、牛皮纸、报纸、油纸、羊皮纸、拼贴、暗色海报背景。
- 小字段落、随机字体、乱码文字、字幕、水印、logo。
- 把禁止项、红叉、反例图或品牌反例作为画面模块展示。

中文角色资产板只使用中文短标签，除 A 编号和角色代码外不要出现英文；英文角色资产板只使用英文短标签，不渲染中文标签。

## 7. 场景资产板生成规则

所有 `SCENE_*` 场景资产板必须套用 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`：

- 16:9 横向白底或近白底。
- 顶部 5-7% 为标题栏，必须显示 `A[编号] / SCENE_CODE / 场景名`。
- 中部为 3x3 九视角网格，每格左上角必须有大号稳定标签。
- 必须包含 `V01 建立`、`V02 入口`、`V03 出口/反向`、`V04 机位A`、`V05 机位B`、`V06 机位C`、`V07 关键物`、`V08 光线`、`V09 尺度`。
- 底部必须包含 `MAP / 俯视图` 和引用标签：`ENTRANCE`、`EXIT`、`CAM_A`、`CAM_B`、`CAM_C`、`CHAR_ZONE`、`PROP_ANCHOR`、`LIGHT_DIR`、`NO_DRIFT`。
- 同一个场景板只控制一个空间，不混入无关地点。
- 场景板只使用无脸灰色人形、背影或位置标记，不生成清晰主角脸。

场景资产板标签是资产引用接口，不是随机字幕。Seedance 提示词可以按 `@图片2 V04 CAMERA A`、`@图片2 MAP PROP_ANCHOR` 引用。

## 8. 道具资产板生成规则

所有 `PROP_*` 道具资产板必须套用 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`：

- 16:9 横向白底或近白底。
- 顶部 5-7% 为标题栏，必须显示 `A[编号] / PROP_CODE / 道具名`。
- 必须包含 `P01 主图`、`P02 正侧`、`P03 背面/顶面/三分之二`、`P04 材质`、`P05 尺度`、`P06 持握`、`P07 状态`、`P08 场景锚点`。
- 底部必须包含 `REFERENCE USE`、`@PROP_CODE`、`HAND`、`SCENE_ANCHOR`、`DO_NOT_CHANGE`。
- 重要道具默认一张板只做一个 `PROP_*`；多道具板只用于次要道具，且每个道具必须有大号 `PROP_*` 编号。
- 同一道具在所有视图中形状、比例、材质、颜色和可读文字规则不能漂移。

道具资产板标签是资产引用接口，不是随机字幕。Seedance 提示词可以按 `@图片3 P06 HAND LOGIC`、`@图片3 P07 STATE`、`@图片3 REFERENCE USE` 引用。

## 9. 故事板生成规则

所有 `STORYBOARD_*` 故事板 Image2 提示词必须套用 `WHITE_STORYBOARD_SHEET_TEMPLATE`：

- 16:9 横向白底，手绘线稿风格，不是成片剧照。
- 必须包含 10 个固定段落，按顺序：`[PROJECT CARD]`、`[CONTINUITY HEADER]`、`[SUBJECTS]`、`[SCENE]`、`[STORYBOARD FORMAT]`、`[VISUAL LANGUAGE]`、`[ACTION DNA]`、`[SHOT DESIGN RULES]`、`[PANEL BEAT MAP]`、`[NEGATIVE]`。
- 风格包（Style Packet）必须写成一段完整的风格声明，不要关键词堆砌。
- `[SUBJECTS]` 中每个角色必须包含动作语言（motion language），不只是外观描述。
- `[PANEL BEAT MAP]` 每格一行：编号 + 景别 + 动作一句话。不要长描写。
- 每格都必须包含动作或动作延续。不要重复对峙格、静止格和空拍。
- 红色框线 = 镜头画框，蓝色箭头 = 运动/力量方向，绿色标签 = 资产码引用。
- 格子编号放在画面外，每格下方加短镜头标签和微小动作说明。
- 带标注故事板只用于人审；进入 Seedance 前必须另出无箭头、无框线、无标签、无编号、无说明文字、无白底故事板 UI 的干净控制帧。

故事板格数必须跟参考片镜头数和新片剧情节奏匹配：

- 1-4 镜：使用 1x4 或 4x1。
- 5-6 镜：使用 3x2。
- 7-8 镜：使用 4x2。
- 9-10 镜：使用 5x2。
- 超过 10 镜：拆成多个故事板，每板最多 10 镜。

每格必须写清：

```text
SH## / timecode / shot size / camera move / action beat / active assets
```

故事板引用资产板模块标签：

- 角色：`use @图片1 M03 FACE CLOSE-UP and M05 ACTION HAND PROP LOGIC`
- 场景：`use @图片2 V04 CAMERA A and MAP/CHAR_ZONE`
- 道具：`use @图片3 P06 HAND LOGIC and P07 STATE`
