# 后端生产 Agent

这是从原型重构系统 B 线单独拎出来的后端生产 agent。

它只负责后端闭环生产，不负责前端创意收集、参考片 DNA 拆解、需求选择或多 agent 协作调度。无论前端入口来自短片复刻、长片重构、广告、漫剧、文旅、产品片或其他方向，只要中间管道已经给出可生产的 B 线输入，本 agent 都按同一套后端逻辑输出最终生产文件。

## Agent 名称

`后端生产`

## 核心用途

把前端和中间多 agent 管道交付的 B 线材料，固定生产为一个 Markdown 文件：

1. 资产提示词：角色、场景、道具。
2. 干净故事板提示词：`S##_CLEAN_STORYBOARD_CONTROL`。
3. Seedance 2.0 视频提示词：资产 + 干净故事板 + `SEEDANCE_MOTION_TEXT` 全能参考。

最终只输出一个 `.md` 文件，提示词全部双语。

## 输入要求

前端或中间管道必须提供：

- 项目名。
- B 线段落编号，例如 `SEG01`。
- 时长与画幅，例如 `15 秒 / 16:9`。
- 角色需求或角色资产。
- 场景需求或场景资产。
- 道具需求或道具资产。
- 镜头数量与故事板布局，例如 `SH01-SH08 / 4x2`。
- 每个镜头的剧情功能、构图、动作状态、运镜、动作方向、切点功能。
- 当前最容易跑偏的风格风险，例如动漫化、游戏 CG、广告棚拍、塑料质感、资产漂移、终帧错误。

如果前端没有给出这些字段，本 agent 不能假装已经完成前端拆解；必须要求前端补齐。

## 输出原则

- 只输出一个 `.md` 文件。
- 绿色上传提醒写在提示词外，不复制进 Image2 或 Seedance。
- 所有提示词双语输出。
- 资产编号固定服务于后续引用，例如 `A01`、`A03`、`A05`。
- 故事板必须是干净视觉控制板，不画箭头、运动线、时间码、编号或文字说明。
- 运镜、动作方向、速度和切点功能写入 `SEEDANCE_MOTION_TEXT`。
- Seedance 视频提示词必须明确引用 `@图片编号 / 资产编号 / 模块标签`。
- `[REALISTIC CINEMA STYLE LOCK]` 和 `[NEGATIVE PROMPT]` 必须根据当前项目的真实跑偏风险动态编写。

## 文件说明

- [AGENT.md](AGENT.md)：后端生产 agent 的完整执行指令。
- [templates/B_LINE_SINGLE_MD_PACKAGE_TEMPLATE_V1.md](templates/B_LINE_SINGLE_MD_PACKAGE_TEMPLATE_V1.md)：最终单文件生产包模板。
- [templates/UPLOAD_REMINDER_STYLE.md](templates/UPLOAD_REMINDER_STYLE.md)：绿色上传提醒规范。
- [templates/FRONTEND_HANDOFF_NORMALIZATION.md](templates/FRONTEND_HANDOFF_NORMALIZATION.md)：模糊前端交接的预检与补齐标准。
- [schemas/backend-production-input.schema.json](schemas/backend-production-input.schema.json)：建议输入字段 schema。
- [examples/example-package-skeleton.md](examples/example-package-skeleton.md)：最终交付文件骨架示例。

## 作为 Skill 分享给同事

如果同事使用 Codex / agent skill，可以直接复制仓库里的：

```text
skills/backend-production/
```

到本机：

```text
~/.codex/skills/backend-production/
```

复制后在新会话里可以这样调用：

```text
使用 $backend-production，把这份 B 线 handoff 生成一个双语后端生产 Markdown 包。
```
