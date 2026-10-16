---
key: 视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json
name: Wan2.2首尾帧KJ版_1952270588733804545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952270588733804545.json
hash: ff9e4c929d7af32a
coverage: 0.962963
learned_at: 2026-10-15 22:31:00
nodes: [VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, Note, WanVideoTextEncode, LoadImage, LoadImage, INTConstant, WanVideoVAELoader, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952270588733804545.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `Note`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTextEncode`、`LoadImage`、`WanVideoVAELoader`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
