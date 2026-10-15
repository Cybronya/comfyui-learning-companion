---
key: 视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json
name: LTX2.3文生视频_2042483704538337282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json
hash: 9f444a0521674822
coverage: 0.965517
learned_at: 2026-10-15 22:45:11
nodes: [CLIPTextEncode, CLIPTextEncode, CreateVideo, LTXVConcatAVLatent, LTXVCropGuides, KSampler, LatentUpscaleModelLoader, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXAVTextEncoderLoader, RH_Translator, Text, LTXVSeparateAVLatent, LTXVLatentUpsampler, Reroute, LoraLoaderModelOnly, LTXVConditioning, VAEDecodeTiled, CheckpointLoaderSimple, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVSeparateAVLatent, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 24, "sampler_name": "euler", "scheduler": "simple", "seed": 1045784703323245, "steps": 4, "width": 241}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `KSampler` ★核心
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAVTextEncoderLoader`
- `RH_Translator`
- `Text`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `SaveVideo`

## 关键参数

- `seed` = `1045784703323245`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `241`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`CLIPTextEncode`、`CreateVideo`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`KSampler`、`LatentUpscaleModelLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXAVTextEncoderLoader`、`RH_Translator`、`Text`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXVConditioning`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`SaveVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
