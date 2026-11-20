---
key: 平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json
name: 视频扩展(Wan2.1-VACE-14B)_1923187127436103682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json
hash: 71a6678a4ca19f99
coverage: 1
learned_at: 2026-11-14 02:37:58
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader, WanVideoDecode, GetImageSize+, MaskToImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTextEncode, String Literal, ImageResizeKJ, ImagePadKJ, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json

> 来源文件 `comfyui_library/workflows/平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSize+`
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `String Literal`
- `ImageResizeKJ`
- `ImagePadKJ`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSize+`、`MaskToImage`、`VHS_VideoCombine`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`String Literal`、`ImageResizeKJ`、`ImagePadKJ`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、GetImageSize+、ImageResizeKJ
