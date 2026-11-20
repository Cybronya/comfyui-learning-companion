---
key: 平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json
name: video_ltx2_i2v_upscale_advanced_2010380854765297665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json
hash: 9059832f5be37414
coverage: 0.785714
learned_at: 2026-11-14 01:18:39
nodes: [LatentUpscaleModelLoader, SamplerCustomAdvanced, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, CLIPTextEncode, LTXVConditioning, VAELoader, VAELoaderKJ, GetImageSize, GetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, SetNode, VAEDecode, GetNode, LTXVEmptyLatentAudio, VAEEncode, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, GetImageRangeFromBatch, RandomNoise, LTXVImgToVideoInplace, LTXVConcatAVLatent, MarkdownNote, MarkdownNote, CLIPTextEncode, VHS_VideoCombine, CFGGuider, MarkdownNote, ImageScaleBy, SetNode, KSamplerSelect, VHS_VideoCombine, ManualSigmas, VHS_LoadVideo, ImageResizeKJv2, LoadImage, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json

> 来源文件 `comfyui_library/workflows/平台全量/video_ltx2_i2v_upscale_advanced_2010380854765297665.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `VAELoader`
- `VAELoaderKJ`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `VAEEncode` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `GetImageRangeFromBatch`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CFGGuider`
- `MarkdownNote`
- `ImageScaleBy`
- `SetNode`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `ManualSigmas`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LTXVConditioning`、`VAELoader`、`VAELoaderKJ`、`GetImageSize`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`VAEDecode`、`LTXVEmptyLatentAudio`、`VAEEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`GetImageRangeFromBatch`、`RandomNoise`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`CFGGuider`、`ImageScaleBy`、`KSamplerSelect`、`ManualSigmas`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
