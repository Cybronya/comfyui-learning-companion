---
name: text_to_image_lora_sampler_clip_107
type: Text To Image
frequency: 9
level: strong
coverage: 0.785222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json, 视频生成/图生视频/我自用的H3-w1_2094228023120846849.json, 视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json, 视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json, 视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json, 视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json, 视频生成/文生视频/MiniMax-H3全能参考｜长视频文生图生视频通吃出片_2101564544643592193.json, 视频生成/文生视频/全能参考生成视频｜MiniMax-H3文生图生视频_2095818212331048962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json、视频生成/图生视频/我自用的H3-w1_2094228023120846849.json、视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json、视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json、视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `LTXVConcatAVLatent` —— 6/9 个有
- `LTXVSeparateAVLatent` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `MinimaxH3LatentUpscaler3D` —— 6/9 个有
- `ModelAttentionBackend` —— 6/9 个有
- `ModelPreviewOverrideKJ` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `ExtendIntermediateSigmas` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `GetNode` —— 4/9 个有
- `MiniMaxH3SigmaShift` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `DisableNoise` —— 3/9 个有
- `SplitSigmas` —— 3/9 个有
- `SplitSigmasDenoise` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `H3SigmaRefiner` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `MiniMaxH3AddGuide` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `AudioCrop` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `FL_UnloadAllModels` —— 1/9 个有
- `ImageAddNoise` —— 1/9 个有
- `MiniMaxChunkFeedForward` —— 1/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/9 个有
- `PlaySound|pysssss` —— 1/9 个有
- `SolAttnMiniMax` —— 1/9 个有
- `Text` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

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
