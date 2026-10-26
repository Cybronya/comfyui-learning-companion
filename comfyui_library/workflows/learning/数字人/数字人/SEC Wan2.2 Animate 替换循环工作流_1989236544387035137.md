---
key: 数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json
name: SEC Wan2.2 Animate 替换循环工作流_1989236544387035137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json
hash: bf0177ab92f672a9
coverage: 0.508333
learned_at: 2026-10-26 01:57:11
nodes: [GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, TrimVideoLatent, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, easy mathInt, easy batchAnything, VHS_VideoCombine, GetNode, ImageConcanate, VHS_GetImageCount, VHS_GetImageCount, VAEDecode, CLIPVisionLoader, easy showAnything, easy forLoopStart, easy forLoopEnd, SetNode, TrimVideoLatent, SetNode, GetNode, GetNode, ImageScale, KSampler, CLIPLoader, Text Multiline, SetNode, SetNode, GetNode, easy int, GetNode, easy int, easy int, easy int, SetNode, SetNode, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, SetNode, GetNode, CM_IntToFloat, SetNode, KSampler, PixelPerfectResolution, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, SetNode, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, GetNode, InvertMask (segment anything), DrawMaskOnImage, DrawMaskOnImage, BlockifyMask, SetNode, SetNode, GrowMask, Note, BlockifyMask, DownloadAndLoadSAM2Model, SeCModelLoader, GrowMask, SetNode, Sam2Segmentation, GetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, GetNode, SeCVideoSegmentation, SetNode, GetNode, DWPreprocessor, ImageFromBatch, GetNode, SetNode, SetNode, ModelSamplingSD3, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, WanAnimateToVideo, WanAnimateToVideo, GetNode, GetNode, GetNode, UNETLoader, SetNode, LoadImage, VHS_LoadVideo, JWInteger, PreviewImage, PointsEditor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1081488464905470, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
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
- `CLIPVisionEncode`
- `TrimVideoLatent`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
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
- `easy showAnything`
- `easy forLoopStart`
- `easy forLoopEnd`
- `SetNode`
- `TrimVideoLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `KSampler` ★核心
- `CLIPLoader`
- `Text Multiline`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy int`
- `GetNode`
- `easy int`
- `easy int`
- `easy int`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `CM_IntToFloat`
- `SetNode`
- `KSampler` ★核心
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `InvertMask (segment anything)`
- `DrawMaskOnImage`
- `DrawMaskOnImage`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `GrowMask`
- `Note`
- `BlockifyMask`
- `DownloadAndLoadSAM2Model`
- `SeCModelLoader`
- `GrowMask`
- `SetNode`
- `Sam2Segmentation`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SeCVideoSegmentation`
- `SetNode`
- `GetNode`
- `DWPreprocessor`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `JWInteger`
- `PreviewImage`
- `PointsEditor`

## 关键参数

- `seed` = `1081488464905470`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **51%**（61/120）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`TrimVideoLatent`、`VAEDecode`、`GetImageRangeFromBatch`、`easy mathInt`、`easy batchAnything`、`VHS_VideoCombine`、`ImageConcanate`、`VHS_GetImageCount`、`CLIPVisionLoader`、`easy forLoopStart`、`easy forLoopEnd`、`ImageScale`、`KSampler`、`CLIPLoader`、`Text Multiline`、`easy int`、`MathExpression|pysssss`、`CM_IntToFloat`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`LoraLoaderModelOnly`、`VAELoader`、`InvertMask (segment anything)`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`DownloadAndLoadSAM2Model`、`SeCModelLoader`、`Sam2Segmentation`、`SeCVideoSegmentation`、`DWPreprocessor`、`ImageFromBatch`、`ModelSamplingSD3`、`WanAnimateToVideo`、`UNETLoader`、`LoadImage`、`VHS_LoadVideo`、`JWInteger`、`PointsEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
