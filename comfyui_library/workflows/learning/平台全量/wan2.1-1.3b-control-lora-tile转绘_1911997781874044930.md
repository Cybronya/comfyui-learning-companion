---
key: 平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json
name: wan2.1-1.3b-control-lora-tile转绘_1911997781874044930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json
hash: 3157740b559bc70b
coverage: 1
learned_at: 2026-11-14 01:19:09
nodes: [WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, WanVideoEncode, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, ImageBlur, VHS_LoadVideo, ImageResizeKJ, LoadWanVideoT5TextEncoder, WanVideoTeaCache, WanVideoTextEncode, WanVideoControlEmbeds]
patterns: []
missing: []
---

# 平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1-1.3b-control-lora-tile转绘_1911997781874044930.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `ImageBlur`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoControlEmbeds`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`ImageBlur`、`VHS_LoadVideo`、`ImageResizeKJ`、`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`WanVideoTextEncode`、`WanVideoControlEmbeds`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJ
