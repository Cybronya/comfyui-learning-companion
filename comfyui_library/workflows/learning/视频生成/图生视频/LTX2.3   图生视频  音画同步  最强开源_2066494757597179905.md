---
key: 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2066494757597179905.json
name: LTX2.3   图生视频  音画同步  最强开源_2066494757597179905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066494757597179905.json
hash: 1e438388154c7124
coverage: 0.95
learned_at: 2026-10-15 22:39:50
nodes: [LTXAVTextEncoderLoader, LTXVCropGuides, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecode, LTXVConcatAVLatent, CreateVideo, CLIPTextEncode, GetImageSize, EmptyImage, DualCLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, LTXVConditioning, CFGGuider, RandomNoise, LatentUpscaleModelLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, KSamplerSelect, LTXVPreprocess, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSampler, ResizeImagesByLongerEdge, PreviewAny, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVScheduler, SaveVideo, LoadImage, TextGenerateLTX2Prompt, ResizeImageMaskNode, PrimitiveInt, EmptyLTXVLatentVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 156434680843129, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2066494757597179905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066494757597179905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXAVTextEncoderLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `EmptyImage`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `ResizeImagesByLongerEdge`
- `PreviewAny`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `SaveVideo`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `156434680843129`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVConcatAVLatent`、`CreateVideo`、`CLIPTextEncode`、`GetImageSize`、`EmptyImage`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`KSampler`、`ResizeImagesByLongerEdge`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`SaveVideo`、`LoadImage`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
