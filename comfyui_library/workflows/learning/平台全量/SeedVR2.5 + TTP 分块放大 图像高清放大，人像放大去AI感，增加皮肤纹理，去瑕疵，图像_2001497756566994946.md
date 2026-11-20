---
key: 平台全量/SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946.json
name: SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946.json
hash: f64b1ace511f27ba
coverage: 0.9375
learned_at: 2026-11-14 00:59:19
nodes: [ImageResize+, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, ImageScaleBy, ImageResize+, Get Image Size, TTP_Image_Assy, Get Image Size, ImageScaleBy, ConstrainImage|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LoadImage]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageScaleBy`
- `ImageResize+`
- `Get Image Size`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScaleBy`
- `ConstrainImage|pysssss`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ImageResize+`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImageScaleBy`、`Get Image Size`、`TTP_Image_Assy`、`ConstrainImage|pysssss`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、Get Image Size、ImageResize+、TTP_Tile_image_size、SaveImage
