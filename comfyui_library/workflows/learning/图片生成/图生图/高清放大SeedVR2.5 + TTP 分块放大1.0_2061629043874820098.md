---
key: 图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json
name: 高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json
hash: f6cefe7620ad1841
coverage: 0.9375
learned_at: 2026-10-23 13:34:39
nodes: [ImageResize+, Image Comparer (rgthree), SaveImage, ImageScaleBy, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadVAEModel, LoadImage, ImageResize+, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler]
patterns: []
missing: []
---

# 图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
- `ImageResize+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageScaleBy`
- `Get Image Size`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScaleBy`
- `ConstrainImage|pysssss`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `ImageResize+`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ImageResize+`、`SaveImage`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadVAEModel`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、Get Image Size、ImageResize+、SaveImage
