---
key: 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json
name: AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json
hash: 46c94f29c820d887
coverage: 0.962963
learned_at: 2026-10-15 22:38:57
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, ImageResizeKJv2, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, VHS_VideoCombine, WanVideoTextEncode, INTConstant, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061806465001803778.json`

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
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `INTConstant`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
