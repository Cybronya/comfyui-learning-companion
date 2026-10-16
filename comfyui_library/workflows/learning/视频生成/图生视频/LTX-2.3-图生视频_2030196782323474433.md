---
key: 视频生成/图生视频/LTX-2.3-图生视频_2030196782323474433.json
name: LTX-2.3-图生视频_2030196782323474433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030196782323474433.json
hash: d7989fc51a2901bf
coverage: 0.973684
learned_at: 2026-10-15 22:35:25
nodes: [LTXVEmptyLatentAudio, LatentUpscaleModelLoader, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CFGGuider, KSamplerSelect, LTXVAudioVAEDecode, CheckpointLoaderSimple, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, CLIPTextEncode, RandomNoise, ImageScaleBy, GetImageSize, LTXVImgToVideoInplace, LoraLoaderModelOnly, VAEDecodeTiled, SaveVideo, LTXVSeparateAVLatent, CreateVideo, EmptyImage, Int, SimpleMath+, PrimitiveFloat, LTXVPreprocess, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, SamplerCustomAdvanced, ImageResizeKJv2, LoadImage, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, ResizeImagesByLongerEdge, LTXVScheduler, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.32000000000000006, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 849342153489369, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX-2.3-图生视频_2030196782323474433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030196782323474433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `EmptyImage`
- `Int`
- `SimpleMath+`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `LTXVScheduler`
- `KSampler` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `849342153489369`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.32000000000000006`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`RandomNoise`、`ImageScaleBy`、`GetImageSize`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`SaveVideo`、`LTXVSeparateAVLatent`、`CreateVideo`、`EmptyImage`、`Int`、`SimpleMath+`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`ImageResizeKJv2`、`LoadImage`、`LTXVConditioning`、`ResizeImagesByLongerEdge`、`LTXVScheduler`、`KSampler`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
