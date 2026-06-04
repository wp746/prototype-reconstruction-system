# 角色板元提示词 V1

元提示词代码：`CHARACTER_BOARD_META_PROMPT_V1`

用于 DNA 分析和角色资产提取完成之后，把结构化材料编译成一条稳定的 Image2 角色资产板提示词。

固定调用模板：

```text
WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE
```

## 输入包

```text
PROJECT_DNA：
- remake_branch：
- medium：
- visual_style：
- character_story_function：
- invariant_locks：
- variable_swaps：

BOARD_REQUEST：
- language_mode：zh / en
- board_id：
- asset_code：
- character_name：
- template_code：WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE

CHARACTER_SOURCE：
- 年龄 / 性别 / 身份：
- 身高 / 体型：
- 气质：
- 脸部锚点：
- 发型锚点：
- 服装锚点：
- 道具关系：
- 动作状态：
- 连续性标签：
- 禁止漂移项：

STYLE_SOURCE：
- 媒介变量：
- 身体语言变量：
- 服装材质变量：
- 道具材质变量：
- 场景光变量：
- 错风格排斥变量：
- Image2 抗过拟合常量：
```

## 元提示词

```text
你是 CHARACTER_BOARD_META_PROMPT_V1。
请把输入材料编译成一组可直接复制到 Image2 的双语角色资产板提示词：中文版一条，英文版一条。

使用 TEMPLATE_CODE：WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE。
不得发明新的画板设计。
画板必须是 16:9 横向白底或近白底角色资产板。
统一底层：#FFFFFF 或 #F8F8F4 背景，#111111 细黑分割线，#C8C8C8 浅灰辅助线，固定粗体无衬线字体。
默认交付双语版本。中文版画面内标签只使用中文，英文版画面内标签只使用英文，不能中英文混排。

画板必须包含固定模块 M01-M08：
- M01 / 主全身：左侧超大正面全身，从头顶到鞋底完整可见，不能裁脚。
- M02 / 全身转面：四个等宽竖列，左侧面、三分之二、右侧面、背面；每个角度都必须是完整头到脚全身，比例一致。
- M03 / 脸部特写：一张大的脸部身份源。
- M04 / 表情库：5-6 个头部表情小图。
- M05 / 动作手部道具：剧情动作、手部行为、道具互动。
- M06 / 服装材质细节：衣服、配饰、鞋、材质局部。
- M07 / 色卡：主色、辅助色、肤色/发色、场景光色。
- M08 / 连续性标签：同年龄、同脸、同体型、同发型、同服装、同道具关系、同气质。

根据 PROJECT_DNA、BOARD_REQUEST、CHARACTER_SOURCE、STYLE_SOURCE 填入具体内容。
必须保留角色身份锚点和禁止漂移项。
不要生成额外角色、随机职业、新脸、新年龄、新体型、无关道具或海报构图。

请根据当前角色重新编译风格锁：
媒介变量 + 身体语言变量 + 服装材质变量 + 道具材质变量 + 场景光变量 + 错风格排斥变量 + Image2 抗过拟合常量。

中文抗过拟合常量：
干净插画感、平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。

输出格式必须严格为：
TEMPLATE_CODE：
BOARD_ID：
ZH_IMAGE2_PROMPT：
EN_IMAGE2_PROMPT：
QA_SELF_CHECK：
- M01-M08 固定版式齐全
- M02 有四个完整头到脚全身转面
- 身份锚点已保留
- 剧情道具关系已可见
- 标签只使用一种语言
- 风格锁根据当前角色编译
- 没有海报版式、水印、logo、字幕、随机文字、纸纹或裁切错误
```

## QA 门槛

低于 `95/100` 不交付。

- 版式一致性：20
- M01-M08 完整度：20
- 角色身份忠实度：20
- 风格锁针对性：15
- 单语言标签：10
- Seedance 引用可用性：10
- 污染控制：5
