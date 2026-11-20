---
key: 平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json
name: 通义万相wan2.1视频转绘支持Control 控制_1907050424120303617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json
hash: 2fd3c6850e3ba128
coverage: 1
learned_at: 2026-11-14 02:48:31
nodes: [WanVideoBlockSwap, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, TextInput_, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_LoadVideo, ImageResizeKJ, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoTeaCache, WanVideoSampler, WanVideoEncode, WanVideoControlEmbeds, GetImageSizeAndCount, WanVideoEmptyEmbeds, WanVideoExperimentalArgs, WanVideoSLG, WanVideoEnhanceAVideo]
patterns: []
missing: []
---

# 平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `TextInput_`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `GetImageSizeAndCount`
- `WanVideoEmptyEmbeds`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`TextInput_`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`ImageResizeKJ`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoControlEmbeds`、`GetImageSizeAndCount`、`WanVideoEmptyEmbeds`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
