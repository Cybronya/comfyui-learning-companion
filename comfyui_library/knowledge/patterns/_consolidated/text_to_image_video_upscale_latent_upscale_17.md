---
name: text_to_image_video_upscale_latent_upscale_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.56125
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfySwitchNode, Compare, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, Int, InversionDemoLazySwitch, JjkText, JoinStrings, KSampler, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SimpleMath+, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2106916761093361666.json, 数字人/数字人/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2112834608520851457.json, 视频生成/图生视频/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2108367943712206849.json, 视频生成/图生视频/图片对口型数字人说话唱歌LTV2.0人物类特效图生视频_2095738274433294338.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2106916761093361666.json、数字人/数字人/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2112834608520851457.json、视频生成/图生视频/LTX2.3图片数字人V1工作流，音频驱动数字人对口型图生图处理工具_2108367943712206849.json、视频生成/图生视频/图片对口型数字人说话唱歌LTV2.0人物类特效图生视频_2095738274433294338.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `Compare`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `InversionDemoLazySwitch`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `VHS_LoadAudioUpload` —— 3/4 个有
- `孤海注释` —— 2/4 个有
- `LTXVChunkFeedForward` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
