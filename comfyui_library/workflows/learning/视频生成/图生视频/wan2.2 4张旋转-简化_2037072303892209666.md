---
key: 视频生成/图生视频/wan2.2 4张旋转-简化_2037072303892209666.json
name: wan2.2 4张旋转-简化_2037072303892209666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 4张旋转-简化_2037072303892209666.json
hash: 444232b4a7f12ce3
coverage: 0.636364
learned_at: 2026-10-15 22:35:54
nodes: [WanVideoTorchCompileSettings, SetNode, WanVideoSampler, GetNode, WanVideoSampler, WanVideoSampler, GetNode, GetNode, PrimitiveNode, WanVideoSigmaToStep, GetNode, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, WanVideoSampler, GetNode, WanVideoSetBlockSwap, SetNode, WanVideoSampler, WanVideoBlockSwap, PrimitiveNode, WanVideoSigmaToStep, GetNode, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, GetNode, PreviewImage, CreateCFGScheduleFloatList, Display Any (rgthree), CreateCFGScheduleFloatList, Display Any (rgthree), Display Any (rgthree), CreateCFGScheduleFloatList, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoVACEEncode, WanVideoVAELoader, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, PrimitiveNode, WanVideoDecode, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoDecode, WanVideoScheduler, WanVideoDecode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, SetNode, SetNode, SetNode, Display Any (rgthree), CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, WanVideoScheduler, easy showAnything, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, PreviewImage, VideoContinuationGenerator, GetNode, GetNode, GetNode, WanVideoBlender, GetNode, WanVideoBlender, GetNode, WanVideoBlender, INTConstant, INTConstant, GetNode, WanVideoSampler, PrimitiveNode, VideoContinuationGenerator, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, VideoContinuationGenerator, VHS_VideoCombine, WanVideoVACEStartToEndFrame, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoVACEStartToEndFrame, Seed (rgthree), INTConstant, WanVideoTextEncodeCached, WanVideoVACEEncode, VideoContinuationGenerator, Seed (rgthree), INTConstant, INTConstant, Seed (rgthree), INTConstant, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, CR Text, WanVideoVACEEncode, CR Text, CR Text, CR Text, Seed (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 4张旋转-简化_2037072303892209666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037072303892209666.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（132 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `GetNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `GetNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `PreviewImage`
- `CreateCFGScheduleFloatList`
- `Display Any (rgthree)`
- `CreateCFGScheduleFloatList`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoScheduler`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Display Any (rgthree)`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `PreviewImage`
- `VideoContinuationGenerator`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlender`
- `GetNode`
- `WanVideoBlender`
- `GetNode`
- `WanVideoBlender`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `VideoContinuationGenerator`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `VideoContinuationGenerator`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoVACEStartToEndFrame`
- `Seed (rgthree)`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `VideoContinuationGenerator`
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `CR Text`
- `WanVideoVACEEncode`
- `CR Text`
- `CR Text`
- `CR Text`
- `Seed (rgthree)`

## 知识

覆盖率 **64%**（84/132）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`INTConstant`、`CreateCFGScheduleFloatList`、`Display Any (rgthree)`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`VideoContinuationGenerator`、`WanVideoBlender`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`WanVideoLoraSelectMulti`、`Seed (rgthree)`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
