---
key: 图片生成/图生图/图生图-高清放大SeedVR2.5 + TTP 分块放大1.0_2068495390776844290.json
name: 图生图-高清放大SeedVR2.5 + TTP 分块放大1.0_2068495390776844290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图-高清放大SeedVR2.5 + TTP 分块放大1.0_2068495390776844290.json
hash: cab27db230bb9f97
coverage: 0.9375
learned_at: 2026-10-23 12:43:07
nodes: [ImageResize+, Image Comparer (rgthree), SaveImage, ImageScaleBy, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadVAEModel, ImageResize+, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/图生图-高清放大SeedVR2.5 + TTP 分块放大1.0_2068495390776844290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图-高清放大SeedVR2.5 + TTP 分块放大1.0_2068495390776844290.json`

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
- `ImageResize+`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LoadImage`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ImageResize+`、`SaveImage`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、Get Image Size、ImageResize+、SaveImage
