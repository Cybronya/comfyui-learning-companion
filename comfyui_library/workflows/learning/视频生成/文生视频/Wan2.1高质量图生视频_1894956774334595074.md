---
key: 视频生成/文生视频/Wan2.1高质量图生视频_1894956774334595074.json
name: Wan2.1高质量图生视频_1894956774334595074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1高质量图生视频_1894956774334595074.json
hash: 9bdc4b6437f4b33e
coverage: 0.928571
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoImageClipEncode, WanVideoModelLoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSampler, LoadImage, Note, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, easy cleanGpuUsed, Note Plus (mtb), LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1高质量图生视频_1894956774334595074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894956774334595074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `LoadImage`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `Note Plus (mtb)`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **93%**（13/14）

**有卡**：`WanVideoImageClipEncode`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`Note Plus (mtb)`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
