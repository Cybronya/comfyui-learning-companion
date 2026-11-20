---
key: 平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json
name: LTX2.0线稿控制视频生成（48G）_2008544083928682497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json
hash: 322e4267ce28e30b
coverage: 0.872727
learned_at: 2026-11-14 00:37:22
nodes: [KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, VAEDecode, PrimitiveInt, PrimitiveFloat, LTXVCropGuides, LTXVLatentUpsampler, LTXVAddGuide, INTConstant, INTConstant, ImageResizeKJv2, MarkdownNote, INTConstant, LoraLoaderModelOnly, GetImageSize, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CFGGuider, LTXVScheduler, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, VHS_LoadVideo, AIO_Preprocessor, PrimitiveBoolean, Reroute, LTXVImgToVideoInplace, CheckpointLoaderSimple, SamplerCustomAdvanced, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, MarkdownNote, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, MarkdownNote, LTXVConcatAVLatent, LoadImage, VHS_VideoCombine, ImageScaleBy, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAddGuide`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `MarkdownNote`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `PrimitiveBoolean`
- `Reroute`
- `LTXVImgToVideoInplace`
- `CheckpointLoaderSimple` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（48/55）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAddGuide`、`INTConstant`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`GetImageSize`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`VHS_LoadVideo`、`AIO_Preprocessor`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConditioning`、`LoadImage`、`ImageScaleBy`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
