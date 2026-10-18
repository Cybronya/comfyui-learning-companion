---
key: 视频生成/图生视频/Wan2.2首尾帧_1972692156160888834.json
name: Wan2.2首尾帧_1972692156160888834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧_1972692156160888834.json
hash: 14d547461072dd77
coverage: 1
learned_at: 2026-10-15 22:32:00
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoSetRadialAttention, WanVideoSetLoRAs, WanVideoSetBlockSwap, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, WanVideoImageToVideoEncode, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, WanVideoTextEncode, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoSetRadialAttention]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧_1972692156160888834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972692156160888834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoSetRadialAttention`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetRadialAttention`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoSetRadialAttention`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`LoadImage`、`WanVideoTextEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
