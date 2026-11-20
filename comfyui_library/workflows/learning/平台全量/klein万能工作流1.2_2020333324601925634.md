---
key: 平台全量/klein万能工作流1.2_2020333324601925634.json
name: klein万能工作流1.2_2020333324601925634
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/klein万能工作流1.2_2020333324601925634.json
hash: f5fa7acaf589ac85
coverage: 0.733871
learned_at: 2026-11-14 01:13:06
nodes: [SetNode, SetNode, GetImageSize+, SetNode, SetNode, SetNode, GetNode, SimpleMath+, GetNode, LayerUtility: If , ImpactInt, ImpactInt, GetNode, ConditioningZeroOut, SetNode, GetNode, Canny, AIO_Preprocessor, Note, GetNode, easy showAnything, GetImageSize+, ImageComposite+, EG_TX_SFBLS, LayerUtility: CropBoxResolve, ImageComposite+, LayerUtility: CropByMask, GetNode, LayerUtility: If , GrowMask, MaskBlur+, KSamplerSelect, ImageToMask, NoiseFromImage+, EG_TX_SFBLS, CR Integer To String, GetNode, GetNode, ImageSmartSharpen+, easy imageSize, Note, CR Text, ResizeImageMixlab, SimpleMath+, SimpleMath+, ResizeImageMixlab, Bounded Image Crop, TTP_Image_Assy, ResizeAndPadImage, ImageToMask, Bounded Image Crop with Mask, GetImageSize+, VAEDecode, easy imageListToImageBatch, GetImageSize+, TTP_Image_Tile_Batch, ImpactInt, easy imageBatchToImageList, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEEncode, TTP_Tile_image_size, SimpleMath+, GetImageSize+, SimpleMath+, ResizeAndPadImage, ImageToMask, Bounded Image Crop, Bounded Image Crop with Mask, ResizeImageMixlab, KSampler, StringContains, ImpactInt, ImpactInt, ImpactSwitch, LayerUtility: ImageBlend, easy imageSize, LayerUtility: If , ConditioningZeroOut, ImpactInt, ImpactInversedSwitch, GetNode, easy imageSize, SimpleMath+, SamplerCustom, GetNode, GetNode, easy textIndexSwitch, ShowText|pysssss, LoraNames_, easy textIndexSwitch, LoraNames_, LayerUtility: If , LoraLoaderModelOnly, PrimitiveString, PrimitiveString, PrimitiveString, DiffusionModelLoaderKJ, LoraLoaderModelOnly, CLIPLoader, VAELoader, PrimitiveString, PrimitiveFloat, LoraLoaderModelOnly, CM_IntBinaryCondition, PathchSageAttentionKJ, BasicScheduler, Note, LoadImage, Image Crop Face, Fast Bypasser (rgthree), AIO_Preprocessor, ImpactInt, ImpactSwitch, ImpactSwitch, Image Comparer (rgthree), VAEDecode, ImpactSwitch, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ColorMatch, PrimitiveFloat]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 645760320548515, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/klein万能工作流1.2_2020333324601925634.json

> 来源文件 `comfyui_library/workflows/平台全量/klein万能工作流1.2_2020333324601925634.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `SetNode`
- `SetNode`
- `GetImageSize+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `LayerUtility: If `
- `ImpactInt`
- `ImpactInt`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `Canny`
- `AIO_Preprocessor`
- `Note`
- `GetNode`
- `easy showAnything`
- `GetImageSize+`
- `ImageComposite+`
- `EG_TX_SFBLS`
- `LayerUtility: CropBoxResolve`
- `ImageComposite+`
- `LayerUtility: CropByMask`
- `GetNode`
- `LayerUtility: If `
- `GrowMask`
- `MaskBlur+`
- `KSamplerSelect` ★核心
- `ImageToMask`
- `NoiseFromImage+`
- `EG_TX_SFBLS`
- `CR Integer To String`
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `easy imageSize`
- `Note`
- `CR Text`
- `ResizeImageMixlab`
- `SimpleMath+`
- `SimpleMath+`
- `ResizeImageMixlab`
- `Bounded Image Crop`
- `TTP_Image_Assy`
- `ResizeAndPadImage`
- `ImageToMask`
- `Bounded Image Crop with Mask`
- `GetImageSize+`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `ImpactInt`
- `easy imageBatchToImageList`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEEncode` ★核心
- `TTP_Tile_image_size`
- `SimpleMath+`
- `GetImageSize+`
- `SimpleMath+`
- `ResizeAndPadImage`
- `ImageToMask`
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `ResizeImageMixlab`
- `KSampler` ★核心
- `StringContains`
- `ImpactInt`
- `ImpactInt`
- `ImpactSwitch`
- `LayerUtility: ImageBlend`
- `easy imageSize`
- `LayerUtility: If `
- `ConditioningZeroOut`
- `ImpactInt`
- `ImpactInversedSwitch`
- `GetNode`
- `easy imageSize`
- `SimpleMath+`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `easy textIndexSwitch`
- `ShowText|pysssss`
- `LoraNames_`
- `easy textIndexSwitch`
- `LoraNames_`
- `LayerUtility: If `
- `LoraLoaderModelOnly` ★核心
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveString`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `CM_IntBinaryCondition`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `Note`
- `LoadImage`
- `Image Crop Face`
- `Fast Bypasser (rgthree)`
- `AIO_Preprocessor`
- `ImpactInt`
- `ImpactSwitch`
- `ImpactSwitch`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ColorMatch`
- `PrimitiveFloat`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `645760320548515`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（91/124）

**有卡**：`GetImageSize+`、`SimpleMath+`、`LayerUtility: If `、`ImpactInt`、`ConditioningZeroOut`、`Canny`、`AIO_Preprocessor`、`ImageComposite+`、`EG_TX_SFBLS`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`GrowMask`、`MaskBlur+`、`KSamplerSelect`、`ImageToMask`、`NoiseFromImage+`、`CR Integer To String`、`ImageSmartSharpen+`、`easy imageSize`、`CR Text`、`ResizeImageMixlab`、`Bounded Image Crop`、`TTP_Image_Assy`、`ResizeAndPadImage`、`Bounded Image Crop with Mask`、`VAEDecode`、`easy imageListToImageBatch`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAEEncode`、`TTP_Tile_image_size`、`KSampler`、`StringContains`、`LayerUtility: ImageBlend`、`ImpactInversedSwitch`、`SamplerCustom`、`easy textIndexSwitch`、`LoraNames_`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`CM_IntBinaryCondition`、`PathchSageAttentionKJ`、`BasicScheduler`、`LoadImage`、`Image Crop Face`、`Fast Bypasser (rgthree)`、`SaveImage`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、Canny

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
