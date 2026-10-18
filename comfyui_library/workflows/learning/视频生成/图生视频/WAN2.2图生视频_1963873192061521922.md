---
key: 视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json
name: WAN2.2图生视频_1963873192061521922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json
hash: 25fb92ad9442f3dd
coverage: 0.964286
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoSetBlockSwap, CreateCFGScheduleFloatList, INTConstant, INTConstant, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, WanVideoSampler, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963873192061521922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
