---
key: 视频生成/图生视频/wan2.2-Fun-VACE首尾帧-KJ_1967848289393606658.json
name: wan2.2-Fun-VACE首尾帧-KJ_1967848289393606658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Fun-VACE首尾帧-KJ_1967848289393606658.json
hash: 82c97a946681663c
coverage: 0.654545
learned_at: 2026-10-15 22:31:43
nodes: [WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoModelLoader, SetNode, INTConstant, INTConstant, SetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, PrimitiveFloat, SetNode, RH_Captioner, Note, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, VHS_VideoCombine, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSampler, GetNode, Reroute, Reroute, easy cleanGpuUsed, WanVideoSampler, WanVideoSetLoRAs, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, GetNode, LoadImage, INTConstant, WanVideoTextEncodeCached, LayerUtility: TextJoin, WanVideoVACEStartToEndFrame, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVACEModelSelect, LoadImage, RH_Translator, ImageResizeKJv2, SetNode, SetNode, GetNode, ImageConcatMulti, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, WanVideoVACEEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE首尾帧-KJ_1967848289393606658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967848289393606658.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `PrimitiveFloat`
- `SetNode`
- `RH_Captioner`
- `Note`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `GetNode`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `LoadImage`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `LayerUtility: TextJoin`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoVACEModelSelect`
- `LoadImage`
- `RH_Translator`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`

## 知识

覆盖率 **65%**（36/55）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`WanVideoVAELoader`、`RH_Captioner`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`LoadImage`、`WanVideoTextEncodeCached`、`LayerUtility: TextJoin`、`WanVideoVACEStartToEndFrame`、`WanVideoLoraSelectMulti`、`RH_Translator`、`ImageResizeKJv2`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEEncode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
