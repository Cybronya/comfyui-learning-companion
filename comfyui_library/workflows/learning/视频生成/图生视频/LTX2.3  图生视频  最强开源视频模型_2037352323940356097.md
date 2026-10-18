---
key: 视频生成/图生视频/LTX2.3  图生视频  最强开源视频模型_2037352323940356097.json
name: LTX2.3  图生视频  最强开源视频模型_2037352323940356097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3  图生视频  最强开源视频模型_2037352323940356097.json
hash: dd340c39458f9cd2
coverage: 0.95
learned_at: 2026-10-15 22:35:56
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVAudioVAEDecode, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVConditioning, LTXVImgToVideoInplace, KSampler, VAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, LatentUpscaleModelLoader, ResizeImagesByLongerEdge, ImageScaleBy, EmptyLTXVLatentVideo, PrimitiveInt, GetImageSize, ResizeImageMaskNode, LTXVPreprocess, EmptyImage, GetImageSize, DualCLIPLoader, PreviewAny, CLIPTextEncode, CLIPTextEncode, TextGenerateLTX2Prompt, LoadImage, LTXVConcatAVLatent, CreateVideo, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 646424227658726, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3  图生视频  最强开源视频模型_2037352323940356097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037352323940356097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `ResizeImagesByLongerEdge`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `GetImageSize`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `EmptyImage`
- `GetImageSize`
- `DualCLIPLoader`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `646424227658726`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`RandomNoise`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`KSampler`、`VAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`ResizeImagesByLongerEdge`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`GetImageSize`、`ResizeImageMaskNode`、`LTXVPreprocess`、`EmptyImage`、`DualCLIPLoader`、`CLIPTextEncode`、`TextGenerateLTX2Prompt`、`LoadImage`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
