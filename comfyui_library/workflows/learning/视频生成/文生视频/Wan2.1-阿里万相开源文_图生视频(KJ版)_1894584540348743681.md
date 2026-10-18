---
key: 视频生成/文生视频/Wan2.1-阿里万相开源文_图生视频(KJ版)_1894584540348743681.json
name: Wan2.1-阿里万相开源文_图生视频(KJ版)_1894584540348743681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-阿里万相开源文_图生视频(KJ版)_1894584540348743681.json
hash: 192dc6acc5c0eec5
coverage: 0.942857
learned_at: 2026-10-15 22:43:19
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoTextEncode, WanVideoImageClipEncode, Note, LoadImage, WanVideoBlockSwap, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], CM_IntToFloat, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoDecode, WanVideoTextEncode, Primitive string [Crystools], WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSampler, WanVideoExperimentalArgs, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, Fast Groups Bypasser (rgthree), LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoVAELoader, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1-阿里万相开源文_图生视频(KJ版)_1894584540348743681.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894584540348743681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `Note`
- `LoadImage`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CM_IntToFloat`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `Primitive string [Crystools]`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `Fast Groups Bypasser (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`LoadImage`、`Primitive integer [Crystools]`、`CM_IntToFloat`、`Primitive string [Crystools]`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
