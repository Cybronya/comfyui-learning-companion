---
key: 数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json
name: wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json
hash: b8e8f8942fd2d45d
coverage: 0.96875
learned_at: 2026-10-26 01:59:28
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoSetBlockSwap, SimpleMath+, LoadWanVideoT5TextEncoder, Note, LoadImage, WanVideoDecode, INTConstant, Int, Int, ImageResizeKJv2, WanVideoVAELoader, VHS_VideoCombine, WanVideoTorchCompileSettings, Int, INTConstant, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `LoadImage`
- `WanVideoDecode`
- `INTConstant`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `Int`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`WanVideoLoraSelect`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoDecode`、`INTConstant`、`Int`、`ImageResizeKJv2`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
