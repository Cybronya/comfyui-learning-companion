---
name: text_to_image_video_upscale_latent_upscale_9
type: Text To Image
frequency: 7
level: strong
coverage: 0.610571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2采五段加速流 视频生成加速方案高效出片_2104985692295229442.json, 视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json, 视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json, 视频生成/图生视频/H3多参考双采5秒一致性版 Singularity精修短片_2098842004485664770.json, 视频生成/图生视频/H3多参考双采5秒一致性版｜多图参考短平快出片不跑脸_2099124913448767489.json, 视频生成/图生视频/MiniMax H3多参考生视频无限流五段二采串联处理工具_2102166646034100225.json, 视频生成/图生视频/五段式加速二采工作流｜角色表演视频一次成型｜图生视频高效出片_2104743299977400322.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2采五段加速流 视频生成加速方案高效出片_2104985692295229442.json、视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json、视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json、视频生成/图生视频/H3多参考双采5秒一致性版 Singularity精修短片_2098842004485664770.json、视频生成/图生视频/H3多参考双采5秒一致性版｜多图参考短平快出片不跑脸_2099124913448767489.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 6/7 个有
- `easy float` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `ModelAttentionBackend` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `LoadAudio` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `AudioConcat` —— 3/7 个有
- `GetImageRangeFromBatch` —— 3/7 个有
- `ImageBatchMulti` —— 3/7 个有
- `MiniMaxH3AddGuide` —— 3/7 个有
- `SaveAudio` —— 3/7 个有
- `TrimAudioDuration` —— 3/7 个有
- `BlockSparseAttention` —— 2/7 个有
- `Lora Loader Stack (rgthree)` —— 2/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `SolAttnMiniMax` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `GH_AudioVideoMerger` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `LayerColor: ColorAdapter` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
