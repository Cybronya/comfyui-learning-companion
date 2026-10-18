---
key: 视频生成/图生视频/KJ-Wan2.1-图生视频_1895074790560956417.json
name: KJ-Wan2.1-图生视频_1895074790560956417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/KJ-Wan2.1-图生视频_1895074790560956417.json
hash: dd12e8ca7f0fc03f
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoSampler, WanVideoDecode, WanVideoBlockSwap, WanVideoImageClipEncode, WanVideoTextEncode, LoadImage, VHS_VideoCombine, String Literal, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ-Wan2.1-图生视频_1895074790560956417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895074790560956417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（12 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `String Literal`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`LoadImage`、`VHS_VideoCombine`、`String Literal`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
