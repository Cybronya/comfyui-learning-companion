---
key: 数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json
name: Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json
hash: 7b7c40ee9f201e52
coverage: 0.903226
learned_at: 2026-10-26 01:57:53
nodes: [ModelSamplingSD3, easy forLoopStart, SimpleMath+, LatentConcat, easy forLoopEnd, WanSoundImageToVideo, KSampler, LatentCut, LatentConcat, VAEDecode, ImageFromBatch, UNETLoader, VAELoader, CLIPLoader, AudioEncoderLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, ImageResizeKJv2, AudioEncoderEncode, MathExpression|pysssss, WanSoundImageToVideoExtend, KSampler, Audio Duration (mtb), PrimitiveInt, LoadAudio, LoadImage, Primitive integer [Crystools], Note, Note, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 84874136191928, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `ModelSamplingSD3`
- `easy forLoopStart`
- `SimpleMath+`
- `LatentConcat`
- `easy forLoopEnd`
- `WanSoundImageToVideo`
- `KSampler` ★核心
- `LatentCut`
- `LatentConcat`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `AudioEncoderEncode`
- `MathExpression|pysssss`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `Audio Duration (mtb)`
- `PrimitiveInt`
- `LoadAudio`
- `LoadImage`
- `Primitive integer [Crystools]`
- `Note`
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `84874136191928`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`ModelSamplingSD3`、`easy forLoopStart`、`SimpleMath+`、`LatentConcat`、`easy forLoopEnd`、`WanSoundImageToVideo`、`KSampler`、`LatentCut`、`VAEDecode`、`ImageFromBatch`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`AudioEncoderLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`AudioEncoderEncode`、`MathExpression|pysssss`、`WanSoundImageToVideoExtend`、`Audio Duration (mtb)`、`LoadAudio`、`LoadImage`、`Primitive integer [Crystools]`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
