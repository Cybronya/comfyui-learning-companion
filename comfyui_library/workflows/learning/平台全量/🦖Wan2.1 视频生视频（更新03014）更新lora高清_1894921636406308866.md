---
key: 平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json
name: 🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json
hash: 4db30bdb161d3ec0
coverage: 0.96
learned_at: 2026-11-14 02:55:46
nodes: [Note _O, ImageResizeKJ, WanVideoEncode, WanVideoVAELoader, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoTorchCompileSettings, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, VHS_LoadVideo, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, FusionText, WanVideoTextEncode, Primitive string multiline [Crystools], String, String, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTeaCache]
patterns: []
missing: []
---

# 平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json`

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
- `VHS_VideoCombine`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `FusionText`
- `WanVideoTextEncode`
- `Primitive string multiline [Crystools]`
- `String`
- `String`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`Note _O`、`ImageResizeKJ`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`FusionText`、`WanVideoTextEncode`、`Primitive string multiline [Crystools]`、`String`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTeaCache`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJ
