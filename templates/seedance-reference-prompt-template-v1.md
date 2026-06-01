# Seedance Reference Prompt Template V1

Template code: `SEEDANCE_EXPLICIT_REFERENCE_TEMPLATE`

本模板用于 Seedance 2.0 图生视频提示词。重点解决两个问题：

1. 资产引用必须明确到图号和模块标签。
2. 故事板引用必须明确几乘几、镜头顺序、切点节奏和连贯性。
3. 15 秒以内参考片默认生成一条连续成片提示词；逐镜 timing 是片内切点，不是拆成多条独立视频。
4. 带箭头、框线、标签、编号和说明文字的标注故事板不得作为 Seedance 视觉输入；必须使用干净控制帧，或只把标注故事板转译成文字 timing。
5. 参考片只存在于后台拆解和 QA，不进入最终模型提示词。最终提示词只写新片自己的执行要求，不写“学习参考片”“不要复制原片”等提醒。

## Required Structure

Seedance 2.0 提示词分三条支线，不能混用。

### Branch A / Asset-only Direct

用于身份一致性优先的生成。不上传故事板。

```text
[VIDEO TASK]
[ASSET LOCK]
[SHOT-BY-SHOT TIMING]
[MOTION CONTINUITY]
[DIALOGUE / VOICE PERFORMANCE]
[SOUND EFFECTS FOR POST]
[NEGATIVE PROMPT]
```

### Branch B / Black-and-white Storyboard Guided

用于切镜、构图、动作方向优先的生成。必须使用黑白手稿故事板。

```text
[VIDEO TASK]
[ASSET LOCK]
[STORYBOARD USE]
[ASSET REFERENCE MAP]
[SHOT-BY-SHOT TIMING]
[MOTION CONTINUITY]
[ACTION / BLOCKING]
[CAMERA MOVEMENT]
[DIALOGUE / VOICE PERFORMANCE]
[LIGHTING / VFX]
[SOUND EFFECTS FOR POST]
[NEGATIVE PROMPT]
```

### Branch C / No-Asset Text-Only Direct

用于用户没有提供资产、也没有要求先出资产或故事板，只要求直接输出一条 Seedance 2.0 提示词时。

```text
[VIDEO TASK]
[NEW FILM TEXT LOCK]
[SHOT-BY-SHOT TIMING]
[MOTION CONTINUITY]
[DIALOGUE / VOICE PERFORMANCE]
[SOUND EFFECTS FOR POST]
[NEGATIVE PROMPT]
```

C 线不上传资产图，不上传故事板图，不写不存在的 `A01 / M03` 或 `@图片1` 资产引用。参考片只用于后台 DNA 分析，最终提示词只描述新片本身。角色、场景、道具、风格必须用短而稳定的文本锚点锁定。

C 线骨架：

```text
[VIDEO TASK]
生成一条完整连续的 [时长] 秒电影级视频，[画幅]，[fps]。视频包含 SH01-SH[N] 的片内硬切节奏；这些镜头是同一条视频里的连续剪辑，不要拆成多条视频，不要一镜到底，不要故事板翻页。

[NEW FILM TEXT LOCK]
主角：[稳定文本锚点：年龄段、脸型/体态、发型、服装、气质、关键配饰。]
场景：[稳定文本锚点：空间、主光方向、前中后景、关键锚点。]
道具/法术/产品：[稳定文本锚点：形状、材质、触发方式、状态变化。]
风格：[画幅、光影、色彩、材质、镜头质感。]

[SHOT-BY-SHOT TIMING]
SH01 / [start-end] / [shot size] / [camera move] / [single action beat + visible result]
SH02 / ...

[MOTION CONTINUITY]
[逐镜动作因果链。]

[DIALOGUE / VOICE PERFORMANCE]
[原创台词、口型或旁白功能；不生成字幕，不生成画面文字。]

[SOUND EFFECTS FOR POST]
无 BGM。SFX：[原创音效点。]

[NEGATIVE PROMPT]
字幕，画面文字，水印，logo，随机文字，乱码，参考片角色脸，参考片服装，参考片道具形状，参考片特效图形，角色脸漂移，服装漂移，道具变形，场景漂移，镜头合并，少于 SH[N] 个镜头，一镜到底，多指，坏手，塑料皮肤，游戏 CG 感。
```

