---
key: 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2067495038166327298.json
name: LTX2.3   图生视频  音画同步  最强开源_2067495038166327298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067495038166327298.json
hash: 15ea5f31edfd8f4e
coverage: 0.95
learned_at: 2026-10-15 22:40:02
nodes: [LTXVCropGuides, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecode, LTXVConcatAVLatent, CreateVideo, LTXVConditioning, CFGGuider, RandomNoise, KSamplerSelect, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSampler, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVScheduler, SaveVideo, TextGenerateLTX2Prompt, ResizeImageMaskNode, CheckpointLoaderSimple, DualCLIPLoader, LoraLoaderModelOnly, PreviewAny, CLIPTextEncode, CLIPTextEncode, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, ResizeImagesByLongerEdge, GetImageSize, EmptyImage, GetImageSize, EmptyLTXVLatentVideo, LTXVPreprocess, ImageScaleBy, PrimitiveInt, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 452271514788038, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2067495038166327298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067495038166327298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `CheckpointLoaderSimple` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `EmptyImage`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `ImageScaleBy`
- `PrimitiveInt`
- `LoadImage`

## 关键参数

- `seed` = `452271514788038`
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

**有卡**：`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVConcatAVLatent`、`CreateVideo`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`KSampler`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`SaveVideo`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`ResizeImagesByLongerEdge`、`GetImageSize`、`EmptyImage`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`ImageScaleBy`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
