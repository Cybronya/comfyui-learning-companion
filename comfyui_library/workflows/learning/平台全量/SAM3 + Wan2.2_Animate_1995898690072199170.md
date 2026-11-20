---
key: 平台全量/SAM3 + Wan2.2_Animate_1995898690072199170.json
name: SAM3 + Wan2.2_Animate_1995898690072199170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SAM3 + Wan2.2_Animate_1995898690072199170.json
hash: 8968413356c3db0e
coverage: 0.460526
learned_at: 2026-11-14 00:55:01
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPTextEncode, TrimVideoLatent, VAEDecode, ModelSamplingSD3, WanAnimateToVideo, KSampler, PrimitiveInt, PrimitiveInt, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, easy showAnything, GetNode, GetNode, easy showAnything, SetNode, DrawMaskOnImage, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoInfoLoaded, SetNode, SetNode, easy showAnything, ImageResizeKJv2, GetImageSizeAndCount, GrowMaskWithBlur, DrawMaskOnImage, BlockifyMask, DrawViTPose, PoseAndFaceDetection, OnnxDetectionModelLoader, GetNode, ImageFromBatch+, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, CLIPVisionEncode, SetNode, LoadImage, SAM3Segmentation, LoadSAM3Model, SAM3Segmentation]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 322717611573271, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SAM3 + Wan2.2_Animate_1995898690072199170.json

> 来源文件 `comfyui_library/workflows/平台全量/SAM3 + Wan2.2_Animate_1995898690072199170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `DrawMaskOnImage`
- `BlockifyMask`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `GetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `CLIPVisionEncode`
- `SetNode`
- `LoadImage`
- `SAM3Segmentation`
- `LoadSAM3Model`
- `SAM3Segmentation`

## 关键参数

- `seed` = `322717611573271`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（35/76）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`WanAnimateToVideo`、`KSampler`、`VHS_VideoCombine`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`ImageFromBatch+`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`CLIPVisionEncode`、`LoadImage`、`SAM3Segmentation`、`LoadSAM3Model`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
