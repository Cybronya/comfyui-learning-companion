---
key: 视频生成/图生视频/LTX2.3  音画同步  图生视频 最强开源_2063908230866231297.json
name: LTX2.3  音画同步  图生视频 最强开源_2063908230866231297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3  音画同步  图生视频 最强开源_2063908230866231297.json
hash: 40c80a0ff2793467
coverage: 0.95
learned_at: 2026-10-15 22:39:18
nodes: [LTXVCropGuides, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecode, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, CFGGuider, RandomNoise, LatentUpscaleModelLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, KSamplerSelect, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSampler, PreviewAny, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVScheduler, DualCLIPLoader, ResizeImageMaskNode, TextGenerateLTX2Prompt, SaveVideo, CreateVideo, CheckpointLoaderSimple, GetImageSize, EmptyImage, PrimitiveInt, GetImageSize, ImageScaleBy, ResizeImagesByLongerEdge, LTXVPreprocess, LTXAVTextEncoderLoader, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 878206429201037, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3  音画同步  图生视频 最强开源_2063908230866231297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063908230866231297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `PreviewAny`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `DualCLIPLoader`
- `ResizeImageMaskNode`
- `TextGenerateLTX2Prompt`
- `SaveVideo`
- `CreateVideo`
- `CheckpointLoaderSimple` ★核心
- `GetImageSize`
- `EmptyImage`
- `PrimitiveInt`
- `GetImageSize`
- `ImageScaleBy`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXAVTextEncoderLoader`
- `LoadImage`

## 关键参数

- `seed` = `878206429201037`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`KSampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`DualCLIPLoader`、`ResizeImageMaskNode`、`TextGenerateLTX2Prompt`、`SaveVideo`、`CreateVideo`、`CheckpointLoaderSimple`、`GetImageSize`、`EmptyImage`、`ImageScaleBy`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXAVTextEncoderLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
