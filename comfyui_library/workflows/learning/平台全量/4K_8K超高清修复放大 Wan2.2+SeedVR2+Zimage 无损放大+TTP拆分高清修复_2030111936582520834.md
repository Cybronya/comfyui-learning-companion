---
key: 平台全量/4K_8K超高清修复放大 Wan2.2+SeedVR2+Zimage 无损放大+TTP拆分高清修复_2030111936582520834.json
name: 4K_8K超高清修复放大 Wan2.2+SeedVR2+Zimage 无损放大+TTP拆分高清修复_2030111936582520834
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/4K_8K超高清修复放大 Wan2.2+SeedVR2+Zimage 无损放大+TTP拆分高清修复_2030111936582520834.json
hash: 081948a7487b266a
coverage: 0.888889
learned_at: 2026-11-14 00:12:59
nodes: [GetNode, KSampler, VAEDecode, easy imageSize, LayerUtility: PurgeVRAM, ReferenceLatent, VAELoader, EmptySD3LatentImage, KSampler, FluxGuidance, ImageToMask, InvertMask, MaskToImage, Image Blend by Mask, Reroute, VAEEncode, easy int, Seed Everywhere, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, HYPIRAdvancedRestoration, PrimitiveFloat, Image Levels Adjustment, ConditioningZeroOut, LayerFilter: AddGrain, GetImageSize+, DualCLIPLoader, CLIPTextEncode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingAuraFlow, ConditioningZeroOut, VAELoader, KSampler, VAEEncode, easy imageSize, TTP_Tile_image_size, ImageListToImageBatch, TTP_Image_Tile_Batch, ImpactImageBatchToImageList, VAEDecodeTiled, easy imageSize, easy imageSize, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, UpscaleModelLoader, ImageResize+, easy imageSize, easy imageSize, GetImageSize+, ImageResize+, ImageScaleBy, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageSharpen, ImageScaleBy, SeedVR2LoadDiTModel, easy imageSize, SeedVR2LoadVAEModel, SaveImage, SetNode, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler, GetNode, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 199971171393001, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/4K_8K超高清修复放大 Wan2.2+SeedVR2+Zimage 无损放大+TTP拆分高清修复_2030111936582520834.json

> 来源文件 `comfyui_library/workflows/平台全量/4K_8K超高清修复放大 Wan2.2+SeedVR2+Zimage 无损放大+TTP拆分高清修复_2030111936582520834.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy imageSize`
- `LayerUtility: PurgeVRAM`
- `ReferenceLatent`
- `VAELoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `FluxGuidance`
- `ImageToMask`
- `InvertMask`
- `MaskToImage`
- `Image Blend by Mask`
- `Reroute`
- `VAEEncode` ★核心
- `easy int`
- `Seed Everywhere`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `HYPIRAdvancedRestoration`
- `PrimitiveFloat`
- `Image Levels Adjustment`
- `ConditioningZeroOut`
- `LayerFilter: AddGrain`
- `GetImageSize+`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `easy imageSize`
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `ImpactImageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `easy imageSize`
- `easy imageSize`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `ImageResize+`
- `easy imageSize`
- `easy imageSize`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `ImageSharpen`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `easy imageSize`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `199971171393001`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **89%**（64/72）

**有卡**：`KSampler`、`VAEDecode`、`easy imageSize`、`LayerUtility: PurgeVRAM`、`ReferenceLatent`、`VAELoader`、`EmptySD3LatentImage`、`FluxGuidance`、`ImageToMask`、`InvertMask`、`MaskToImage`、`Image Blend by Mask`、`VAEEncode`、`easy int`、`Seed Everywhere`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`HYPIRAdvancedRestoration`、`Image Levels Adjustment`、`ConditioningZeroOut`、`LayerFilter: AddGrain`、`GetImageSize+`、`DualCLIPLoader`、`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingAuraFlow`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`VAEDecodeTiled`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`ImageResize+`、`ImageScaleBy`、`TTP_Image_Assy`、`ImageSharpen`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`LoadImage`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
