---
key: 视频生成/图生视频/LTX2.3   图生视频 最强开源_2066440178742419458.json
name: LTX2.3   图生视频 最强开源_2066440178742419458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3   图生视频 最强开源_2066440178742419458.json
hash: cf7de713d3466375
coverage: 0.95
learned_at: 2026-10-15 22:39:50
nodes: [LTXVCropGuides, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecode, CreateVideo, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSampler, SaveVideo, ResizeImageMaskNode, ResizeImagesByLongerEdge, GetImageSize, DualCLIPLoader, TextGenerateLTX2Prompt, CheckpointLoaderSimple, LTXAVTextEncoderLoader, CLIPTextEncode, PreviewAny, EmptyImage, ImageScaleBy, LTXVPreprocess, CLIPTextEncode, LatentUpscaleModelLoader, GetImageSize, PrimitiveInt, EmptyLTXVLatentVideo, LTXVAudioVAELoader, LTXVEmptyLatentAudio, LTXVConditioning, RandomNoise, LoraLoaderModelOnly, CFGGuider, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVScheduler, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 579962232668304, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3   图生视频 最强开源_2066440178742419458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066440178742419458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `SaveVideo`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `DualCLIPLoader`
- `TextGenerateLTX2Prompt`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `EmptyImage`
- `ImageScaleBy`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `GetImageSize`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`

## 关键参数

- `seed` = `579962232668304`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecode`、`CreateVideo`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`KSampler`、`SaveVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`EmptyImage`、`ImageScaleBy`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`RandomNoise`、`LoraLoaderModelOnly`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
