# Scene Asset Board Template V1

Template code: `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`

This is the default scene asset board template for all `SCENE_*` Image2 + Seedance 2.0 production packages. Its goal is not to make a landscape poster. Its goal is to make one space readable, repeatable, and referable by Seedance prompts through stable visible labels.

## Label Contract

Scene boards must contain clear visible labels. These labels are part of the asset board and are intentionally rendered.

- Top title must include: `A[NUMBER] / SCENE_CODE / SCENE NAME`.
- Every view panel must have a large stable label: `V01` to `V09`.
- Bottom map must have stable labels: `MAP`, `ENTRANCE`, `EXIT`, `CAM_A`, `CAM_B`, `CAM_C`, `CHAR_ZONE`, `PROP_ANCHOR`, `LIGHT_DIR`, `NO_DRIFT`.
- Chinese board uses Chinese short labels plus stable codes.
- English board uses English short labels plus stable codes.
- Labels must be large enough to read. No tiny paragraphs, no random text, no decorative typography.

## Fixed Layout

- Canvas: 16:9 landscape, recommended `3840x2160`.
- Background: white or near-white, `#FFFFFF` / `#F8F8F4`.
- Dividers: thin black `#111111`, subtle gray guides `#C8C8C8`.
- Typography: bold sans-serif.
- Main grid: 3x3 labeled scene views.
- Bottom strip: top-down geography/floor map and reference-use notes.

## Required Modules

| Label | Module | Required Content |
|---|---|---|
| `V01` | Establishing | full space identity and horizon/direction |
| `V02` | Entrance | main entry direction or incoming route |
| `V03` | Exit / Reverse | exit or reverse direction |
| `V04` | Camera A | primary shooting angle |
| `V05` | Camera B | reverse angle |
| `V06` | Camera C | side or diagonal angle |
| `V07` | Key Fixed Detail | fixed object, road, gate, platform, window, pillar, etc. |
| `V08` | Light / Weather | light source, shadow direction, weather state |
| `V09` | Scale / Blocking | faceless scale placeholders and action zones |
| `MAP` | Geography Plan | top-down plan with entrance/exit arrows, camera safe zones, character zones, prop anchors, light direction |

## Human Placeholder Rule

Scene boards must not create new character identities. Use only:

- faceless gray silhouettes
- backs or distant silhouettes
- labeled position markers such as `CHAR_ZONE`, `EXTRA_ZONE`

Do not render clear main-character faces in scene boards unless an integrated board is explicitly requested.

## Scene Style Lock Compiler

场景风格锁必须根据当下空间重新编译变量，不能照搬角色风格锁。

固定公式：

```text
场景风格锁 = 媒介变量 + 空间类型变量 + 建筑/地貌材质变量 + 天气/时间/光源变量 + 可拍区域变量 + 抗错风格排斥变量 + Image2 抗过拟合不变量
```

变量写法示例：

- 真人电影写实古战场：湿泥、冷灰天光、残破城墙、氧化铜锚点、烟尘和远景雾压。
- 二次元城市街道：干净平涂建筑、清晰外轮廓、柔和天空渐变、少量可读招牌区但不生成随机文字。
- 三维卡通厨房：亚光塑料厨具、圆润家具边缘、糖果色环境光、干净棚拍反射。
- 超现实梦境花园：反重力地貌、漂浮台阶、半透明植物、梦境渐变天幕。

中文固定抗噪不变量：`干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节`。

English constants: `clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.`

## Chinese Universal Prompt

