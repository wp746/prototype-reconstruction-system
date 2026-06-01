# Prop Asset Board Template V1

Template code: `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`

This is the default prop asset board template for all `PROP_*` Image2 + Seedance 2.0 production packages. Its goal is not to make a product poster. Its goal is to lock prop identity, hand logic, scale, scripted state changes, and reference labels for later Seedance prompts.

## Label Contract

Prop boards must contain clear visible labels. These labels are part of the asset board and are intentionally rendered.

- Top title must include: `A[NUMBER] / PROP_CODE / PROP NAME`.
- Every module must have a large stable label: `P01` to `P08`.
- Bottom strip must include: `REFERENCE USE`, `@PROP_CODE`, `HAND`, `SCENE_ANCHOR`, `DO_NOT_CHANGE`.
- Chinese board uses Chinese short labels plus stable codes.
- English board uses English short labels plus stable codes.
- Labels must be large enough to read. No tiny paragraphs, no random text, no decorative typography.

## Fixed Layout

- Canvas: 16:9 landscape, recommended `3840x2160`.
- Background: white or near-white, `#FFFFFF` / `#F8F8F4`.
- Dividers: thin black `#111111`, subtle gray guides `#C8C8C8`.
- Typography: bold sans-serif.
- One plot-critical hero prop per board by default.
- Multi-prop boards are allowed only for secondary props, and each prop must still have a clear code.

## Required Modules

| Label | Module | Required Content |
|---|---|---|
| `P01` | Hero View | largest clean main view |
| `P02` | Front / Side | front and side views |
| `P03` | Back / Top / 3Q | back, top, or 3/4 construction view |
| `P04` | Material Detail | material, wear, edge, texture, markings |
| `P05` | Scale | hand/body/common-object scale |
| `P06` | Hand Logic | left/right hand, grip, finger position, use posture |
| `P07` | State Change | clean/damaged/open/closed/on/off/charged/discharged if scripted |
| `P08` | Scene Anchor | where it sits, where it appears, which scene and character use it |
| `REFERENCE USE` | Reference Strip | exact @ reference duty for later prompts |

## Text/UI Props

If exact readable text is needed:

- isolate it in a large single module;
- keep it short;
- prefer one text state per board;
- do not hide critical text in scene or storyboard boards.

## Prop Style Lock Compiler

道具风格锁必须根据道具功能、材质、尺度和使用方式重新编译变量，不能照搬角色或场景风格锁。

固定公式：

```text
道具风格锁 = 媒介变量 + 道具身份变量 + 主材质变量 + 使用/持握变量 + 状态变化变量 + 场景锚点光变量 + 抗错风格排斥变量 + Image2 抗过拟合不变量
```

变量写法示例：

- 真人电影写实青铜戒：氧化青铜、手汗磨损、细划痕、真实手指比例、冷灰反光。
- 二次元魔法书：干净手绘平涂封面、清晰厚书脊、简化金属包角、可控发光页边，不生成乱码文字。
- 三维卡通玩具车：亚光塑料、圆润轮廓、橡胶轮胎、糖果色棚拍反射。
- 超现实水晶钥匙：半透明晶体、内部发光裂纹、反重力碎片、梦境色散。

中文固定抗噪不变量：`干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节`。

English constants: `clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.`

## Chinese Universal Prompt

