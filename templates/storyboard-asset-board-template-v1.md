# Storyboard Asset Board Template V1

Template code: `WHITE_STORYBOARD_SHEET_TEMPLATE`

This is the default storyboard sheet template for all Image2 storyboard prompts in this project. It absorbs the structural logic from professional storyboard prompt patterns (especially the 10-section skeleton from @aimikoda's GPT Image 2 workflow) and adds our project's asset-code referencing, bilingual rules, and Seedance handoff compatibility.

## Why This Structure Works

The key insight from professional storyboard prompts:

- **Style Packet** locks the visual language in one complete paragraph, not scattered keywords.
- **Subjects include motion language**, not just appearance — how a character moves matters more for storyboards than what they wear.
- **Every panel beat uses `shot-type + action` in one concise line**, not long descriptions.
- **Red frame boxes + blue motion arrows** create a universal annotation system.
- **Forced action in every panel** — no dead air, no repeated stare-downs, no empty posing.
- **Negative section at the end** prevents common drift patterns.

## Required Sections

Every storyboard prompt must contain these 10 sections in this exact order:

| Section | Purpose | Required Content |
|---|---|---|
| `[PROJECT CARD]` | Project lock | Title, genre/mood line, priority line, micro brief |
| `[CONTINUITY HEADER]` | Sequence identity | Sequence ID, style packet, reference priority |
| `[SUBJECTS]` | Character + motion | Each character's identity + their motion language |
| `[SCENE]` | Space + readability | Environment, orientation, readability rules |
| `[STORYBOARD FORMAT]` | Sheet format | Grid size, panel numbering, annotation color rules |
| `[VISUAL LANGUAGE]` | Drawing style | Linework, shading, color annotations, not-finished-frame rule |
| `[ACTION DNA]` | Rhythm + choreo | Overall rhythm, camera language, cause-effect logic |
| `[SHOT DESIGN RULES]` | Shot variety | Shot size variety, geography, one-idea-per-panel |
| `[PANEL BEAT MAP]` | Panel-by-panel | Numbered beats: shot type + action in one line each |
| `[NEGATIVE]` | Forbidden patterns | Common drift patterns to avoid |

## Annotation Color System

- **Red frame boxes** = camera framing and shot boundaries.
- **Blue arrows** = motion direction, attack direction, camera movement, body travel, force lines.
- **Green labels** (optional) = asset codes like `CHAR_A`, `SCENE_01`, `PROP_01` for Seedance reference.
- Panel numbers must be **outside the frames**.
- Add **short shot labels** and **tiny micro-action captions** under each panel.

## Chinese Universal Prompt

```text
请生成一张 16:9 横向故事板设定图，使用固定白底故事板模板，不是成片剧照，不是精修海报，不是产品展示。

[PROJECT CARD]
创建一个排版设计标题栏在页面顶部，不是表格。
TITLE LOCKUP：[中文片名]
类型线：[类型/情绪/节奏]
优先级线：[核心节奏优先级，如：非停止作、可读地理、XX风格动感]
微 BRIEF：[一句完整的功能描述：多少秒、什么风格、角色A做什么、角色B如何回应、序列必须从头到尾全是动作]

[CONTINUITY HEADER]
序列 ID：[SEQUENCE_CODE]
PART：[SINGLE / PART_A / PART_B]
风格包：[一段完整的影像风格描述，包括：画风、材质感、色彩、光线、镜头运动感、速度线/运动模糊倾向、人物渲染方式、整体节奏感。不要用关键词堆砌，要写成一段连贯的风格声明。]
引用优先级：使用 @图片1 作为 [CHAR_A] 身份参考，@图片2 作为 [SCENE_01] 空间参考，@图片3 作为 [PROP_01] 道具参考。

[SUBJECTS]
[CHAR_A]：[身份描述]。TA的动作语言是[怎么动]：[具体动作特征]。
[CHAR_B]：[身份描述]。TA的动作语言是[怎么动]：[具体动作特征]。

[SCENE]
设定在[场景空间描述]。空间必须[可读性要求]。显示[空间中需要清晰可见的元素：方向、压力变化、落地弧线、布料轨迹、尘土痕迹、小碎片等]。

[STORYBOARD FORMAT]
使用 [列]x[行] 网格，共 [N] 格。
每一格都必须包含动作或动作的直接延续。
不要重复对峙格。
不要重复静止格。
不要空拍。

格子编号放在画面外。
每格下方加短镜头标签和微小动作说明。
红色框线表示镜头画框。
蓝色箭头表示运动方向、攻击方向、机位运动、身体位移和力量线。
绿色标签（可选）标注资产码如 CHAR_A、SCENE_01、PROP_01。
保持整张图干净、专业、电影感和易扫描。

[VISUAL LANGUAGE]
粗略手绘故事板质感。
松动黑色线条。
灰色调阴影。
红色画框框线。
蓝色运动箭头。
最少但清晰的环境绘画。
角色简化但表达清晰，剪影即可分辨。
不要画成精修插图。
这必须看起来像专业的动画/实拍导演预演故事板。

[ACTION DNA]
编排应该感觉[风格关键词]：[具体的节奏、韵律、镜头运动逻辑描述]。
强调[节奏要求：快切、动态透视、强剪影、布料/尾巴流动、速度线、因果关系]。
动作应该感觉[整体气质]，不要[不想要的气质]。
每一个动作都必须有清晰的前后因果逻辑。

[SHOT DESIGN RULES]
使用强镜头变化：
大全景、
中全景、
中景、
近景、
特写、
低角度、
高角度、
过肩、
追拍感镜头、
冲击插入、
反应插入。
保持战斗/动作地理可读。
包含偶尔的大全景重置，但重置格里仍然必须有活跃运动，不是静止摆拍。
不要塞满格子。
每格优先只传达一个清晰的动作意图。

[PANEL BEAT MAP]
01. [景别] [动作描述]
02. [景别] [动作描述]
03. [景别] [动作描述]
...（每格一行，编号 + 景别 + 动作一句话）

[NEGATIVE]
不要精修成片插图
不要模糊姿势
不要不可读的动作堆叠
不要重复对峙格
不要重复静止格
不要[项目特定禁止项]
不要 logo
不要水印
不要画面内字幕
```

## English Universal Prompt

```text
Create a 16:9 STORYBOARD SHEET image. Use the fixed white storyboard template. This is not a finished movie still, not a polished poster, and not a product display.

[PROJECT CARD]
Create a designed typographic masthead at the top of the sheet, not a table.
TITLE LOCKUP: [PROJECT TITLE]
META LINE: [genre / mood / rhythm]
PRIORITY LINE: [core rhythm priority, e.g. nonstop action, readable geography, lyrical motion]
MICRO BRIEF: [one complete functional sentence: duration, style, what character A does, how character B responds, sequence must be full of action from first panel to last]

[CONTINUITY HEADER]
SEQUENCE ID: [SEQUENCE_CODE]
PART: [SINGLE / PART_A / PART_B]
STYLE PACKET: [one complete paragraph of visual style declaration: drawing style, material feel, color, light, camera motion feel, speed line / motion blur tendency, character rendering, overall rhythm. Do not use keyword lists. Write a coherent style statement.]
REFERENCE PRIORITY: use @图片1 as [CHAR_A] identity reference, @图片2 as [SCENE_01] space reference, @图片3 as [PROP_01] prop reference.

[SUBJECTS]
[CHAR_A]: [identity description]. Their fighting/action language is [how they move]: [specific motion characteristics].
[CHAR_B]: [identity description]. Their fighting/action language is [how they move]: [specific motion characteristics].

[SCENE]
Set the sequence in [environment description]. The space must [readability requirement]. Show [spatial elements that must be clearly visible: direction, counter direction, pressure changes, landing arcs, cloth trails, dust trails, small debris accents].

[STORYBOARD FORMAT]
Use a [columns] x [rows] grid for [N] panels.
Every panel should contain action or immediate action continuation.
No repeated face-off panels.
No repeated stillness panels.
No dead air.

Panel numbers should be outside the frames.
Add short shot labels and tiny micro-action captions under each panel.
Use red frame boxes to indicate camera framing.
Use blue arrows to indicate motion, attack direction, camera movement, body travel, and force lines.
Use green labels (optional) to mark asset codes like CHAR_A, SCENE_01, PROP_01.
Keep the sheet clean, premium, cinematic, and easy to scan.

[VISUAL LANGUAGE]
Rough hand-drawn storyboard look.
Loose black linework.
Gray tonal shading.
Red framing boxes.
Blue motion arrows.
Minimal but clear environment drawing.
Characters simplified but expressive and instantly distinguishable by silhouette.
Do not render as a finished illustration.
This must look like a professional action previs storyboard sheet.

[ACTION DNA]
The choreography should feel [style keywords]: [specific rhythm, cutting tempo, camera language, cause-effect logic].
Emphasize [fast rhythmic cutting, dynamic perspective, strong silhouettes, cloth/tail flow, speed-line energy, elegant cause-effect combat/action beats].
The action should feel [overall quality], not [unwanted quality].
Every movement should have a clear before-and-after logic.

[SHOT DESIGN RULES]
Use strong shot variety:
wide,
medium-wide,
medium,
close-up,
extreme close-up,
low angle,
high angle,
over-shoulder,
tracking-feel shots,
impact inserts,
reaction inserts.

Maintain readable action geography.
Include occasional wide resets, but they must still contain active movement, not static posing.
Do not clutter panels.
Prioritize one clear action idea per panel.

[PANEL BEAT MAP]
01. [shot type] [action description]
02. [shot type] [action description]
03. [shot type] [action description]
... (one line per panel, number + shot type + action in one sentence)

[NEGATIVE]
no polished final illustration
no soft vague posing
no unreadable action clutter
no repeated staring panels
no repeated stillness panels
no [project-specific forbidden items]
no logos
no watermark
no in-frame subtitles
```

## Beat Map Writing Rules

Each panel beat must follow this format:

```text
[NUMBER]. [SHOT TYPE], [ACTION]
```

Examples of good beats:

- `01. Wide action opening, CHAR_A is already airborne lunging across the courtyard toward CHAR_B.`
- `04. Close impact insert, forearm parry with dust burst and cloth arc.`
- `09. Wide active reset, both circle in motion around broken pillars, kicking up dust while re-engaging.`
- `20. Strong ending frame, CHAR_B's finishing strike stops at CHAR_A's throat while CHAR_A is still in motion, both forming a dramatic frozen-action silhouette.`

Bad beats (avoid):

- `01. CHAR_A looks at CHAR_B.` — No action, just looking.
- `03. Close-up of CHAR_A's face.` — No motion, no cause-effect.
- `07. Wide shot of the courtyard.` — No action, dead air.
- `12. CHAR_A and CHAR_B face off again.` — Repeated face-off, repeated stillness.

## Style Packet Writing Rules

The style packet must be written as one coherent paragraph, not a keyword list. It should cover:

1. Drawing style / rendering approach
2. Material feel (cloth, metal, dust, light, skin)
3. Color palette and light direction
4. Camera motion tendency
5. Speed line / motion blur approach
6. Character rendering level
7. Overall rhythm and energy

Bad style packet: `cinematic, anime, dusty, warm, action, fast`

Good style packet: `stylized cinematic anime-wuxia action previs, sculpted character forms, warm dusty stone courtyard palette, muted orange costume accents, graphite-black serpent scales, gray monkey fur, soft late-afternoon light, drifting dust haze, flowing cloth motion, elegant speed lines, crisp silhouettes, restrained motion blur, dynamic camera language, premium animated feature storyboard energy.`

## Integration With Asset Templates

Storyboard prompts should reference asset boards by their module labels:

- Character: `use @图片1 M03 FACE CLOSE-UP and M05 ACTION HAND PROP LOGIC as CHAR_A identity and motion reference`
- Scene: `use @图片2 V04 CAMERA A and MAP/CHAR_ZONE as space reference`
- Prop: `use @图片3 P06 HAND LOGIC and P07 STATE as prop action reference`

This lets Seedance later match storyboard panels to specific asset modules.
