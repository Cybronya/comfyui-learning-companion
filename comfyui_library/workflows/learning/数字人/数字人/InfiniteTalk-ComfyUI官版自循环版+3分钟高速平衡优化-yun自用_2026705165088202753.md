---
key: 数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json
name: InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json
hash: f175f71c0bec0773
coverage: 1
learned_at: 2026-10-26 01:55:03
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, WanInfiniteTalkToVideo, WanInfiniteTalkToVideo, AudioEncoderEncode, ImageFromBatch, ImageBatch, Evaluate Integers, LoraLoaderModelOnly, ModelPatchLoader, AudioEncoderLoader, MelBandRoFormerSampler, MelBandRoFormerModelLoader, easy mathInt, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, easy forLoopStart, KSampler, KSampler, easy forLoopEnd, AudioInfo, ImageFromBatch, easy int, Evaluate Integers, AudioTrim, VHS_VideoCombine, VAEDecode, VAEDecode, LoadImage, LoadImage, LoadImage, LoadAudio, JWFloat, Text Multiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 845509539872213, "steps": 3}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `WanInfiniteTalkToVideo`
- `WanInfiniteTalkToVideo`
- `AudioEncoderEncode`
- `ImageFromBatch`
- `ImageBatch`
- `Evaluate Integers`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `easy mathInt`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `easy forLoopStart`
- `KSampler` ★核心
- `KSampler` ★核心
- `easy forLoopEnd`
- `AudioInfo`
- `ImageFromBatch`
- `easy int`
- `Evaluate Integers`
- `AudioTrim`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `JWFloat`
- `Text Multiline`

## 关键参数

- `seed` = `845509539872213`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`WanInfiniteTalkToVideo`、`AudioEncoderEncode`、`ImageFromBatch`、`ImageBatch`、`Evaluate Integers`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`AudioEncoderLoader`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`easy mathInt`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`easy forLoopStart`、`KSampler`、`easy forLoopEnd`、`AudioInfo`、`easy int`、`AudioTrim`、`VHS_VideoCombine`、`VAEDecode`、`LoadImage`、`LoadAudio`、`JWFloat`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
