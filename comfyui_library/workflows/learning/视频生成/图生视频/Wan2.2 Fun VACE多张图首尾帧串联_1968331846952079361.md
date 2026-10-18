---
key: 视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json
name: Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json
hash: 32d65a921c973fc4
coverage: 0.62
learned_at: 2026-10-15 22:31:44
nodes: [WanVideoTorchCompileSettings, SetNode, WanVideoSampler, GetNode, WanVideoSampler, WanVideoSampler, GetNode, GetNode, PrimitiveNode, WanVideoSigmaToStep, GetNode, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, WanVideoSampler, GetNode, WanVideoSetBlockSwap, SetNode, WanVideoSampler, WanVideoBlockSwap, PrimitiveNode, WanVideoSigmaToStep, GetNode, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, WanVideoVACEEncode, INTConstant, GetNode, PreviewImage, PreviewImage, CreateCFGScheduleFloatList, Display Any (rgthree), CreateCFGScheduleFloatList, Display Any (rgthree), Display Any (rgthree), CreateCFGScheduleFloatList, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoVACEEncode, WanVideoVAELoader, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, GetNode, WanVideoDecode, Seed (rgthree), INTConstant, GetNode, INTConstant, INTConstant, INTConstant, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, INTConstant, easy showAnything, RH_LLMAPI_NODE, ImpactSwitch, RH_LLMAPI_NODE, VideoContinuationGenerator, easy showAnything, RH_LLMAPI_NODE, ImpactSwitch, GetNode, VideoContinuationGenerator, easy showAnything, RH_LLMAPI_NODE, CR Text, ImpactSwitch, ImageConcanate, LoadImage, ImageConcanate, LoadImage, ImageConcanate, LoadImage, LoadImage, GetNode, WanVideoSetBlockSwap, WanVideoDecode, WanVideoBlender, GetNode, WanVideoDecode, CR Text, WanVideoBlender, easy showAnything, ImpactSwitch, WanVideoScheduler, Seed (rgthree), WanVideoDecode, LoadImage, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageConcanate, GetNode, GetNode, GetNode, Seed (rgthree), Seed (rgthree), VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, SetNode, CR Text, Display Any (rgthree), CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, WanVideoScheduler, easy showAnything, GetNode, GetNode, GetNode, GetNode, CR Text, WanVideoVACEEncode, VideoContinuationGenerator, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, PreviewImage, VideoContinuationGenerator, GetNode, WanVideoBlender, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968331846952079361.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（150 个）：
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
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoVACEEncode`
- `INTConstant`
- `GetNode`
- `PreviewImage`
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
- `PrimitiveNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoDecode`
- `Seed (rgthree)`
- `INTConstant`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `RH_LLMAPI_NODE`
- `VideoContinuationGenerator`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `GetNode`
- `VideoContinuationGenerator`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `CR Text`
- `ImpactSwitch`
- `ImageConcanate`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoBlender`
- `GetNode`
- `WanVideoDecode`
- `CR Text`
- `WanVideoBlender`
- `easy showAnything`
- `ImpactSwitch`
- `WanVideoScheduler`
- `Seed (rgthree)`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GetNode`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
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
- `CR Text`
- `WanVideoVACEEncode`
- `VideoContinuationGenerator`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `VideoContinuationGenerator`
- `GetNode`
- `WanVideoBlender`
- `INTConstant`
- `VHS_VideoCombine`

## 知识

覆盖率 **62%**（93/150）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`Display Any (rgthree)`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`Seed (rgthree)`、`RH_LLMAPI_NODE`、`VideoContinuationGenerator`、`CR Text`、`ImageConcanate`、`LoadImage`、`WanVideoBlender`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
