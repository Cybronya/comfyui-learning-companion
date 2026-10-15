---
key: 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json
name: LTX2.3-文生视频_2066069178989240321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json
hash: e5f402116fb57d53
coverage: 0.804878
learned_at: 2026-10-15 22:45:04
nodes: [MarkdownNote, MarkdownNote, LTXVScheduler, ImageScaleBy, LTXVEmptyLatentAudio, LTXVConditioning, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, KSamplerSelect, RandomNoise, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVConcatAVLatent, CheckpointLoaderSimple, CLIPTextEncode, EmptyLTXVLatentVideo, EmptyImage, PrimitiveInt, GetImageSize, CreateVideo, LTXVAudioVAEDecode, VAEDecode, KSampler, DualCLIPLoader, PreviewAny, Seed (rgthree), SaveVideo, TextGenerateLTX2Prompt, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 797985848768046, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `MarkdownNote`
- `MarkdownNote`
- `LTXVScheduler`
- `ImageScaleBy`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `EmptyImage`
- `PrimitiveInt`
- `GetImageSize`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `PreviewAny`
- `Seed (rgthree)`
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `797985848768046`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`LTXVScheduler`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`EmptyImage`、`GetImageSize`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecode`、`KSampler`、`DualCLIPLoader`、`Seed (rgthree)`、`SaveVideo`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
