---
key: 图片生成/图生图/SeedVR2.5 + TTP 分块放大_2059230793272225793.json
name: SeedVR2.5 + TTP 分块放大_2059230793272225793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5 + TTP 分块放大_2059230793272225793.json
hash: 7b2c4b38274d890f
coverage: 0.956522
learned_at: 2026-10-23 11:24:56
nodes: [ImageResize+, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LoadImage, SaveImage, LoadImage, SeedVR2LoadVAEModel, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5 + TTP 分块放大_2059230793272225793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5 + TTP 分块放大_2059230793272225793.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（23 个）：
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `Get Image Size`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScaleBy`
- `ConstrainImage|pysssss`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`ImageResize+`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LoadImage`、`SaveImage`、`SeedVR2LoadVAEModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、Get Image Size、ImageResize+、SaveImage
