# QA Checklist

## Reference Intake

- [ ] 参考片来源已记录。
- [ ] 权限和复用边界已记录。
- [ ] 新主题、目标风格、画幅、平台、时长已记录。
- [ ] 已询问并记录用户要复刻的范围：镜头节奏、运镜、剧情、角色、场景、风格、台词/旁白、音效、特效、剪辑或全部方法层。
- [ ] 已记录用户要替换的变量：新主题、新角色、新场景、新道具、新台词、新风格、新画幅、新时长和新平台。
- [ ] 已询问用户是否准备了自己的角色、场景、道具、产品或素材包。
- [ ] 如果用户提供资产，已记录 `input_mode = REFERENCE_PLUS_USER_ASSETS` 和 `user_asset_manifest`。
- [ ] 禁止复制项已列出：原台词、原音乐、logo、名人脸、IP 符号、可识别场景。

## Shot Ledger

- [ ] 已完成 `media_probe`，并记录时长、分辨率、fps、codec、音频状态和画幅。
- [ ] 已完成 `frame_sampling_plan`，抽帧覆盖均匀帧、视觉变化点和音频分段边界。
- [ ] 15 秒以内片段已完成逐帧/逐变化拆解；0.5 秒接触表只作为导航，不作为唯一证据。
- [ ] 已完成 `frame_observations`，每帧都有主体、环境、镜头、光影、风格、情绪和风险标记。
- [ ] 已完成 `state_change_ledger`：角色变身/换装/法身前态、道具状态、法术升级、群体反应和终帧前态均已命名或标记为 `not present`。
- [ ] 已完成 `audio_transcript`，低置信 ASR 已标记人工确认。
- [ ] 已完成 `audio_segments`，台词只提炼功能，不复写原句。
- [ ] 已完成 `multimodal_sync`，音画事件、剪辑信号和叙事功能已对齐。
- [ ] 已输出 `shot_count_estimate` 或等效镜头数量判断。
- [ ] 每个切点都有证据：视觉突变、构图变化、景别变化、运镜变化、动作触发、声音/台词点或情绪点。
- [ ] 每个镜头有 `REF_###` 编号。
- [ ] 每个镜头有 timecode 和 duration。
- [ ] 每个镜头有叙事功能和情绪功能。
- [ ] 每个镜头有景别、角度、构图和运镜。
- [ ] 每个镜头有动作、调度、道具、光影、色彩、VFX、声音和剪辑点。
- [ ] 每个镜头都说明了与前后镜头如何连贯：动作、视线、线条方向、声音点、构图重心或情绪推进。
- [ ] 没有只写“电影感”“高级”“节奏好”这类空话。

## DNA Forensic Audit

- [ ] 已输出 `Frame Ledger`、`Shot Ledger`、`DNA Invariant Ledger` 和 `Omission Audit`。
- [ ] 已检查主角是否存在变身、能级升级、法身前态或终帧前态；如存在，已进入镜头表和 Seedance 中段动作，不只写在终帧。
- [ ] 已检查道具/法术机制是否有触发、扩散、回拉、升级和终帧结果。
- [ ] 已检查群体反应是否存在被勒停、冻结、击退、后仰、跪下、散开或聚拢。
- [ ] 已区分后期字幕、角色台词、旁白、咒语和 BGM；后期内容不会进入画面生成。
- [ ] `DNA_SIGNOFF: PASS` 后才进入资产、故事板或 Seedance。

## Preservation / Variation

- [ ] 每个保留项都是方法，不是可识别表达。
- [ ] 每个风险元素都有替换方案。
- [ ] 原片台词只保留功能，不保留原句。
- [ ] 原音乐只保留节奏功能，不保留素材。
- [ ] 品牌、logo、包装、IP、名人脸已替换。

## New Production Mapping

- [ ] 进入资产、故事板和 Seedance 前，已提供至少 3 个新片重构方向供用户选择，除非用户明确指定唯一方向。
- [ ] 每个参考镜头都有对应新片 segment。
- [ ] 每个新片 segment 有新剧情 beat。
- [ ] 每个新片 segment 绑定角色、场景和道具资产码。
- [ ] 如果用户提供自带资产，每个 segment 已绑定用户资产模块，并说明替代参考片中的哪个资产功能。
- [ ] 如果用户选择镜头节奏复刻，新片镜头数量、切点顺序和运镜逻辑已与参考片对齐。
- [ ] 动画转写实时已迁移材质、表演和摄影逻辑。
- [ ] 9:16 项目已完成竖屏构图迁移。

## User Asset Ingestion

