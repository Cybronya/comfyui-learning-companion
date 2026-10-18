---
key: 视频生成/图生视频/LTX2.3图生视频-有人声极速版_2070027759010795521.json
name: LTX2.3图生视频-有人声极速版_2070027759010795521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频-有人声极速版_2070027759010795521.json
hash: df15186996aa9e1c
coverage: 0.95
learned_at: 2026-10-15 22:40:34
nodes: [EmptyImage, GetImageSize, PrimitiveInt, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, CreateVideo, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVPreprocess, LTXAVTextEncoderLoader, LTXVSeparateAVLatent, LTXVAudioVAELoader, VAEDecode, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, SaveVideo, GetImageSize, ResizeImageMaskNode, KSampler, LoraLoaderModelOnly, LTXVCropGuides, LatentUpscaleModelLoader, LTXVLatentUpsampler, CheckpointLoaderSimple, EmptyLTXVLatentVideo, ImageScaleBy, DualCLIPLoader, LoadImage, PreviewAny, TextGenerateLTX2Prompt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.3500000000000001, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 322577470942695, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频-有人声极速版_2070027759010795521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070027759010795521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `EmptyImage`
- `GetImageSize`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXAVTextEncoderLoader`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `GetImageSize`
- `ResizeImageMaskNode`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `EmptyLTXVLatentVideo`
- `ImageScaleBy`
- `DualCLIPLoader`
- `LoadImage`
- `PreviewAny`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `322577470942695`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`EmptyImage`、`GetImageSize`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`CreateVideo`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`VAEDecode`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`SaveVideo`、`ResizeImageMaskNode`、`KSampler`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`DualCLIPLoader`、`LoadImage`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