```text
请生成一张 16:9 横向白底场景资产板，顶部第一行大标题必须是：A[编号] / [SCENE_CODE] / [中文场景名]场景资产板。标题最大、左对齐、高对比。整体使用固定“3x3九视角 + 底部俯视地图 + 稳定引用标签”的白底场景资产模板，不是风景海报，不是故事板，不是剧照。背景#FFFFFF或#F8F8F4，细黑分割线#111111，灰色辅助线#C8C8C8，标签黑色，固定粗体无衬线字体。画板内必须有清晰可读的模块标签：V01建立、V02入口、V03出口/反向、V04机位A、V05机位B、V06机位C、V07关键物、V08光线、V09尺度、MAP俯视图、ENTRANCE、EXIT、CAM_A、CAM_B、CAM_C、CHAR_ZONE、PROP_ANCHOR、LIGHT_DIR、NO_DRIFT。除 A编号、SCENE_CODE、V编号、CAM编号外，中文板只使用中文短标签。禁止小字长段落、乱码文字、字幕、水印、logo、品牌字、随机装饰文字。

固定版式：
顶部 5-7% 是标题栏。
中部 78-82% 是 3x3 九视角网格，每个格子左上角必须有大号标签。
底部 12-16% 是 MAP / 俯视图与引用标签条，必须标出入口、出口、摄影机安全区、人物站位区、道具锚点、光线方向和禁止漂移。

场景代码：[SCENE_CODE]。
场景设定：[空间身份、时代/风格、天气/时间、核心地貌或建筑、可拍区域]。
空间锚点：[入口、出口、主方向、前景、中景、后景、固定道具、光源方向]。

V01 / 建立：[全空间建立视角]
V02 / 入口：[入口或角色进入方向]
V03 / 出口/反向：[出口或反向视角]
V04 / 机位A：[主拍摄机位]
V05 / 机位B：[反打或逆向机位]
V06 / 机位C：[侧向或斜向机位]
V07 / 关键物：[固定关键物或空间识别物]
V08 / 光线：[光源、天气、阴影方向]
V09 / 尺度：[无脸灰色人形/位置标记展示尺度和走位区]
MAP / 俯视图：[俯视平面/地理图，标注 ENTRANCE、EXIT、CAM_A、CAM_B、CAM_C、CHAR_ZONE、PROP_ANCHOR、LIGHT_DIR、NO_DRIFT]

风格锁：[根据场景与风格类型选取并填入标准双层架构风格锁，锁定不变画质控制量与变化变量参数，如：真人电影写实风格锁。必须追加 Image2 去除过拟合噪点提示词：干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。]

硬规则：同一个SCENE只做一个空间，不混入无关地点；所有视角必须属于同一空间；门、柱、道路、平台、光线方向和道具锚点不能在不同格子漂移；只使用无脸灰色人形或位置标记，不生成清晰主角脸。
```

## English Universal Prompt

```text
Create a 16:9 horizontal white-background scene asset board. The first visible top title must be exactly: A[NUMBER] / [SCENE_CODE] / [SCENE NAME] SCENE ASSET BOARD. The title must be largest, left-aligned, high contrast. Use the fixed white "3x3 nine-view + bottom top-down map + stable reference labels" scene asset template. This is not a landscape poster, not a storyboard, and not a movie still. Background #FFFFFF or #F8F8F4, thin black divider lines #111111, subtle gray guide lines #C8C8C8, black labels, fixed bold sans-serif typography. The board must contain clear readable module labels: V01 ESTABLISHING, V02 ENTRANCE, V03 EXIT/REVERSE, V04 CAMERA A, V05 CAMERA B, V06 CAMERA C, V07 KEY DETAIL, V08 LIGHT, V09 SCALE, MAP, ENTRANCE, EXIT, CAM_A, CAM_B, CAM_C, CHAR_ZONE, PROP_ANCHOR, LIGHT_DIR, NO_DRIFT. Use English short labels only. No tiny paragraphs, corrupted text, subtitles, watermarks, logos, brand text, or random decorative words.

Fixed layout:
Top 5-7% is the title bar.
Middle 78-82% is a 3x3 nine-view grid, each panel with a large label in the upper-left corner.
Bottom 12-16% is MAP / top-down geography and reference-label strip, marking entrance, exit, camera-safe zones, character blocking zones, prop anchors, light direction, and forbidden drift.

Scene code: [SCENE_CODE].
Scene: [space identity, era/style, weather/time, core terrain or architecture, shootable area].
Spatial anchors: [entrance, exit, main direction, foreground, midground, background, fixed props, light direction].

V01 / ESTABLISHING: [full space establishing view]
V02 / ENTRANCE: [entry route or arrival direction]
V03 / EXIT/REVERSE: [exit or reverse view]
V04 / CAMERA A: [primary shooting angle]
V05 / CAMERA B: [reverse angle]
V06 / CAMERA C: [side or diagonal angle]
V07 / KEY DETAIL: [fixed key object or spatial identity detail]
V08 / LIGHT: [light source, weather, shadow direction]
V09 / SCALE: [faceless gray silhouettes or markers showing scale and blocking zones]
MAP / TOP-DOWN: [top-down floor/geography plan labeled ENTRANCE, EXIT, CAM_A, CAM_B, CAM_C, CHAR_ZONE, PROP_ANCHOR, LIGHT_DIR, NO_DRIFT]

Style lock: [Select and fill standard decoupled style lock matching the art style and scene, locking rendering constants and style variables. Must append Image2 overfitting-noise removal prompt: clean illustration, smooth shading, soft lighting, controlled details, minimal texture, high clarity, refined edges, smooth gradients --no noise, grain, artifacts, high frequency detail, dirty texture, oversharpen, blotchy, chaotic details.]

Hard rule: one SCENE board controls one space only; do not mix unrelated locations. All views must belong to the same geography. Doors, pillars, roads, platforms, light direction, and prop anchors must not drift between panels. Use faceless gray silhouettes or position markers only; do not create clear main-character faces.
```
