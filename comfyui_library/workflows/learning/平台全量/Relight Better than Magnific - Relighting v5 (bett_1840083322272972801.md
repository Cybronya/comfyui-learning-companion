---
key: 平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json
name: Relight Better than Magnific - Relighting v5 (bett_1840083322272972801
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json
hash: 35d5dca9de539640
coverage: 0.787611
learned_at: 2026-11-14 00:54:52
nodes: [Image Size to Number, Note, Note, Note, Note, Note, ImageScaleToMegapixels, SAMModelLoader (segment anything), GroundingDinoModelLoader (segment anything), PreviewImage, PreviewImage, MaskToImage, PreviewImage, CLIPTextEncode, ConditioningConcat, CLIPTextEncode, VAEEncode, IPAdapterUnifiedLoader, GrowMaskWithBlur, RemapMaskRange, MaskToImage, MaskToImage, PreviewImage, JWImageResize, GrowMaskWithBlur, MaskFromRGBCMYBW+, ICLightConditioning, VAEEncode, VAEDecode, CheckpointLoaderSimple, RemapImageRange, RemapImageRange, RemapImageRange, RemapImageRange, ColorMatchImage, ColorMatchImage, ColorMatchImage, ColorMatchImage, Reroute, BatchAverageImage, BatchAverageImage, ImageBatch, BatchAverageImage, FrequencySeparationHSV, PreviewImage, PreviewImage, PreviewImage, PreviewImage, FrequencySeparation, Image Blending Mode, PreviewImage, GrowMaskWithBlur, CLIPTextEncode, JWImageResize, Image Comparer (rgthree), ImageBatch, Image Blending Mode, ImageBatchMulti, JWImageResize, PreviewBridge, RemapMaskRange, MaskToImage, Note, Image Comparer (rgthree), Image Blending Mode, Note, Float, Image Blending Mode, CheckpointLoaderSimple, PreviewImage, Cfg Literal, PreviewImage, VAEEncode, VAEEncode, FrequencyCombination, SaveImage, SaveImage, FrequencyCombination, Image Comparer (rgthree), RemapImageRange, RemapImageRange, GroundingDinoSAMSegment (segment anything), Image Blend by Mask, KSampler, VAEDecode, JWImageResize, Image Blend by Mask, DepthAnythingPreprocessor, IPAdapterAdvanced, ControlNetApply, Float, CLIPTextEncode, CLIPTextEncode, ImageCrop, JWImageResize, JWImageResize, JWImageResize, JWImageResize, JWImageResize, Number to Int, Number to Int, Int, LoadImage, ControlNetLoader, Image Comparer (rgthree), LoadImage, PreviewImage, JWImageResize, LoadImageMask, Switch any [Crystools], Switch any [Crystools], KSampler, LoadAndApplyICLightUnet]
patterns: [image_to_image, controlnet]
missing: []
parameters: {"cfg": 2.5, "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors", "controlnet_strength": 0.85, "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 100361857014346, "steps": 30}
---

# 平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json

> 来源文件 `comfyui_library/workflows/平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `Image Size to Number`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `ImageScaleToMegapixels`
- `SAMModelLoader (segment anything)`
- `GroundingDinoModelLoader (segment anything)`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningConcat`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `IPAdapterUnifiedLoader`
- `GrowMaskWithBlur`
- `RemapMaskRange`
- `MaskToImage`
- `MaskToImage`
- `PreviewImage`
- `JWImageResize`
- `GrowMaskWithBlur`
- `MaskFromRGBCMYBW+`
- `ICLightConditioning`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `RemapImageRange`
- `RemapImageRange`
- `RemapImageRange`
- `RemapImageRange`
- `ColorMatchImage`
- `ColorMatchImage`
- `ColorMatchImage`
- `ColorMatchImage`
- `Reroute`
- `BatchAverageImage`
- `BatchAverageImage`
- `ImageBatch`
- `BatchAverageImage`
- `FrequencySeparationHSV`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `FrequencySeparation`
- `Image Blending Mode`
- `PreviewImage`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `JWImageResize`
- `Image Comparer (rgthree)`
- `ImageBatch`
- `Image Blending Mode`
- `ImageBatchMulti`
- `JWImageResize`
- `PreviewBridge`
- `RemapMaskRange`
- `MaskToImage`
- `Note`
- `Image Comparer (rgthree)`
- `Image Blending Mode`
- `Note`
- `Float`
- `Image Blending Mode`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `Cfg Literal`
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `FrequencyCombination`
- `SaveImage`
- `SaveImage`
- `FrequencyCombination`
- `Image Comparer (rgthree)`
- `RemapImageRange`
- `RemapImageRange`
- `GroundingDinoSAMSegment (segment anything)`
- `Image Blend by Mask`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JWImageResize`
- `Image Blend by Mask`
- `DepthAnythingPreprocessor`
- `IPAdapterAdvanced`
- `ControlNetApply` ★核心
- `Float`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `JWImageResize`
- `JWImageResize`
- `JWImageResize`
- `JWImageResize`
- `JWImageResize`
- `Number to Int`
- `Number to Int`
- `Int`
- `LoadImage`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `JWImageResize`
- `LoadImageMask`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `KSampler` ★核心
- `LoadAndApplyICLightUnet`

**识别到的模式**：image_to_image、controlnet

## 关键参数

- `checkpoint` = `epicrealism_naturalSinRC1VAE.safetensors`
- `seed` = `100361857014346`
- `steps` = `30`
- `cfg` = `2.5`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `0.85`

## 知识

覆盖率 **79%**（89/113）

**有卡**：`Image Size to Number`、`ImageScaleToMegapixels`、`SAMModelLoader (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`MaskToImage`、`CLIPTextEncode`、`ConditioningConcat`、`VAEEncode`、`IPAdapterUnifiedLoader`、`GrowMaskWithBlur`、`RemapMaskRange`、`JWImageResize`、`MaskFromRGBCMYBW+`、`ICLightConditioning`、`VAEDecode`、`CheckpointLoaderSimple`、`RemapImageRange`、`ColorMatchImage`、`BatchAverageImage`、`ImageBatch`、`FrequencySeparationHSV`、`FrequencySeparation`、`Image Blending Mode`、`ImageBatchMulti`、`PreviewBridge`、`Float`、`Cfg Literal`、`FrequencyCombination`、`SaveImage`、`GroundingDinoSAMSegment (segment anything)`、`Image Blend by Mask`、`KSampler`、`DepthAnythingPreprocessor`、`IPAdapterAdvanced`、`ControlNetApply`、`ImageCrop`、`Number to Int`、`Int`、`LoadImage`、`ControlNetLoader`、`LoadImageMask`、`Switch any [Crystools]`、`LoadAndApplyICLightUnet`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApply、ControlNetLoader、DepthAnythingPreprocessor
