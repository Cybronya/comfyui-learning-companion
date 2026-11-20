---
key: 平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json
name: Wan2.1-KJ-视频到视频编辑_1895342414981169154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json
hash: b73aff484d81db3f
coverage: 1
learned_at: 2026-11-14 01:04:39
nodes: [WanVideoEmptyEmbeds, VHS_LoadVideo, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSampler, WanVideoEncode, WanVideoDecode, ImageConcatMulti, Primitive integer [Crystools], VHS_VideoCombine, CM_IntToFloat, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoModelLoader, VHS_VideoCombine, ImageResizeKJ, WanVideoTextEncode, Primitive string [Crystools], Primitive integer [Crystools]]
patterns: []
missing: []
---

# 平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoEmptyEmbeds`
- `VHS_LoadVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `CM_IntToFloat`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `Primitive string [Crystools]`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`WanVideoEmptyEmbeds`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoDecode`、`ImageConcatMulti`、`Primitive integer [Crystools]`、`VHS_VideoCombine`、`CM_IntToFloat`、`WanVideoModelLoader`、`ImageResizeKJ`、`WanVideoTextEncode`、`Primitive string [Crystools]`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ、CM_IntToFloat
