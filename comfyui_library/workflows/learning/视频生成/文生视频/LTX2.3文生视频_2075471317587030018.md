---
key: 视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json
name: LTX2.3文生视频_2075471317587030018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json
hash: 990a0c6de82b033a
coverage: 0.939394
learned_at: 2026-10-15 22:45:12
nodes: [CLIPTextEncode, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, TextGenerateLTX2Prompt, DualCLIPLoader, JjkText, EmptyImage, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConcatAVLatent, EmptyLTXVLatentVideo, CLIPTextEncode, PrimitiveInt, LTXVConditioning, CFGGuider, LTXVScheduler, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4000000000000001, "height": 24, "sampler_name": "euler", "scheduler": "simple", "seed": 784263003975090, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `TextGenerateLTX2Prompt`
- `DualCLIPLoader`
- `JjkText`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `784263003975090`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`TextGenerateLTX2Prompt`、`DualCLIPLoader`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CFGGuider`、`LTXVScheduler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`KSampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
