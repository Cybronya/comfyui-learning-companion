---
key: 图片生成/图生图/人物写真高清放大 SeedVR2.5 + TTP分块放大_2071498345759199233.json
name: 人物写真高清放大 SeedVR2.5 + TTP分块放大_2071498345759199233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物写真高清放大 SeedVR2.5 + TTP分块放大_2071498345759199233.json
hash: 73fb5b92d17d1230
coverage: 1
learned_at: 2026-10-23 12:09:36
nodes: [ImageResize+, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/人物写真高清放大 SeedVR2.5 + TTP分块放大_2071498345759199233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物写真高清放大 SeedVR2.5 + TTP分块放大_2071498345759199233.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
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
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`ImageResize+`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、Get Image Size、ImageResize+、SaveImage
