---
key: 视频生成/图生视频/首尾帧 Wan2.2_1972327481543946241.json
name: 首尾帧 Wan2.2_1972327481543946241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972327481543946241.json
hash: 3d69bf69d7b01d34
coverage: 0.870968
learned_at: 2026-10-15 22:31:59
nodes: [easy cleanGpuUsed, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, WanVideoModelLoader, WanVideoModelLoader, ImpactInt, WanVideoLoraSelectMulti, ImpactInt, WanVideoVAELoader, GetNode, GetNode, SimpleMath+, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, SimpleMath+, easy cleanGpuUsed, LoadImage, LoadImage, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoBlockSwap, WanVideoSampler, Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧 Wan2.2_1972327481543946241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972327481543946241.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `easy cleanGpuUsed`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `ImpactInt`
- `WanVideoLoraSelectMulti`
- `ImpactInt`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoModelLoader`、`ImpactInt`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoBlockSwap`、`Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
