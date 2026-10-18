---
key: 视频生成/图生视频/InfiniteTalk-ComfyUI官版数字人MV_2019621453360013313.json
name: InfiniteTalk-ComfyUI官版数字人MV_2019621453360013313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/InfiniteTalk-ComfyUI官版数字人MV_2019621453360013313.json
hash: fb4c0478d74115a2
coverage: 0.928571
learned_at: 2026-10-15 22:35:03
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: ImageScaleByAspectRatio V2, AudioTrim, WanInfiniteTalkToVideo, easy showAnything, VAEDecode, WanInfiniteTalkToVideo, AudioEncoderEncode, VAEDecode, ImageFromBatch, ImageBatch, Evaluate Integers, AudioInfo, LoraLoaderModelOnly, easy mathInt, CLIPTextEncode, ConditioningZeroOut, easy forLoopEnd, KSampler, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, MathExpression|pysssss, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, ModelPatchLoader, AudioEncoderLoader, MelBandRoFormerModelLoader, CLIPLoader, VAELoader, easy int, UNETLoader, easy showAnything, ImageBatchMulti, GetImageSize, Evaluate Integers, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewAudio, MelBandRoFormerSampler, easy forLoopStart, VHS_VideoCombine, VHS_VideoCombine, LoadAudio, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 562765850503178, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/InfiniteTalk-ComfyUI官版数字人MV_2019621453360013313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019621453360013313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioTrim`
- `WanInfiniteTalkToVideo`
- `easy showAnything`
- `VAEDecode` ★核心
- `WanInfiniteTalkToVideo`
- `AudioEncoderEncode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `Evaluate Integers`
- `AudioInfo`
- `LoraLoaderModelOnly` ★核心
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `easy forLoopEnd`
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text Multiline`
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `MelBandRoFormerModelLoader`
- `CLIPLoader`
- `VAELoader`
- `easy int`
- `UNETLoader` ★核心
- `easy showAnything`
- `ImageBatchMulti`
- `GetImageSize`
- `Evaluate Integers`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `easy forLoopStart`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadAudio`
- `easy showAnything`

## 关键参数

- `seed` = `562765850503178`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（52/56）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioTrim`、`WanInfiniteTalkToVideo`、`VAEDecode`、`AudioEncoderEncode`、`ImageFromBatch`、`ImageBatch`、`Evaluate Integers`、`AudioInfo`、`LoraLoaderModelOnly`、`easy mathInt`、`CLIPTextEncode`、`ConditioningZeroOut`、`easy forLoopEnd`、`KSampler`、`MathExpression|pysssss`、`Text Multiline`、`ModelPatchLoader`、`AudioEncoderLoader`、`MelBandRoFormerModelLoader`、`CLIPLoader`、`VAELoader`、`easy int`、`UNETLoader`、`ImageBatchMulti`、`GetImageSize`、`LoadImage`、`PreviewAudio`、`MelBandRoFormerSampler`、`easy forLoopStart`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