- [ ] 如果用户提供角色图，已完成 `Visible / Inferred / Missing`，并基于用户图补全 M01-M08。
- [ ] 如果生成真人角色资产，已执行 GPT-image2 真人人像减法锁：没有默认堆叠 `ultra realistic`、`photorealistic`、`highly detailed`、`8k`、`masterpiece`、`best quality`、`sharp focus`、`film grain`、`Kodak Portra`、`85mm f/1.2`、`skin pores` 或 `subsurface scattering`。
- [ ] 真人角色资产风格锁使用商业摄影/影视人像、自然柔光、真实但克制皮肤质感；没有写“极致毛孔”“过度高清锐化”“假胶片颗粒”作为默认质量方向。
- [ ] 如果用户提供场景图，已完成 `Visible / Inferred / Missing`，并基于用户图补全 V01-V09 和 MAP。
- [ ] 如果用户提供道具图，已完成 `Visible / Inferred / Missing`，并基于用户图补全 P01-P08。
- [ ] 用户资产的脸、体型、服装、媒介风格、场景地理、道具形状、材质、比例和使用方式没有被参考片覆盖。
- [ ] 每个用户资产都有 `source_asset_id`、`media_dna`、`visible_lock`、`inferred_fill`、`missing_or_confirm`、`remake_function` 和 `module_reference_plan`。
- [ ] 如果用户资产与参考片方法冲突，已优先保护用户资产身份，并调整镜头调度。

## Storyboard

- [ ] 故事板 panel 数等于参考片镜头数；超过 10 镜已拆成多个故事板。
- [ ] 故事板布局符合镜头数：1-4 用 1x4/4x1，5-6 用 3x2，7-8 用 4x2，9-10 用 5x2。
- [ ] 每格包含 `SH## / timecode / 景别 / 运镜 / 动作 / active assets`。
- [ ] 每格基于当下剧情和当下节奏，不是重复姿势、空镜或泛化氛围图。
- [ ] 故事板明确引用资产图号和模块标签。
- [ ] 若导演审片故事板包含箭头、框线、标签、编号或文字说明，已额外生成 `S##_CLEAN_BW_STORYBOARD` 黑白手稿故事板，且 Seedance 上传图不含任何可被视频模型复制的版式标注。

## Seedance Reference

- [ ] 已选择 Seedance 交付支线：A 线资产直出 / B 线黑白故事板参考 / C 线无资产文本直出；并说明推荐先跑哪条。
- [ ] A 线没有上传故事板，所有身份、场景、道具只由资产图定义。
- [ ] B 线使用的是黑白手稿故事板，不是彩色关键帧或精修图。
- [ ] C 线仅在用户没有资产、没有要求资产/故事板、且明确只要一条 Seedance 提示词时使用；已说明角色/场景/道具一致性弱于 A 线，切点控制弱于 B 线。
- [ ] A/B 线 Seedance 提示词写明参考图号和标签，例如 `A01 / M03 FACE CLOSE-UP`、`A02 / V04 CAMERA A`、`A03 / P06 HAND LOGIC`；C 线不写不存在的资产编号，改用短而稳定的文本锚点。
- [ ] Seedance 提示词写明将提供的 `S01_CLEAN_BW_STORYBOARD / [列]x[行]` 黑白手稿故事板制作成流畅电影级动画视频，或明确标注 `S01_ANNOTATED_STORYBOARD` 只供导演理解、不作为图片输入。
- [ ] 15 秒以内短片的 Seedance 提示词是一条完整连续视频；逐镜 timing 是片内切点，不是多条独立视频或故事板翻页。
- [ ] Seedance 提示词要求保持 `SH01-SH##` 的镜头顺序、切点节奏、构图重心、动作方向和镜头连贯性。
- [ ] Seedance 提示词明确禁止渲染故事板边框、编号、箭头、文字标注或面板布局。
- [ ] Seedance 上传清单没有包含任何带蓝色箭头、红色框线、绿色标签、标题栏、编号、说明文字或白底故事板 UI 的图片。
- [ ] 若使用 B 线，故事板只控制运动、构图、镜头切点和动作方向，不控制角色身份、服装、脸、发型、道具形状或场景身份。
- [ ] 参考片文字若承担台词/咒语功能，只重写为新片原创声音/表演节奏，不作为画面字幕生成。
- [ ] Seedance 提示词包含逐镜 timing、Motion Continuity、Do Not Copy 和 Negative Prompt。

## Backend Handoff

- [ ] Markdown 结构完整。
- [ ] JSON 顶层字段完整。
- [ ] `asset_matrix` 使用稳定资产码。
- [ ] `segment_plan` runtime 在 4-15 秒之间。
- [ ] 精确文字进入 `UI_TEXT_*` 或 post duties。
- [ ] 后端指令为 `image2_seedance_2_0` 和 `asset_storyboard_seedance_prompt_factory`。

## Compliance

- [ ] 没有 high risk open 项。
- [ ] 所有 medium risk 有替换策略。
- [ ] `do_not_copy` 规则进入每个新片映射。
- [ ] 风格参考不覆盖身份、场景地理、道具和剧情事实。

## Validation

- [ ] 已运行 `python3 scripts/check_project.py`。
- [ ] 已运行 `python3 scripts/validate_handoff.py [handoff.json]`。
- [ ] 所有 errors 已修复。
- [ ] warnings 已确认并写明接受理由。
