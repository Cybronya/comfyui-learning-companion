---
key: 数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json
name: wan2.2 视频转绘生成一镜到底vlog_1954830072336179202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json
hash: 9257196b5ca625e8
coverage: 1
learned_at: 2026-10-26 01:59:26
nodes: [WanVideoDecode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoTextEncode, ImageResizeKJv2, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoContextOptions, VHS_LoadVideo, VHS_VideoCombine, WanVideoSampler]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（15 个）：
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoContextOptions`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`WanVideoContextOptions`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect、ImageResizeKJv2
