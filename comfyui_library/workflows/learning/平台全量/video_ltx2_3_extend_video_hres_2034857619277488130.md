---
key: 平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json
name: video_ltx2_3_extend_video_hres_2034857619277488130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json
hash: a80e830fdf36c997
coverage: 0.566667
learned_at: 2026-11-14 01:18:35
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, Reroute, KSamplerSelect, SetNode, PrimitiveInt, PrimitiveInt, SetNode, SetNode, GetNode, VAELoaderKJ, SetNode, SetNode, ManualSigmas, DualCLIPLoader, PrimitiveBoolean, MarkdownNote, MarkdownNote, NormalizeAudioLoudness, GetNode, GetNode, ComfyMathExpression, GetNode, SetNode, GetImage, PrimitiveInt, SetNode, LTXVConditioning, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, GetNode, GetNode, VHS_VideoInfo, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, LTXVSeparateAVLatent, PreviewAudio, LTXVAudioVAEDecode, GetNode, GetNode, ComfyMathExpression, GetNode, ComfyMathExpression, VHS_VideoCombine, VHS_VideoCombine, LatentUpscaleModelLoader, UNETLoader, PreviewAny, TrimAudio, ImageResizeKJv2, SetNode, GetImageRangeFromBatch, SetNode, GetNode, AudioConcat, SetNode, GetNode, CLIPTextEncode, CFGGuider, LTXVCropGuides, VAEDecodeTiled, GetImageRangeFromBatch, ImageBatchMulti, GetNode, VHS_VideoCombine, ImageBatchExtendWithOverlap, CLIPTextEncode, TextGenerateLTX2Prompt, VAELoaderKJ, RTXVideoSuperResolution, easy showAnything, GetImageSizeAndCount, VHS_LoadVideo, PrimitiveInt, SetNode, PrimitiveInt, SetNode, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, easy showAnything, easy showAnything, ImageResizeKJv2, GetImageRangeFromBatch, GetNode, PrimitiveInt, TrimAudioDuration, ComfyMathExpression, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAEEncodeTiled, LTXVAudioVAEEncode, SetNode, ComfyMathExpression, LTXVAudioVideoMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, SamplerCustomAdvanced]
patterns: []
missing: []
---

# 平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json

> 来源文件 `comfyui_library/workflows/平台全量/video_ltx2_3_extend_video_hres_2034857619277488130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（120 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `Reroute`
- `KSamplerSelect` ★核心
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `DualCLIPLoader`
- `PrimitiveBoolean`
- `MarkdownNote`
- `MarkdownNote`
- `NormalizeAudioLoudness`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `GetImage`
- `PrimitiveInt`
- `SetNode`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `PreviewAudio`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `PreviewAny`
- `TrimAudio`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `AudioConcat`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `GetNode`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `VAELoaderKJ`
- `RTXVideoSuperResolution`
- `easy showAnything`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy showAnything`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `GetNode`
- `PrimitiveInt`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncodeTiled` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `ComfyMathExpression`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心

## 知识

覆盖率 **57%**（68/120）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`VAELoaderKJ`、`DualCLIPLoader`、`PrimitiveBoolean`、`NormalizeAudioLoudness`、`ComfyMathExpression`、`GetImage`、`LTXVConditioning`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVSeparateAVLatent`、`PreviewAudio`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`UNETLoader`、`TrimAudio`、`GetImageRangeFromBatch`、`AudioConcat`、`CLIPTextEncode`、`LTXVCropGuides`、`ImageBatchMulti`、`ImageBatchExtendWithOverlap`、`TextGenerateLTX2Prompt`、`RTXVideoSuperResolution`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`TrimAudioDuration`、`VAEEncodeTiled`、`LTXVAudioVAEEncode`、`LTXVAudioVideoMask`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`

**用到的条目**：CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced、LatentUpscaleModelLoader、LTXVAudioVAEDecode
