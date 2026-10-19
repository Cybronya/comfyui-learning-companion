---
name: unknown_workflow_video_upscale_latent_upscale_133
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5125
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, JWFloat, JWLoadImageSequenceWithStopIndex, JWSaveImageSequence, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAddGuide, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PreviewAny, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy float, easy forLoopEnd, easy forLoopStart, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/2038825068578480130.json, 视频生成/图生视频/2038747014028075010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_133

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2038825068578480130.json、视频生成/图生视频/2038747014028075010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JWFloat`
- `JWLoadImageSequenceWithStopIndex`
- `JWSaveImageSequence`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAddGuide`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
