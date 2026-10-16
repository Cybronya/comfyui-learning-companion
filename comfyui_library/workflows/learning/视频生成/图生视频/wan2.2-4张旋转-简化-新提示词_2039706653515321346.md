---
key: 视频生成/图生视频/wan2.2-4张旋转-简化-新提示词_2039706653515321346.json
name: wan2.2-4张旋转-简化-新提示词_2039706653515321346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039706653515321346.json
hash: 8fdaf440e16af6ba
coverage: 0.619048
learned_at: 2026-10-15 22:36:11
nodes: [GetNode, GetNode, SetNode, PrimitiveNode, WanVideoSigmaToStep, PrimitiveNode, GetNode, CreateCFGScheduleFloatList, GetNode, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, INTConstant, WanVideoLoraSelectMulti, Display Any (rgthree), WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, easy showAnything, WanVideoSampler, GetNode, WanVideoScheduler, WanVideoSampler, VHS_VideoCombine, GetNode, INTConstant, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, Display Any (rgthree), GetNode, PrimitiveNode, PrimitiveNode, WanVideoScheduler, WanVideoSampler, WanVideoSampler, GetNode, GetNode, WanVideoDecode, WanVideoBlender, VHS_VideoCombine, WanVideoDecode, Display Any (rgthree), GetNode, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, CreateCFGScheduleFloatList, WanVideoScheduler, WanVideoSampler, WanVideoSampler, WanVideoScheduler, WanVideoDecode, WanVideoBlender, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, Display Any (rgthree), GetNode, WanVideoScheduler, WanVideoSampler, WanVideoScheduler, WanVideoSampler, GetNode, WanVideoDecode, GetNode, WanVideoBlender, VHS_VideoCombine, SetNode, VideoContinuationGenerator, WanVideoVAELoader, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, INTConstant, SetNode, INTConstant, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, GetNode, Seed (rgthree), WanVideoVACEStartToEndFrame, INTConstant, GetNode, WanVideoVACEEncode, GetNode, GetNode, ImageConcanate, CR Text, easy showAnything, ImpactSwitch, GetNode, Seed (rgthree), WanVideoVACEEncode, PreviewImage, VideoContinuationGenerator, CR Text, easy showAnything, ImpactSwitch, INTConstant, WanVideoVACEEncode, GetNode, CR Text, easy showAnything, VideoContinuationGenerator, PreviewImage, Seed (rgthree), ImpactSwitch, GetNode, Seed (rgthree), INTConstant, GetNode, GetNode, GetNode, GetNode, VideoContinuationGenerator, PreviewImage, WanVideoVACEEncode, CR Text, ImpactSwitch, easy showAnything, LoadImage, ImageConcanate, LoadImage, ImageConcanate, LoadImage, ImageConcanate, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_LLMAPI_NODE, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, SetNode, WanVideoVACEStartToEndFrame, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-4张旋转-简化-新提示词_2039706653515321346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039706653515321346.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（147 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `INTConstant`
- `WanVideoLoraSelectMulti`
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
- `INTConstant`
- `GetNode`
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
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `GetNode`
- `Seed (rgthree)`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `GetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `CR Text`
- `easy showAnything`
- `ImpactSwitch`
- `GetNode`
- `Seed (rgthree)`
- `WanVideoVACEEncode`
- `PreviewImage`
- `VideoContinuationGenerator`
- `CR Text`
- `easy showAnything`
- `ImpactSwitch`
- `INTConstant`
- `WanVideoVACEEncode`
- `GetNode`
- `CR Text`
- `easy showAnything`
- `VideoContinuationGenerator`
- `PreviewImage`
- `Seed (rgthree)`
- `ImpactSwitch`
- `GetNode`
- `Seed (rgthree)`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VideoContinuationGenerator`
- `PreviewImage`
- `WanVideoVACEEncode`
- `CR Text`
- `ImpactSwitch`
- `easy showAnything`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `ImageConcanate`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`

## 知识

覆盖率 **62%**（91/147）

**有卡**：`WanVideoSigmaToStep`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoLoraSelectMulti`、`Display Any (rgthree)`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoBlender`、`VideoContinuationGenerator`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Seed (rgthree)`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`ImageConcanate`、`CR Text`、`LoadImage`、`RH_LLMAPI_NODE`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
