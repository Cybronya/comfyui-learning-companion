---
key: 图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json
name: wan2.2 2张旋转-简化_2038442502138630146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json
hash: 7372ef0686661155
coverage: 0.643836
learned_at: 2026-10-23 11:45:53
nodes: [INTConstant, INTConstant, WanVideoLoraSelectMulti, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, GetNode, Display Any (rgthree), WanVideoScheduler, WanVideoSampler, WanVideoScheduler, GetNode, GetNode, WanVideoSampler, GetNode, Seed (rgthree), INTConstant, GetNode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, GetNode, Display Any (rgthree), WanVideoScheduler, easy showAnything, WanVideoSampler, GetNode, WanVideoSampler, GetNode, PreviewImage, WanVideoTextEncodeCached, VideoContinuationGenerator, WanVideoVACEEncode, WanVideoTextEncodeCached, WanVideoVACEEncode, Seed (rgthree), WanVideoVACEStartToEndFrame, GetNode, INTConstant, GetNode, GetNode, LoadImage, LoadImage, WanVideoScheduler, WanVideoDecode, VHS_VideoCombine, WanVideoDecode, WanVideoBlender, VHS_VideoCombine, INTConstant, SetNode, SetNode, SetNode, WanVideoVACEStartToEndFrame, VideoContinuationGenerator, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoVAELoader]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（73 个）：
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `Display Any (rgthree)`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `Seed (rgthree)`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `Display Any (rgthree)`
- `WanVideoScheduler`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `VideoContinuationGenerator`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `Seed (rgthree)`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `WanVideoScheduler`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoBlender`
- `VHS_VideoCombine`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `VideoContinuationGenerator`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVAELoader`

## 知识

覆盖率 **64%**（47/73）

**有卡**：`INTConstant`、`WanVideoLoraSelectMulti`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`Display Any (rgthree)`、`WanVideoScheduler`、`WanVideoSampler`、`Seed (rgthree)`、`WanVideoTextEncodeCached`、`VideoContinuationGenerator`、`WanVideoVACEEncode`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlender`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
