---
key: 图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json
name: 一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json
hash: 075ef699bbca8e3d
coverage: 0.944444
learned_at: 2026-10-23 11:54:22
nodes: [LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_Model, FlashVSR_SM_KSampler, GetImageRangeFromBatch, ImageResize+, TTP_Image_Tile_Batch, ImageCASharpening+, ImageResize+, SeedVR2, LayerUtility: PurgeVRAM, SaveImage, TTP_Image_Assy, ImageCASharpening+, Image Comparer (rgthree), LayerUtility: PurgeVRAM, Get Image Size, ImpactMinMax, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 552470383}
---

# 图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（18 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageRangeFromBatch`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `ImageCASharpening+`
- `ImageResize+`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM`
- `Get Image Size`
- `ImpactMinMax`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `552470383`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`GetImageRangeFromBatch`、`ImageResize+`、`TTP_Image_Tile_Batch`、`ImageCASharpening+`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`SaveImage`、`TTP_Image_Assy`、`Get Image Size`、`ImpactMinMax`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、SeedVR2、FlashVSR_SM_KSampler、Get Image Size、ImageResize+、SaveImage、GetImageRangeFromBatch
