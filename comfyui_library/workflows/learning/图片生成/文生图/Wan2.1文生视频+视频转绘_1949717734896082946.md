---
key: 图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json
name: Wan2.1文生视频+视频转绘_1949717734896082946.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json
hash: 5074105b603c66fd
coverage: 0.947368
learned_at: 2026-10-07 22:58:11
nodes: [WanVideoDecode, WanVideoTextEncodeSingle, ImageResizeKJv2, PreviewImage, WanVideoVACEEncode, WanVideoTextEncodeSingle, WanVideoVAELoader, WanVideoApplyNAG, WanVideoSampler, WanVideoContextOptions, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, Int, Int, VHS_VideoCombine, VHS_LoadVideo, DWPreprocessor]
patterns: []
missing: []
---

# 图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1949717734896082946.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `WanVideoDecode`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `DWPreprocessor`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoDecode`、`WanVideoTextEncodeSingle`、`ImageResizeKJv2`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoContextOptions`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`Int`、`VHS_VideoCombine`、`VHS_LoadVideo`、`DWPreprocessor`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、WanVideoLoraSelect、ImageResizeKJv2
