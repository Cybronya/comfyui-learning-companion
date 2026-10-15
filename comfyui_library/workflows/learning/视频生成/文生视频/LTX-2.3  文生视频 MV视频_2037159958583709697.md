---
key: 视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json
name: LTX-2.3  文生视频 MV视频_2037159958583709697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json
hash: 9b63eed63c3bb148
coverage: 0.885714
learned_at: 2026-10-15 22:44:37
nodes: [LTXVConcatAVLatent, LTXVConcatAVLatent, PreviewAny, CLIPTextEncode, CLIPTextEncode, SaveVideo, TextGenerateLTX2Prompt, LTXVConditioning, EmptyImage, LoraLoaderModelOnly, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXVAudioVAELoader, DualCLIPLoader, LTXAVTextEncoderLoader, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVScheduler, KSamplerSelect, CFGGuider, RandomNoise, KSampler, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PrimitiveInt, ImageScaleBy, PrimitiveFloat, GetImageSize, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 707187750518046, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `LTXVConditioning`
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `DualCLIPLoader`
- `LTXAVTextEncoderLoader`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `ImageScaleBy`
- `PrimitiveFloat`
- `GetImageSize`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `707187750518046`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`LTXVConcatAVLatent`、`CLIPTextEncode`、`SaveVideo`、`TextGenerateLTX2Prompt`、`LTXVConditioning`、`EmptyImage`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVScheduler`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`KSampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GetImageSize`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
