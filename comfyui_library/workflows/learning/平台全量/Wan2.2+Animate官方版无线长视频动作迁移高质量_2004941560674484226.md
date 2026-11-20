---
key: 平台全量/Wan2.2+Animate官方版无线长视频动作迁移高质量_2004941560674484226.json
name: Wan2.2+Animate官方版无线长视频动作迁移高质量_2004941560674484226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+Animate官方版无线长视频动作迁移高质量_2004941560674484226.json
hash: d26fdc1ddde0bfe5
coverage: 0.588235
learned_at: 2026-11-14 01:05:50
nodes: [TrimVideoLatent, KSampler, SetNode, LayerUtility: BooleanOperatorV2, GetNode, Reroute, GetNode, LayerUtility: BooleanOperatorV2, GetNode, ImageFromBatch, PointsEditor, ImageFromBatch, ImageFromBatch, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, CLIPLoaderGGUF, LoraLoaderModelOnly, CLIPTextEncode, VAELoader, CLIPVisionLoader, CM_IntToFloat, SetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, SetNode, GetNode, LayerUtility: If , GetNode, GetNode, GetNode, PrimitiveInt, SimpleMath+, ImageFromBatch, GetNode, LayerMask: ImageToMask, GetNode, SetNode, SeCModelLoader, SeCVideoSegmentation, GrowMaskWithBlur, BlockifyMask, DrawMaskOnImage, GetNode, MaskToImage, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, PrimitiveInt, PrimitiveInt, SetNode, SetNode, easy showAnything, PrimitiveInt, LayerUtility: If , VAEDecode, ImageFromBatch, easy forLoopEnd, easy forLoopStart, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, SetNode, LoadImage, GetNode, ImageFromBatch, GetNode, GetNode, easy batchAnything, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, ImageScale, CLIPTextEncode, CLIPVisionEncode, ImageFromBatch, Reroute, SetNode, SimpleMath+, LayerUtility: If , LayerUtility: BooleanOperatorV2, SimpleMath+, Reroute, WanAnimateToVideo, GetImageSizeAndCount, Int, VHS_VideoCombine, PoseAndFaceDetection, SetNode, Int, Int, easy showAnything, SimpleMath+, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_sde", "scheduler": "beta", "seed": 2025, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2+Animate官方版无线长视频动作迁移高质量_2004941560674484226.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+Animate官方版无线长视频动作迁移高质量_2004941560674484226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（102 个）：
- `TrimVideoLatent`
- `KSampler` ★核心
- `SetNode`
- `LayerUtility: BooleanOperatorV2`
- `GetNode`
- `Reroute`
- `GetNode`
- `LayerUtility: BooleanOperatorV2`
- `GetNode`
- `ImageFromBatch`
- `PointsEditor`
- `ImageFromBatch`
- `ImageFromBatch`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `SetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `SetNode`
- `GetNode`
- `LayerUtility: If `
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SimpleMath+`
- `ImageFromBatch`
- `GetNode`
- `LayerMask: ImageToMask`
- `GetNode`
- `SetNode`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GetNode`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `PrimitiveInt`
- `LayerUtility: If `
- `VAEDecode` ★核心
- `ImageFromBatch`
- `easy forLoopEnd`
- `easy forLoopStart`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `SetNode`
- `LoadImage`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `easy batchAnything`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ImageFromBatch`
- `Reroute`
- `SetNode`
- `SimpleMath+`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `SimpleMath+`
- `Reroute`
- `WanAnimateToVideo`
- `GetImageSizeAndCount`
- `Int`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `SetNode`
- `Int`
- `Int`
- `easy showAnything`
- `SimpleMath+`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `2025`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **59%**（60/102）

**有卡**：`TrimVideoLatent`、`KSampler`、`LayerUtility: BooleanOperatorV2`、`ImageFromBatch`、`PointsEditor`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoaderGGUF`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`CM_IntToFloat`、`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`LayerUtility: If `、`SimpleMath+`、`LayerMask: ImageToMask`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`MaskToImage`、`VAEDecode`、`easy forLoopEnd`、`easy forLoopStart`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy batchAnything`、`ImageScale`、`CLIPVisionEncode`、`WanAnimateToVideo`、`GetImageSizeAndCount`、`Int`、`PoseAndFaceDetection`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
