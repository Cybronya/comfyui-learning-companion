---
key: 视频生成/图生视频/【效果惊艳】WAN2.1 万相图生视频_1901173335622066177.json
name: 【效果惊艳】WAN2.1 万相图生视频_1901173335622066177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901173335622066177.json
hash: 4134ab2e0010a314
coverage: 1
learned_at: 2026-10-15 22:29:23
nodes: [WanVideoDecode, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoImageClipEncode, WanVideoModelLoader, RIFE VFI, LoadImage, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CR Upscale Image, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/【效果惊艳】WAN2.1 万相图生视频_1901173335622066177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901173335622066177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（14 个）：
- `WanVideoDecode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `RIFE VFI`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `CR Upscale Image`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoDecode`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`WanVideoModelLoader`、`RIFE VFI`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CR Upscale Image`、`VHS_VideoCombine`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
