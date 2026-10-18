---
key: 视频生成/图生视频/基础图生视频  WAN2.2_1988338285892255745.json
name: 基础图生视频  WAN2.2_1988338285892255745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/基础图生视频  WAN2.2_1988338285892255745.json
hash: 038618cf89342bd4
coverage: 0.862069
learned_at: 2026-10-15 22:33:02
nodes: [easy cleanGpuUsed, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, ImpactInt, WanVideoLoraSelectMulti, ImpactInt, WanVideoVAELoader, GetNode, GetNode, SimpleMath+, ImpactInt, SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, SimpleMath+, easy cleanGpuUsed, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoBlockSwap, WanVideoSampler, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoModelLoader, Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/基础图生视频  WAN2.2_1988338285892255745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988338285892255745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `easy cleanGpuUsed`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `ImpactInt`
- `WanVideoLoraSelectMulti`
- `ImpactInt`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Text`
- `LoadImage`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`ImpactInt`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
