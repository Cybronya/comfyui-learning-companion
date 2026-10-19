---
name: image_to_image_video_upscale_latent_upscale_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.565
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, Flux2Scheduler, GetImageSize, GetNode, ImageScaleToTotalPixels, ImpactInt, KSampler, KSamplerSelect, LTX2_NAG, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RTXVideoSuperResolution, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, String Replace (mtb), Switch any [Crystools], TextEncodeQwenImageEditPlus, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VRAM_Debug, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2043904012268871681.json, 视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json]
source: knowledge_consolidation
---

# image_to_image_video_upscale_latent_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2043904012268871681.json、视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImpactInt`
- `KSampler`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `String Replace (mtb)`
- `Switch any [Crystools]`
- `TextEncodeQwenImageEditPlus`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `BatchTextReplace` —— 1/2 个有
- `IntToString` —— 1/2 个有
- `NumberClamp` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `SomethingToString` —— 1/2 个有
- `ToInt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
