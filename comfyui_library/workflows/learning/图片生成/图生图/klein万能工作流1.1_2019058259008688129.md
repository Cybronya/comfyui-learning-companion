---
key: 图片生成/图生图/klein万能工作流1.1_2019058259008688129.json
name: klein万能工作流1.1_2019058259008688129
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/klein万能工作流1.1_2019058259008688129.json
hash: 6f011e1ad083dc82
coverage: 0.700935
learned_at: 2026-10-23 11:38:25
nodes: [SetNode, SetNode, LayerUtility: CropBoxResolve, GetImageSize+, SetNode, EG_TX_SFBLS, SetNode, SetNode, GetNode, GetImageSize+, SimpleMath+, ImageComposite+, GetNode, LayerUtility: If , ImpactInt, ImpactInt, VAEEncode, SamplerCustom, ImpactInt, ImpactInt, GetNode, GetNode, LayerUtility: If , ImpactSwitch, GetNode, GetNode, GetNode, VAEDecodeTiled, Latent Noise Injection, KSamplerSelect, BasicScheduler, AIO_Preprocessor, ConditioningZeroOut, LayerUtility: ImageBlend, TextEncodeQwenImageEdit, ImageSmartSharpen+, NoiseFromImage+, ResizeImageMixlab, ImageToMask, SetNode, GetNode, ResizeImageMixlab, SimpleMath+, SimpleMath+, easy imageSize, ImpactInt, ImageScaleBy, Canny, AIO_Preprocessor, Note, GetNode, ImpactSwitch, GetNode, PathchSageAttentionKJ, easy textIndexSwitch, ShowText|pysssss, LoraNames_, easy textIndexSwitch, LoraNames_, CR Integer To String, StringContains, ImpactInt, LayerUtility: If , GetImageSize+, easy showAnything, LayerUtility: If , ImpactSwitch, CFGZeroStar, LoraLoaderModelOnly, Image Crop Face, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetImageSize+, DyPE_FLUX, LoraLoaderModelOnly, PrimitiveString, PrimitiveString, PrimitiveString, Fast Bypasser (rgthree), DiffusionModelLoaderKJ, LoraLoaderModelOnly, CLIPLoader, VAELoader, Note, ImpactInt, Note, PrimitiveString, ImpactSwitch, SaveImage, CR Text, EG_TX_SFBLS, ImageComposite+, CM_IntBinaryCondition, GetNode, LayerUtility: CropByMask, LoadImage, VAEDecode, Bounded Image Crop, ResizeAndPadImage, Bounded Image Crop with Mask, ImageToMask, PrimitiveFloat, LoraLoaderModelOnly, PrimitiveFloat, KSampler, GrowMask, MaskBlur+]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1043101749336876, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/klein万能工作流1.1_2019058259008688129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/klein万能工作流1.1_2019058259008688129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `LayerUtility: CropBoxResolve`
- `GetImageSize+`
- `SetNode`
- `EG_TX_SFBLS`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSize+`
- `SimpleMath+`
- `ImageComposite+`
- `GetNode`
- `LayerUtility: If `
- `ImpactInt`
- `ImpactInt`
- `VAEEncode` ★核心
- `SamplerCustom` ★核心
- `ImpactInt`
- `ImpactInt`
- `GetNode`
- `GetNode`
- `LayerUtility: If `
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `Latent Noise Injection`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `LayerUtility: ImageBlend`
- `TextEncodeQwenImageEdit`
- `ImageSmartSharpen+`
- `NoiseFromImage+`
- `ResizeImageMixlab`
- `ImageToMask`
- `SetNode`
- `GetNode`
- `ResizeImageMixlab`
- `SimpleMath+`
- `SimpleMath+`
- `easy imageSize`
- `ImpactInt`
- `ImageScaleBy`
- `Canny`
- `AIO_Preprocessor`
- `Note`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `PathchSageAttentionKJ`
- `easy textIndexSwitch`
- `ShowText|pysssss`
- `LoraNames_`
- `easy textIndexSwitch`
- `LoraNames_`
- `CR Integer To String`
- `StringContains`
- `ImpactInt`
- `LayerUtility: If `
- `GetImageSize+`
- `easy showAnything`
- `LayerUtility: If `
- `ImpactSwitch`
- `CFGZeroStar`
- `LoraLoaderModelOnly` ★核心
- `Image Crop Face`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetImageSize+`
- `DyPE_FLUX`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `Fast Bypasser (rgthree)`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `ImpactInt`
- `Note`
- `PrimitiveString`
- `ImpactSwitch`
- `SaveImage`
- `CR Text`
- `EG_TX_SFBLS`
- `ImageComposite+`
- `CM_IntBinaryCondition`
- `GetNode`
- `LayerUtility: CropByMask`
- `LoadImage`
- `VAEDecode` ★核心
- `Bounded Image Crop`
- `ResizeAndPadImage`
- `Bounded Image Crop with Mask`
- `ImageToMask`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `KSampler` ★核心
- `GrowMask`
- `MaskBlur+`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1043101749336876`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（75/107）

**有卡**：`LayerUtility: CropBoxResolve`、`GetImageSize+`、`EG_TX_SFBLS`、`SimpleMath+`、`ImageComposite+`、`LayerUtility: If `、`ImpactInt`、`VAEEncode`、`SamplerCustom`、`VAEDecodeTiled`、`Latent Noise Injection`、`KSamplerSelect`、`BasicScheduler`、`AIO_Preprocessor`、`ConditioningZeroOut`、`LayerUtility: ImageBlend`、`TextEncodeQwenImageEdit`、`ImageSmartSharpen+`、`NoiseFromImage+`、`ResizeImageMixlab`、`ImageToMask`、`easy imageSize`、`ImageScaleBy`、`Canny`、`PathchSageAttentionKJ`、`easy textIndexSwitch`、`LoraNames_`、`CR Integer To String`、`StringContains`、`CFGZeroStar`、`LoraLoaderModelOnly`、`Image Crop Face`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`DyPE_FLUX`、`Fast Bypasser (rgthree)`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`SaveImage`、`CR Text`、`CM_IntBinaryCondition`、`LayerUtility: CropByMask`、`VAEDecode`、`Bounded Image Crop`、`ResizeAndPadImage`、`Bounded Image Crop with Mask`、`KSampler`、`GrowMask`、`MaskBlur+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、Canny

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
