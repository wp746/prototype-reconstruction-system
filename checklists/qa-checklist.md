# QA Checklist

## Reference Intake

- [ ] 参考片来源已记录。
- [ ] 权限和复用边界已记录。
- [ ] 新主题、目标风格、画幅、平台、时长已记录。
- [ ] 禁止复制项已列出：原台词、原音乐、logo、名人脸、IP 符号、可识别场景。

## Shot Ledger

- [ ] 已完成 `media_probe`，并记录时长、分辨率、fps、codec、音频状态和画幅。
- [ ] 已完成 `frame_sampling_plan`，抽帧覆盖均匀帧、视觉变化点和音频分段边界。
- [ ] 已完成 `frame_observations`，每帧都有主体、环境、镜头、光影、风格、情绪和风险标记。
- [ ] 已完成 `audio_transcript`，低置信 ASR 已标记人工确认。
- [ ] 已完成 `audio_segments`，台词只提炼功能，不复写原句。
- [ ] 已完成 `multimodal_sync`，音画事件、剪辑信号和叙事功能已对齐。
- [ ] 每个镜头有 `REF_###` 编号。
- [ ] 每个镜头有 timecode 和 duration。
- [ ] 每个镜头有叙事功能和情绪功能。
- [ ] 每个镜头有景别、角度、构图和运镜。
- [ ] 每个镜头有动作、调度、道具、光影、色彩、VFX、声音和剪辑点。
- [ ] 没有只写“电影感”“高级”“节奏好”这类空话。

## Preservation / Variation

- [ ] 每个保留项都是方法，不是可识别表达。
- [ ] 每个风险元素都有替换方案。
- [ ] 原片台词只保留功能，不保留原句。
- [ ] 原音乐只保留节奏功能，不保留素材。
- [ ] 品牌、logo、包装、IP、名人脸已替换。

## New Production Mapping

- [ ] 每个参考镜头都有对应新片 segment。
- [ ] 每个新片 segment 有新剧情 beat。
- [ ] 每个新片 segment 绑定角色、场景和道具资产码。
- [ ] 动画转写实时已迁移材质、表演和摄影逻辑。
- [ ] 9:16 项目已完成竖屏构图迁移。

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

- [ ] 已运行 `python3 scripts/validate_handoff.py [handoff.json]`。
- [ ] 所有 errors 已修复。
- [ ] warnings 已确认并写明接受理由。
