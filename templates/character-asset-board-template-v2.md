# Character Asset Board Template V2

Template code: `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`

This is the default character asset board template for all Image2 + Seedance 2.0 production packages in this project.

## Layout Lock

- Canvas: 16:9 landscape, recommended `3840x2160`.
- Background: white or near-white, `#FFFFFF` / `#F8F8F4`.
- Dividers: thin black `#111111`, subtle gray guides `#C8C8C8`.
- Typography: bold sans-serif. Chinese board uses Chinese labels only. English board uses English labels only.
- Do not show forbidden examples, red-X panels, brand counterexamples, subtitles, watermarks, logos, or negative prompt text inside the image.

## Fixed Modules

| Module | Position | Required Content |
|---|---|---|
| Title bar | top 5-7% height | `A[NUMBER] / [CHAR_CODE] / [CHARACTER NAME]` |
| M01 / Hero Full Body | left 26-30% width, 70-76% height | huge front full body, head to soles visible |
| M02 / Full-Body Turnaround | top-center 44-48% width, 34-40% height | 4 equal full-body columns: left side, 3/4 view, right side, back view |
| M03 / Face Close-Up | top-right 22-26% width, 18-22% height | one large face identity source |
| M04 / Facial Expressions | below M03, 14-18% height | 5-6 head expression thumbnails |
| M05 / Action Hand Prop Logic | center-lower 44-48% width, 20-26% height | story action, hands, prop interactions |
| M06 / Wardrobe Material Details | lower-right 22-26% width, 20-26% height | clothing, accessories, shoes, material details |
| M07 / Color Palette | bottom strip | main colors, support colors, skin/hair, scene light |
| M08 / Continuity Notes | bottom strip | same age, face, body, hair, wardrobe, prop relationship, temperament |

## M02 Hard Rule

`M02 / Full-Body Turnaround` is the most important identity-lock module.

It must:

- Sit in the top-center large horizontal area.
- Use at least 34-40% of the whole board height.
- Split into 4 equal vertical columns.
- Show complete head-to-toe bodies in every column.
- Keep feet, shoes, trouser hem, coat hem, bag straps, and back silhouette visible.
- Keep all four angles at the same scale.

It must not:

- Become half-body views.
- Become busts.
- Crop at the waist.
- Crop at the knees.
- Show head-and-shoulder views only.
- Be compressed by the face close-up or lower modules.

## Chinese Universal Prompt

```text
请生成一张 16:9 横向白底角色资产板，顶部第一行大标题必须是：A[编号] / [角色代码] / [中文角色名]角色资产板。标题最大、左对齐、高对比。整体使用固定“左大主图 + 顶部全身转面大条 + 右侧脸部表情 + 下方动作材质色卡”的白底角色资产模板，不是海报，不是故事板。背景#FFFFFF或#F8F8F4，细黑分割线#111111，灰色辅助线#C8C8C8，标签黑色，固定粗体无衬线字体，类似 Noto Sans CJK / Source Han Sans。画板内标签必须使用中文短标签，除 A编号 和 角色代码外不要出现英文。禁止纸纹、牛皮纸、报纸、油纸、羊皮纸、拼贴、暗色海报背景、随机字体、宋体、手写体、书法体、小字段落、乱码文字、字幕、水印、logo。

固定版式比例：
顶部 5-7% 是标题栏。
左侧 26-30% 宽、70-76% 高是 M01 / 主全身：一张超大正面全身，从头顶到鞋底完整可见，人物占该面板高度 88-94%。
顶部中间 44-48% 宽、34-40% 高是 M02 / 全身转面：分成4个等宽竖列，分别是左侧面、三分之二、右侧面、背面。每一列都必须是从头顶到鞋底完整可见的全身体，脚、鞋、裤脚、衣摆、包带和背部轮廓都要完整出现；禁止半身、胸像、腰部裁切、只画头肩或只画上半身。
右上 22-26% 宽、18-22% 高是 M03 / 脸部特写：一张大脸部身份源。
M03 下方 22-26% 宽、14-18% 高是 M04 / 表情库：5-6 个头部表情。
中下 44-48% 宽、20-26% 高是 M05 / 动作手部道具：当前剧情动作、手部、道具互动。
右下 22-26% 宽、20-26% 高是 M06 / 服装材质细节：服装、配饰、包、鞋、湿痕、材质。
底部通栏是 M07 / 色卡 和 M08 / 连续性标签。

角色代码：[角色代码]。
角色设定：[年龄、性别、身份、身高、体型、气质、心理状态]。
外观锚点：[脸型、发型、妆容、眼神、主要服装、配饰、鞋、包、特殊痕迹]。

M01 / 主全身：
[正面全身姿态描述]
要求：超大主图，完整头到脚，不能裁脚，不能只到膝盖，不能变半身。

M02 / 全身转面：
左侧面：[左侧面全身描述]
三分之二：[3/4全身描述]
右侧面：[右侧面全身描述]
背面：[背面全身描述]
硬规则：四个角度全部必须是完整全身体，从头顶到鞋底完整可见，脚和鞋必须出现，衣摆/裤脚/包带必须完整，比例一致。禁止半身、胸像、腰部裁切、头肩图、上半身图。

M03 / 脸部特写：
[正面或主角度脸部身份描述]

M04 / 表情库：
表情1：[短标签]
表情2：[短标签]
表情3：[短标签]
表情4：[短标签]
表情5：[短标签]
可选表情6：[短标签]

M05 / 动作手部道具：
动作1：[当前剧情动作]
动作2：[手部动作]
动作3：[道具互动]
动作4：[关键姿态]

M06 / 服装材质细节：
服装：[面料/颜色/磨损/湿痕]
配饰：[包/耳环/表/帽子等]
鞋：[鞋型/颜色/状态]
细节：[袖口/领口/包带/发梢/雨水高光]

M07 / 色卡：
[主色1]、[主色2]、[辅助色]、[肤色/发色]、[场景光色]

M08 / 连续性标签：
同一年龄、同一脸、同一体型、同一发型、同一服装、同一道具关系、同一气质。

禁止项只作为提示词约束，不要展示在图里：不要换脸、不要换年龄、不要换体型、不要换发型、不要换服装、不要新增无关配饰、不要明星脸、不要随机职业、不要夸张表情、不要多角色、不要红叉示例、不要反例图、不要字幕、不要品牌字。
```

