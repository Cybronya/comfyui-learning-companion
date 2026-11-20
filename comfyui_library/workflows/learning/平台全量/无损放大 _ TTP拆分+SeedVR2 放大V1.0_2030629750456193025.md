---
key: 平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json
name: 无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json
hash: 808f86479fd6f739
coverage: 0.823529
learned_at: 2026-11-14 02:12:50
nodes: [Image Tiled, ImageFromBatch, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, ImageUpscaleWithModel, Images to RGB, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, easy imageBatchToImageList, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanate, ImageConcanate, GetImageSize+, ImpactCompare, easy if, ImageConcanate, SeedVR2VideoUpscaler, ImageListToBatch+, TTP_Image_Assy, ImageConcanate, SetNode, Image Comparer (rgthree), LoadImage, UpscaleModelLoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, PreviewImage, GetNode, SaveImage]
patterns: []
missing: []
---

# 平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json

> 来源文件 `comfyui_library/workflows/平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（34 个）：
- `Image Tiled`
- `ImageFromBatch`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanate`
- `ImageConcanate`
- `GetImageSize+`
- `ImpactCompare`
- `easy if`
- `ImageConcanate`
- `SeedVR2VideoUpscaler`
- `ImageListToBatch+`
- `TTP_Image_Assy`
- `ImageConcanate`
- `SetNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `UpscaleModelLoader`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `GetNode`
- `SaveImage`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`Image Tiled`、`ImageFromBatch`、`TTP_Image_Tile_Batch`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`Images to RGB`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageConcanate`、`GetImageSize+`、`ImpactCompare`、`easy if`、`SeedVR2VideoUpscaler`、`ImageListToBatch+`、`TTP_Image_Assy`、`LoadImage`、`UpscaleModelLoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ImageUpscaleWithModel、UpscaleModelLoader、GetImageSize+、TTP_Tile_image_size
