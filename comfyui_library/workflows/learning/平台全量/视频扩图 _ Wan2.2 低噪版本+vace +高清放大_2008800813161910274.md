---
key: 平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json
name: 视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json
hash: 9fc7c874b51dda14
coverage: 0.952381
learned_at: 2026-11-14 02:37:56
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, GetImageRangeFromBatch, PreviewImage, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEEncode, WanVideoSampler, GetImageSizeAndCount, FlashVSRNode, VHS_VideoCombine, VHS_LoadVideo, WanVideoDecode, VHS_VideoCombine, ImagePadKJ, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json

> 来源文件 `comfyui_library/workflows/平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（21 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `FlashVSRNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImagePadKJ`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`GetImageRangeFromBatch`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoSampler`、`GetImageSizeAndCount`、`FlashVSRNode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoDecode`、`ImagePadKJ`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
