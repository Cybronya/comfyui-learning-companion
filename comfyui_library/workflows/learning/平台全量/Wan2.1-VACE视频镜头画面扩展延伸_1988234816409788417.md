---
key: 平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json
name: Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json
hash: 6ee61ae0848faf97
coverage: 0.69697
learned_at: 2026-11-14 01:04:39
nodes: [WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoDecode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, GetNode, SetNode, WanVideoVACEEncode, ImageResizeKJ, ImagePadKJ, GetImageSize+, MaskToImage, SetNode, WanVideoTorchCompileSettings, VHS_VideoCombine, Note, WanVideoTextEncode, String Literal, Note]
patterns: []
missing: []
---

# 平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `ImagePadKJ`
- `GetImageSize+`
- `MaskToImage`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncode`
- `String Literal`
- `Note`

## 知识

覆盖率 **70%**（23/33）

**有卡**：`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`ImageResizeKJ`、`ImagePadKJ`、`GetImageSize+`、`MaskToImage`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、GetImageSize+、ImageResizeKJ
