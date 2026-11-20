---
key: 平台全量/wan2.2 lora 换脸_2034647765032112130.json
name: wan2.2 lora 换脸_2034647765032112130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 lora 换脸_2034647765032112130.json
hash: feb6827079123a13
coverage: 0.791045
learned_at: 2026-11-14 01:19:21
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoVACEModelSelect, PrimitiveNode, LayerUtility: PurgeVRAM V2, WanVideoSetLoRAs, SetNode, WanVideoSetLoRAs, LayerUtility: PurgeVRAM V2, SimpleMath+, easy indexAnything, easy sam3GetObjectMask, easy ifElse, easy sam3GetObjectMask, easy sam3GetObjectIds, GrowMask, Reroute, easy sam3ModelLoader, Int, Reroute, GetImageSizeAndCount, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, GetNode, GetNode, easy sam3Visualization, WanVideoDecode, WanVideoVAELoader, CM_IntToFloat, Int, ImageFromBatch+, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, CreateVideo, SaveVideo, SetNode, WanVideoVACEEncode, WanVideoLoraSelect, CreateCFGScheduleFloatList, INTConstant, easy int, Int, VHS_LoadVideo, Note, WanVideoLoraSelect, Note, Note, Note, Note, Note, INTConstant, WanVideoSampler, WanVideoSampler, RH_Translator, WanVideoTextEncode, easy sam3VideoSegmentation, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/wan2.2 lora 换脸_2034647765032112130.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 lora 换脸_2034647765032112130.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM V2`
- `SimpleMath+`
- `easy indexAnything`
- `easy sam3GetObjectMask`
- `easy ifElse`
- `easy sam3GetObjectMask`
- `easy sam3GetObjectIds`
- `GrowMask`
- `Reroute`
- `easy sam3ModelLoader`
- `Int`
- `Reroute`
- `GetImageSizeAndCount`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `easy sam3Visualization`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `CM_IntToFloat`
- `Int`
- `ImageFromBatch+`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `CreateVideo`
- `SaveVideo`
- `SetNode`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `easy int`
- `Int`
- `VHS_LoadVideo`
- `Note`
- `WanVideoLoraSelect`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RH_Translator`
- `WanVideoTextEncode`
- `easy sam3VideoSegmentation`
- `VHS_VideoCombine`

## 知识

覆盖率 **79%**（53/67）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`LayerUtility: PurgeVRAM V2`、`WanVideoSetLoRAs`、`SimpleMath+`、`easy indexAnything`、`easy sam3GetObjectMask`、`easy sam3GetObjectIds`、`GrowMask`、`easy sam3ModelLoader`、`Int`、`GetImageSizeAndCount`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`easy sam3Visualization`、`WanVideoDecode`、`WanVideoVAELoader`、`CM_IntToFloat`、`ImageFromBatch+`、`LoadWanVideoT5TextEncoder`、`CreateVideo`、`SaveVideo`、`WanVideoVACEEncode`、`CreateCFGScheduleFloatList`、`INTConstant`、`easy int`、`VHS_LoadVideo`、`WanVideoSampler`、`RH_Translator`、`WanVideoTextEncode`、`easy sam3VideoSegmentation`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
