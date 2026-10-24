---
key: 图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json
name: 图生视频  Wan2.2_1972296101548191746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json
hash: 2fc92226c358a545
coverage: 0.862069
learned_at: 2026-10-23 12:44:08
nodes: [easy cleanGpuUsed, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, ImpactInt, WanVideoLoraSelectMulti, ImpactInt, WanVideoVAELoader, GetNode, GetNode, SimpleMath+, ImpactInt, SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, SimpleMath+, easy cleanGpuUsed, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoBlockSwap, WanVideoSampler, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, Text, LoadImage, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json`

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
- `Text`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`ImpactInt`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
