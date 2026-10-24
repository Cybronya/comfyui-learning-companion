---
key: 图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json
name: 图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json
hash: 8ec7a7cbed23a48b
coverage: 0.705882
learned_at: 2026-10-23 12:42:03
nodes: [TTP_Image_Tile_Batch, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, ImageResize+, ImageCASharpening+, SeedVR2, Get Image Size, Image Comparer (rgthree), SaveImage, SaveImage, ImageResize+, GetImageRangeFromBatch, LayerUtility: PurgeVRAM, FlashVSR_SM_KSampler, FlashVSR_SM_Model, SaveImage, ImpactMinMax, easy showAnything, LoadImage, MarkdownNote, LoadImage, Image Comparer (rgthree), SaveImage, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote, JWInteger, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1820593083}
---

# 图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（34 个）：
- `TTP_Image_Tile_Batch`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageCASharpening+`
- `SeedVR2`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `ImageResize+`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM`
- `FlashVSR_SM_KSampler` ★核心
- `FlashVSR_SM_Model`
- `SaveImage`
- `ImpactMinMax`
- `easy showAnything`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `JWInteger`
- `MarkdownNote`

## 关键参数

- `seed` = `1280`
- `steps` = `1820593083`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`TTP_Image_Tile_Batch`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`ImageCASharpening+`、`ImageResize+`、`SeedVR2`、`Get Image Size`、`SaveImage`、`GetImageRangeFromBatch`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`ImpactMinMax`、`LoadImage`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、SeedVR2、FlashVSR_SM_KSampler、Get Image Size、ImageResize+、SaveImage、GetImageRangeFromBatch
