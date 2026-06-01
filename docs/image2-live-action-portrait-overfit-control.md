# Image2 真人人像防过拟合减法规则

来源沉淀：用户提供的 94vanAI X Article《愿你习得此文，成就无双人像生图神功》。该文的核心判断是：GPT-image2 真人人像不适合 Nano Banana 式长提示词堆砌，更适合极简、高信号、少冲突的提示词。

## 核心结论

真人资产出图的过拟合，不只靠负面词解决。更关键的是前半段提示词必须做减法，避免模型被重复质量词、复杂相机参数和冲突质感拉向“AI 后期味”。

## 常见翻车源

- 质量词重复：`ultra realistic`、`photorealistic`、`highly detailed`、`8k`、`masterpiece`、`best quality`、`sharp focus` 同时出现，会诱导过度锐化和过度完成。
- 相机参数过载：`85mm f/1.2`、`Kodak Portra`、`film grain`、`cinematic bokeh` 等堆在一起，会让模型模拟滤镜而不是塑造真人。
- 质感冲突：自然皮肤、胶片颗粒、过度高清、柔和空气感、锐利对焦同时出现，会产生妥协渲染。
- 毛孔误用：`skin pores`、`micro pores`、`subsurface scattering` 在真人资产里只能谨慎使用；默认不写“极致毛孔”。

## 推荐结构

中文：

```text
商业杂志风格专业人像写真，{主体身份与外貌锚点}，{情绪/姿态}，自然柔和光影，干净真实摄影质感，真实但克制的皮肤质感。
```

English:

```text
Commercial magazine editorial portrait of {subject}, {mood / pose}, natural soft lighting, clean professional photography style, realistic but controlled skin texture.
```

## 项目落地规则

- `templates/character-asset-board-template-v2.md` 的真人电影写实风格锁必须使用“商业摄影 + 自然柔光 + 克制皮肤质感”，不得再默认写“极致皮肤/微观毛孔”。
- 真人资产提示词先控制在 50-100 个汉字的核心描述内；如果用户需要资产板结构，再由模板补 M01-M08 模块，而不是把摄影词堆进风格锁。
- 相机语言只保留一个整体方向，例如“专业人像摄影 / 自然浅景深 / editorial lighting”，不要写完整镜头参数清单。
- 先极简出第一版，再按问题单点修复：脸假加真实皮肤，光硬加自然柔光，背景乱加干净背景，网红味重加商业编辑感。
- 角色资产风格锁最后仍拼接 Image2 抗过拟合不变量：平滑阴影、柔和光照、可控细节、最小化纹理、高清晰度、精致边缘、平滑渐变；不要噪点、颗粒、人工痕迹、高频细节、脏乱纹理、过度锐化、斑驳、混乱细节。

## 禁止默认写入真人人像风格锁

```text
ultra realistic, photorealistic, highly detailed, 8k, masterpiece, best quality, sharp focus, film grain, Kodak Portra, 85mm f/1.2, cinematic bokeh, subsurface scattering, extreme pores, micro pores
```

这些词不是永远不能用，而是不能作为默认堆叠项。只有当用户明确要某种摄影测试或特定质感时，才单独、少量、可控地加入。
