---
key: 平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json
name: Wan2.1-Fun-首尾帧_1905531418771132418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json
hash: 025fb5411d3c0570
coverage: 1
learned_at: 2026-11-14 01:04:38
nodes: [WanVideoEnhanceAVideo, GetImageSizeAndCount, WanVideoEncode, WanVideoControlEmbeds, WanVideoEmptyEmbeds, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoLoraSelect, WanVideoTeaCache, WanVideoSLG, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoExperimentalArgs, WanVideoModelLoader, AIO_Preprocessor, VHS_LoadVideo, ImageResizeKJ, KepStringLiteral]
patterns: []
missing: []
---

# 平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `WanVideoEnhanceAVideo`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `AIO_Preprocessor`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `KepStringLiteral`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`WanVideoEnhanceAVideo`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoExperimentalArgs`、`WanVideoModelLoader`、`AIO_Preprocessor`、`VHS_LoadVideo`、`ImageResizeKJ`、`KepStringLiteral`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
