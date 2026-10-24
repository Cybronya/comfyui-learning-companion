---
key: 图片生成/图生图/kontext全自动贴图换脸V1.0TEST_1948721957064384513.json
name: kontext全自动贴图换脸V1.0TEST_1948721957064384513
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext全自动贴图换脸V1.0TEST_1948721957064384513.json
hash: 45ab01e4c4040e61
coverage: 0.8
learned_at: 2026-10-23 11:39:27
nodes: [ReferenceLatent, ConditioningZeroOut, SetNode, DualCLIPLoader, VAELoader, PreviewAny, easy cleanGpuUsed, CR Text, SetNode, DetectFaces, ImageFromBatch+, CLIPTextEncode, VAEEncode, FluxGuidance, GetNode, GetNode, MaskToImage, ImageFromBatch+, InvertMask (segment anything), Image Blend by Mask, WarpFacesBack, PreviewImage, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageConcanate, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, VAEDecode, DetectFaces, SaveImage, GrowMask, ImageConcanate, PreviewImage, LoadImage, NunchakuFluxLoraLoader, CropFaces, KSampler, GrowMask, LoadImage, CropFaces]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 688, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/kontext全自动贴图换脸V1.0TEST_1948721957064384513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext全自动贴图换脸V1.0TEST_1948721957064384513.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `PreviewAny`
- `easy cleanGpuUsed`
- `CR Text`
- `SetNode`
- `DetectFaces`
- `ImageFromBatch+`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `ImageFromBatch+`
- `InvertMask (segment anything)`
- `Image Blend by Mask`
- `WarpFacesBack`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `VAEDecode` ★核心
- `DetectFaces`
- `SaveImage`
- `GrowMask`
- `ImageConcanate`
- `PreviewImage`
- `LoadImage`
- `NunchakuFluxLoraLoader` ★核心
- `CropFaces`
- `KSampler` ★核心
- `GrowMask`
- `LoadImage`
- `CropFaces`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `688`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`CR Text`、`DetectFaces`、`ImageFromBatch+`、`CLIPTextEncode`、`VAEEncode`、`FluxGuidance`、`MaskToImage`、`InvertMask (segment anything)`、`Image Blend by Mask`、`WarpFacesBack`、`ImageScaleToTotalPixels`、`ImageConcanate`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`VAEDecode`、`SaveImage`、`GrowMask`、`LoadImage`、`CropFaces`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
