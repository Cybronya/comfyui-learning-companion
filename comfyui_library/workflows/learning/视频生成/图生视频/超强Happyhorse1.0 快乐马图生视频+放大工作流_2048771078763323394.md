---
key: 视频生成/图生视频/超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json
name: 超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json
hash: 6e25425c00c0cfe0
coverage: 0.5
learned_at: 2026-10-15 22:37:11
nodes: [SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SetNode, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM, SetNode, VHS_VideoInfoSource, GetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, 1hew_SaveVideo, GetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, SeedVR2VideoUpscaler, DF_Integer, GetNode, GetNode, GetNode, DF_Integer, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, DF_Integer, SeedVR2VideoUpscaler, RH_AlibabaHappyhorse10ImageToVideo, CR Prompt Text, LayerUtility: PurgeVRAM, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048771078763323394.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（46 个）：
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `VHS_VideoInfoSource`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `1hew_SaveVideo`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `DF_Integer`
- `GetNode`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `RH_AlibabaHappyhorse10ImageToVideo`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **50%**（23/46）

**有卡**：`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2LoadDiTModel`、`VHS_VideoInfoSource`、`VHS_LoadVideo`、`1hew_SaveVideo`、`SeedVR2VideoUpscaler`、`DF_Integer`、`VHS_VideoCombine`、`RH_AlibabaHappyhorse10ImageToVideo`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、CR Prompt Text、1hew_SaveVideo、DF_Integer、VHS_LoadVideo
