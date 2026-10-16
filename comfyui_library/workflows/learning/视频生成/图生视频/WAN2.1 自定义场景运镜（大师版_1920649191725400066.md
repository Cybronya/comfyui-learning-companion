---
key: 视频生成/图生视频/WAN2.1 自定义场景运镜（大师版_1920649191725400066.json
name: WAN2.1 自定义场景运镜（大师版_1920649191725400066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1920649191725400066.json
hash: 79df8aaf5a30f6b9
coverage: 1
learned_at: 2026-10-15 22:29:42
nodes: [WanVideoDecode, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoImageClipEncode, WanVideoSampler, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, VHS_VideoCombine, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 自定义场景运镜（大师版_1920649191725400066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920649191725400066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（12 个）：
- `WanVideoDecode`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（12/12）

**有卡**：`WanVideoDecode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
