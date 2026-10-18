---
key: 视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json
name: 通义万相WAN2.1 图生视频_1913599266676273153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json
hash: 1b50cbe212040b32
coverage: 1
learned_at: 2026-10-15 22:29:34
nodes: [WanVideoTeaCache, WanVideoImageClipEncode, WanVideoBlockSwap, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, ImageScaleToTotalPixels, easy imageSize, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相WAN2.1 图生视频_1913599266676273153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913599266676273153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（14 个）：
- `WanVideoTeaCache`
- `WanVideoImageClipEncode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoTeaCache`、`WanVideoImageClipEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`ImageScaleToTotalPixels`、`easy imageSize`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
