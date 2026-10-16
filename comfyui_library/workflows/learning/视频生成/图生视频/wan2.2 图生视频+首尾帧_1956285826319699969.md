---
key: 视频生成/图生视频/wan2.2 图生视频+首尾帧_1956285826319699969.json
name: wan2.2 图生视频+首尾帧_1956285826319699969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956285826319699969.json
hash: 968a0149bd993ae1
coverage: 1
learned_at: 2026-10-15 22:31:12
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, CreateCFGScheduleFloatList, GetImageSizeAndCount, VHS_VideoCombine, WanVideoBlockSwap, ImageResizeKJv2, WanVideoSampler, WanVideoDecode, SimpleMath+, WanVideoImageToVideoEncode, ImageResizeKJv2, WanVideoSampler, INTConstant, INTConstant, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadImage, LoadImage, easy int, WanVideoTextEncode, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频+首尾帧_1956285826319699969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956285826319699969.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadImage`
- `LoadImage`
- `easy int`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoDecode`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`easy int`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
