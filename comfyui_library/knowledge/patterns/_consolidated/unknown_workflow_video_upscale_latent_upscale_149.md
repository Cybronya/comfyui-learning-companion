---
name: unknown_workflow_video_upscale_latent_upscale_149
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5715
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, GetImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageBatchMulti, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, NormalizeAudioLoudness, PreviewAny, PreviewAudio, PrimitiveBoolean, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, TextGenerateLTX2Prompt, TrimAudio, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json, 视频生成/图生视频/LTX-2.3  2K高清视频扩展工作流 V1.0_2038707377737834497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_149

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json、视频生成/图生视频/LTX-2.3  2K高清视频扩展工作流 V1.0_2038707377737834497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `GetImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `TextGenerateLTX2Prompt`
- `TrimAudio`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
