---
key: 图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850.json
name: 最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850.json
hash: f5f31b150415ab69
coverage: 0.793103
learned_at: 2026-10-23 13:05:29
nodes: [FlashVSR_SM_Model, FlashVSR_SM_KSampler, GetImageRangeFromBatch, ImageResize+, ImageCASharpening+, ImageConcanate, ImageResize+, Get Image Size, ImpactMinMax, easy showAnything, TTP_Image_Tile_Batch, JWInteger, JWInteger, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, LayerUtility: PurgeVRAM, SaveImage, SaveImage, SaveImage, PreviewImage, LoadImage, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 642784151}
---

# 图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（29 个）：
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageRangeFromBatch`
- `ImageResize+`
- `ImageCASharpening+`
- `ImageConcanate`
- `ImageResize+`
- `Get Image Size`
- `ImpactMinMax`
- `easy showAnything`
- `TTP_Image_Tile_Batch`
- `JWInteger`
- `JWInteger`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageCASharpening+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `1280`
- `steps` = `642784151`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`GetImageRangeFromBatch`、`ImageResize+`、`ImageCASharpening+`、`ImageConcanate`、`Get Image Size`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`JWInteger`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、SeedVR2、FlashVSR_SM_KSampler、Get Image Size、ImageResize+、SaveImage、GetImageRangeFromBatch
