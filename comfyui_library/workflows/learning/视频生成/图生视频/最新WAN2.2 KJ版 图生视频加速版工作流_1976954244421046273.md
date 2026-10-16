---
key: 视频生成/图生视频/最新WAN2.2 KJ版 图生视频加速版工作流_1976954244421046273.json
name: 最新WAN2.2 KJ版 图生视频加速版工作流_1976954244421046273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976954244421046273.json
hash: 6d1e9014c1d9f707
coverage: 0.666667
learned_at: 2026-10-15 22:32:13
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoTextEncode, SetNode, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, LoadImage, WanVideoModelLoader, WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, GetNode, CR Prompt Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEasyCache, PrimitiveNode, INTConstant, ImageResizeKJv2, JWInteger, SetNode, WanVideoLoraSelect, WanVideoVAELoader, WanVideoDecode, SetNode, Int, Int, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/最新WAN2.2 KJ版 图生视频加速版工作流_1976954244421046273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976954244421046273.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `SetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEasyCache`
- `PrimitiveNode`
- `INTConstant`
- `ImageResizeKJv2`
- `JWInteger`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `SetNode`
- `Int`
- `Int`
- `INTConstant`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`CR Prompt Text`、`WanVideoEasyCache`、`INTConstant`、`ImageResizeKJv2`、`JWInteger`、`WanVideoVAELoader`、`WanVideoDecode`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
