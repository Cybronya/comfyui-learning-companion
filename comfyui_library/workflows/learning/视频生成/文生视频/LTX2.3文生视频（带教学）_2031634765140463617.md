---
key: 视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json
name: LTX2.3文生视频（带教学）_2031634765140463617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json
hash: 4869557737e1a83b
coverage: 0.666667
learned_at: 2026-10-15 22:45:13
nodes: [LTXVEmptyLatentAudio, Note, LTXVConditioning, LTXVConcatAVLatent, PrimitiveInt, SamplerCustomAdvanced, CLIPTextEncode, LTXVConcatAVLatent, KSampler, LTXVScheduler, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, Note, Note, Note, LTXVAudioVAEDecode, LTXVCropGuides, CreateVideo, Note, VAEDecodeTiled, PrimitiveFloat, Note, Note, KSamplerSelect, RandomNoise, Note, Note, Note, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CFGGuider, CheckpointLoaderSimple, Note, CLIPTextEncode, SaveVideo, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 24, "sampler_name": "euler", "scheduler": "simple", "seed": 572641473909537, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVScheduler`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Note`
- `Note`
- `Note`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `CreateVideo`
- `Note`
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `Note`
- `Note`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Note`
- `Note`
- `Note`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `572641473909537`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **67%**（26/39）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`KSampler`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`CreateVideo`、`VAEDecodeTiled`、`KSamplerSelect`、`RandomNoise`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CFGGuider`、`CheckpointLoaderSimple`、`SaveVideo`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
