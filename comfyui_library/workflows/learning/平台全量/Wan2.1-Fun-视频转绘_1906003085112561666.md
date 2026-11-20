---
key: 平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json
name: Wan2.1-Fun-视频转绘_1906003085112561666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json
hash: c710ebe249450818
coverage: 1
learned_at: 2026-11-14 01:04:37
nodes: [Florence2ModelLoader, GetImageSizeAndCount, WanVideoEncode, WanVideoControlEmbeds, WanVideoEmptyEmbeds, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, KepStringLiteral, WanVideoLoraSelect, WanVideoSLG, WanVideoSampler, WanVideoDecode, WanVideoExperimentalArgs, VHS_VideoCombine, AIO_Preprocessor, AIO_Preprocessor, ImageResizeKJ, ImageBlend, Florence2Run, LayerUtility: PurgeVRAM, VHS_LoadVideo, LoadImage, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoModelLoader, WanVideoBlockSwap]
patterns: []
missing: []
---

# 平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `Florence2ModelLoader`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `KepStringLiteral`
- `WanVideoLoraSelect`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `ImageBlend`
- `Florence2Run`
- `LayerUtility: PurgeVRAM`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`Florence2ModelLoader`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`KepStringLiteral`、`WanVideoLoraSelect`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`AIO_Preprocessor`、`ImageResizeKJ`、`ImageBlend`、`Florence2Run`、`LayerUtility: PurgeVRAM`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoModelLoader`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
