---
key: 视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json
name: 一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1895658256604266497.json
hash: c0e059f425172071
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoEmptyEmbeds, ImageResizeKJ, ImageConcatMulti, WanVideoModelLoader, WanVideoVAELoader, VHS_LoadVideo, LoadImage, ImageScaleDownToSize, Primitive string [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoEncode, ImageConcatMulti, WanVideoTextEncode, Primitive integer [Crystools], VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoTeaCache, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895658256604266497.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `ImageResizeKJ`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageScaleDownToSize`
- `Primitive string [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoEncode`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`ImageResizeKJ`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`、`ImageScaleDownToSize`、`Primitive string [Crystools]`、`Primitive integer [Crystools]`、`WanVideoEncode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、ImageResizeKJ
