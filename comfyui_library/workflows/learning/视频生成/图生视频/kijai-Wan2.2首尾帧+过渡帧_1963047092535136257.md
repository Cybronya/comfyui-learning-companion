---
key: 视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json
name: kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json
hash: 6edd977b0b3e5145
coverage: 1
learned_at: 2026-10-15 22:31:32
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoDecode, INTConstant, INTConstant, INTConstant, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, ImageResizeKJv2, WanVideoImageToVideoEncode, ImageResizeKJv2, ImageResizeKJv2, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LoadImage, LoadImage, LoadImage, WanVideoVAELoader, WanVideoEncodeLatentBatch, WanVideoContextOptions, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963047092535136257.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoEncodeLatentBatch`
- `WanVideoContextOptions`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`INTConstant`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoVAELoader`、`WanVideoEncodeLatentBatch`、`WanVideoContextOptions`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
