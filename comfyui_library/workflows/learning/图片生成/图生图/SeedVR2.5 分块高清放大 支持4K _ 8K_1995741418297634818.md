---
key: 图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json
name: SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json
hash: 55c48a886187b2c8
coverage: 0.9375
learned_at: 2026-10-23 11:24:57
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy imageBatchToImageList, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), easy int, easy imageSizeBySide, ImageScale]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy imageBatchToImageList`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy int`
- `easy imageSizeBySide`
- `ImageScale`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`easy imageBatchToImageList`、`SeedVR2VideoUpscaler`、`SaveImage`、`easy int`、`easy imageSizeBySide`、`ImageScale`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSizeBySide、SaveImage、ImageScale
