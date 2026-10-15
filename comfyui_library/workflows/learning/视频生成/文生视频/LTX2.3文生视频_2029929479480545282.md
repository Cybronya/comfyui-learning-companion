---
key: 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json
name: LTX2.3文生视频_2029929479480545282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json
hash: 3e4e6a7433b706bb
coverage: 0.888889
learned_at: 2026-10-15 22:45:10
nodes: [LTXVScheduler, LatentUpscaleModelLoader, LTXVCropGuides, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CLIPTextEncode, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, CLIPTextEncode, CreateVideo, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, LoraLoaderModelOnly, KSamplerSelect, DualCLIPLoader, PreviewAny, RandomNoise, EmptyImage, LTXAVTextEncoderLoader, CheckpointLoaderSimple, KSampler, SaveVideo, TextGenerateLTX2Prompt, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4000000000000001, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 182620311649531, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `LTXVScheduler`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `PreviewAny`
- `RandomNoise`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `182620311649531`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`LTXVScheduler`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CFGGuider`、`LoraLoaderModelOnly`、`KSamplerSelect`、`DualCLIPLoader`、`RandomNoise`、`EmptyImage`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`KSampler`、`SaveVideo`、`TextGenerateLTX2Prompt`、`CR Text`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
