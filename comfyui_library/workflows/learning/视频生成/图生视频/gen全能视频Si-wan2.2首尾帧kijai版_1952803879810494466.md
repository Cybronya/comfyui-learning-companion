---
key: 视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json
name: gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json
hash: 3c700bbd50e0b9d5
coverage: 1
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, ImageResizeKJv2, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadImage, LoadImage, WanVideoTextEncode, INTConstant, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952803879810494466.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
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
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoTextEncode`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
