---
key: 视频生成/图生视频/LTX2.0 图生视频工作流_2014596837386231809.json
name: LTX2.0 图生视频工作流_2014596837386231809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0 图生视频工作流_2014596837386231809.json
hash: 5cfe285db37da9af
coverage: 0.897959
learned_at: 2026-10-15 22:34:35
nodes: [MarkdownNote, KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, ImageScaleBy, PrimitiveInt, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, MarkdownNote, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, MarkdownNote, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, GetImageSize, LoadImage, MarkdownNote, VAEDecode, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, RandomNoise, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 图生视频工作流_2014596837386231809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014596837386231809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（49 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `MarkdownNote`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `GetImageSize`
- `LoadImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`LoadImage`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
