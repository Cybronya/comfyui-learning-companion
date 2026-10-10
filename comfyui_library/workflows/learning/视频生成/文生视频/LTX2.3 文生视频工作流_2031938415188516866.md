---
key: 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json
name: LTX2.3 文生视频工作流_2031938415188516866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json
hash: e699497a0f8a1314
coverage: 0.804878
learned_at: 2026-10-11 03:16:46
nodes: [MarkdownNote, MarkdownNote, LTXVScheduler, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, CreateVideo, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, KSamplerSelect, RandomNoise, Reroute, PreviewAny, KSampler, LTXVSeparateAVLatent, PrimitiveInt, LTXVCropGuides, SaveVideo, LoraLoaderModelOnly, DualCLIPLoader, EmptyImage, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, TextGenerateLTX2Prompt, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 205486804366356, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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
- `CreateVideo`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `PreviewAny`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `LTXVCropGuides`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `205486804366356`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`LTXVScheduler`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`SaveVideo`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`EmptyImage`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`TextGenerateLTX2Prompt`、`Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
