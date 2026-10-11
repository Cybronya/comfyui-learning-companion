---
key: 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json
name: LTX-2.3-文生视频_2037040523202007042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json
hash: 9614716719b7d3fa
coverage: 0.864865
learned_at: 2026-10-11 03:48:35
nodes: [LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, KSamplerSelect, RandomNoise, Reroute, KSampler, LTXVSeparateAVLatent, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PrimitiveInt, GetImageSize, PrimitiveInt, ImageScaleBy, EmptyImage, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, DualCLIPLoader, LTXVAudioVAELoader, PreviewAny, CLIPTextEncode, PrimitiveFloat, LTXVConditioning, LTXVConcatAVLatent, LTXVConcatAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LatentUpscaleModelLoader, LTXVLatentUpsampler, CLIPTextEncode, TextGenerateLTX2Prompt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 140661918577066, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `GetImageSize`
- `PrimitiveInt`
- `ImageScaleBy`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LTXVAudioVAELoader`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`

## 关键参数

- `seed` = `140661918577066`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`GetImageSize`、`ImageScaleBy`、`EmptyImage`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
