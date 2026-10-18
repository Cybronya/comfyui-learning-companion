---
key: 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json
name: WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json
hash: 3bb9cf171e0a082c
coverage: 1
learned_at: 2026-10-15 22:29:30
nodes: [RIFE VFI, VHS_VideoCombine, easy cleanGpuUsed, WanVideoSampler, WanVideoDecode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoVAELoader, LoadImage, WanVideoTextEncode, CR Upscale Image, VHS_VideoCombine, WanVideoImageClipEncode, ImageResizeAdvanced]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1910561597662920706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（16 个）：
- `RIFE VFI`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoTextEncode`
- `CR Upscale Image`
- `VHS_VideoCombine`
- `WanVideoImageClipEncode`
- `ImageResizeAdvanced`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`RIFE VFI`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`、`CR Upscale Image`、`WanVideoImageClipEncode`、`ImageResizeAdvanced`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
