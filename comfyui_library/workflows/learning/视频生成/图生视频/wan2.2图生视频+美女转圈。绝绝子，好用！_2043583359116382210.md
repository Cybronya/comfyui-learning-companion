---
key: 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json
name: wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043583359116382210.json
hash: f5907c53f11b7c9e
coverage: 1
learned_at: 2026-10-15 22:36:32
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoSetBlockSwap, SimpleMath+, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, WanVideoDecode, INTConstant, Int, Int, ImageResizeKJv2, WanVideoVAELoader, WanVideoModelLoader, VHS_VideoCombine, WanVideoTorchCompileSettings, Int, INTConstant, WanVideoModelLoader, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043583359116382210.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `INTConstant`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `Int`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanVideoLoraSelect`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: PurgeVRAM`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`INTConstant`、`Int`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
