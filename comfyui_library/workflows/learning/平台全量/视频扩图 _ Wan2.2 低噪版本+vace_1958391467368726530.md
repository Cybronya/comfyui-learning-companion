---
key: 平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json
name: 视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json
hash: d1c49a092d466c00
coverage: 0.958333
learned_at: 2026-11-14 02:37:58
nodes: [GetImageSizeAndCount, EmptyImage, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoModelLoader, GetImageSizeAndCount, WanVideoVACEEncode, AddLabel, ImageConcatMulti, RIFE VFI, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, GetImageRangeFromBatch, ImagePadKJ, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json

> 来源文件 `comfyui_library/workflows/平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（24 个）：
- `GetImageSizeAndCount`
- `EmptyImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `AddLabel`
- `ImageConcatMulti`
- `RIFE VFI`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `GetImageRangeFromBatch`
- `ImagePadKJ`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **96%**（23/24）

**有卡**：`GetImageSizeAndCount`、`EmptyImage`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`AddLabel`、`ImageConcatMulti`、`RIFE VFI`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`GetImageRangeFromBatch`、`ImagePadKJ`、`VHS_VideoCombine`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
