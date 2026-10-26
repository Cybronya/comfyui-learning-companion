---
key: 数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json
name: Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json
hash: 3f94ec486092d19d
coverage: 0.514286
learned_at: 2026-10-26 01:57:50
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, GetNode, GetNode, PixelPerfectResolution, SetNode, SetNode, GrowMask, Sam2Segmentation, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, WanAnimateToVideo, TrimVideoLatent, Reroute, GetNode, GetNode, GetNode, VAEDecode, DownloadAndLoadSAM2Model, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, easy mathInt, easy batchAnything, VHS_VideoCombine, GetNode, ImageConcanate, VHS_GetImageCount, VHS_GetImageCount, VAEDecode, CLIPVisionLoader, ModelSamplingSD3, easy showAnything, easy forLoopStart, BlockifyMask, DrawMaskOnImage, InvertMask (segment anything), GetNode, SetNode, DrawMaskOnImage, easy forLoopEnd, SetNode, TrimVideoLatent, WanAnimateToVideo, SetNode, GetNode, GetNode, ImageScale, easy int, easy int, Text Multiline, MathExpression|pysssss, KSampler, GetNode, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy int, SetNode, easy int, GetNode, KSampler, SetNode, PointsEditor, VAELoader, CM_IntToFloat, GetNode, VHS_VideoCombine, MathExpression|pysssss, GetNode, GetNode, MathExpression|pysssss, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 458172117041110, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（105 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `SetNode`
- `SetNode`
- `GrowMask`
- `Sam2Segmentation`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `WanAnimateToVideo`
- `TrimVideoLatent`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `easy mathInt`
- `easy batchAnything`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcanate`
- `VHS_GetImageCount`
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `easy showAnything`
- `easy forLoopStart`
- `BlockifyMask`
- `DrawMaskOnImage`
- `InvertMask (segment anything)`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `easy forLoopEnd`
- `SetNode`
- `TrimVideoLatent`
- `WanAnimateToVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `easy int`
- `easy int`
- `Text Multiline`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `GetNode`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy int`
- `SetNode`
- `easy int`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `PointsEditor`
- `VAELoader`
- `CM_IntToFloat`
- `GetNode`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `458172117041110`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **51%**（54/105）

**有卡**：`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`GrowMask`、`Sam2Segmentation`、`CLIPTextEncode`、`CLIPVisionEncode`、`WanAnimateToVideo`、`TrimVideoLatent`、`VAEDecode`、`DownloadAndLoadSAM2Model`、`GetImageRangeFromBatch`、`easy mathInt`、`easy batchAnything`、`VHS_VideoCombine`、`ImageConcanate`、`VHS_GetImageCount`、`CLIPVisionLoader`、`ModelSamplingSD3`、`easy forLoopStart`、`BlockifyMask`、`DrawMaskOnImage`、`InvertMask (segment anything)`、`easy forLoopEnd`、`ImageScale`、`easy int`、`Text Multiline`、`MathExpression|pysssss`、`KSampler`、`DWPreprocessor`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`PointsEditor`、`VAELoader`、`CM_IntToFloat`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