## English Universal Prompt

```text
Create a 16:9 horizontal white-background character asset board. The first visible top title must be exactly: A[NUMBER] / [CHAR_CODE] / [CHARACTER NAME] CHARACTER ASSET BOARD. The title must be largest, left-aligned, high contrast. Use the fixed white "large hero body + full-body turnaround bar + right face/expression + lower action/material/palette" character asset template. This is not a poster and not a storyboard. Background #FFFFFF or #F8F8F4, thin black divider lines #111111, subtle gray guide lines #C8C8C8, black labels, fixed bold sans-serif typography similar to Inter / Helvetica. All in-image labels must be English short labels. Do not render Chinese labels on the English board. No paper texture, kraft paper, newspaper, oil paper, parchment, collage, dark poster background, mixed fonts, serif fonts, handwriting, calligraphy, tiny paragraphs, corrupted text, subtitles, watermarks, or logos.

Fixed layout proportions:
Top 5-7% is the title bar.
Left 26-30% width and 70-76% height is M01 / HERO FULL BODY: one huge front full-body source, complete from top of head to soles of shoes, filling 88-94% of the panel height.
Top-center 44-48% width and 34-40% height is M02 / FULL-BODY TURNAROUND: four equal vertical columns: left side, 3/4 view, right side, back view. Every column must show a complete head-to-toe full body; feet, shoes, trouser hem/coat hem, bag strap, and back silhouette must be fully visible. No half-body, no bust crop, no waist-up crop, no head-and-shoulder view, no upper-body-only view.
Top-right 22-26% width and 18-22% height is M03 / FACE CLOSE-UP: one large face identity source.
Below M03, 22-26% width and 14-18% height is M04 / FACIAL EXPRESSIONS: 5-6 head expression thumbnails.
Center-lower 44-48% width and 20-26% height is M05 / ACTION HAND PROP LOGIC: current-story action, hands, and prop interactions.
Lower-right 22-26% width and 20-26% height is M06 / WARDROBE MATERIAL DETAILS: clothing, accessories, bag, shoes, wet marks, materials.
Bottom strip contains M07 / COLOR PALETTE and M08 / CONTINUITY NOTES.

Character code: [CHAR_CODE].
Character: [age, gender, role, height, body type, temperament, psychological state].
Appearance anchors: [face shape, hairstyle, makeup, eyes, main wardrobe, accessories, shoes, bag, marks].

M01 / HERO FULL BODY:
[front full-body pose description]
Requirement: huge hero body, complete head-to-toe, do not crop feet, do not stop at knees, do not make it half-body.

M02 / FULL-BODY TURNAROUND:
Left side: [left side full-body description]
3/4 view: [3/4 full-body description]
Right side: [right side full-body description]
Back view: [back full-body description]
Hard rule: all four angles must be complete full-body views from top of head to soles of shoes. Feet and shoes must appear. Coat hem/trouser hem/bag strap must be complete. Same scale across all angles. No half-body, no bust crop, no waist-up crop, no head-and-shoulder view, no upper-body-only view.

M03 / FACE CLOSE-UP:
[front or primary face identity description]

M04 / FACIAL EXPRESSIONS:
Expression 1: [short label]
Expression 2: [short label]
Expression 3: [short label]
Expression 4: [short label]
Expression 5: [short label]
Optional expression 6: [short label]

M05 / ACTION HAND PROP LOGIC:
Action 1: [current story action]
Action 2: [hand action]
Action 3: [prop interaction]
Action 4: [key pose]

M06 / WARDROBE MATERIAL DETAILS:
Wardrobe: [fabric/color/wear/wet marks]
Accessories: [bag/earrings/watch/hat]
Shoes: [shoe type/color/state]
Details: [cuffs/collar/bag strap/hair ends/rain highlights]

M07 / COLOR PALETTE:
[main color 1], [main color 2], [support color], [skin/hair color], [scene light color]

M08 / CONTINUITY NOTES:
same age, same face, same body type, same hairstyle, same wardrobe, same prop relationship, same temperament.

Negative constraints are prompt-only and must not appear as a visible image module: no face change, no age change, no body type change, no hairstyle change, no wardrobe change, no unrelated accessories, no celebrity face, no random profession, no exaggerated expression, no extra characters, no red-X examples, no forbidden example images, no subtitles, no brand text.
```
