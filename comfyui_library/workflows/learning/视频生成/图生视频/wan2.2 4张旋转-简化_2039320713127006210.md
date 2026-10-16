---
key: 视频生成/图生视频/wan2.2 4张旋转-简化_2039320713127006210.json
name: wan2.2 4张旋转-简化_2039320713127006210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039320713127006210.json
hash: a7bf57f74d5590cc
coverage: 0.622047
learned_at: 2026-10-15 22:36:08
nodes: [GetNode, GetNode, SetNode, PrimitiveNode, WanVideoSigmaToStep, PrimitiveNode, GetNode, GetNode, PreviewImage, CreateCFGScheduleFloatList, GetNode, GetNode, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, GetNode, GetNode, INTConstant, WanVideoLoraSelectMulti, Seed (rgthree), WanVideoVACEStartToEndFrame, INTConstant, GetNode, GetNode, WanVideoVACEEncode, WanVideoTextEncodeCached, Seed (rgthree), Display Any (rgthree), WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, easy showAnything, WanVideoSampler, GetNode, WanVideoScheduler, WanVideoSampler, VHS_VideoCombine, GetNode, GetNode, PreviewImage, Seed (rgthree), VideoContinuationGenerator, INTConstant, GetNode, WanVideoVACEEncode, WanVideoTextEncodeCached, CreateCFGScheduleFloatList, WanVideoSigmaToStep, Display Any (rgthree), GetNode, PrimitiveNode, PrimitiveNode, WanVideoScheduler, WanVideoSampler, WanVideoSampler, GetNode, GetNode, WanVideoDecode, WanVideoBlender, VHS_VideoCombine, WanVideoDecode, INTConstant, VideoContinuationGenerator, WanVideoVACEEncode, WanVideoTextEncodeCached, PreviewImage, Display Any (rgthree), GetNode, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, CreateCFGScheduleFloatList, WanVideoScheduler, WanVideoSampler, WanVideoSampler, WanVideoScheduler, WanVideoDecode, WanVideoBlender, GetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoVACEEncode, VideoContinuationGenerator, WanVideoTextEncodeCached, Seed (rgthree), INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, Display Any (rgthree), GetNode, WanVideoScheduler, WanVideoSampler, WanVideoScheduler, WanVideoSampler, GetNode, WanVideoDecode, GetNode, WanVideoBlender, VHS_VideoCombine, SetNode, VideoContinuationGenerator, WanVideoVACEStartToEndFrame, WanVideoVAELoader, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, INTConstant, SetNode, INTConstant, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 4张旋转-简化_2039320713127006210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039320713127006210.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（127 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `Seed (rgthree)`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeCached`
- `Seed (rgthree)`
- `Display Any (rgthree)`
- `WanVideoScheduler`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `Seed (rgthree)`
- `VideoContinuationGenerator`
- `INTConstant`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeCached`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `Display Any (rgthree)`
- `GetNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoBlender`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `INTConstant`
- `VideoContinuationGenerator`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `Display Any (rgthree)`
- `GetNode`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `CreateCFGScheduleFloatList`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoDecode`
- `WanVideoBlender`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `VideoContinuationGenerator`
- `WanVideoTextEncodeCached`
- `Seed (rgthree)`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Display Any (rgthree)`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoBlender`
- `VHS_VideoCombine`
- `SetNode`
- `VideoContinuationGenerator`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **62%**（79/127）

**有卡**：`WanVideoSigmaToStep`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoLoraSelectMulti`、`Seed (rgthree)`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`WanVideoTextEncodeCached`、`Display Any (rgthree)`、`WanVideoSampler`、`VHS_VideoCombine`、`VideoContinuationGenerator`、`WanVideoDecode`、`WanVideoBlender`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
