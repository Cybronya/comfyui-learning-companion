---
key: 平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json
name: Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json
hash: 7cd43415407fb99b
coverage: 0.878788
learned_at: 2026-11-14 01:04:38
nodes: [WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoLoraSelect, WanVideoExperimentalArgs, WanVideoDecode, AIO_Preprocessor, WanVideoEncode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, WanVideoControlEmbeds, ImageResizeKJ, LoadWanVideoClipTextEncoder, WanVideoTeaCache, WanVideoSLG, Florence2ModelLoader, KepStringLiteral, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoBlockSwap, LayerUtility: PurgeVRAM, Florence2Run, VHS_LoadVideo, WanVideoModelLoader, LoadImage, WanVideoVAELoader, WanVideoClipVisionEncode, ImageResizeKJ, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `AIO_Preprocessor`
- `WanVideoEncode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoControlEmbeds`
- `ImageResizeKJ`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTeaCache`
- `WanVideoSLG`
- `Florence2ModelLoader`
- `KepStringLiteral`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `Florence2Run`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`AIO_Preprocessor`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoControlEmbeds`、`ImageResizeKJ`、`LoadWanVideoClipTextEncoder`、`WanVideoTeaCache`、`WanVideoSLG`、`Florence2ModelLoader`、`KepStringLiteral`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`Florence2Run`、`VHS_LoadVideo`、`WanVideoModelLoader`、`LoadImage`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode
