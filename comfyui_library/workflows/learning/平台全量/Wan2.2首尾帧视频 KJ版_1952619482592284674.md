---
key: 平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json
name: Wan2.2首尾帧视频 KJ版_1952619482592284674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json
hash: 2dfca6b43a9d8f77
coverage: 0.962963
learned_at: 2026-11-14 01:06:26
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, ImageResizeKJv2, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTextEncode, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2首尾帧视频 KJ版_1952619482592284674.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader
