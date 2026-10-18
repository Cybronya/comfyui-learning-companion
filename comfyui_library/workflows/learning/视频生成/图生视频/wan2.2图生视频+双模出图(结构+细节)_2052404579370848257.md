---
key: 视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json
name: wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json
hash: 47eae7ce36ea4bb0
coverage: 0.969697
learned_at: 2026-10-15 22:37:29
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoVAELoader, WanVideoLoraSelect, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, Note, LoadImage, Int, Int, Int, ImageResizeKJv2, SimpleMath+, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM, GetImageSizeAndCount, WanVideoDecode, Int, VHS_VideoCombine, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052404579370848257.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `Int`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadImage`、`Int`、`ImageResizeKJv2`、`SimpleMath+`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
