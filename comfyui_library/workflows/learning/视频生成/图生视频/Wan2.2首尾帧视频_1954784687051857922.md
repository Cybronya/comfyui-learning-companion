---
key: 视频生成/图生视频/Wan2.2首尾帧视频_1954784687051857922.json
name: Wan2.2首尾帧视频_1954784687051857922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧视频_1954784687051857922.json
hash: 244d1d99c5aa1ed7
coverage: 1
learned_at: 2026-10-15 22:31:07
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, INTConstant, INTConstant, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, ImageResizeKJv2, LoadImage, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoTextEncode, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧视频_1954784687051857922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954784687051857922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
