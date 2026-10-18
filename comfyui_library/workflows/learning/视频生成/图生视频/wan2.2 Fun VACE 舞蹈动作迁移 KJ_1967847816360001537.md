---
key: 视频生成/图生视频/wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json
name: wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json
hash: d67a9d8874371f30
coverage: 0.730769
learned_at: 2026-10-15 22:31:43
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, VHS_VideoCombine, SetNode, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoVAELoader, ImageConcatMulti, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, GetImageSizeAndCount, INTConstant, INTConstant, GetNode, GetNode, WanVideoVACEEncode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncodeCached, LayerUtility: TextJoin, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, RH_Captioner]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967847816360001537.json`

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
- `SetNode`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `WanVideoVAELoader`
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `RH_Captioner`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`WanVideoScheduler`、`WanVideoVAELoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoVACEEncode`、`WanVideoLoraSelectMulti`、`CreateCFGScheduleFloatList`、`WanVideoTextEncodeCached`、`LayerUtility: TextJoin`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`RH_Captioner`

**用到的条目**：LoadImage、Zoe-DepthMapPreprocessor、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
