---
key: 平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json
name: Wan2.1（阿里万相）视频转视频_1904483791740796930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json
hash: a7f8a627c97695c1
coverage: 1
learned_at: 2026-11-14 01:04:48
nodes: [WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, VHS_LoadVideo, WanVideoTextEncode, ImageResizeKJ, WanVideoSampler, WanVideoEncode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（13 个）：
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncode`、`ImageResizeKJ`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ、ImageConcatMulti
