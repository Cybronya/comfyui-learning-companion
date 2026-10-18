---
key: 视频生成/图生视频/wan2.2-Fun-VACE突击侦查动作迁移-KJ_1967232757493534722.json
name: wan2.2-Fun-VACE突击侦查动作迁移-KJ_1967232757493534722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Fun-VACE突击侦查动作迁移-KJ_1967232757493534722.json
hash: ec077f446caa24ba
coverage: 0.730769
learned_at: 2026-10-15 22:31:40
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, VHS_VideoCombine, SetNode, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoVAELoader, ImageConcatMulti, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, GetImageSizeAndCount, GetNode, GetNode, WanVideoVACEEncode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoTextEncodeCached, RH_Captioner, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, INTConstant, INTConstant, LayerUtility: TextJoin]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE突击侦查动作迁移-KJ_1967232757493534722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967232757493534722.json`

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
- `RH_Captioner`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `LayerUtility: TextJoin`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`WanVideoScheduler`、`WanVideoVAELoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoLoraSelectMulti`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoTextEncodeCached`、`RH_Captioner`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: TextJoin`

**用到的条目**：LoadImage、Zoe-DepthMapPreprocessor、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
