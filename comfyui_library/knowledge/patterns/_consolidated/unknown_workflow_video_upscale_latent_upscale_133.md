---
name: unknown_workflow_video_upscale_latent_upscale_133
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8255
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, TrimAudioDuration, UnetLoaderGGUF, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json, 视频生成/图生视频/LTX2.3-文+图+音频_2039311541685719041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_133

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json、视频生成/图生视频/LTX2.3-文+图+音频_2039311541685719041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `TrimAudioDuration`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Float To Integer` —— 1/2 个有
- `CreateShapeMask` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `FL_IntToFloat` —— 1/2 个有
- `FL_Math` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTX2_NAG` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `LTXVSetAudioVideoMaskByTime` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `TextGenerateLTX2Prompt` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

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
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
