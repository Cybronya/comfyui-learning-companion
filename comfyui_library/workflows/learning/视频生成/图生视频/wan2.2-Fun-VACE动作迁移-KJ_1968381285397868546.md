---
key: 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1968381285397868546.json
name: wan2.2-Fun-VACE动作迁移-KJ_1968381285397868546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1968381285397868546.json
hash: 16e4e3895d60c591
coverage: 0.730769
learned_at: 2026-10-15 22:31:45
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoBlockSwap, SetNode, Reroute, DWPreprocessor, ImageBlend, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, VHS_LoadVideo, ImageConcatMulti, WanVideoDecode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, GetImageSizeAndCount, INTConstant, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, INTConstant, WanVideoTextEncodeCached, ImageResizeKJv2, Zoe-DepthMapPreprocessor, INTConstant, LoadImage, WanVideoSampler, WanVideoVACEEncode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, Note, Note, WanVideoVAELoader, SetNode, RH_Captioner, LayerUtility: TextJoin, ImageResizeKJv2, SetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1968381285397868546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968381285397868546.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `SetNode`
- `Reroute`
- `DWPreprocessor`
- `ImageBlend`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `GetImageSizeAndCount`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `Zoe-DepthMapPreprocessor`
- `INTConstant`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `SetNode`
- `RH_Captioner`
- `LayerUtility: TextJoin`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`DWPreprocessor`、`ImageBlend`、`WanVideoScheduler`、`VHS_LoadVideo`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`Zoe-DepthMapPreprocessor`、`LoadImage`、`WanVideoVACEEncode`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`RH_Captioner`、`LayerUtility: TextJoin`、`VHS_VideoCombine`

**用到的条目**：LoadImage、Zoe-DepthMapPreprocessor、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
