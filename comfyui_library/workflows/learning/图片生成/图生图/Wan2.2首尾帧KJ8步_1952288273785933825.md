---
key: 图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json
name: Wan2.2首尾帧KJ8步_1952288273785933825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json
hash: d3d95044ebfde462
coverage: 0.603774
learned_at: 2026-10-23 11:28:25
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, SetNode, SetNode, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, SetNode, WanVideoSampler, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, GetNode, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoDecode, SetNode, WanVideoSampler, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, GetNode, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, GetNode, GetNode, INTConstant, JWInteger, GetNode, WanVideoTextEncode, ImageResize+, ImageResize+, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, LoadImage, LoadImage, CR Prompt Text, SetNode, SetNode, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（53 个）：
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `JWInteger`
- `GetNode`
- `WanVideoTextEncode`
- `ImageResize+`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **60%**（32/53）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`INTConstant`、`JWInteger`、`WanVideoTextEncode`、`ImageResize+`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