`[DO NOT COPY]` 只保留在后台分析和 QA 文档中。最终可复制给模型的 Seedance 提示词不得出现原片、参考片、source、copy、do not copy 等源片提醒。

## Video Task Continuity

15 秒以内的参考片复刻，Seedance 提示词必须写成一条连续视频任务：

```text
生成一条完整连续的 12 秒电影级视频，包含 SH01-SH08 的片内切镜。8 个镜头是同一条视频里的连续剪辑节奏，不要拆成 8 条视频，不要拆成多个独立片段，不要做故事板翻页。
```

英文版：

```text
Generate one complete continuous 12-second cinematic video with internal cuts from SH01 to SH08. The 8 shots are the cut rhythm inside one single video, not 8 separate videos, not multiple disconnected segments, and not a storyboard slideshow.
```

## Asset Reference Map

不要只写“参考角色图”“参考场景图”“参考道具图”。必须写：

```text
参考 A01 / M01 HERO FULL BODY 锁定角色全身比例、服装轮廓和终帧剪影。
参考 A01 / M03 FACE CLOSE-UP 锁定角色脸部身份。
参考 A01 / M05 ACTION HAND PROP LOGIC 锁定手部动作和道具接触点。
参考 A02 / V01 ESTABLISHING 锁定场景总体空间。
参考 A02 / V04 CAMERA A 锁定本镜头机位。
参考 A02 / MAP CHAR_ZONE / PROP_ANCHOR 锁定角色区和道具锚点。
参考 A03 / P06 HAND LOGIC 锁定道具持握和接触关系。
参考 A03 / P07 STATE 锁定道具状态变化。
```

英文版：

```text
Reference A01 / M01 HERO FULL BODY to lock full-body scale, wardrobe silhouette, and final silhouette.
Reference A01 / M03 FACE CLOSE-UP to lock character identity.
Reference A01 / M05 ACTION HAND PROP LOGIC to lock hand action and prop contact points.
Reference A02 / V01 ESTABLISHING to lock the overall scene geography.
Reference A02 / V04 CAMERA A to lock the camera angle for this shot.
Reference A02 / MAP CHAR_ZONE / PROP_ANCHOR to lock character zone and prop anchors.
Reference A03 / P06 HAND LOGIC to lock prop grip and contact mechanics.
Reference A03 / P07 STATE to lock prop state change.
```

Asset-only direct branch must make the identity hierarchy explicit:

```text
@图片1 / A01 是唯一角色身份源，锁定脸、发型、体型、服装、手部和气质。
@图片2 / A02 锁定场景空间。
@图片3 / A03 锁定道具/法术媒介。
不上传故事板；镜头顺序、构图和动作方向全部由下方 SH01-SH[N] 文字 timing 控制。
```

```text
@image1 / A01 is the only character identity source, locking face, hairstyle, body scale, wardrobe, hands, and presence.
@image2 / A02 locks the scene space.
@image3 / A03 locks the prop or magic medium.
No storyboard is uploaded; shot order, composition, and action direction are controlled by the SH01-SH[N] text timing below.
```

## Storyboard Reference

中文版固定写法：

```text
将提供的 @[图片编号] / [列]x[行] 的故事板制作成一段流畅的电影级动画视频。
严格保持 SH01-SH[N] 的镜头顺序、切点节奏、构图重心、动作方向和镜头连贯性。
不要渲染故事板边框、编号、箭头、文字标注或面板布局。
故事板只作为运动、构图、镜头切点和动作方向参考，最终必须是一条连续成片。
角色身份、服装、发型、脸部、道具形状和场景身份以资产图为准；故事板不得覆盖资产身份。若故事板与资产图冲突，以资产图为准，只保留故事板的运动、构图、切点和动作方向。
本次视频输入不得上传带箭头、框线、绿色标签、编号、标题栏、说明文字或白底故事板 UI 的 S01_ANNOTATED_STORYBOARD。
@[图片编号] 必须是 S##_CLEAN_BW_STORYBOARD / [列]x[行] 黑白手稿故事板。
```

英文版固定写法：

