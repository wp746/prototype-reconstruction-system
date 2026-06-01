# Changelog

## Unreleased

- 暂无。

## v0.3.0 - 2026-06-02

- 新增 [docs/global-three-branch-remake-system.md](docs/global-three-branch-remake-system.md)：把复刻/重构系统的 A/B/C 三条支线经验全局化，沉淀资产职责隔离、黑白故事板控制、纯文本 C 线因果锁、跨支线失败诊断和拆段生成规则。
- 更新 `README.md` 首页“三支线速览”，让 A/B/C 线的使用场景、输入条件、控制目标、风险和 86/95 质量基准在 GitHub 首页可直接读取。
- 新增 [docs/dna-forensic-audit-system.md](docs/dna-forensic-audit-system.md)：所有复刻任务在生产前必须通过 `DNA_SIGNOFF`，15 秒以内片段执行逐帧/逐变化拆解，并强制审核主角变身、道具机制、法术升级、群体反应和终帧前态，防止漏掉核心 DNA。
- 沉淀 GPT-image2 真人人像防过拟合“减法锁”：真人资产提示词优先短、准、统一，禁止默认堆叠质量词、复杂相机参数、胶片颗粒和极致毛孔词。
- 新增 [docs/image2-live-action-portrait-overfit-control.md](docs/image2-live-action-portrait-overfit-control.md)，并将角色资产模板中的真人电影写实风格锁从“极致毛孔”改为“商业摄影/影视人像 + 自然柔光 + 克制真实肤感”。
- 将“Image2 去除过拟合噪点提示词”（来源：鲤鱼老师）加入资产板与故事板图像生成风格锁；中文提示词使用中文抗噪声明，英文提示词使用英文原句。
- 升级风格锁为“变量 + 不变量”编译规则：不同角色、场景、道具、故事板和媒介风格必须替换当下资产变量，再拼接抗过拟合不变量，避免机械复制同一条风格锁。
- 新增 `REFERENCE_PLUS_USER_ASSETS` 分支：当用户提供自己的角色、场景、道具、产品或素材包时，先做用户资产摄取和资产板补全，再用这些资产去承接参考片镜头方法。
- 新增 `scripts/check_project.py` 仓库级健康检查脚本，统一检查必需文件、Markdown 本地链接、handoff JSON 模板和本地 `outputs/` 样例交付包。
- 修正 `README.md` Quick Start 和仓库结构排版，补充 `outputs/` 本地样例产物的提交边界。
- 更新 QA 发布检查项，要求发布前运行仓库级健康检查。
- 新增 `docs/remake-reconstruction-protocol.md`，把复刻需求收集、多维 DNA 拆解、变量/不变量映射、故事板镜头数规则和 Seedance 显式引用规则固化为前置协议。
- 更新 SOP、Agent Cards 和视频分析模块：复刻任务必须先询问用户要复刻哪些层，15 秒内片段必须确认镜头数量和切点证据。
- 升级故事板规则：故事板格数必须等于参考片镜头数，超过 10 镜拆成多个故事板。
- 新增 `templates/seedance-reference-prompt-template-v1.md`，要求 Seedance 明确引用 `A01 / M03`、`A02 / V04`、`A03 / P06` 等资产图号和模块标签，并明确引用几乘几故事板。
- 新增 `templates/remake-master-agent-prompt-v1.md`，沉淀一版可直接复用的复刻与原型重构总控提示词。
- 新增创意方向门禁：进入资产、故事板和 Seedance 前，必须至少提供 3 个新片重构方向供用户选择。

## v0.2.0 - 2026-05-31

### 1. 核心升级：大师级“解耦风格锁”（Decoupled Style Lock）
- **画质常数（不变层）**：提取出 16 个超高画质、防脏、防过度锐化的负反馈/正反馈约束常量（例如`平滑阴影、柔光处理、细节控制、无噪点、无过度锐化`等）。
- **媒介/质感变量（变化层）**：解耦出电影写实、日系动漫、美式 3D 卡通、超现实画境 4 套预设公式，按需动态填入。
- **模板升级**：将“解耦风格锁标准”深度融入 `templates/` 下的所有核心资产板模板中。

### 2. 双语隔离协议（Bilingual Segregation Protocol）
- 彻底禁止在同一个资产板内混排中英文标签。
- 引入**纯中文标签版式**（使用`正面全身`、`场景示意图`等）和**纯英文标签版式**（使用`FRONT`、`MAP`等），满足出图时纯中文/纯英文输入的一致性要求。

### 3. 视频编排（Seedance 2.0）与 12s 预算控制
- 引入严格的 12 秒视频生成控制预算，明确 `0.0s - 3.0s`（In-state/动作诱导）与 `3.0s - 12.0s`（主体高保真运动及平滑出场）的精密时序编排。
- 在 Image2 提示词模板中完全移除了结尾多余的 `--ar 16:9` 参数，避免解析器和生成器参数冲突，提供更纯净的提示词输出。

### 4. 核心自动化脚本与文档库更新
- 重构并硬编码 `/Users/wangpeng/.gemini/antigravity/brain/cc20ea06-5428-4a49-81a1-31107a6e40f0/scratch/generate_v3_package.py`，全量自动化生成符合 V2/V3 规范的新武侠和打工人原型重构交付包。
- 升级全局 `README.md` 系统说明与 SOP 指引，确保系统架构与前沿实践百分百同步。

## v0.1.0 - 2026-05-29

- 初始化原型重构多智能体工作流系统。
- 增加 A0-A11 Agent 职责卡。
- 增加 PromptLens 式视频分析模块：媒体探测、抽帧、单帧分析、序列分析、音频转写、音频分段、音画对齐。
- 增加 Markdown + JSON 后端交接模板。
- 增加 JSON Schema 和无依赖校验脚本。
- 增加 QA Checklist。
- 校验结果：`python3 scripts/validate_handoff.py templates/handoff-template.json` 通过，0 errors，0 warnings。
