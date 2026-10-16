---
key: 视频生成/图生视频/Wan2.2首尾帧加速版_1959587431169339394.json
name: Wan2.2首尾帧加速版_1959587431169339394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1959587431169339394.json
hash: 818270424740c956
coverage: 0.962963
learned_at: 2026-10-15 22:31:24
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ImageResizeKJv2, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoTextEncode, INTConstant, INTConstant, VHS_VideoCombine, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoBlockSwap, ImageResizeKJv2, LoadImage, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧加速版_1959587431169339394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959587431169339394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`INTConstant`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
