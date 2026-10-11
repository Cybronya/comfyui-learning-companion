---
key: 视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json
name: 真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json
hash: 3042f68111b36f21
coverage: 0.446809
learned_at: 2026-10-11 19:49:51
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SeedVR2LoadVAEModel, SetNode, SeedVR2LoadDiTModel, SetNode, LoadImage, SetNode, SetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DF_Integer, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), PrimitiveNode, PrimitiveNode, PrimitiveNode, LoadImage, GetNode, VHS_VideoInfoSource, CR Prompt Text, DF_Integer, GetNode, GetNode, 1hew_SaveVideo, GetNode, SetNode, SeedVR2VideoUpscaler, VHS_VideoCombine, VHS_LoadVideo, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, RH_BytedanceSeedance20GlobalFastMultimodalVideo, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（47 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DF_Integer`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `GetNode`
- `VHS_VideoInfoSource`
- `CR Prompt Text`
- `DF_Integer`
- `GetNode`
- `GetNode`
- `1hew_SaveVideo`
- `GetNode`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **45%**（21/47）

**有卡**：`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`DF_Integer`、`SeedVR2VideoUpscaler`、`VHS_VideoInfoSource`、`1hew_SaveVideo`、`VHS_VideoCombine`、`VHS_LoadVideo`、`RH_BytedanceSeedance20GlobalFastMultimodalVideo`

**缺卡**（5）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、RH_BytedanceSeedance20GlobalFastMultimodalVideo、1hew_SaveVideo、DF_Integer、VHS_LoadVideo

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
