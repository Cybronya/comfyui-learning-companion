---
name: text_to_image_video_lora_sampler_24
type: Text To Image
frequency: 23
level: strong
coverage: 0.788261
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json, 视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json, 视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频 漫剧工作流，角色设计图生视频方案_2107927267103035393.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频短剧漫剧工作流，角色设计图生视频方案_2107965040040177666.json, 视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json, 视频生成/图生视频/Minimax海螺H3加速版｜图生视频8步高质量，极速出片_2099892617046740993.json, 视频生成/图生视频/Minimax海螺h3图生视频8步极速优化版t8｜高质量加速_2100809902179573761.json, 视频生成/图生视频/SLA脸部动作稳定版｜Minimax-H3开源参考生视频角色一致_2091613796845572097.json, 视频生成/图生视频/SLA脸部动作稳定｜Minimax-H3参考生视频角色一致性_2091785773665316865.json, 视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json, 视频生成/图生视频/双采样潜空间放大DSW｜MiniMax H3二次优化生成_2095951614468251650.json, 视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json, 视频生成/图生视频/潜空间放大二次优化｜MiniMax H3 双采样DSW图生视频_2096239277662363650.json, 视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json, 视频生成/文生视频/H3电影级LORA双采去油PRO版 巅峰画质视频生成_2098288538583392257.json, 视频生成/文生视频/MiniMax H3多合一极速生视频｜二采优化全能工作流_2097533751998898178.json, 视频生成/文生视频/MiniMax H3武戏全能视频V3｜打斗高质量生成_2095598787678007297.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json、视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json、视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json、视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json、视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 22/23 个有
- `孤海注释` —— 21/23 个有
- `LoraLoaderBypassModelOnly` —— 19/23 个有
- `MiniMaxH3AVDecodeT8` —— 18/23 个有
- `CR Prompt Text` —— 17/23 个有
- `MiniMaxH3AudioConditioningT8` —— 15/23 个有
- `MiniMaxH3DualClockSamplerT8` —— 14/23 个有
- `ModelAttentionBackend` —— 13/23 个有
- `SolAttnMiniMax` —— 11/23 个有
- `BasicScheduler` —— 10/23 个有
- `KSamplerSelect` —— 10/23 个有
- `GetNode` —— 8/23 个有
- `MiniMaxH3ReferenceToVideo` —— 8/23 个有
- `SetNode` —— 8/23 个有
- `LoadAudio` —— 7/23 个有
- `LTXVSeparateAVLatent` —— 6/23 个有
- `MinimaxH3LatentUpscaler3D` —— 6/23 个有
- `PT_H3ConcatAVLatent` —— 6/23 个有
- `VHS_LoadVideo` —— 6/23 个有
- `SaveImage` —— 5/23 个有
- `Text` —— 5/23 个有
- `VAEDecodeAudio` —— 5/23 个有
- `Fast Groups Bypasser (rgthree)` —— 4/23 个有
- `ImageResizeKJv2` —— 4/23 个有
- `LTXVConcatAVLatent` —— 4/23 个有
- `SplitSigmas` —— 4/23 个有
- `VAEEncode` —— 4/23 个有
- `Float` —— 3/23 个有
- `H3SigmaRefiner` —— 3/23 个有
- `Label (rgthree)` —— 2/23 个有
- `easy cleanGpuUsed` —— 2/23 个有
- `ExtendIntermediateSigmas` —— 1/23 个有
- `PreviewImage` —— 1/23 个有
- `easy float` —— 1/23 个有
- `忽略多组孤海` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（24/23 个样本）：Steps较低可能导致细节不足
