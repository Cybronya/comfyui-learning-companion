---
key: 图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json
name: SeedVR2.5图片高清放大_2038075237920673794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json
hash: d6faea055e441a4e
coverage: 0.931034
learned_at: 2026-10-21 00:44:24
nodes: [CR Value, CR Value, CR Value, CR Value, SimpleMath+, CR Value, CR Value, DF_Integer, TTP_Image_Tile_Batch, Get Image Size, ImageResize+, ImpactMinMax, InvertMask (segment anything), AutoImageResize, MaskToImage, ImageResize+, SeedVR2, ImageCASharpening+, TTP_Image_Assy, Get Image Size, ImageScale, Cut By Mask, ImageCASharpening+, SaveImage, Image Comparer (rgthree), Note, DF_Integer, easy anythingIndexSwitch, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（29 个）：
- `CR Value`
- `CR Value`
- `CR Value`
- `CR Value`
- `SimpleMath+`
- `CR Value`
- `CR Value`
- `DF_Integer`
- `TTP_Image_Tile_Batch`
- `Get Image Size`
- `ImageResize+`
- `ImpactMinMax`
- `InvertMask (segment anything)`
- `AutoImageResize`
- `MaskToImage`
- `ImageResize+`
- `SeedVR2`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImageScale`
- `Cut By Mask`
- `ImageCASharpening+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `DF_Integer`
- `easy anythingIndexSwitch`
- `LoadImage`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`CR Value`、`SimpleMath+`、`DF_Integer`、`TTP_Image_Tile_Batch`、`Get Image Size`、`ImageResize+`、`ImpactMinMax`、`InvertMask (segment anything)`、`AutoImageResize`、`MaskToImage`、`SeedVR2`、`ImageCASharpening+`、`TTP_Image_Assy`、`ImageScale`、`Cut By Mask`、`SaveImage`、`easy anythingIndexSwitch`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2、Get Image Size、ImageResize+、AutoImageResize、SaveImage、DF_Integer、ImageScale
