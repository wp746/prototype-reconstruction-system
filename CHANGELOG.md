# Changelog

## Unreleased

- 固定角色资产板模板为 `WHITE_HERO_FULLBODY_TURNAROUND_TEMPLATE`。
- 新增 `templates/character-asset-board-template-v2.md`，明确左大主全身、顶部完整全身转面、右侧脸部表情、下方动作材质色卡版式。
- 更新 README、SOP 和 Agent Cards，要求所有 `CHAR_*` Image2 资产提示词默认套用角色资产板固定模板 V2。
- 固定场景资产板模板为 `WHITE_SCENE_NINE_VIEW_LABEL_TEMPLATE`，要求 `V01`-`V09`、`MAP`、`CAM_A/B/C`、`CHAR_ZONE`、`PROP_ANCHOR`、`LIGHT_DIR`、`NO_DRIFT` 等可见稳定标签。
- 固定道具资产板模板为 `WHITE_PROP_MULTI_VIEW_LABEL_TEMPLATE`，要求 `P01`-`P08`、`REFERENCE USE`、`@PROP_CODE`、`HAND`、`SCENE_ANCHOR`、`DO_NOT_CHANGE` 等可见稳定标签。

## v0.1.0 - 2026-05-29

- 初始化原型重构多智能体工作流系统。
- 增加 A0-A11 Agent 职责卡。
- 增加 PromptLens 式视频分析模块：媒体探测、抽帧、单帧分析、序列分析、音频转写、音频分段、音画对齐。
- 增加 Markdown + JSON 后端交接模板。
- 增加 JSON Schema 和无依赖校验脚本。
- 增加 QA Checklist。
- 校验结果：`python3 scripts/validate_handoff.py templates/handoff-template.json` 通过，0 errors，0 warnings。
