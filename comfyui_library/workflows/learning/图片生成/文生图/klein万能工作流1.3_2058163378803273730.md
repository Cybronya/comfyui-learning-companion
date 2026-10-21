---
key: 图片生成/文生图/klein万能工作流1.3_2058163378803273730.json
name: klein万能工作流1.3_2058163378803273730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/klein万能工作流1.3_2058163378803273730.json
hash: d246edf8b316e6c7
coverage: 0.728
learned_at: 2026-10-19 22:46:11
nodes: [SetNode, SetNode, GetImageSize+, SetNode, SetNode, SetNode, GetNode, SimpleMath+, ImpactInt, ImpactInt, GetNode, ConditioningZeroOut, SetNode, GetNode, Canny, AIO_Preprocessor, Note, easy showAnything, GetImageSize+, EG_TX_SFBLS, LayerUtility: CropBoxResolve, ImageComposite+, LayerUtility: If , GrowMask, MaskBlur+, ResizeImageMixlab, Bounded Image Crop, ResizeAndPadImage, ImageToMask, Bounded Image Crop with Mask, GetImageSize+, TextEncodeQwenImageEditPlusAdvance_lrzjason, LayerUtility: If , CLIPLoader, VAELoader, CM_IntBinaryCondition, LoadImage, Image Crop Face, Fast Bypasser (rgthree), AIO_Preprocessor, ImpactSwitch, ImpactSwitch, Image Comparer (rgthree), SaveImage, LoadImage, KSamplerSelect, SamplerCustom, ImageToMask, ResizeAndPadImage, ConditioningZeroOut, GetNode, Bounded Image Crop with Mask, VAEDecode, GetImageSize+, Bounded Image Crop, ResizeImageMixlab, easy imageListToImageBatch, ColorMatch, easy imageBatchToImageList, easy imageBatchToImageList, easy imageSize, TTP_Image_Tile_Batch, SimpleMath+, SimpleMath+, easy imageSize, ImageToMask, ImageSmartSharpen+, GetNode, ImpactInt, BasicScheduler, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, easy imageSize, SimpleMath+, SimpleMath+, TTP_Image_Assy, NoiseFromImage+, TTP_Image_Tile_Batch, LoraLoaderModelOnly, PrimitiveFloat, LoraLoaderModelOnly, LayerUtility: ImageBlend, TTP_Tile_image_size, ImpactInt, ResizeImageMixlab, PrimitiveFloat, LayerUtility: If , ImpactInversedSwitch, PrimitiveString, PrimitiveString, GetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, Note, VAEDecode, KSampler, EG_TX_SFBLS, ImpactInt, CR Integer To String, StringContains, ImpactInt, LayerUtility: If , ImpactSwitch, ImageComposite+, ImpactInt, ImpactInt, LoraNames_, LoraLoaderModelOnly, GetNode, ImpactSwitch, LayerUtility: CropByMask, GetNode, Note, CR Text, ImpactInt, easy textIndexSwitch, LoraNames_, PrimitiveString, PrimitiveString, GetNode, easy textIndexSwitch, PrimitiveString, PrimitiveString, GetNode, ShowText|pysssss]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "simple", "seed": 645760320548515, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/klein万能工作流1.3_2058163378803273730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/klein万能工作流1.3_2058163378803273730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（125 个）：
- `SetNode`
- `SetNode`
- `GetImageSize+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `Canny`
- `AIO_Preprocessor`
- `Note`
- `easy showAnything`
- `GetImageSize+`
- `EG_TX_SFBLS`
- `LayerUtility: CropBoxResolve`
- `ImageComposite+`
- `LayerUtility: If `
- `GrowMask`
- `MaskBlur+`
- `ResizeImageMixlab`
- `Bounded Image Crop`
- `ResizeAndPadImage`
- `ImageToMask`
- `Bounded Image Crop with Mask`
- `GetImageSize+`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LayerUtility: If `
- `CLIPLoader`
- `VAELoader`
- `CM_IntBinaryCondition`
- `LoadImage`
- `Image Crop Face`
- `Fast Bypasser (rgthree)`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `ImpactSwitch`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `ImageToMask`
- `ResizeAndPadImage`
- `ConditioningZeroOut`
- `GetNode`
- `Bounded Image Crop with Mask`
- `VAEDecode` ★核心
- `GetImageSize+`
- `Bounded Image Crop`
- `ResizeImageMixlab`
- `easy imageListToImageBatch`
- `ColorMatch`
- `easy imageBatchToImageList`
- `easy imageBatchToImageList`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SimpleMath+`
- `SimpleMath+`
- `easy imageSize`
- `ImageToMask`
- `ImageSmartSharpen+`
- `GetNode`
- `ImpactInt`
- `BasicScheduler`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy imageSize`
- `SimpleMath+`
- `SimpleMath+`
- `TTP_Image_Assy`
- `NoiseFromImage+`
- `TTP_Image_Tile_Batch`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageBlend`
- `TTP_Tile_image_size`
- `ImpactInt`
- `ResizeImageMixlab`
- `PrimitiveFloat`
- `LayerUtility: If `
- `ImpactInversedSwitch`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Note`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EG_TX_SFBLS`
- `ImpactInt`
- `CR Integer To String`
- `StringContains`
- `ImpactInt`
- `LayerUtility: If `
- `ImpactSwitch`
- `ImageComposite+`
- `ImpactInt`
- `ImpactInt`
- `LoraNames_`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `ImpactSwitch`
- `LayerUtility: CropByMask`
- `GetNode`
- `Note`
- `CR Text`
- `ImpactInt`
- `easy textIndexSwitch`
- `LoraNames_`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `easy textIndexSwitch`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `ShowText|pysssss`

## 关键参数

- `seed` = `645760320548515`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（91/125）

**有卡**：`GetImageSize+`、`SimpleMath+`、`ImpactInt`、`ConditioningZeroOut`、`Canny`、`AIO_Preprocessor`、`EG_TX_SFBLS`、`LayerUtility: CropBoxResolve`、`ImageComposite+`、`LayerUtility: If `、`GrowMask`、`MaskBlur+`、`ResizeImageMixlab`、`Bounded Image Crop`、`ResizeAndPadImage`、`ImageToMask`、`Bounded Image Crop with Mask`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`CLIPLoader`、`VAELoader`、`CM_IntBinaryCondition`、`LoadImage`、`Image Crop Face`、`Fast Bypasser (rgthree)`、`SaveImage`、`KSamplerSelect`、`SamplerCustom`、`VAEDecode`、`easy imageListToImageBatch`、`ColorMatch`、`easy imageBatchToImageList`、`easy imageSize`、`TTP_Image_Tile_Batch`、`ImageSmartSharpen+`、`BasicScheduler`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`TTP_Image_Assy`、`NoiseFromImage+`、`LayerUtility: ImageBlend`、`TTP_Tile_image_size`、`ImpactInversedSwitch`、`KSampler`、`CR Integer To String`、`StringContains`、`LoraNames_`、`LayerUtility: CropByMask`、`CR Text`、`easy textIndexSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、Canny

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
