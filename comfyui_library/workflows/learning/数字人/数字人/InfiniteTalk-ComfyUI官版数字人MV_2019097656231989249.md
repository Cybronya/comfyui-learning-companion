---
key: 数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json
name: InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json
hash: 09b54aeee6711f95
coverage: 0.915254
learned_at: 2026-10-26 01:55:03
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), UNETLoader, Mute / Bypass Repeater (rgthree), VHS_VideoCombine, WanInfiniteTalkToVideo, easy showAnything, WanInfiniteTalkToVideo, AudioEncoderEncode, VAEDecode, ImageFromBatch, ImageBatch, Evaluate Integers, AudioInfo, LoraLoaderModelOnly, ModelPatchLoader, AudioEncoderLoader, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PreviewAudio, Evaluate Integers, CLIPLoader, VAELoader, MarkdownNote, CLIPTextEncode, ConditioningZeroOut, Text Multiline, KSampler, KSampler, LoadImage, LoadAudio, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VAEDecode, easy mathInt, AudioTrim, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, ImageBatchMulti, GetImageSize, easy showAnything, easy showAnything, easy forLoopStart, MathExpression|pysssss, ImageFromBatch, easy forLoopEnd, easy int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 70572066047003, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `UNETLoader` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy showAnything`
- `WanInfiniteTalkToVideo`
- `AudioEncoderEncode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `Evaluate Integers`
- `AudioInfo`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `Evaluate Integers`
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Text Multiline`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadAudio`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VAEDecode` ★核心
- `easy mathInt`
- `AudioTrim`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `GetImageSize`
- `easy showAnything`
- `easy showAnything`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy forLoopEnd`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 关键参数

- `seed` = `70572066047003`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **92%**（54/59）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`UNETLoader`、`Mute / Bypass Repeater (rgthree)`、`VHS_VideoCombine`、`WanInfiniteTalkToVideo`、`AudioEncoderEncode`、`VAEDecode`、`ImageFromBatch`、`ImageBatch`、`Evaluate Integers`、`AudioInfo`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`AudioEncoderLoader`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`Text Multiline`、`KSampler`、`LoadImage`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy mathInt`、`AudioTrim`、`ImageBatchMulti`、`GetImageSize`、`easy forLoopStart`、`MathExpression|pysssss`、`easy forLoopEnd`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
