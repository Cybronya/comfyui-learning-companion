---
key: 视频生成/图生视频/多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json
name: 多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json
hash: 6873d9c675fc313c
coverage: 0.625
learned_at: 2026-10-15 22:37:14
nodes: [SeedVR2LoadVAEModel, SetNode, SeedVR2LoadDiTModel, SetNode, SetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, Fast Groups Bypasser (rgthree), PrimitiveNode, PrimitiveNode, GetNode, VHS_VideoInfoSource, GetNode, GetNode, GetNode, SetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, 1hew_SaveVideo, VHS_LoadVideo, PrimitiveNode, GetNode, GetNode, DF_Integer, SeedVR2VideoUpscaler, VHS_VideoCombine, SeedVR2VideoUpscaler, GetNode, DF_Integer, VHS_VideoCombine, CR Prompt Text, RH_AlibabaHappyhorse10ReferenceToVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049414589812580354.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（56 个）：
- `SeedVR2LoadVAEModel`
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `VHS_VideoInfoSource`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `1hew_SaveVideo`
- `VHS_LoadVideo`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `DF_Integer`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `RH_AlibabaHappyhorse10ReferenceToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **62%**（35/56）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LayerUtility: PurgeVRAM`、`VHS_VideoInfoSource`、`1hew_SaveVideo`、`VHS_LoadVideo`、`DF_Integer`、`SeedVR2VideoUpscaler`、`VHS_VideoCombine`、`CR Prompt Text`、`RH_AlibabaHappyhorse10ReferenceToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、CR Prompt Text、1hew_SaveVideo、DF_Integer、VHS_LoadVideo
