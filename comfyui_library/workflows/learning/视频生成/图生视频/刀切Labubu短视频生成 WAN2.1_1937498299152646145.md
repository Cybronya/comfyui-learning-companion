---
key: 视频生成/图生视频/刀切Labubu短视频生成 WAN2.1_1937498299152646145.json
name: 刀切Labubu短视频生成 WAN2.1_1937498299152646145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/刀切Labubu短视频生成 WAN2.1_1937498299152646145.json
hash: b31b458e345aa1ec
coverage: 1
learned_at: 2026-10-15 22:30:29
nodes: [WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoModelLoader, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJ, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/刀切Labubu短视频生成 WAN2.1_1937498299152646145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937498299152646145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageResizeKJ`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（17/17）

**有卡**：`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`ImageResizeKJ`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
