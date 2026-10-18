---
key: 视频生成/图生视频/wan2.2-Fun-VACE舞蹈动作迁移-KJ_1967220964087959554.json
name: wan2.2-Fun-VACE舞蹈动作迁移-KJ_1967220964087959554.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Fun-VACE舞蹈动作迁移-KJ_1967220964087959554.json
hash: 09c79cb4466dfad6
coverage: 0.730769
learned_at: 2026-10-15 22:31:40
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, VHS_VideoCombine, LoadImage, SetNode, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoVAELoader, VHS_LoadVideo, ImageConcatMulti, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, GetImageSizeAndCount, INTConstant, INTConstant, GetNode, GetNode, WanVideoVACEEncode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncodeCached, LayerUtility: TextJoin, RH_Captioner, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE舞蹈动作迁移-KJ_1967220964087959554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967220964087959554.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncodeCached`
- `LayerUtility: TextJoin`
- `RH_Captioner`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LoadImage`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`WanVideoScheduler`、`WanVideoVAELoader`、`VHS_LoadVideo`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoVACEEncode`、`WanVideoLoraSelectMulti`、`CreateCFGScheduleFloatList`、`WanVideoTextEncodeCached`、`LayerUtility: TextJoin`、`RH_Captioner`、`ImageResizeKJv2`

**用到的条目**：LoadImage、Zoe-DepthMapPreprocessor、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
