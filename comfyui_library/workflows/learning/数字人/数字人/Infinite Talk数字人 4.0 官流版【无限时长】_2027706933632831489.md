---
key: 数字人/数字人/Infinite Talk数字人 4.0 官流版【无限时长】_2027706933632831489.json
name: Infinite Talk数字人 4.0 官流版【无限时长】_2027706933632831489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Infinite Talk数字人 4.0 官流版【无限时长】_2027706933632831489.json
hash: 75d8925834172dac
coverage: 0.466667
learned_at: 2026-10-26 01:54:51
nodes: [GetNode, GetNode, GetNode, GetNode, ImageFromBatch, CLIPVisionEncode, easy forLoopEnd, easy forLoopStart, GetNode, MathExpression|pysssss, GetNode, GetNode, easy indexAnything, Int, Compare, easy ifElse, ImageBatch, WanInfiniteTalkToVideo, SetNode, SetNode, ModelPatchLoader, GetNode, SetNode, SetNode, PreviewAudio, AudioSeparation, SetNode, CLIPVisionLoader, SetNode, SetNode, GetNode, LongTextToList, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CLIPTextEncode, GetNode, VAEDecode, SetNode, SetNode, SetNode, SetNode, GetNode, VAELoader, KSampler, CLIPTextEncode, LoadImage, GetNode, GetNode, AudioEncoderEncode, AudioEncoderLoader, SetNode, SetNode, MathExpression|pysssss, GetNode, VRGDG_AudioCropTime, INTConstant, INTConstant, ttN float, LoadAudio, VHS_VideoCombine, JjkText, SetNode, SetNode, CLIPLoader, RHHiddenNodes, GetNode, GetNode, RHHiddenNodes, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1021175899090845, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Infinite Talk数字人 4.0 官流版【无限时长】_2027706933632831489.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Infinite Talk数字人 4.0 官流版【无限时长】_2027706933632831489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（75 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `CLIPVisionEncode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy indexAnything`
- `Int`
- `Compare`
- `easy ifElse`
- `ImageBatch`
- `WanInfiniteTalkToVideo`
- `SetNode`
- `SetNode`
- `ModelPatchLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewAudio`
- `AudioSeparation`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `LongTextToList`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `VRGDG_AudioCropTime`
- `INTConstant`
- `INTConstant`
- `ttN float`
- `LoadAudio`
- `VHS_VideoCombine`
- `JjkText`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `LoadImage`

## 关键参数

- `seed` = `1021175899090845`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **47%**（35/75）

**有卡**：`ImageFromBatch`、`CLIPVisionEncode`、`easy forLoopEnd`、`easy forLoopStart`、`MathExpression|pysssss`、`easy indexAnything`、`Int`、`Compare`、`ImageBatch`、`WanInfiniteTalkToVideo`、`ModelPatchLoader`、`PreviewAudio`、`AudioSeparation`、`CLIPVisionLoader`、`LongTextToList`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`KSampler`、`LoadImage`、`AudioEncoderEncode`、`AudioEncoderLoader`、`VRGDG_AudioCropTime`、`INTConstant`、`ttN float`、`LoadAudio`、`VHS_VideoCombine`、`CLIPLoader`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、AudioEncoderLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
