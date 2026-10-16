---
key: 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json
name: (KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964938797580472321.json
hash: 2ab9bc6ce6589ec7
coverage: 0.888889
learned_at: 2026-10-15 22:31:36
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, CR Prompt Text, WanVideoBlockSwap, WanVideoTorchCompileSettings, Float, INTConstant, CreateCFGScheduleFloatList, JWInteger, LoadImage, PrimitiveNode, WanVideoLoraSelect, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964938797580472321.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `Note`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Float`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `LoadImage`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `Note`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Float`、`INTConstant`、`CreateCFGScheduleFloatList`、`JWInteger`、`LoadImage`、`WanVideoScheduler`、`WanVideoSigmaToStep`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
