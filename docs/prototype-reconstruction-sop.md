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

## 3. 主流程

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

- 单帧观察：主体、环境、景别、角度、构图、光影、色彩、风格、情绪、可见文字/logo。
- 序列观察：帧间变化、运动轨迹、镜头起止、视觉突变、节奏速度。
- 剧情功能：这一镜改变了观众什么认知。
- 景别角度：景别、垂直角度、水平角度。
- 构图：主体位置、前后景、视觉引导线、负空间、安全区。
- 运镜：推拉摇移跟、手持、锁定、旋转、升降、速度曲线。
- 表演调度：人物站位、视线、动作、道具接触点。
- 美术风格：场景、服装、道具、材质、光影、色彩。
- VFX：特效类型、触发点、与实拍画面的关系。
- 声音：音乐、环境声、音效、静默、对白功能。
- 剪辑：入点、出点、动作剪辑、声音剪辑、情绪剪辑。

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

通过标准：后端能从映射表直接知道每段要生成什么，不需要补创意。

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
