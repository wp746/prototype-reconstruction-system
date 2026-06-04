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

STYLE_CONTRACT:
source_style_evidence:
render_style:
medium:
realism_level:
material_finish:
lighting_language:
lens_language:
color_palette:
forbidden_styles:
style_source: explicit / inferred_from_assets / inferred_from_reference / needs_user
```

## 后端最舒服的前端标准

```text
- project/runtime/aspect/model 已知
- 至少有角色、场景、道具/机制，或明确不需要
- shot_count 和 storyboard_layout 已知
- 每个 SH 有 timecode、景别、构图、动作状态、运镜、动作方向、切点功能
- in_state/action_chain/out_state 清楚
- style_contract 已明确或可靠推断，包含风格、媒介、真实度、材质、光线、镜头、色彩和禁用风格
- style_risk 包含风格跑偏、漏镜头、终帧风险
```

## 风格合同硬门槛

`STYLE_CONTRACT` 是后端生产准入字段。没有它，不进入资产提示词生产。

- 前端明确写了风格时，直接锁定。
- 前端没写风格但给了资产图、参考帧或物料描述时，保守推断并写明证据。
- 风格证据冲突时，先问用户哪个风格优先。
- 无法判断时，`handoff_ready = no`，只问最小问题。

最小问题：

```text
这个项目最终统一成哪种风格：3D 动画电影、真人电影感、动漫、卡通、超现实，还是其他？
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

STYLE_CONTRACT:
...
```
