---
key: 平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json
name: Wan2.1+视频生视频 lora高清_2041685485076090882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json
hash: 0d577438cfc56fb4
coverage: 0.96
learned_at: 2026-11-14 01:04:34
nodes: [Note _O, ImageResizeKJ, WanVideoEncode, WanVideoVAELoader, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, Note, WanVideoTorchCompileSettings, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, FusionText, WanVideoTextEncode, String, WanVideoSampler, WanVideoTeaCache, String, LoadWanVideoT5TextEncoder, Primitive string multiline [Crystools], VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `Note _O`
- `ImageResizeKJ`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `FusionText`
- `WanVideoTextEncode`
- `String`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `String`
- `LoadWanVideoT5TextEncoder`
- `Primitive string multiline [Crystools]`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`Note _O`、`ImageResizeKJ`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`FusionText`、`WanVideoTextEncode`、`String`、`WanVideoSampler`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`Primitive string multiline [Crystools]`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJ
