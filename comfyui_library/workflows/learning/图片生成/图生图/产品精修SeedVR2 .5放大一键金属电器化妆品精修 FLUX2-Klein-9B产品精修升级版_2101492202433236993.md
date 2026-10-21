---
key: 图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json
name: 产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json
hash: 1897013a09102e18
coverage: 0.754717
learned_at: 2026-10-21 00:47:44
nodes: [KSamplerSelect, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, CFGGuider, CLIPTextEncode, ConditioningZeroOut, GetImageSize, ReferenceLatent, ReferenceLatent, VAEEncode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, LoraLoaderModelOnly, Image Comparer (rgthree), LayerUtility: ImageReel, Flux2Scheduler, JWInteger, easy imageScaleDownToSize, TTP_Image_Tile_Batch, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2VideoUpscaler, INTConstant, Note, easy imageBatchToImageList, SeedVR2LoadDiTModel, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, Image Comparer (rgthree), LayerUtility: ImageReelComposit, PreviewImage, LoadImage, CR Text, SaveImage, easy cleanGpuUsed, PreviewImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `Flux2Scheduler`
- `JWInteger`
- `easy imageScaleDownToSize`
- `TTP_Image_Tile_Batch`
- `ImageScale`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `easy imageSize`
- `easy imageSizeBySide`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2VideoUpscaler`
- `INTConstant`
- `Note`
- `easy imageBatchToImageList`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `LoadImage`
- `CR Text`
- `SaveImage`
- `easy cleanGpuUsed`
- `PreviewImage`
- `PreviewImage`

## 知识

覆盖率 **75%**（40/53）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize`、`ReferenceLatent`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: ImageReel`、`Flux2Scheduler`、`JWInteger`、`easy imageScaleDownToSize`、`TTP_Image_Tile_Batch`、`ImageScale`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy imageSize`、`easy imageSizeBySide`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2VideoUpscaler`、`INTConstant`、`easy imageBatchToImageList`、`SeedVR2LoadDiTModel`、`VAEDecode`、`EmptyFlux2LatentImage`、`LayerUtility: ImageReelComposit`、`LoadImage`、`CR Text`、`SaveImage`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
