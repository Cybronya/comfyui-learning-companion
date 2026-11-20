---
key: 平台全量/Wan2.2 Fun VACE 视频扩图V1_1966846434014322690.json
name: Wan2.2 Fun VACE 视频扩图V1_1966846434014322690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Fun VACE 视频扩图V1_1966846434014322690.json
hash: 1dd0f9302d56ec95
coverage: 0.744681
learned_at: 2026-11-14 01:05:27
nodes: [WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, SetNode, GetNode, VHS_VideoCombine, WanVideoScheduler, GetNode, WanVideoTextEncodeCached, JWInteger, ImpactSwitch, Note, LayerUtility: ImageScaleByAspectRatio V2, GrowMaskWithBlur, VHS_DuplicateMasks, RH_LLMAPI_NODE, GetNode, WanVideoVACEEncode, GetImageSizeAndCount, VHS_VideoInfo, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, easy showAnything, WanVideoSampler, GetImageRangeFromBatch, WanVideoSigmaToStep, VHS_LoadVideo, ImagePadForOutpaint, CR Text, PrimitiveNode, PrimitiveNode, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Fun VACE 视频扩图V1_1966846434014322690.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Fun VACE 视频扩图V1_1966846434014322690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `GetNode`
- `WanVideoTextEncodeCached`
- `JWInteger`
- `ImpactSwitch`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMaskWithBlur`
- `VHS_DuplicateMasks`
- `RH_LLMAPI_NODE`
- `GetNode`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `WanVideoSigmaToStep`
- `VHS_LoadVideo`
- `ImagePadForOutpaint`
- `CR Text`
- `PrimitiveNode`
- `PrimitiveNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（35/47）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`VHS_DuplicateMasks`、`RH_LLMAPI_NODE`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`VHS_VideoInfo`、`WanVideoDecode`、`WanVideoSampler`、`GetImageRangeFromBatch`、`WanVideoSigmaToStep`、`VHS_LoadVideo`、`ImagePadForOutpaint`、`CR Text`、`ImageConcatMulti`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount
