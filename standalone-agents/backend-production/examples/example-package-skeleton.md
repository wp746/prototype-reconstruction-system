# 示例：B 线后端生产包骨架

这是结构示例，不是完整成片提示词。

## 0. 使用说明

绿色上传提醒只用于用户操作，不复制进生成模型。

## 0.1 前端交接标准化

```text
FRONTEND_HANDOFF_NORMALIZATION:
handoff_ready:

STYLE_CONTRACT:
render_style:
medium:
forbidden_styles:
```

## 0.2 元提示词编译链路

```text
META_PROMPT_COMPILE_TRACE:
- board_compiler: BOARD_META_PROMPT_COMPILER_V1
- character_asset_prompt: CHARACTER_BOARD_META_PROMPT_V1
- scene_asset_prompt: SCENE_BOARD_META_PROMPT_V1
- prop_asset_prompt: PROP_BOARD_META_PROMPT_V1
- storyboard_prompt: STORYBOARD_BOARD_META_PROMPT_V1
- seedance_video_prompt: SEEDANCE_VIDEO_META_PROMPT_V1
- final_package: B_LINE_SINGLE_MD_PACKAGE_TEMPLATE_V1
compile_status:
```

## 1. 阶段一：资产提示词

### 1.1 角色资产 / Character Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考角色，请上传 @图片1 = A01 / 角色参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
COMPILED_BY: CHARACTER_BOARD_META_PROMPT_V1
STYLE_CONTRACT_LOCK:
STYLE_NEGATIVE:
生成 A01 角色资产板……
```

#### EN_IMAGE2_PROMPT

```text
COMPILED_BY: CHARACTER_BOARD_META_PROMPT_V1
STYLE_CONTRACT_LOCK:
STYLE_NEGATIVE:
Generate the A01 character asset board...
```

## 2. 阶段二：干净故事板提示词

<span style="color:#15803d;font-weight:600;">上传提醒：生成故事板时请上传 @图片1 = A01，@图片2 = A03，@图片3 = A05。此提醒不属于提示词。</span>

```text
COMPILED_BY: STORYBOARD_BOARD_META_PROMPT_V1
TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID: S01_CLEAN_STORYBOARD_CONTROL
```

## 3. 阶段三：Seedance 2.0 视频提示词

<span style="color:#15803d;font-weight:600;">上传提醒：Seedance 请上传 @图片1 = A01、@图片2 = A03、@图片3 = A05、@图片4 = S01_CLEAN_STORYBOARD_CONTROL。此提醒不属于提示词。</span>

```text
COMPILED_BY: SEEDANCE_VIDEO_META_PROMPT_V1
[VIDEO TASK]
...

[REALISTIC CINEMA STYLE LOCK]
...

[NEGATIVE PROMPT]
...
```
