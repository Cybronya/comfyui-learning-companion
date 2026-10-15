---
key: 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json
name: LTX2.0 图生视频工作流（48G）_2008873261282627585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json
hash: cbe6b003e42efb90
coverage: 0.897959
learned_at: 2026-10-15 22:44:49
nodes: [MarkdownNote, KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ImageScaleBy, PrimitiveInt, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, MarkdownNote, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, MarkdownNote, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, VAEDecode, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, RandomNoise, GetImageSize, VHS_VideoCombine, VHS_VideoCombine, LTXVAudioVAEDecode, VAEDecode, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVLatentUpsampler, LoadImage, CLIPTextEncode, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（49 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `MarkdownNote`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `GetImageSize`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`LoraLoaderModelOnly`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
