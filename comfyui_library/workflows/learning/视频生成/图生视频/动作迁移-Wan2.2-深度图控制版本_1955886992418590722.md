---
key: 视频生成/图生视频/动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json
name: 动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json
hash: 414bed1a09be7da4
coverage: 0.553571
learned_at: 2026-10-15 22:31:10
nodes: [GetNode, VHS_VideoCombine, WanVideoLoraSelectMulti, PrimitiveNode, WanVideoModelLoader, WanVideoTorchCompileSettings, SetNode, DownloadAndLoadDepthAnythingV2Model, PrimitiveNode, WanVideoSampler, GetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, SetNode, SetNode, LoadImage, GetNode, GetNode, PrimitiveNode, WanVideoDecode, ImageConcatMulti, GetImageRangeFromBatch, GetImageSizeAndCount, DepthAnything_V2, WanVideoImageToVideoEncode, ImageResizeKJv2, GetNode, VHS_VideoCombine, GetNode, PrimitiveNode, GetNode, SetNode, GetNode, GetNode, WanVideoSampler, GetNode, WanVideoEncode, WanVideoControlEmbeds, SetNode, GetNode, GetNode, VHS_LoadVideo, ImageResizeKJv2, WanVideoSetBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955886992418590722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `DownloadAndLoadDepthAnythingV2Model`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `DepthAnything_V2`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`

## 知识

覆盖率 **55%**（31/56）

**有卡**：`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`DepthAnything_V2`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoControlEmbeds`、`VHS_LoadVideo`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
