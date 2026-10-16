---
key: 视频生成/图生视频/LTX2.0 图生视频工作流（48G）中文对白友好_2008824264467685377.json
name: LTX2.0 图生视频工作流（48G）中文对白友好_2008824264467685377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008824264467685377.json
hash: 44c01d6748f16016
coverage: 0.88
learned_at: 2026-10-15 22:34:09
nodes: [KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, ImageScaleBy, PrimitiveInt, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, MarkdownNote, ResizeImagesByLongerEdge, LTXVPreprocess, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, GetImageSize, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, LoadImage, ImageResizeKJv2, MarkdownNote, MarkdownNote, LTXVAudioVAEDecode, RandomNoise, CLIPTextEncode, MarkdownNote, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 图生视频工作流（48G）中文对白友好_2008824264467685377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008824264467685377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `GetImageSize`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`LTXVAudioVAEDecode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
