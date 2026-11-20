---
key: 平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json
name: Wan2.2 VACE 视频动作迁移_1979193024913772546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json
hash: 9aa9f05d719490c8
coverage: 1
learned_at: 2026-11-14 01:05:33
nodes: [INTConstant, WanVideoSampler, INTConstant, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, PixelPerfectResolution, DWPreprocessor, ImageResizeKJv2, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoVACEEncode, VHS_LoadVideo, SimpleMath+, INTConstant, LoadImage, INTConstant, INTConstant]
patterns: []
missing: []
---

# 平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `INTConstant`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoVACEEncode`
- `VHS_LoadVideo`
- `SimpleMath+`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`PixelPerfectResolution`、`DWPreprocessor`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoVACEEncode`、`VHS_LoadVideo`、`SimpleMath+`、`LoadImage`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti
