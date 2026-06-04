# 板类元提示词编译器 V1

元提示词代码：`BOARD_META_PROMPT_COMPILER_V1`

这个文件是所有 Image2 板类提示词的上游总编译器。它不直接替代角色板、场景板、道具板、故事板模板，而是在它们前面统一接收 DNA、资产变量、风格锁和分镜计划，再输出稳定、可复制、可审核的 Image2 提示词。

目标：防止每个项目、每一轮出图时，资产板和故事板的设计、排版、字体、布局、标签语言和风格锁随机漂移。

## 调用的固定模板

- 角色资产板：`WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`
- 场景资产板：`WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`
- 道具资产板：`WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`
- 故事板：`WHITE_STORYBOARD_SHEET_TEMPLATE`

## 独立中文版元提示词

- [角色板元提示词 V1](character-board-meta-prompt-zh-v1.md)
- [场景板元提示词 V1](scene-board-meta-prompt-zh-v1.md)
- [道具板元提示词 V1](prop-board-meta-prompt-zh-v1.md)
- [故事板元提示词 V1](storyboard-board-meta-prompt-zh-v1.md)

## 输入材料

```text
PROJECT_DNA：
- remake_branch：A / B / C / D / A+B / D+B
- medium：真人电影写实 / 动漫 / 三维风格化 / 超现实 / 其他
- visual_style：色彩、光线、材质、渲染方式、氛围
- story_function：这个资产或故事板在影片里承担什么功能
- invariant_locks：必须保持不变的内容
- variable_swaps：已经被重构替换的变量

BOARD_REQUEST：
- board_type：character / scene / prop / storyboard_annotated / storyboard_clean_bw
- language_mode：zh / en
- aspect_ratio：16:9
- asset_code：A## / CHAR_CODE / SCENE_CODE / PROP_CODE / S##
- board_title：画面顶部可见标题
- template_code：对应固定模板代码

ASSET_SOURCE：
- identity_anchors：脸、体型、剪影、尺度、形状、材质、颜色
- module_requirements：M01-M08 / V01-V09+MAP / P01-P08 / SH01-SH[N]
- continuity_notes：后续 Seedance 必须引用和保持的连续性
- forbidden_drift：脸、身体、服装、道具、空间、光线、状态、风格禁止漂移项

STYLE_SOURCE：
- medium_variable：媒介变量
- subject_material_variable：主体材质变量
- wardrobe_or_surface_variable：服装、表面或道具变量
- scene_light_variable：场景光变量
- anti_mismatch_variable：排斥错风格变量
- Image2_overfit_noise_constants：Image2 抗过拟合常量

STORYBOARD_SOURCE，仅故事板使用：
- SEG##、runtime、in_state、action_chain、out_state、continuity_to_next
- shot_count、grid_layout、panel_beats
- 每镜 active_assets
- 镜头节奏和运动方向
```

## 输出要求

默认每次输出一组双语 Image2 板类提示词：中文版一条，英文版一条。

必须包含：

- `TEMPLATE_CODE`
- `BOARD_ID`
- `ZH_IMAGE2_PROMPT`
- `EN_IMAGE2_PROMPT`
- 固定版式要求
- 从 DNA 和资产材料中填入的项目变量
- 重新编译后的风格锁
- 只作为提示词约束的禁止项，不能把禁止项画进图里
- `QA_SELF_CHECK`

禁止：

- 临时发明新板式
- 改背景色、字体、分割线、模块比例和标签系统
- 中英文混排
- 在图里生成长段文字、乱码、字幕、水印、logo、品牌字
- 让故事板覆盖资产身份
- 把带箭头、编号、框线、标签的标注故事板上传给 Seedance

场景板额外禁止：`V01-V09` 九个场景画面内部不得出现文字、箭头、尺寸线、区域圈、机位图标、虚线、图例、说明标注或 UI 标记；所有标注只允许出现在底部 `MAP / 俯视图` 区域。

## 双语成对交付规则

资产板和故事板永远默认给用户两版提示词：

- `ZH_IMAGE2_PROMPT`：中文版提示词，画面内标签只使用中文。`A01`、`CHAR_CODE`、`SCENE_CODE`、`PROP_CODE`、`M01`、`V01`、`P01`、`SH01`、`CAM_A` 这类生产代码可以保留。
- `EN_IMAGE2_PROMPT`：英文版提示词，画面内标签只使用英文，不渲染中文标签。
- 两版提示词必须描述同一版式、同一资产身份、同一模块、同一故事板 beat、同一风格锁逻辑和同一 QA 门槛。
- 中文版不要混入英文描述性标签，英文版不要混入中文描述性标签。生产代码例外。
- 如果用户明确只要一种语言，可以只展示该语言，但后台仍要按双语逻辑自检一致性。

## 统一画板底层锁

```text
画幅：16:9 横向，推荐 3840x2160。
背景：白色或近白色 #FFFFFF / #F8F8F4。
分割线：细黑线 #111111，浅灰辅助线 #C8C8C8。
字体：固定粗体无衬线。
文字：只允许大号、可读、稳定的模块标签，不允许小段落。
语言：中文板只用中文短标签，英文板只用英文短标签。
```

## 风格锁编译公式

风格锁不能机械复制，必须按当下主体重新编译。

```text
风格锁 =
媒介变量
+ 当前主体材质变量
+ 服装 / 表面 / 道具 / 地理变量
+ 场景光变量
+ 错风格排斥变量
+ Image2 抗过拟合常量
```

中文抗过拟合常量：

```text
干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。
```

## 故事板第五版调用规则

当 `board_type = storyboard_seedance_v5` 时，调用 [故事板元提示词 V1 中文版](storyboard-board-meta-prompt-zh-v1.md)。

硬规则：

- 单个故事板 Part 不超过 15 秒。
- 长戏自动拆成 `Part 1 (00:00-00:15)`、`Part 2 (00:15-00:30)`。
- 每个 Panel 必须有当前 Part 内绝对时间码，格式 `[00:00s - 00:02s]`，但时间码只写在提示词文本里，不画进故事板图像。
- 时间码按电影呼吸切，不机械均分。
- 中文画布只用中文说明，英文画布只用英文说明。
- 故事板图像必须干净：无箭头、无运动线、无彩色标注、无编号、无时间码、无文字说明、无图例、无标签、无白底 UI。
- 运镜、动作方向、速度和切点功能必须输出为 `SEEDANCE_MOTION_TEXT`。

## QA 门槛

低于 `95/100` 不交付。

- 版式和字体一致性：20
- 模块完整度：20
- DNA 与资产变量忠实度：20
- 风格锁针对性：15
- 单语言标签纪律：10
- Seedance 引用可用性：10
- 污染控制：5
