# Changelog

## v0.1.0 - 2026-05-29

- 初始化原型重构多智能体工作流系统。
- 增加 A0-A11 Agent 职责卡。
- 增加 PromptLens 式视频分析模块：媒体探测、抽帧、单帧分析、序列分析、音频转写、音频分段、音画对齐。
- 增加 Markdown + JSON 后端交接模板。
- 增加 JSON Schema 和无依赖校验脚本。
- 增加 QA Checklist。
- 校验结果：`python3 scripts/validate_handoff.py templates/handoff-template.json` 通过，0 errors，0 warnings。
