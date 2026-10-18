---
key: 视频生成/图生视频/LTX2.0图生视频V1_2008532910646763522.json
name: LTX2.0图生视频V1_2008532910646763522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0图生视频V1_2008532910646763522.json
hash: f63b14fce4b7dc77
coverage: 0.893617
learned_at: 2026-10-15 22:34:07
nodes: [KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, RandomNoise, CreateVideo, LTXVSeparateAVLatent, VAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, ImageScaleBy, GetImageSize, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, ResizeImagesByLongerEdge, MarkdownNote, SaveVideo, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetImageSize, MarkdownNote, MarkdownNote, PrimitiveInt, CLIPTextEncode, EmptyImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0图生视频V1_2008532910646763522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008532910646763522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetImageSize`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `EmptyImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`CreateVideo`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`SaveVideo`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
