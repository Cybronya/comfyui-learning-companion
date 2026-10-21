---
key: 图片生成/图生图/高清放大 8K HD Upscaling, 8K Quality, HD Restoration,_2104737913069203458.json
name: 高清放大 8K HD Upscaling, 8K Quality, HD Restoration,_2104737913069203458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清放大 8K HD Upscaling, 8K Quality, HD Restoration,_2104737913069203458.json
hash: de1a6cd5f7d2dcb2
coverage: 0.848485
learned_at: 2026-10-21 00:56:56
nodes: [easy imageSizeByLongerSide, SeedVR2LoadVAEModel, easy cleanGpuUsed, Image Comparer (rgthree), easy boolean, easy ifElse, LayerUtility: BooleanOperatorV2, ImageResize+, easy ifElse, SeedVR2VideoUpscaler, DF_Integer, TTP_Image_Tile_Batch, easy ifElse, SeedVR2VideoUpscaler, ImageCASharpening+, easy ifElse, Int, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, SimpleMath+, DF_Integer, 数学运算_孤海, MathExpression|pysssss, ImageResize+, LayerUtility: BooleanOperatorV2, Int, TTP_Image_Assy, easy imageSizeBySide, Blur, ImageResize+, SaveImageJPG_GH, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/高清放大 8K HD Upscaling, 8K Quality, HD Restoration,_2104737913069203458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清放大 8K HD Upscaling, 8K Quality, HD Restoration,_2104737913069203458.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（33 个）：
- `easy imageSizeByLongerSide`
- `SeedVR2LoadVAEModel`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `easy boolean`
- `easy ifElse`
- `LayerUtility: BooleanOperatorV2`
- `ImageResize+`
- `easy ifElse`
- `SeedVR2VideoUpscaler`
- `DF_Integer`
- `TTP_Image_Tile_Batch`
- `easy ifElse`
- `SeedVR2VideoUpscaler`
- `ImageCASharpening+`
- `easy ifElse`
- `Int`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `SimpleMath+`
- `DF_Integer`
- `数学运算_孤海`
- `MathExpression|pysssss`
- `ImageResize+`
- `LayerUtility: BooleanOperatorV2`
- `Int`
- `TTP_Image_Assy`
- `easy imageSizeBySide`
- `Blur`
- `ImageResize+`
- `SaveImageJPG_GH`
- `LoadImage`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`easy imageSizeByLongerSide`、`SeedVR2LoadVAEModel`、`easy cleanGpuUsed`、`easy boolean`、`LayerUtility: BooleanOperatorV2`、`ImageResize+`、`SeedVR2VideoUpscaler`、`DF_Integer`、`TTP_Image_Tile_Batch`、`ImageCASharpening+`、`Int`、`SeedVR2LoadDiTModel`、`SimpleMath+`、`数学运算_孤海`、`MathExpression|pysssss`、`TTP_Image_Assy`、`easy imageSizeBySide`、`Blur`、`SaveImageJPG_GH`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSizeByLongerSide、easy imageSizeBySide、ImageResize+、SaveImageJPG_GH
