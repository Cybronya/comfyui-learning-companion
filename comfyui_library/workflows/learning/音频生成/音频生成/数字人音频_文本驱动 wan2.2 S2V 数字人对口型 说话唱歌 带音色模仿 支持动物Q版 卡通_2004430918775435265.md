---
key: 音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json
name: 数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json
hash: 1dfe0b7baf825fd7
coverage: 0.933333
learned_at: 2026-10-18 01:47:05
nodes: [ModelSamplingSD3, MathExpression|pysssss, easy forLoopStart, SimpleMath+, PrimitiveInt, Audio Duration (mtb), LatentConcat, easy forLoopEnd, KSampler, CLIPTextEncode, ImageResizeKJv2, AudioEncoderEncode, WanSoundImageToVideo, KSampler, LatentCut, LatentConcat, VAEDecode, WanSoundImageToVideoExtend, Note, CLIPTextEncode, Primitive integer [Crystools], ImageFromBatch, VHS_VideoCombine, LoadImage, LoadAudio, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, AudioEncoderLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 624053721295944, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `SimpleMath+`
- `PrimitiveInt`
- `Audio Duration (mtb)`
- `LatentConcat`
- `easy forLoopEnd`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `AudioEncoderEncode`
- `WanSoundImageToVideo`
- `KSampler` ★核心
- `LatentCut`
- `LatentConcat`
- `VAEDecode` ★核心
- `WanSoundImageToVideoExtend`
- `Note`
- `CLIPTextEncode` ★核心
- `Primitive integer [Crystools]`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `AudioEncoderLoader`

## 关键参数

- `seed` = `624053721295944`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`ModelSamplingSD3`、`MathExpression|pysssss`、`easy forLoopStart`、`SimpleMath+`、`Audio Duration (mtb)`、`LatentConcat`、`easy forLoopEnd`、`KSampler`、`CLIPTextEncode`、`ImageResizeKJv2`、`AudioEncoderEncode`、`WanSoundImageToVideo`、`LatentCut`、`VAEDecode`、`WanSoundImageToVideoExtend`、`Primitive integer [Crystools]`、`ImageFromBatch`、`VHS_VideoCombine`、`LoadImage`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`AudioEncoderLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
