---
key: 图片生成/图生图/SeedVR2_Zimage_FLUX_ SUPIR无损高清放大集成工作流（去油腻）_2046863005584986113.json
name: SeedVR2_Zimage_FLUX_ SUPIR无损高清放大集成工作流（去油腻）_2046863005584986113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2_Zimage_FLUX_ SUPIR无损高清放大集成工作流（去油腻）_2046863005584986113.json
hash: a3ec72f775dcff62
coverage: 0.95
learned_at: 2026-10-23 11:25:13
nodes: [Image Comparer (rgthree), ImageFromBatch, easy imageBatchToImageList, GetImageSize+, ImpactCompare, SeedVR2VideoUpscaler, If ANY execute A else B, easy imageListToImageBatch, TTP_Image_Assy, TTP_Image_Tile_Batch, easy int, ImageResizeKJv2, SaveImage, LoadImage, GetImageSizeAndCount, MathExpression|pysssss, TTP_Tile_image_size, MathExpression|pysssss, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2_Zimage_FLUX_ SUPIR无损高清放大集成工作流（去油腻）_2046863005584986113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2_Zimage_FLUX_ SUPIR无损高清放大集成工作流（去油腻）_2046863005584986113.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（20 个）：
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `easy imageBatchToImageList`
- `GetImageSize+`
- `ImpactCompare`
- `SeedVR2VideoUpscaler`
- `If ANY execute A else B`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy int`
- `ImageResizeKJv2`
- `SaveImage`
- `LoadImage`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `TTP_Tile_image_size`
- `MathExpression|pysssss`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`ImageFromBatch`、`easy imageBatchToImageList`、`GetImageSize+`、`ImpactCompare`、`SeedVR2VideoUpscaler`、`If ANY execute A else B`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy int`、`ImageResizeKJv2`、`SaveImage`、`LoadImage`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`TTP_Tile_image_size`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、GetImageSizeAndCount、ImageResizeKJv2、TTP_Tile_image_size、GetImageSize+
