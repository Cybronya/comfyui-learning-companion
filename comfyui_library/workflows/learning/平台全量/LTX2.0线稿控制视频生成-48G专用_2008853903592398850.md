---
key: 平台全量/LTX2.0线稿控制视频生成-48G专用_2008853903592398850.json
name: LTX2.0线稿控制视频生成-48G专用_2008853903592398850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.0线稿控制视频生成-48G专用_2008853903592398850.json
hash: b18b47a80a50a622
coverage: 0.814815
learned_at: 2026-11-14 00:37:22
nodes: [MarkdownNote, CFGGuider, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVConcatAVLatent, CFGGuider, LTXVConditioning, CLIPTextEncode, LTXVSeparateAVLatent, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, VAEDecode, PrimitiveInt, PrimitiveFloat, LTXVCropGuides, MarkdownNote, VAEDecodeTiled, LTXVAudioVAEDecode, ImageScaleBy, PrimitiveInt, VHS_VideoCombine, LTXAVTextEncoderLoader, GetImageSize, ImageResizeKJv2, Canny, SamplerCustomAdvanced, GetVideoComponents, PrimitiveBoolean, LTXVLatentUpsampler, PrimitiveInt, PrimitiveInt, LTXVScheduler, ImageFromBatch, ImageFromBatch, EmptyLTXVLatentVideo, Reroute, LTXVImgToVideoInplace, LoadVideo, CLIPTextEncode, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, ImageResizeKJv2, LTXVImgToVideoInplace, MarkdownNote, PreviewImage, LTXVEmptyLatentAudio, LTXVAddGuide, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.0线稿控制视频生成-48G专用_2008853903592398850.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.0线稿控制视频生成-48G专用_2008853903592398850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `MarkdownNote`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVCropGuides`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LTXAVTextEncoderLoader`
- `GetImageSize`
- `ImageResizeKJv2`
- `Canny`
- `SamplerCustomAdvanced` ★核心
- `GetVideoComponents`
- `PrimitiveBoolean`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVScheduler`
- `ImageFromBatch`
- `ImageFromBatch`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `LTXVImgToVideoInplace`
- `LoadVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `PreviewImage`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAddGuide`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **81%**（44/54）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageScaleBy`、`VHS_VideoCombine`、`LTXAVTextEncoderLoader`、`GetImageSize`、`ImageResizeKJv2`、`Canny`、`GetVideoComponents`、`PrimitiveBoolean`、`LTXVLatentUpsampler`、`LTXVScheduler`、`ImageFromBatch`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoadVideo`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`LTXVAddGuide`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、Canny、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
