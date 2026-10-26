---
key: 图片生成/图生图/Qwen_Image_2.1_文生、图像编辑一体化_2113534149595324417.json
name: Qwen_Image_2.1_文生、图像编辑一体化_2113534149595324417
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_文生、图像编辑一体化_2113534149595324417.json
hash: aa397d65255a68b5
coverage: 0.982456
learned_at: 2026-10-26 22:03:34
nodes: [VAEEncode, LayerUtility: ImageBlend, ConditioningZeroOut, TTP_Image_Tile_Batch, TTP_Tile_image_size, GetImageSize+, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, ImageResize+, LayerUtility: PurgeVRAM, GetImageSize+, ImageScaleBy, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, KOOK_ImageCompression, TTP_Image_Assy, LayerUtility: PurgeVRAM, AIO_Preprocessor, LayerUtility: ImageRemoveAlpha, DrawMaskOnImage, BlockifyMask, ImageConcanate, QwenEditConfigPreparer, QwenEditConfigPreparer, LayerUtility: PurgeVRAM, CropWithPadInfo, VAEDecode, LayerUtility: PurgeVRAM, KSampler, CFGNorm, ModelSamplingAuraFlow, VAELoader, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, CLIPLoader, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LayerUtility: PurgeVRAM, ImageConcanate, LoadImage, SaveImage, SaveImage, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusCustom_lrzjason, Int, LoadImage, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 575908145069341, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1_文生、图像编辑一体化_2113534149595324417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_文生、图像编辑一体化_2113534149595324417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `VAEEncode` ★核心
- `LayerUtility: ImageBlend`
- `ConditioningZeroOut`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `ImageResize+`
- `LayerUtility: PurgeVRAM`
- `GetImageSize+`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `KOOK_ImageCompression`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM`
- `AIO_Preprocessor`
- `LayerUtility: ImageRemoveAlpha`
- `DrawMaskOnImage`
- `BlockifyMask`
- `ImageConcanate`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `LayerUtility: PurgeVRAM`
- `CropWithPadInfo`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `ImageConcanate`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `Int`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `575908145069341`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **98%**（56/57）

**有卡**：`VAEEncode`、`LayerUtility: ImageBlend`、`ConditioningZeroOut`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`GetImageSize+`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`KOOK_ImageCompression`、`TTP_Image_Assy`、`AIO_Preprocessor`、`LayerUtility: ImageRemoveAlpha`、`DrawMaskOnImage`、`BlockifyMask`、`ImageConcanate`、`QwenEditConfigPreparer`、`CropWithPadInfo`、`VAEDecode`、`KSampler`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModelV2`、`LoadImage`、`SaveImage`、`UNETLoader`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
