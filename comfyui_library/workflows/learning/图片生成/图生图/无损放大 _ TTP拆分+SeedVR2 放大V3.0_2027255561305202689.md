---
key: 图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json
name: 无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json
hash: 6b35985ae1f974d6
coverage: 0.756757
learned_at: 2026-10-23 13:04:15
nodes: [SetNode, GetNode, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, ImpactCompare, Image Tiled, GetImageSize+, ImageFromBatch, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch, PrimitiveInt, ImageUpscaleWithModel, Images to RGB, PrimitiveInt, ImageConcanateOfUtils, ImageConcanateOfUtils, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, TTP_Tile_image_size, ImageListToBatch+, easy imageBatchToImageList, If ANY execute A else B, PreviewImage, ImageConcanate, PreviewImage, TTP_Image_Assy, PreviewImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UpscaleModelLoader, SeedVR2LoadDiTModel, Image Comparer (rgthree), LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（37 个）：
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImpactCompare`
- `Image Tiled`
- `GetImageSize+`
- `ImageFromBatch`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch`
- `PrimitiveInt`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `PrimitiveInt`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `TTP_Tile_image_size`
- `ImageListToBatch+`
- `easy imageBatchToImageList`
- `If ANY execute A else B`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `TTP_Image_Assy`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UpscaleModelLoader`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`ImageFromBatch`、`ImageConcanateOfUtils`、`ImpactCompare`、`Image Tiled`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`Images to RGB`、`TTP_Tile_image_size`、`ImageListToBatch+`、`easy imageBatchToImageList`、`If ANY execute A else B`、`ImageConcanate`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`UpscaleModelLoader`、`SeedVR2LoadDiTModel`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader、TTP_Tile_image_size
