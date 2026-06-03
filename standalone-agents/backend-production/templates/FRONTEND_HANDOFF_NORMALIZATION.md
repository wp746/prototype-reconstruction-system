# 前端交接标准化

当前端交付材料模糊、不完整或格式不标准时，先执行这一层，再进入后端生产。

## 输出格式

```text
FRONTEND_HANDOFF_NORMALIZATION:
input_quality: standard / usable_but_incomplete / vague / blocked
inferred_fields:
missing_fields:
assumptions:
needs_model_completion: yes / no
user_questions:
handoff_ready: yes / no
```

## 后端最舒服的前端标准

```text
- project/runtime/aspect/model 已知
- 至少有角色、场景、道具/机制，或明确不需要
- shot_count 和 storyboard_layout 已知
- 每个 SH 有 timecode、景别、构图、动作状态、运镜、动作方向、切点功能
- in_state/action_chain/out_state 清楚
- style_risk 包含风格跑偏、漏镜头、终帧风险
```

## 补齐规则

- 能保守推断的字段，补齐并标记 `inferred`。
- 不能推断的字段，列入 `missing_fields`。
- 用户允许模型补齐时，先输出标准 handoff，再进入后端生产。
- `handoff_ready = no` 时，不输出最终生产包。

## 模型补齐提示词

```text
请把以下模糊前端材料整理成 B 线后端生产可用 handoff。能保守推断的字段请补齐并标记 inferred；不能推断的字段列入 missing_fields。不要进入资产、故事板或 Seedance 生产，只输出标准 handoff。

[RAW_FRONTEND_INPUT]
...

[OUTPUT_FORMAT]
FRONTEND_HANDOFF_NORMALIZATION:
input_quality:
inferred_fields:
missing_fields:
assumptions:
needs_model_completion:
user_questions:
handoff_ready:

PROJECT:
...

FRONTEND_HANDOFF:
...

ASSET_PLAN:
...

SHOT_PLAN:
...

STYLE_RISK:
...
```

