---
name: text_to_image_video_lora_sampler_142
type: Text To Image
frequency: 5
level: strong
coverage: 0.597
common_nodes: [AudioCrop, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, SetNode, Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy seed, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json, 视频生成/图生视频/MiniMax H3 sigma强化+Selflift双采｜文不油武不糊小脸不崩_2108071344842821633.json, 视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json, 视频生成/图生视频/Selflift双采加sigma强化Minimax H3 多图音频参考视频生成_2110355179118882817.json, 视频生成/图生视频/超强Minimax H3 sigma强化加Selflift双采文不油武不糊全能多图3音频参考生视频量_2108279560327487489.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_142

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json、视频生成/图生视频/MiniMax H3 sigma强化+Selflift双采｜文不油武不糊小脸不崩_2108071344842821633.json、视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json、视频生成/图生视频/Selflift双采加sigma强化Minimax H3 多图音频参考视频生成_2110355179118882817.json、视频生成/图生视频/超强Minimax H3 sigma强化加Selflift双采文不油武不糊全能多图3音频参考生视频量_2108279560327487489.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any To String (mtb)` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `Float` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `PreviewAudio` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `ComfyNumberConvert` —— 1/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `LTXVAudioVAEEncode` —— 1/5 个有
- `LTXVConcatAVLatent` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `SolidMask` —— 1/5 个有
- `SoundFlow_GetLength` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
