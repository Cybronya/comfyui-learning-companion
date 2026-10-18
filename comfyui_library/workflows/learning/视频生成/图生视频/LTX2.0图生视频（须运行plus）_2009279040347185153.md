---
key: 视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json
name: LTX2.0图生视频（须运行plus）_2009279040347185153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json
hash: d004db12fb539e40
coverage: 0.87234
learned_at: 2026-10-15 22:34:12
nodes: [ManualSigmas, LatentUpscaleModelLoader, CFGGuider, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, MarkdownNote, MarkdownNote, ImageScaleBy, GetImageSize, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXAVTextEncoderLoader, SamplerCustomAdvanced, CFGGuider, LTXVScheduler, LTXVConditioning, KSamplerSelect, PrimitiveInt, PrimitiveInt, RandomNoise, RandomNoise, LoadImage, PrimitiveFloat, LTXVAudioVAELoader, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVCropGuides, SaveVideo, CreateVideo, VAEDecodeTiled, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, EmptyImage, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplace, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009279040347185153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `RandomNoise`
- `LoadImage`
- `PrimitiveFloat`
- `LTXVAudioVAELoader`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVCropGuides`
- `SaveVideo`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyImage`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`ManualSigmas`、`LatentUpscaleModelLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ImageScaleBy`、`GetImageSize`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`LTXVConditioning`、`RandomNoise`、`LoadImage`、`LTXVAudioVAELoader`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVCropGuides`、`SaveVideo`、`CreateVideo`、`VAEDecodeTiled`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyImage`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`CheckpointLoaderSimple`、`LTXVLatentUpsampler`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
