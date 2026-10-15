---
key: 视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json
name: LTX2.3文生哭泣视频_2073302607023656962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json
hash: 6efa767b6b6f3737
coverage: 0.810811
learned_at: 2026-10-15 22:45:10
nodes: [MarkdownNote, MarkdownNote, LTXVScheduler, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, KSamplerSelect, RandomNoise, Reroute, KSampler, LTXVSeparateAVLatent, LTXVCropGuides, SaveVideo, LoraLoaderModelOnly, CLIPTextEncode, EmptyImage, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVConcatAVLatent, CLIPTextEncode, MarkdownNote, CreateVideo, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 702953997513802, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `MarkdownNote`
- `MarkdownNote`
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
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CreateVideo`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `702953997513802`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`LTXVScheduler`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`SaveVideo`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyImage`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CreateVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
