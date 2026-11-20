---
key: 平台全量/wan2.2换脸视频换脸专用工作流_2002016613614383105.json
name: wan2.2换脸视频换脸专用工作流_2002016613614383105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2换脸视频换脸专用工作流_2002016613614383105.json
hash: 685cd3a431e30fed
coverage: 0.632353
learned_at: 2026-11-14 01:19:48
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, TrimVideoLatent, CLIPTextEncode, OnnxDetectionModelLoader, PoseAndFaceDetection, easy float, MathExpression|pysssss, SetNode, easy showAnything, RebatchImages, DrawMaskOnImage, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, GetNode, GetNode, CLIPLoaderGGUF, VAELoader, CLIPTextEncode, VHS_VideoCombine, SetNode, VAEDecode, GetNode, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, GrowMaskWithBlur, SegsToCombinedMask, MaskToImage, RebatchImages, KSampler, SetNode, SetNode, BboxDetectorSEGS, UltralyticsDetectorProvider, ImageToMask, BlockifyMask, LoraLoaderModelOnly, UnetLoaderGGUF, UNETLoader, VHS_VideoCombine, DrawViTPose, GetNode, MathExpression|pysssss, GetNode, SetNode, GetNode, LoadImage, VHS_VideoInfo, ImageResizeKJv2, MathExpression|pysssss, MathExpression|pysssss, SetNode, MathExpression|pysssss, MathExpression|pysssss, GetImageSize, VHS_VideoCombine, SetNode, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 322717611573275, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2换脸视频换脸专用工作流_2002016613614383105.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2换脸视频换脸专用工作流_2002016613614383105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（68 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `TrimVideoLatent`
- `CLIPTextEncode` ★核心
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `easy float`
- `MathExpression|pysssss`
- `SetNode`
- `easy showAnything`
- `RebatchImages`
- `DrawMaskOnImage`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPLoaderGGUF`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `SegsToCombinedMask`
- `MaskToImage`
- `RebatchImages`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `BboxDetectorSEGS`
- `UltralyticsDetectorProvider`
- `ImageToMask`
- `BlockifyMask`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `DrawViTPose`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetImageSize`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `322717611573275`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（43/68）

**有卡**：`WanAnimateToVideo`、`TrimVideoLatent`、`CLIPTextEncode`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy float`、`MathExpression|pysssss`、`RebatchImages`、`DrawMaskOnImage`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoaderGGUF`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`GrowMaskWithBlur`、`SegsToCombinedMask`、`MaskToImage`、`KSampler`、`BboxDetectorSEGS`、`UltralyticsDetectorProvider`、`ImageToMask`、`BlockifyMask`、`UnetLoaderGGUF`、`UNETLoader`、`DrawViTPose`、`LoadImage`、`VHS_VideoInfo`、`ImageResizeKJv2`、`GetImageSize`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、TrimVideoLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
