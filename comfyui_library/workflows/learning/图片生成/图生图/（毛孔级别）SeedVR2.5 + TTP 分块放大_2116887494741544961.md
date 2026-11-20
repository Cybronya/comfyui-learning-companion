---
key: 图片生成/图生图/（毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961.json
name: （毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961.json
hash: 9f37cec911d2ec78
coverage: 1
learned_at: 2026-11-02 19:15:07
nodes: [ImageResize+, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadDiTModel, LoadImage, SaveImage, SeedVR2LoadVAEModel]
patterns: []
missing: []
---

# 图片生成/图生图/（毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
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
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadVAEModel`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ImageResize+`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LoadImage`、`SaveImage`、`SeedVR2LoadVAEModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、Get Image Size、ImageResize+、TTP_Tile_image_size、SaveImage
