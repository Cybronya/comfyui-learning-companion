---
key: 视频生成/图生视频/LTX2.0 图生视频工作流（抖音1024_1536_9_16）_2026499302796828674.json
name: LTX2.0 图生视频工作流（抖音1024_1536_9_16）_2026499302796828674.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2026499302796828674.json
hash: 2b9cd6ef4c467805
coverage: 0.897959
learned_at: 2026-10-15 22:35:14
nodes: [MarkdownNote, KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, MarkdownNote, LTXVPreprocess, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, MarkdownNote, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, GetImageSize, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, VAEDecode, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, RandomNoise, LoadImage, ImageResizeKJv2, ResizeImagesByLongerEdge, PrimitiveInt, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 图生视频工作流（抖音1024_1536_9_16）_2026499302796828674.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026499302796828674.json`

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
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `MarkdownNote`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `GetImageSize`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `LoadImage`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
