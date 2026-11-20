---
key: 平台全量/Wan2.2 VACE视频扩图_1979922003790565378.json
name: Wan2.2 VACE视频扩图_1979922003790565378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 VACE视频扩图_1979922003790565378.json
hash: 64aa8b049de74e93
coverage: 1
learned_at: 2026-11-14 01:05:35
nodes: [WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoVACEModelSelect, WanVideoVAELoader, INTConstant, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, VHS_LoadVideo, INTConstant, INTConstant, WanVideoVACEEncode, ImagePadForOutpaint, GetImageSizeAndCount, VHS_DuplicateMasks, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, CreateCFGScheduleFloatList, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2 VACE视频扩图_1979922003790565378.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 VACE视频扩图_1979922003790565378.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEEncode`
- `ImagePadForOutpaint`
- `GetImageSizeAndCount`
- `VHS_DuplicateMasks`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`INTConstant`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`ImagePadForOutpaint`、`GetImageSizeAndCount`、`VHS_DuplicateMasks`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount
