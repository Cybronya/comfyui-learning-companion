---
key: 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1967789727392890881.json
name: wan2.2-Fun-VACE动作迁移-KJ_1967789727392890881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967789727392890881.json
hash: 896ffb847165575d
coverage: 0.666667
learned_at: 2026-10-15 22:31:42
nodes: [WanVideoLoraSelectMulti, WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoModelLoader, SetNode, INTConstant, INTConstant, SetNode, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, ImageResizeKJv2, PrimitiveFloat, SetNode, RH_Captioner, Note, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, WanVideoTextEncodeCached, GetNode, Zoe-DepthMapPreprocessor, SetNode, VHS_LoadVideo, SetNode, VHS_VideoCombine, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSampler, GetNode, WanVideoVACEEncode, Reroute, Reroute, easy cleanGpuUsed, WanVideoSampler, WanVideoSetLoRAs, VHS_VideoCombine, easy cleanGpuUsed, VHS_VideoCombine, LayerUtility: TextJoin, INTConstant, RH_Translator, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SetNode, GetNode, WanVideoDecode, GetNode, ImageConcatMulti, GetNode, GetNode, LoadImage, DWPreprocessor, ImageBlend, GetImageSizeAndCount]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1967789727392890881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967789727392890881.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `SetNode`
- `RH_Captioner`
- `Note`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoTextEncodeCached`
- `GetNode`
- `Zoe-DepthMapPreprocessor`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoVACEEncode`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LayerUtility: TextJoin`
- `INTConstant`
- `RH_Translator`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `LoadImage`
- `DWPreprocessor`
- `ImageBlend`
- `GetImageSizeAndCount`

## 知识

覆盖率 **67%**（40/60）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`WanVideoVAELoader`、`ImageResizeKJv2`、`RH_Captioner`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`Zoe-DepthMapPreprocessor`、`VHS_LoadVideo`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoVACEEncode`、`easy cleanGpuUsed`、`LayerUtility: TextJoin`、`RH_Translator`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`ImageConcatMulti`、`LoadImage`、`DWPreprocessor`、`ImageBlend`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、Zoe-DepthMapPreprocessor、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode
