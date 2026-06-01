# DNA Forensic Audit System

本系统用于防止复刻/原型重构任务在前期漏掉原片 DNA。任何参考片、短片、片段或链接，在进入资产、故事板、Seedance 提示词之前，必须先通过本审核系统。

## 1. 核心原则

不能只做“看起来像”的宏观拆解。必须先把原片拆成可验证证据，再进入创作迁移。

硬规则：

- 本系统适用于任何长度的片子：短片、广告、漫剧片段、MV、文旅片、比赛片、长片段落。片子越长，先分段；每个被复刻段落都必须独立完成全维度 DNA 拆解和审核。
- DNA 不是单一镜头节奏。每次拆解和审核都必须同时覆盖剧情、分镜、运镜、表演、角色状态、场景、道具、服化道、构图、光影、色彩、声音、台词/旁白、剪辑、节奏、VFX、状态变化、群体反应、终帧 payoff 和后期元素边界。
- 任何维度不能因为“当前用户没强调”就默认跳过。用户可以选择最终复刻哪一部分，但分析阶段必须把所有维度看全。
- 15 秒以内片段：逐帧/逐变化拆解，至少输出 0.25 秒级联系表，并补充所有视觉突变点、动作变化点、形态变化点。
- 15-60 秒短片：先按段落切成 5-15 秒单元，每个单元执行同样的逐帧/逐变化拆解。
- 长片：先做全片结构段落表，再对用户要复刻的段落逐帧/逐变化拆解；每个被复刻段落必须独立通过 DNA 审核。
- 只要画面中出现“状态变化”，必须单独命名：变身、换装、武器展开、法术升级、角色显形、空间转换、群体反应、终帧形态变化等。
- 没有 `DNA_SIGNOFF: PASS`，不得输出资产提示词、故事板提示词或 Seedance 提示词。

## 2. 三层证据表

每个参考片都必须产出三张表。

### 2.1 Frame Ledger

逐帧或高密度帧观察表，记录“每一帧看见了什么变化”。

字段：

```text
frame_id
timecode
visual_state
main_subject
body_state
wardrobe_state
prop_state
vfx_state
camera_state
composition_state
sound_or_dialogue_state
new_information
possible_hidden_function
```

`possible_hidden_function` 专门用于捕捉“看见了但还没命名”的东西。例如：角色身上甲胄展开、衣袍被线拉开、身体被抬起，这不能只写成“动作变化”，必须标记为“疑似变身/形态升级”。

### 2.2 Shot Ledger

镜头表，记录镜头切点和镜头功能。

字段：

```text
SH##
start-end
duration
cut_evidence
shot_size
camera_move
composition_center
main_action
character_state_change
prop_or_vfx_state_change
sound_function
narrative_function
continuity_link
```

`character_state_change` 和 `prop_or_vfx_state_change` 不得为空。如果没有变化，必须写 `none observed`，不能省略。

### 2.3 DNA Invariant Ledger

DNA 不变量表，记录要迁移的“方法层”。

必须覆盖：

```text
shot_count
cut_timing
camera_path
composition_logic
character_entrance
performance_state
transformation_or_state_change
prop_trigger
vfx_trigger
group_reaction
dialogue_or_caption_function
sfx_function
final_payoff
```

如果参考片没有某项，写 `not present`；如果存在但不确定，写 `uncertain / needs review`。禁止因为不确定就跳过。

## 3. 多维漏项审计

逐帧拆完后，必须做一次“漏项审计”。逐项追问：

| Audit Item | Required Question |
|---|---|
| 剧情结构 | 片子的信息释放、转折、悬念、反转、爆点、收束是否都被命名？ |
| 镜头结构 | 镜头数量、切点、景别推进、镜头顺序和段落结构是否确认？ |
| 运镜组合 | 推拉摇移跟、升降、旋转、手持、锁定、速度曲线和组合方式是否记录？ |
| 构图逻辑 | 主体重心、视觉引导线、前中后景、负空间、安全区和终帧构图是否记录？ |
| 主体状态 | 主角是否发生姿态、身份、服装、形态、位置或能级变化？ |
| 变身/升级 | 是否存在从人形到战斗形态、法相前态、终帧形态的中间过程？ |
| 表演动作 | 眼神、手势、姿态、步伐、身体重心、情绪变化是否被命名？ |
| 服化道 | 服装、发型、妆容、甲胄、配饰、材质状态是否发生变化？ |
| 场景空间 | 空间入口、出口、地理关系、机位区、角色区、道具锚点是否被确认？ |
| 道具机制 | 道具是否只出现，还是触发了动作、空间、群体或特效变化？ |
| 法术/VFX | 特效是否有触发点、扩散点、回拉点、升级点、终帧点？ |
| 群体反应 | 群体是否被击退、冻结、勒停、跪下、后仰、散开、聚拢？ |
| 台词/字幕 | 文字/台词是后期字幕、角色台词、旁白、咒语还是信息提示？ |
| 声音 | 声音是否驱动切点、动作、冲击或终帧余韵？ |
| 剪辑节奏 | 快切、停顿、动作匹配、视线匹配、声音切点和锁帧位置是否记录？ |
| 光影色彩 | 光源方向、色温、对比度、主色、材质反光和后期调色是否记录？ |
| 后期边界 | BGM、字幕、水印、平台标识、后期音效是否已从画面生成中剥离？ |
| 终帧 | 终帧是突然出现，还是由前面动作/特效/变身因果推出来？ |

任一项回答为“有可能但未确认”，必须回到帧表补证据。

## 4. DNA Signoff Gate

进入生产前必须输出：

```text
DNA_SIGNOFF: PASS / FAIL
shot_count_verified: yes/no
frame_ledger_complete: yes/no
state_changes_named: yes/no
transformation_checked: yes/no
prop_vfx_causality_checked: yes/no
group_reaction_checked: yes/no
dialogue_caption_separated: yes/no
bgm_post_separated: yes/no
final_prompt_source_free: yes/no
```

任一关键项为 `no`，不得进入资产、故事板、Seedance。

## 5. 对当前项目的修正教训

`夺命.mov` 的 A 线 v006-v008 漏掉了主角变身过程。错误原因不是 Seedance，而是前期 DNA 审核没有把中段“人形操线 -> 金属战斗形态/法身前态 -> 最终法相”的状态变化单独命名。

以后遇到类似片段，必须在 Frame Ledger 和 DNA Invariant Ledger 里显式检查：

```text
transformation_or_state_change:
human/control state -> armor/body mechanism reveals -> powered battle form -> final avatar/dharma form
```

如果存在这一层，Seedance 提示词必须把它写进中段镜头，而不是只在终帧写法相。
