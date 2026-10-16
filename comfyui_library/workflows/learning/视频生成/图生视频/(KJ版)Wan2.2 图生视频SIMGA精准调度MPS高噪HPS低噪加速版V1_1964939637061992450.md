---
key: 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964939637061992450.json
name: (KJ版)Wan2.2 图生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964939637061992450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964939637061992450.json
hash: ef6ce1e5cedc198b
coverage: 0.914286
learned_at: 2026-10-15 22:31:36
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, VHS_VideoCombine, WanVideoLoraSelect, WanVideoTextEncode, CR Prompt Text, WanVideoBlockSwap, WanVideoTorchCompileSettings, Float, INTConstant, CreateCFGScheduleFloatList, JWInteger, LoadImage, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoModelLoader, WanVideoModelLoader, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964939637061992450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964939637061992450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
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
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Float`、`INTConstant`、`CreateCFGScheduleFloatList`、`JWInteger`、`LoadImage`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
