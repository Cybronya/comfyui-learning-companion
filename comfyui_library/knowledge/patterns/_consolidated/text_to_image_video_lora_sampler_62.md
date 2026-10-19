---
name: text_to_image_video_lora_sampler_62
type: Text To Image
frequency: 11
level: strong
coverage: 0.745727
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json, 视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json, 视频生成/图生视频/MMH3 Selflift常规万能流，直出1080p最高质量版_2110447282897383425.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110255149494132737.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110369401181655042.json, 视频生成/图生视频/MiniMax H3 SelfLift数字人1080p图生视频处理工具_2101012772418052098.json, 视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json, 视频生成/图生视频/MiniMax H3 sigma强化+Selflift双采｜文不油武不糊小脸不崩_2108071344842821633.json, 视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json, 视频生成/图生视频/Selflift双采加sigma强化Minimax H3 多图音频参考视频生成_2110355179118882817.json, 视频生成/图生视频/超强Minimax H3 sigma强化加Selflift双采文不油武不糊全能多图3音频参考生视频量_2108279560327487489.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json、视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json、视频生成/图生视频/MMH3 Selflift常规万能流，直出1080p最高质量版_2110447282897383425.json、视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110255149494132737.json、视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110369401181655042.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 10/11 个有
- `ModelPreviewOverrideKJ` —— 9/11 个有
- `VAEDecodeAudio` —— 7/11 个有
- `PreviewAny` —— 6/11 个有
- `PrimitiveFloat` —— 6/11 个有
- `AudioCrop` —— 5/11 个有
- `GetNode` —— 5/11 个有
- `H3SigmaRefiner` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `LayerUtility: PurgeVRAM V2` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `Text Concatenate` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `easy seed` —— 5/11 个有
- `easy showAnything` —— 5/11 个有
- `Any To String (mtb)` —— 4/11 个有
- `ComfyNumberConvert` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `Float` —— 4/11 个有
- `LTXVAudioVAEEncode` —— 4/11 个有
- `LTXVConcatAVLatent` —— 4/11 个有
- `LoraLoaderBypassModelOnly` —— 4/11 个有
- `PreviewAudio` —— 4/11 个有
- `PrimitiveInt` —— 4/11 个有
- `SetLatentNoiseMask` —— 4/11 个有
- `SolidMask` —— 4/11 个有
- `SoundFlow_GetLength` —— 4/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `TrimAudioDuration` —— 3/11 个有
- `Int` —— 2/11 个有
- `Textbox` —— 2/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `JWStringToFloat` —— 1/11 个有
- `QwenH3PromptLocal` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（16/11 个样本）：Steps较低可能导致细节不足
