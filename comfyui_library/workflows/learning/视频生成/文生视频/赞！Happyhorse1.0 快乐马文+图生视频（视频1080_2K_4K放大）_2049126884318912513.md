---
key: 视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json
name: 赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json
hash: 926c189ac5ac1714
coverage: 0.336957
learned_at: 2026-10-11 19:49:51
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM, SetNode, LayerUtility: PurgeVRAM, SetNode, GetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, 1hew_SaveVideo, VHS_VideoInfoSource, GetNode, GetNode, GetNode, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, GetNode, GetNode, DF_Integer, VHS_VideoCombine, GetNode, GetNode, GetNode, SeedVR2VideoUpscaler, DF_Integer, GetNode, LayerUtility: PurgeVRAM, GetNode, VHS_VideoCombine, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, GetNode, GetNode, DF_Integer, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, SeedVR2VideoUpscaler, GetNode, SetNode, SeedVR2LoadVAEModel, SetNode, LayerUtility: PurgeVRAM, SeedVR2LoadDiTModel, SetNode, LayerUtility: PurgeVRAM, RH_AlibabaHappyhorse10ImageToVideo, CR Prompt Text, PrimitiveNode, PrimitiveNode, PrimitiveNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, SetNode, SetNode, VHS_VideoInfoSource, GetNode, LayerUtility: PurgeVRAM, DF_Integer, SeedVR2VideoUpscaler, GetNode, GetNode, GetNode, VHS_VideoCombine, DF_Integer, GetNode, GetNode, LayerUtility: PurgeVRAM, 1hew_SaveVideo, SetNode, VHS_VideoCombine, SeedVR2VideoUpscaler, GetNode, DF_Integer, VHS_VideoCombine, JjkText, VHS_LoadVideo, RH_AlibabaHappyhorse10TextToVideo, Fast Groups Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（92 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `1hew_SaveVideo`
- `VHS_VideoInfoSource`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `DF_Integer`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `VHS_VideoCombine`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `SetNode`
- `SeedVR2LoadVAEModel`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `SeedVR2LoadDiTModel`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `RH_AlibabaHappyhorse10ImageToVideo`
- `CR Prompt Text`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoSource`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `DF_Integer`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DF_Integer`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `1hew_SaveVideo`
- `SetNode`
- `VHS_VideoCombine`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `DF_Integer`
- `VHS_VideoCombine`
- `JjkText`
- `VHS_LoadVideo`
- `RH_AlibabaHappyhorse10TextToVideo`
- `Fast Groups Muter (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **34%**（31/92）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VHS_LoadVideo`、`1hew_SaveVideo`、`VHS_VideoInfoSource`、`SeedVR2VideoUpscaler`、`DF_Integer`、`VHS_VideoCombine`、`RH_AlibabaHappyhorse10ImageToVideo`、`RH_AlibabaHappyhorse10TextToVideo`、`LoadImage`

**缺卡**（12）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、1hew_SaveVideo、DF_Integer、VHS_LoadVideo、VHS_VideoCombine

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
