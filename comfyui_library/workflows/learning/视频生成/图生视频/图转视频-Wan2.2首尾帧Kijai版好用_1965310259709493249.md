---
key: 视频生成/图生视频/图转视频-Wan2.2首尾帧Kijai版好用_1965310259709493249.json
name: 图转视频-Wan2.2首尾帧Kijai版好用_1965310259709493249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965310259709493249.json
hash: 32acabcc08fe943a
coverage: 0.962963
learned_at: 2026-10-15 22:31:37
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, LoadImage, LoadImage, WanVideoTextEncode, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/图转视频-Wan2.2首尾帧Kijai版好用_1965310259709493249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965310259709493249.json`

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
- `WanVideoVAELoader`
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
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `ImageResizeKJv2`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
