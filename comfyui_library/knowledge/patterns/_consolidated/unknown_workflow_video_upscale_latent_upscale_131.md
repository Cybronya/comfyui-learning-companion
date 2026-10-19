---
name: unknown_workflow_video_upscale_latent_upscale_131
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.77
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVEnhanceAVideoKJ, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2036795915394093058.json, 视频生成/图生视频/2035619730907734018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_131

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2036795915394093058.json、视频生成/图生视频/2035619730907734018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVEnhanceAVideoKJ`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `FastFilmGrain` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVImgToVideoInplace` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_PruneOutputs` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
