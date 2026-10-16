---
key: 视频生成/文生视频/最新wan2.1 首_中_尾多 图生视频_1935254064009498626.json
name: 最新wan2.1 首_中_尾多 图生视频_1935254064009498626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1935254064009498626.json
hash: baf2ac6c9bbe3295
coverage: 1
learned_at: 2026-10-15 22:43:28
nodes: [ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, INTConstant, INTConstant, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, GetImageRangeFromBatch, GetImageSizeAndCount, ImageBatchMulti, MaskBatchMulti, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSampler, WanVideoTextEncode, VHS_VideoCombine, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/最新wan2.1 首_中_尾多 图生视频_1935254064009498626.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1935254064009498626.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `MaskBatchMulti`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ImageResizeKJ`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`ImageBatchMulti`、`MaskBatchMulti`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
