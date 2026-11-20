---
key: 平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json
name: Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json
hash: 13cfc9f872816fff
coverage: 0.615385
learned_at: 2026-11-14 01:04:46
nodes: [WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, ImageResize+, PreviewImage, PreviewImage, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoSampler, WanVideoBlockSwap, WanVideoVAELoader, PreviewImage, SetNode, SetNode, SetNode, SetNode, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, LoadImage, LoadImage, RH_Translator, LayerUtility: ImageScaleByAspectRatio V2, WanVideoExperimentalArgs, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, SetNode, MaskPreview+, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `ImageResize+`
- `PreviewImage`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadImage`
- `RH_Translator`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `MaskPreview+`
- `VHS_VideoCombine`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoLoraSelect`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`ImageResize+`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`LoadImage`、`RH_Translator`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`MaskPreview+`、`VHS_VideoCombine`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
