---
key: 平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json
name: video_ltx2_i2v_HD_upscale_basic_2010357744250920961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json
hash: 2de8fc00b2372747
coverage: 0.775
learned_at: 2026-11-14 01:18:38
nodes: [CLIPTextEncode, LTXVConditioning, GetImageSize, GetNode, GetNode, SetNode, SetNode, VAEDecode, LTXVConcatAVLatent, MarkdownNote, MarkdownNote, CLIPTextEncode, VHS_VideoCombine, MarkdownNote, SetNode, VHS_VideoCombine, VHS_LoadVideo, UNETLoader, VAELoader, VAELoaderKJ, DualCLIPLoader, ImageResizeKJv2, LatentUpscaleModelLoader, ImageScaleBy, LTXVPreprocess, LTXVCropGuides, VAEEncode, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVEmptyLatentAudio, RandomNoise, CFGGuider, LoraLoaderModelOnly, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, ResizeImagesByLongerEdge, GetImageRangeFromBatch]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json

> 来源文件 `comfyui_library/workflows/平台全量/video_ltx2_i2v_HD_upscale_basic_2010357744250920961.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（40 个）：
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `LTXVPreprocess`
- `LTXVCropGuides`
- `VAEEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `GetImageRangeFromBatch`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（31/40）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`GetImageSize`、`VAEDecode`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`VHS_LoadVideo`、`UNETLoader`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVPreprocess`、`LTXVCropGuides`、`VAEEncode`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVEmptyLatentAudio`、`RandomNoise`、`CFGGuider`、`LoraLoaderModelOnly`、`ManualSigmas`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ResizeImagesByLongerEdge`、`GetImageRangeFromBatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
