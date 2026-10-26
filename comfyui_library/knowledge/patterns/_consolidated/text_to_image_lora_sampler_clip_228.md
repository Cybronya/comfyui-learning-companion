---
name: text_to_image_lora_sampler_clip_228
type: Text To Image
frequency: 9
level: strong
coverage: 0.913556
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/极速MiniMax H3多参考视频 双重采样1080P长视频处理工具_2113042498112282626.json, 视频生成/文生视频/MiniMax H3 Easy Hybrid全能参考极简多合一工作流，文生视频图生视频方案_2105737236565282818.json, 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json, 视频生成/文生视频/Minimax H3开源加速版Lora6步直出1080P-文生视频短剧人物特效_2087379686644084738.json, 视频生成/文生视频/Minimax-H3加速一站式-文生视频图生视频工作流_2087399914660777986.json, 视频生成/文生视频/minimaxlora）ENG加速一站式工作流（文生视频图生视频首尾帧全能参考加速ENG_2087115789043331074.json, 视频生成/文生视频/加速lora一站式｜minimax文生图生视频首尾帧全能参考_2092878945308991490.json, 视频生成/文生视频/多合一极简工作流｜那颗星星MinimaxH3视频生成_2093449231817330689.json, 视频生成/文生视频/海螺Minimax H3开源版文生视频H3加速Lora6步直出1080P_2086443392405430273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_228

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/极速MiniMax H3多参考视频 双重采样1080P长视频处理工具_2113042498112282626.json、视频生成/文生视频/MiniMax H3 Easy Hybrid全能参考极简多合一工作流，文生视频图生视频方案_2105737236565282818.json、视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json、视频生成/文生视频/Minimax H3开源加速版Lora6步直出1080P-文生视频短剧人物特效_2087379686644084738.json、视频生成/文生视频/Minimax-H3加速一站式-文生视频图生视频工作流_2087399914660777986.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 8/9 个有
- `RandomNoise` —— 8/9 个有
- `SamplerCustomAdvanced` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `BasicScheduler` —— 6/9 个有
- `KSamplerSelect` —— 6/9 个有
- `MiniMaxH3EasyMediaLoader` —— 3/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `SpectrumApplyMiniMaxH3` —— 2/9 个有
- `SpectrumSDXL` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `MiniMaxH3VAEDecodeFast` —— 1/9 个有
- `SelfLiftAvatarH3Sampler` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
