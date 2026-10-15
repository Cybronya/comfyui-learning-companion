---
key: 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json
name: LTX2.3文生视频_2033356584612532225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json
hash: f72ce22afd6b1ddd
coverage: 0.815789
learned_at: 2026-10-15 22:45:11
nodes: [LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, KSamplerSelect, RandomNoise, KSampler, LTXVSeparateAVLatent, LTXVCropGuides, DualCLIPLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, ImageScaleBy, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, GetImageSize, PrimitiveInt, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, MarkdownNote, MarkdownNote, MarkdownNote, TextGenerateLTX2Prompt, LTXVConcatAVLatent, LTXVLatentUpsampler, PreviewAny, EmptyImage, SaveVideo, PrimitiveFloat, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 266547934432427, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ImageScaleBy`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextGenerateLTX2Prompt`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `EmptyImage`
- `SaveVideo`
- `PrimitiveFloat`
- `PrimitiveInt`

## 关键参数

- `seed` = `266547934432427`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConditioning`、`ImageScaleBy`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`GetImageSize`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`TextGenerateLTX2Prompt`、`LTXVLatentUpsampler`、`EmptyImage`、`SaveVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
