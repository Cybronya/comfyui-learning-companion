---
key: 视频生成/图生视频/LTX2.0图生视频(已修复)_2008482127481933826.json
name: LTX2.0图生视频(已修复)_2008482127481933826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0图生视频(已修复)_2008482127481933826.json
hash: 3dd35cc741a3d585
coverage: 0.891304
learned_at: 2026-10-15 22:34:07
nodes: [MarkdownNote, KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, EmptyImage, SamplerCustomAdvanced, RandomNoise, RandomNoise, CLIPTextEncode, CreateVideo, LTXVSeparateAVLatent, VAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, ImageScaleBy, PrimitiveInt, GetImageSize, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, ResizeImagesByLongerEdge, MarkdownNote, SaveVideo, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, MarkdownNote, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0图生视频(已修复)_2008482127481933826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008482127481933826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
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
- `EmptyImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `GetImageSize`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `ResizeImagesByLongerEdge`
- `MarkdownNote`
- `SaveVideo`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyImage`、`SamplerCustomAdvanced`、`RandomNoise`、`CreateVideo`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`SaveVideo`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
