---
key: 平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json
name: 通义万相Wan2.1视频转绘teacache加速版_1899717715358076930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json
hash: 8ac8fd22014b6536
coverage: 1
learned_at: 2026-11-14 02:48:30
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoEncode, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTeaCache, VHS_VideoCombine, WanVideoDecode, CR Upscale Image, ImageResizeKJ, WanVideoSampler, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（15 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `CR Upscale Image`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTeaCache`、`VHS_VideoCombine`、`WanVideoDecode`、`CR Upscale Image`、`ImageResizeKJ`、`WanVideoSampler`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、CR Upscale Image、ImageResizeKJ
