---
name: unknown_workflow_video_upscale_latent_upscale_125
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7425
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, CreateVideo, DF_Int_to_Float, DrawMaskOnImage, DualCLIPLoader, GetImageSize, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcanate, ImageResizeKJv2, ImageScaleBy, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, QZ_ResolutionPreset, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetNode, SimpleMath+, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/ltx2.3 视频编辑工作流 速度贼拉快_2041799615799894018.json, 视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_125

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ltx2.3 视频编辑工作流 速度贼拉快_2041799615799894018.json、视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DF_Int_to_Float`
- `DrawMaskOnImage`
- `DualCLIPLoader`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `QZ_ResolutionPreset`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `ImageCompositeFromMaskBatch+` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageInvert` —— 1/2 个有
- `LTX2_NAG` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVEmptyLatentAudio` —— 1/2 个有
- `LTXVReferenceAudio` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `ModelMemoryUsageFactorOverride` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `SAM3Segment` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 116 | - | 1 | 100% |
| 高度 | 24 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
