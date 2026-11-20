---
key: 平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json
name: 一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json
hash: b2b362bc5db07236
coverage: 0.846154
learned_at: 2026-11-14 01:27:54
nodes: [LoadImage, LayerMask: BiRefNetUltraV2, LayerUtility: CropByMask V2, LayerMask: SegformerB2ClothesUltra, PreviewImage, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageRemoveAlpha, PreviewImage, SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, RH_Jimeng4_Image2Image, RH_Jimeng4_Image2Image]
patterns: []
missing: []
---

# 平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json

> 来源文件 `comfyui_library/workflows/平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `LoadImage`
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: CropByMask V2`
- `LayerMask: SegformerB2ClothesUltra`
- `PreviewImage`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Jimeng4_Image2Image`
- `RH_Jimeng4_Image2Image`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`LoadImage`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: CropByMask V2`、`LayerMask: SegformerB2ClothesUltra`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Jimeng4_Image2Image`

**用到的条目**：LoadImage、SaveImage、LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2、LayerMask: SegformerB2ClothesUltra、LayerUtility: CropByMask V2、LayerUtility: ImageRemoveAlpha、LayerUtility: ImageScaleByAspectRatio V2
