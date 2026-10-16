---
key: 视频生成/图生视频/LTX2.3图生视频支持宽高比高清视频_2029754649418403842.json
name: LTX2.3图生视频支持宽高比高清视频_2029754649418403842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029754649418403842.json
hash: d7f57001bee2f3d4
coverage: 0.916667
learned_at: 2026-10-15 22:35:23
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetImageSize, CFGGuider, LatentUpscaleModelLoader, EmptyImage, CLIPTextEncode, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, MarkdownNote, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, LTXVConditioning, RandomNoise, DualCLIPLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageScaleBy, GetImageSize, KSampler, MarkdownNote, PreviewAny, CLIPTextEncode, TextGenerateLTX2Prompt, ResizeImageMaskNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int, PrimitiveInt, Int, Int, MathExpression|pysssss, ResizeImagesByLongerEdge, LTXVPreprocess, CR Text, CreateVideo, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 329347841018560, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频支持宽高比高清视频_2029754649418403842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029754649418403842.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetImageSize`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVConditioning`
- `RandomNoise`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `KSampler` ★核心
- `MarkdownNote`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Int`
- `PrimitiveInt`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CR Text`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `329347841018560`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GetImageSize`、`CFGGuider`、`LatentUpscaleModelLoader`、`EmptyImage`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVConditioning`、`RandomNoise`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageScaleBy`、`KSampler`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`、`MathExpression|pysssss`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CR Text`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
