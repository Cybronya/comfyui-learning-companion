---
key: 平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json
name: seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json
hash: e9b48a309ce30c0d
coverage: 0.714286
learned_at: 2026-11-14 01:17:34
nodes: [Image Comparer (rgthree), TTP_Image_Tile_Batch, ImageResize+, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, SimpleMath+, DF_Integer, ImageCASharpening+, easy cleanGpuUsed, SaveImage, PreviewImage, PreviewImage, SetNode, SetNode, GetNode, GetNode, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, TextPreview, CR Integer To String, Load Image Batch, Note, LoadImage, TTP_Image_Assy, SeedVR2LoadDiTModel, DF_Integer]
patterns: []
missing: []
---

# 平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json

> 来源文件 `comfyui_library/workflows/平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（28 个）：
- `Image Comparer (rgthree)`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `ImageResize+`
- `ImageCASharpening+`
- `Get Image Size`
- `ImpactMinMax`
- `SimpleMath+`
- `DF_Integer`
- `ImageCASharpening+`
- `easy cleanGpuUsed`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `TextPreview`
- `CR Integer To String`
- `Load Image Batch`
- `Note`
- `LoadImage`
- `TTP_Image_Assy`
- `SeedVR2LoadDiTModel`
- `DF_Integer`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`TTP_Image_Tile_Batch`、`ImageResize+`、`ImageCASharpening+`、`Get Image Size`、`ImpactMinMax`、`SimpleMath+`、`DF_Integer`、`easy cleanGpuUsed`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`TextPreview`、`CR Integer To String`、`Load Image Batch`、`LoadImage`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、Get Image Size、ImageResize+、SaveImage、TextPreview
