---
key: 视频生成/图生视频/LTX2.3声画同步开源模型_2030149051974422529.json
name: LTX2.3声画同步开源模型_2030149051974422529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3声画同步开源模型_2030149051974422529.json
hash: f00661a0bf0469ff
coverage: 0.95
learned_at: 2026-10-15 22:35:25
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVPreprocess, CFGGuider, EmptyImage, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVCropGuides, CreateVideo, LTXVConditioning, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, ImageScaleBy, GetImageSize, PrimitiveInt, GetImageSize, LTXAVTextEncoderLoader, ResizeImageMaskNode, CLIPTextEncode, LTXVConcatAVLatent, KSampler, VAEDecode, DualCLIPLoader, PreviewAny, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVImgToVideoInplace, LoadImage, SaveVideo, TextGenerateLTX2Prompt, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 746346594638747, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3声画同步开源模型_2030149051974422529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030149051974422529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `CFGGuider`
- `EmptyImage`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `CreateVideo`
- `LTXVConditioning`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `ImageScaleBy`
- `GetImageSize`
- `PrimitiveInt`
- `GetImageSize`
- `LTXAVTextEncoderLoader`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LoadImage`
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `746346594638747`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`CFGGuider`、`EmptyImage`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`CreateVideo`、`LTXVConditioning`、`RandomNoise`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`ImageScaleBy`、`GetImageSize`、`LTXAVTextEncoderLoader`、`ResizeImageMaskNode`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LoadImage`、`SaveVideo`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
