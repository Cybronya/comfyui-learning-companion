---
key: 视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json
name: LTX2.3文生视频短剧分镜人物12秒_2030776760257744898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json
hash: 54bff466cfa330c1
coverage: 0.861111
learned_at: 2026-10-11 03:16:47
nodes: [LTXVScheduler, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, KSamplerSelect, RandomNoise, Reroute, PreviewAny, KSampler, LTXVSeparateAVLatent, LTXVCropGuides, SaveVideo, LoraLoaderModelOnly, CLIPTextEncode, DualCLIPLoader, CLIPTextEncode, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVConcatAVLatent, TextGenerateLTX2Prompt, EmptyImage, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 242940641124429, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `LTXVScheduler`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `PreviewAny`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `TextGenerateLTX2Prompt`
- `EmptyImage`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `242940641124429`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`LTXVScheduler`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`SaveVideo`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`EmptyImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
