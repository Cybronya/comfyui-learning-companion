---
key: 视频生成/图生视频/LTX2.0 音画同步生视频_2009155672465743874.json
name: LTX2.0 音画同步生视频_2009155672465743874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0 音画同步生视频_2009155672465743874.json
hash: 82f93ead36b22a2f
coverage: 0.893617
learned_at: 2026-10-15 22:34:10
nodes: [KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, RandomNoise, CreateVideo, LTXVSeparateAVLatent, VAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, ImageScaleBy, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, ResizeImagesByLongerEdge, MarkdownNote, SaveVideo, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, GetImageSize, PrimitiveInt, CLIPTextEncode, MarkdownNote, MarkdownNote, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, EmptyImage, CheckpointLoaderSimple, LTXVConditioning]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 音画同步生视频_2009155672465743874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009155672465743874.json`

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
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `GetImageSize`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `EmptyImage`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`CreateVideo`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ImageScaleBy`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`SaveVideo`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`GetImageSize`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyImage`、`CheckpointLoaderSimple`、`LTXVConditioning`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
