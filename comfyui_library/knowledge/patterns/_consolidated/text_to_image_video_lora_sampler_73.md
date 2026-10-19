---
name: text_to_image_video_lora_sampler_73
type: Text To Image
frequency: 10
level: strong
coverage: 0.6448
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3去油保护光影｜视频去AI油光质感自用款_2103073378214174722.json, 视频生成/图生视频/Minimax H3参考生视频+高动态｜图生视频生成_2095268329618497537.json, 视频生成/图生视频/Minimax H3参考生视频自用版｜高动态可出20s长片_2107687775708475394.json, 视频生成/图生视频/Minimax H3参考生视频高动态自用版可生成20秒以上视频工作流，图生视频方案_2107905533574471681.json, 视频生成/图生视频/MinimaxH3长视频生成｜高清不劣化图生视频_2095576583376556034.json, 视频生成/图生视频/二采首尾帧+参考音｜Minimax H3图生视频生成_2092586326188191745.json, 视频生成/图生视频/二采首尾帧参考音｜Minimax H3图生视频直出_2092337325798940674.json, 视频生成/图生视频/单采打戏流畅出片｜Minimax 图生视频动作拉满_2096266436170838018.json, 视频生成/图生视频/图生视频二采+1参考音｜Minimax H3批量API用_2094054081001250817.json, 视频生成/图生视频/长视频一键生成｜MinimaxH3图生视频续写_2095819929332314113.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_73

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax H3去油保护光影｜视频去AI油光质感自用款_2103073378214174722.json、视频生成/图生视频/Minimax H3参考生视频+高动态｜图生视频生成_2095268329618497537.json、视频生成/图生视频/Minimax H3参考生视频自用版｜高动态可出20s长片_2107687775708475394.json、视频生成/图生视频/Minimax H3参考生视频高动态自用版可生成20秒以上视频工作流，图生视频方案_2107905533574471681.json、视频生成/图生视频/MinimaxH3长视频生成｜高清不劣化图生视频_2095576583376556034.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 9/10 个有
- `ComfyMathExpression` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 8/10 个有
- `LTXVSeparateAVLatent` —— 6/10 个有
- `LayerColor: Brightness & Contrast` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `MinimaxH3LatentUpscaler3D` —— 6/10 个有
- `PT_H3ConcatAVLatent` —— 6/10 个有
- `LoadAudio` —— 5/10 个有
- `ResolutionSelector` —— 4/10 个有
- `SolAttnPatch` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `SplitSigmas` —— 3/10 个有
- `TrimAudioDuration` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `BlockSparseAttention` —— 2/10 个有
- `FrameInterpolate` —— 2/10 个有
- `FrameInterpolationModelLoader` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `MiniMaxH3AddGuide` —— 2/10 个有
- `CFGGuider` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `QwenH3PromptLocal` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
