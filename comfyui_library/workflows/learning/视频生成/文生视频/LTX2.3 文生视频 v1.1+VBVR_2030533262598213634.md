---
key: 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json
name: LTX2.3 文生视频 v1.1+VBVR_2030533262598213634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json
hash: c88935c5cc139cae
coverage: 0.8
learned_at: 2026-10-15 22:45:00
nodes: [MarkdownNote, MarkdownNote, ImageScaleBy, LTXVEmptyLatentAudio, LTXVConditioning, LTXVConcatAVLatent, LTXVSeparateAVLatent, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, MarkdownNote, KSamplerSelect, Reroute, PreviewAny, KSampler, LTXVSeparateAVLatent, LTXVCropGuides, SaveVideo, DualCLIPLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, TextGenerateLTX2Prompt, PrimitiveInt, PrimitiveFloat, GetImageSize, CLIPTextEncode, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, LoraLoaderModelOnly, CFGGuider, LTXVScheduler, EmptyLTXVLatentVideo, CheckpointLoaderSimple, VAEDecode, LTXVLatentUpsampler, LTXVConcatAVLatent, EmptyImage, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 259089915385124, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleBy`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `Reroute`
- `PreviewAny`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SaveVideo`
- `DualCLIPLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `TextGenerateLTX2Prompt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `EmptyImage`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `259089915385124`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`KSampler`、`LTXVCropGuides`、`SaveVideo`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`GetImageSize`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`CFGGuider`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`VAEDecode`、`LTXVLatentUpsampler`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
