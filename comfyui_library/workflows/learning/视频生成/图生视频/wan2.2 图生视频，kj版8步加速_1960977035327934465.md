---
key: 视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json
name: wan2.2 图生视频，kj版8步加速_1960977035327934465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json
hash: 3876809f9c25996b
coverage: 0.965517
learned_at: 2026-10-15 22:31:27
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoDecode, GetImageSizeAndCount, WanVideoVAELoader, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoTextEncode, INTConstant, CreateCFGScheduleFloatList, INTConstant, PrimitiveNode, WanVideoImageToVideoEncode, LoadImage, LoadImage, LoadImage, CR Prompt Text, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960977035327934465.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTextEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
