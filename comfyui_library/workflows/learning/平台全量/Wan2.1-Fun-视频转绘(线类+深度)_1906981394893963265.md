---
key: 平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json
name: Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json
hash: 59334a91b8fbcd03
coverage: 0.885714
learned_at: 2026-11-14 01:04:36
nodes: [WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoExperimentalArgs, WanVideoDecode, VHS_VideoCombine, WanVideoTeaCache, WanVideoSLG, KepStringLiteral, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, ImageBlend, AIO_Preprocessor, WanVideoSampler, AIO_Preprocessor, VHS_VideoCombine, LayerUtility: PurgeVRAM, Florence2Run, LoadImage, WanVideoTorchCompileSettings, WanVideoModelLoader, Florence2ModelLoader, WanVideoEncode, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoControlEmbeds, LoadWanVideoClipTextEncoder, ImageResizeKJ, easy showAnything, easy showAnything, easy showAnything, easy showAnything, VHS_LoadVideo, ImageResizeKJ]
patterns: []
missing: []
---

# 平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `KepStringLiteral`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `ImageBlend`
- `AIO_Preprocessor`
- `WanVideoSampler` ★核心
- `AIO_Preprocessor`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `Florence2Run`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `Florence2ModelLoader`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoControlEmbeds`
- `LoadWanVideoClipTextEncoder` ★核心
- `ImageResizeKJ`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VHS_LoadVideo`
- `ImageResizeKJ`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoLoraSelect`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTeaCache`、`WanVideoSLG`、`KepStringLiteral`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageBlend`、`AIO_Preprocessor`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`Florence2Run`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`Florence2ModelLoader`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoControlEmbeds`、`LoadWanVideoClipTextEncoder`、`ImageResizeKJ`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode
