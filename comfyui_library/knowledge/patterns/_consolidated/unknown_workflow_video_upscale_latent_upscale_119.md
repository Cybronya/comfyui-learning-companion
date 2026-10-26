---
name: unknown_workflow_video_upscale_latent_upscale_119
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.618
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, GetImageSize, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【老金驿站】LTX2.3图生视频+精准口型视频工作流_2041756040752009217.json, 视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json, 视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_119

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【老金驿站】LTX2.3图生视频+精准口型视频工作流_2041756040752009217.json、视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json、视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTX2SamplingPreviewOverride` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `LTXVChunkFeedForward` —— 2/3 个有
- `LTXVEmptyLatentAudio` —— 2/3 个有
- `Power Lora Loader (rgthree)` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LTXVAddGuideMulti` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVCropGuides` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有
- `VHS_LoadAudioUpload` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 109 | - | 2 | 89% |
| 高度 | 24.5 | - | 2 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 109，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 24.5，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
