---
name: text_to_image_lora_sampler_clip_68
type: Text To Image
frequency: 13
level: strong
coverage: 0.905077
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [MiniMaxH3EasyLoader, MiniMaxH3EasyMediaLoader]
members: [视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json, 视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json, 视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json, 视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json, 视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json, 视频生成/文生视频/H3六步文生视频短片预检版｜六步走完从想法到成片_2099146163709628418.json, 视频生成/文生视频/MiniMax H3 Easy Hybrid全能参考极简多合一工作流_文生视频图_2105737236565282818.json, 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json, 视频生成/文生视频/Minimax H3开源加速版Lora6步直出1080P-文生视频短剧人物特效_2087379686644084738.json, 视频生成/文生视频/Minimax-H3加速一站式-文生视频图生视频工作流_2087399914660777986.json, 视频生成/文生视频/minimaxlora）ENG加速一站式工作流（文生视频图生视频首尾帧全能参考加速ENG_2087115789043331074.json, 视频生成/文生视频/加速lora一站式｜minimax文生图生视频首尾帧全能参考_2092878945308991490.json, 视频生成/文生视频/海螺Minimax H3开源版文生视频H3加速Lora6步直出1080P_2086443392405430273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json、视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json、视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json、视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json、视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3Easy` —— 12/13 个有
- `MiniMaxH3EasyLoader` —— 12/13 个有
- `MiniMaxH3EasyOutput` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `CreateVideo` —— 10/13 个有
- `PathchSageAttentionKJ` —— 10/13 个有
- `SaveVideo` —— 10/13 个有
- `BasicScheduler` —— 9/13 个有
- `KSamplerSelect` —— 9/13 个有
- `ImageResizeKJv2` —— 4/13 个有
- `LoadImage` —— 4/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/13 个有
- `MiniMaxH3SigmaShift` —— 4/13 个有
- `PrimitiveStringMultiline` —— 3/13 个有
- `SpectrumSDXL` —— 3/13 个有
- `VHS_VideoCombine` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `MiniMaxH3EasyMediaLoader` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `LoadVideo` —— 1/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `SFH3MultimodalDirector` —— 1/13 个有
- `SpectrumApplyMiniMaxH3` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：MiniMaxH3EasyLoader、MiniMaxH3EasyMediaLoader