```text
Convert the provided @[image number] / [columns]x[rows] storyboard into a smooth cinematic animated video.
Strictly preserve the SH01-SH[N] shot order, cut rhythm, composition center, action direction, and shot continuity.
Do not render storyboard borders, panel numbers, arrows, text labels, or panel layout.
Use the storyboard only as motion, composition, cut-point, and action-direction reference. The final result must be one continuous film clip.
Character identity, wardrobe, hairstyle, face, prop shape, and scene identity come from the asset images. The storyboard must not override asset identity. If the storyboard conflicts with the asset images, follow the asset images and preserve only storyboard motion, composition, cut points, and action direction.
Do not upload any S01_ANNOTATED_STORYBOARD that contains arrows, frame boxes, green labels, panel numbers, title bars, captions, or white storyboard UI as video input.
@[image number] must be S##_CLEAN_BW_STORYBOARD / [columns]x[rows] black-and-white rough storyboard.
```

如果项目暂时只有带标注故事板，必须改用以下写法，不把故事板作为图片上传：

```text
S01_ANNOTATED_STORYBOARD 仅供导演理解，不作为本次 Seedance 图片输入。请根据下方 SH01-SH[N] 文字 timing、镜头运动、动作方向和资产引用生成连续视频，不要从任何带箭头或标签的图像中取样。
```

```text
S01_ANNOTATED_STORYBOARD is for director review only and is not used as Seedance image input. Generate the continuous video from the SH01-SH[N] text timing, camera movement, action direction, and asset references below. Do not sample from any image containing arrows or labels.
```

多个故事板时：

```text
先使用 S01 完成 SH01-SH10，再使用 S02 完成 SH11-SH20。保持两个故事板之间的动作连续、空间连续和角色连续。
```

```text
Use S01 for SH01-SH10, then S02 for SH11-SH20. Preserve action continuity, spatial continuity, and character continuity across both storyboards.
```

## Shot-By-Shot Timing

每个镜头必须写：

```text
SH## / [start-end] / [shot size] / [camera move] / [action beat] / references: [A01/Mxx, A02/Vxx, A03/Pxx]
```

示例：

```text
SH05 / 0:04.3-0:05.4 / hand macro / hard cut / fingers pull the black cord through the bronze ring with clear contact points / references: A01/M05, A03/P06, A03/P04
```

## Motion Continuity

必须说明镜头之间如何一气呵成：

```text
SH01 的前推接 SH02 的背向推进；SH02 的线条方向接 SH03 的横向漂移；SH03 的线条收束接 SH04 的眼神；SH04 的眼神切到 SH05 的手部动作。
```

```text
SH01 push-in connects to SH02 rear push; SH02 cord direction connects to SH03 lateral drift; SH03 line convergence motivates SH04 eye close-up; SH04 gaze cuts into SH05 hand action.
```

## Dialogue / Voice Performance

如果参考片里的文字实际承担台词、咒语、旁白或宣判功能，只复刻其功能和节奏，不复刻原句，不做字幕：

```text
台词作为声音/表演设计，不作为画面文字。角色在 SH01-SH02 低声说出[新台词1]，在 SH03-SH08 冷声说出[新台词2]，声音节奏贴合切点和动作触发。不要生成字幕，不要生成画面内文字。
```

英文版：

```text
Dialogue is voice/performance design, not on-screen text. The character quietly speaks [new line 1] during SH01-SH02, then delivers [new line 2] with a cold decisive tone during SH03-SH08. The vocal rhythm follows the cut points and action triggers. Do not generate subtitles or any on-screen text.
```

## Sound Effects For Post

如果用户说明背景音乐是后期添加或不需要分析，写短生产指令，不写解释过程：

```text
无 BGM。SFX：风声、脚步、布料、金属、冲击、静默、终帧余音。
```

```text
No BGM. SFX: wind, footsteps, cloth, metal, impacts, silence, final resonance tail.
```

## Negative Prompt Must Include

```text
subtitles, on-screen text, watermark, logo, random text, corrupted text, storyboard borders, panel numbers, arrows, blue arrows, motion arrows, labels, green labels, red frame boxes, title bars, white storyboard UI, panel layout, asset board layout, cloned faces, extra fingers, broken hands, fused fingers, face drift, costume drift, prop deformation, scene drift, impossible camera movement, cluttered VFX blocking the subject
```
