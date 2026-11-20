---
key: 平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json
name: video_ltx2_canny_to_video_unpack_2008733579580284929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json
hash: 1f0af75bc5eedd33
coverage: 0.8
learned_at: 2026-11-14 01:18:37
nodes: [MarkdownNote, PrimitiveBoolean, PreviewImage, MarkdownNote, CFGGuider, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVConcatAVLatent, CFGGuider, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVConditioning, CLIPTextEncode, LTXVSeparateAVLatent, KSamplerSelect, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, VAEDecode, GetImageSize, PrimitiveInt, PrimitiveFloat, EmptyLTXVLatentVideo, Reroute, LTXVCropGuides, LTXVLatentUpsampler, MarkdownNote, VAEDecodeTiled, LTXVAudioVAEDecode, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ImageScaleBy, GetVideoComponents, LTXVAddGuide, LTXVConcatAVLatent, PrimitiveInt, LTXVImgToVideoInplace, MarkdownNote, Canny, CLIPTextEncode, VHS_VideoCombine, LTXVImgToVideoInplace, LoadVideo, ImageFromBatch, ImageResizeKJv2, ImageFromBatch, PrimitiveInt, PrimitiveInt, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json

> 来源文件 `comfyui_library/workflows/平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `MarkdownNote`
- `PrimitiveBoolean`
- `PreviewImage`
- `MarkdownNote`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetImageSize`
- `PrimitiveInt`
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ImageScaleBy`
- `GetVideoComponents`
- `LTXVAddGuide`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `Canny`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `LoadVideo`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageFromBatch`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`PrimitiveBoolean`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVScheduler`、`RandomNoise`、`VAEDecode`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ImageScaleBy`、`GetVideoComponents`、`LTXVAddGuide`、`LTXVImgToVideoInplace`、`Canny`、`VHS_VideoCombine`、`LoadVideo`、`ImageFromBatch`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、Canny、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
