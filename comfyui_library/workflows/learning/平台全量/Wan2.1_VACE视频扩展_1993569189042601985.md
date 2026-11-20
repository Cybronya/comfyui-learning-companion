---
key: 平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json
name: Wan2.1_VACE视频扩展_1993569189042601985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json
hash: b0ca66f0e2551dc4
coverage: 0.96
learned_at: 2026-11-14 01:04:44
nodes: [GetImageRangeFromBatch, PreviewImage, GetImageRangeFromBatch, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVACEEncode, GetImageSizeAndCount, AddLabel, GetImageSizeAndCount, ImageConcatMulti, EmptyImage, WanVideoDecode, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, MaskPreview+, LoadWanVideoT5TextEncoder, VHS_LoadVideo, WanVideoTextEncode, ImageResizeKJ, VHS_VideoCombine, VHS_VideoCombine, ImagePadKJ, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（25 个）：
- `GetImageRangeFromBatch`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `AddLabel`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `EmptyImage`
- `WanVideoDecode`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `MaskPreview+`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImagePadKJ`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **96%**（24/25）

**有卡**：`GetImageRangeFromBatch`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`AddLabel`、`ImageConcatMulti`、`EmptyImage`、`WanVideoDecode`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`MaskPreview+`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`WanVideoTextEncode`、`ImageResizeKJ`、`VHS_VideoCombine`、`ImagePadKJ`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount
