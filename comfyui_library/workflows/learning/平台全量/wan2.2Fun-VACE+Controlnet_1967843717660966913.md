---
key: 平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json
name: wan2.2Fun-VACE+Controlnet_1967843717660966913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json
hash: a6e3f6f1a5119645
coverage: 1
learned_at: 2026-11-14 01:19:36
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, ImageResizeKJv2, WanVideoSampler, WanVideoVACEEncode, ImageResizeKJv2, LoadImage, INTConstant, WanVideoSampler, PurgeVRAM_UTK, ImageConcatMulti, WanVideoDecode, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine, DepthAnythingV2Preprocessor, CreateCFGScheduleFloatList, VHS_LoadVideo, INTConstant, INTConstant]
patterns: []
missing: []
---

# 平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2Fun-VACE+Controlnet_1967843717660966913.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `LoadImage`
- `INTConstant`
- `WanVideoSampler` ★核心
- `PurgeVRAM_UTK`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DepthAnythingV2Preprocessor`
- `CreateCFGScheduleFloatList`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoVACEEncode`、`LoadImage`、`PurgeVRAM_UTK`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoInfo`、`VHS_VideoCombine`、`DepthAnythingV2Preprocessor`、`CreateCFGScheduleFloatList`、`VHS_LoadVideo`

**用到的条目**：LoadImage、DepthAnythingV2Preprocessor、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode
