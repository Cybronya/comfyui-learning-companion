---
key: 平台全量/🤖WAN2.1-VACE一键视频扩展_1924687955204763649.json
name: 🤖WAN2.1-VACE一键视频扩展_1924687955204763649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🤖WAN2.1-VACE一键视频扩展_1924687955204763649.json
hash: 16ed0fae83ac9be4
coverage: 1
learned_at: 2026-11-14 02:55:28
nodes: [WanVideoTextEncode, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, GetImageSize+, MaskToImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, VHS_LoadVideo, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, String Literal, ImageResizeKJ, ImagePadKJ, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/🤖WAN2.1-VACE一键视频扩展_1924687955204763649.json

> 来源文件 `comfyui_library/workflows/平台全量/🤖WAN2.1-VACE一键视频扩展_1924687955204763649.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `GetImageSize+`
- `MaskToImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `String Literal`
- `ImageResizeKJ`
- `ImagePadKJ`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`GetImageSize+`、`MaskToImage`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoDecode`、`WanVideoSampler`、`String Literal`、`ImageResizeKJ`、`ImagePadKJ`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、GetImageSize+、ImageResizeKJ
