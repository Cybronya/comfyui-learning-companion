---
key: 平台全量/FlashVsr1.1+SeedVR2.5+TTP图像高清修复_2086373630421852161.json
name: FlashVsr1.1+SeedVR2.5+TTP图像高清修复_2086373630421852161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVsr1.1+SeedVR2.5+TTP图像高清修复_2086373630421852161.json
hash: f246a2ad9126ec83
coverage: 1
learned_at: 2026-11-14 00:27:17
nodes: [LayerUtility: PurgeVRAM, SeedVR2, Get Image Size, ImpactMinMax, LayerUtility: PurgeVRAM, ImageCASharpening+, SaveImage, ComfyMathExpression, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Tile_Batch, TTP_Image_Assy, FlashVSR_SM_KSampler, GetImageRangeFromBatch, ImageCASharpening+, JWInteger, DF_Get_image_size, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 115123290}
---

# 平台全量/FlashVsr1.1+SeedVR2.5+TTP图像高清修复_2086373630421852161.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVsr1.1+SeedVR2.5+TTP图像高清修复_2086373630421852161.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（18 个）：
- `LayerUtility: PurgeVRAM`
- `SeedVR2`
- `Get Image Size`
- `ImpactMinMax`
- `LayerUtility: PurgeVRAM`
- `ImageCASharpening+`
- `SaveImage`
- `ComfyMathExpression`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageRangeFromBatch`
- `ImageCASharpening+`
- `JWInteger`
- `DF_Get_image_size`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `115123290`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`LayerUtility: PurgeVRAM`、`SeedVR2`、`Get Image Size`、`ImpactMinMax`、`ImageCASharpening+`、`SaveImage`、`ComfyMathExpression`、`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`FlashVSR_SM_KSampler`、`GetImageRangeFromBatch`、`JWInteger`、`DF_Get_image_size`、`LoadImage`

**用到的条目**：LoadImage、FlashVSR_SM_KSampler、SeedVR2、DF_Get_image_size、Get Image Size、SaveImage、ComfyMathExpression、FlashVSR_SM_Model
