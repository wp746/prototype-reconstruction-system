# 示例：B 线后端生产包骨架

这是结构示例，不是完整成片提示词。

## 0. 使用说明

绿色上传提醒只用于用户操作，不复制进生成模型。

## 1. 阶段一：资产提示词

### 1.1 角色资产 / Character Asset

<span style="color:#15803d;font-weight:600;">上传提醒：如需参考角色，请上传 @图片1 = A01 / 角色参考图。此提醒不属于提示词。</span>

#### ZH_IMAGE2_PROMPT

```text
生成 A01 角色资产板……
```

#### EN_IMAGE2_PROMPT

```text
Generate the A01 character asset board...
```

## 2. 阶段二：干净故事板提示词

<span style="color:#15803d;font-weight:600;">上传提醒：生成故事板时请上传 @图片1 = A01，@图片2 = A03，@图片3 = A05。此提醒不属于提示词。</span>

```text
TEMPLATE_CODE: CLEAN_STORYBOARD_CONTROL_TEMPLATE
BOARD_ID: S01_CLEAN_STORYBOARD_CONTROL
```

## 3. 阶段三：Seedance 2.0 视频提示词

<span style="color:#15803d;font-weight:600;">上传提醒：Seedance 请上传 @图片1 = A01、@图片2 = A03、@图片3 = A05、@图片4 = S01_CLEAN_STORYBOARD_CONTROL。此提醒不属于提示词。</span>

```text
[VIDEO TASK]
...

[REALISTIC CINEMA STYLE LOCK]
...

[NEGATIVE PROMPT]
...
```

