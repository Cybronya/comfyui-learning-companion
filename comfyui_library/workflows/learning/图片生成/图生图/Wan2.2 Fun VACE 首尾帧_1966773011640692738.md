---
key: 图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json
name: Wan2.2 Fun VACE 首尾帧_1966773011640692738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json
hash: 96c4a65ca1b03ded
coverage: 0.755102
learned_at: 2026-10-23 11:28:00
nodes: [JWInteger, RH_LLMAPI_NODE, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, GetNode, JWInteger, CR Text, WanVideoVACEStartToEndFrame, MathExpression|pysssss, GetNode, ImageResizeKJ, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, LoadImage, LoadImage, WanVideoVACEModelSelect, GetNode, ImpactSwitch, Note, VHS_VideoCombine, WanVideoVACEEncode, easy showAnything, WanVideoTextEncodeCached, GetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, WanVideoDecode, ImageConcanate, ImageConcanate, VHS_VideoCombine, CreateCFGScheduleFloatList, WanVideoLoraSelectMulti, PrimitiveNode, PrimitiveNode, WanVideoSigmaToStep, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `JWInteger`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `GetNode`
- `JWInteger`
- `CR Text`
- `WanVideoVACEStartToEndFrame`
- `MathExpression|pysssss`
- `GetNode`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `GetNode`
- `ImpactSwitch`
- `Note`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `easy showAnything`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoDecode`
- `ImageConcanate`
- `ImageConcanate`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelectMulti`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（37/49）

**有卡**：`JWInteger`、`RH_LLMAPI_NODE`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoScheduler`、`CR Text`、`WanVideoVACEStartToEndFrame`、`MathExpression|pysssss`、`ImageResizeKJ`、`LoadImage`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