```text
请生成一张 16:9 横向白底道具资产板，顶部第一行大标题必须是：A[编号] / [PROP_CODE] / [中文道具名]道具资产板。标题最大、左对齐、高对比。整体使用固定“主道具大图 + 多视图结构 + 材质细节 + 手部尺度 + 状态变化 + 场景锚点 + 引用标签条”的白底道具资产模板，不是产品海报，不是故事板，不是剧照。背景#FFFFFF或#F8F8F4，细黑分割线#111111，灰色辅助线#C8C8C8，标签黑色，固定粗体无衬线字体。画板内必须有清晰可读的模块标签：P01主图、P02正侧、P03背面/顶面/三分之二、P04材质、P05尺度、P06持握、P07状态、P08场景锚点、REFERENCE USE、@PROP_CODE、HAND、SCENE_ANCHOR、DO_NOT_CHANGE。除 A编号、PROP_CODE、P编号和@引用码外，中文板只使用中文短标签。禁止小字长段落、乱码文字、字幕、水印、logo、品牌字、随机装饰文字。

固定版式：
顶部 5-7% 是标题栏。
左侧 32-36% 宽、70-76% 高是 P01 / 主图：最大、最干净的道具身份源。
中上 34-38% 宽是 P02 / 正侧 和 P03 / 背面/顶面/三分之二：多角度结构视图。
右上 24-28% 宽是 P04 / 材质：边缘、磨损、纹理、发光或文字局部。
中下是 P05 / 尺度 和 P06 / 持握：相对手部/身体比例、左右手、手指位置、使用姿态。
右下是 P07 / 状态 和 P08 / 场景锚点：剧情状态变化、所在场景、角色使用关系、摆放位置。
底部通栏是 REFERENCE USE / 引用标签条，写明 @PROP_CODE 在后续 Seedance 中引用什么，不要写长段落。

道具代码：[PROP_CODE]。
道具设定：[道具身份、剧情功能、使用者、所在场景、材质、尺寸、状态变化]。
身份锚点：[形状、颜色、材质、纹理、发光、磨损、边缘、可读文字或无文字规则]。

P01 / 主图：[最大主视图]
P02 / 正侧：[正面和侧面结构]
P03 / 背面/顶面/三分之二：[背面、顶面或3/4结构]
P04 / 材质：[材质、磨损、纹理、发光、边缘细节]
P05 / 尺度：[与手、身体或场景物体的比例]
P06 / 持握：[左/右手、手指、抓握点、使用姿态]
P07 / 状态：[剧情中需要的状态变化；没有状态变化则写稳定状态]
P08 / 场景锚点：[出现在哪个SCENE、靠近哪个CHAR、摆放或运动锚点]
REFERENCE USE：[例如 @PROP_CODE = 形状、材质、持握方式、状态变化和场景锚点]

风格锁：[根据道具与风格类型选取并填入标准双层架构风格锁，锁定不变画质控制量与变化变量参数，如：真人电影写实风格锁。必须追加 Image2 去除过拟合噪点提示词：干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。]

硬规则：重要道具一张图只做一个PROP；多道具板只用于次要道具且每个道具必须有大号PROP编号；同一道具在所有视图中形状、比例、材质、颜色和可读文字规则不能漂移。
```

## English Universal Prompt

```text
Create a 16:9 horizontal white-background prop asset board. The first visible top title must be exactly: A[NUMBER] / [PROP_CODE] / [PROP NAME] PROP ASSET BOARD. The title must be largest, left-aligned, high contrast. Use the fixed white "large hero prop + multi-view construction + material detail + hand scale + state change + scene anchor + reference strip" prop asset template. This is not a product poster, not a storyboard, and not a movie still. Background #FFFFFF or #F8F8F4, thin black divider lines #111111, subtle gray guide lines #C8C8C8, black labels, fixed bold sans-serif typography. The board must contain clear readable module labels: P01 HERO, P02 FRONT/SIDE, P03 BACK/TOP/3Q, P04 MATERIAL, P05 SCALE, P06 HAND LOGIC, P07 STATE, P08 SCENE ANCHOR, REFERENCE USE, @PROP_CODE, HAND, SCENE_ANCHOR, DO_NOT_CHANGE. Use English short labels only. No tiny paragraphs, corrupted text, subtitles, watermarks, logos, brand text, or random decorative words.

Fixed layout:
Top 5-7% is the title bar.
Left 32-36% width and 70-76% height is P01 / HERO: largest clean prop identity source.
Upper center 34-38% width is P02 / FRONT-SIDE and P03 / BACK-TOP-3Q: multi-angle construction views.
Upper right 24-28% width is P04 / MATERIAL: edge, wear, texture, glow, or readable-text detail.
Lower center is P05 / SCALE and P06 / HAND LOGIC: hand/body ratio, left/right hand, finger position, use posture.
Lower right is P07 / STATE and P08 / SCENE ANCHOR: scripted state changes, scene, character relationship, placement.
Bottom strip is REFERENCE USE: exact @ reference duty for later Seedance prompts, no long paragraphs.

Prop code: [PROP_CODE].
Prop: [identity, story function, user, scene, material, size, state change].
Identity anchors: [shape, color, material, texture, glow, wear, edge, readable text or no-text rule].

P01 / HERO: [largest main view]
P02 / FRONT-SIDE: [front and side construction]
P03 / BACK-TOP-3Q: [back, top, or 3/4 construction]
P04 / MATERIAL: [material, wear, texture, glow, edge detail]
P05 / SCALE: [ratio to hand, body, or scene object]
P06 / HAND LOGIC: [left/right hand, fingers, grip point, use posture]
P07 / STATE: [scripted state change; if none, write stable state]
P08 / SCENE ANCHOR: [which SCENE, which CHAR, placement or motion anchor]
REFERENCE USE: [example: @PROP_CODE = shape, material, grip logic, state change, and scene anchor]

Style lock: [Select and fill standard decoupled style lock matching the art style and prop, locking rendering constants and style variables. Must append Image2 overfitting-noise removal prompt: clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.]

Hard rule: one important hero prop per board. Multi-prop boards are only for secondary props, and every prop must have a large visible PROP code. The same prop must not drift in shape, scale, material, color, or readable-text rule across views.
```
