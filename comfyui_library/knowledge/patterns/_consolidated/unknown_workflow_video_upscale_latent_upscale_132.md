---
name: unknown_workflow_video_upscale_latent_upscale_132
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5805
common_nodes: [AudioCrop, BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, ImageBatchMulti, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXSequencer, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, SimpleMath+, Text Concatenate, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2075065970321874946.json, 视频生成/图生视频/2075069452714078209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_132

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2075065970321874946.json、视频生成/图生视频/2075069452714078209.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXSequencer`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVEmptyLatentAudio` —— 1/2 个有
- `LTXVReferenceAudio` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `PainterAudioLength` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1 | - | 1 | 100% |
| 高度 | 24 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
