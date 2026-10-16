---
key: 视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json
name: wan2.1图生视频(cache加速版)_1954434539328290817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954434539328290817.json
hash: daff0e6eeee3a286
coverage: 0.714286
learned_at: 2026-10-15 22:31:06
nodes: [VHS_VideoCombine, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note, WanVideoContextOptions, WanVideoTeaCache, PrimitiveNode, PrimitiveNode, Note, LoadWanVideoClipTextEncoder, LoadImage, WanVideoModelLoader, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, Note, WanVideoTextEncode, PrimitiveNode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954434539328290817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（21 个）：
- `VHS_VideoCombine`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoContextOptions`
- `WanVideoTeaCache`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadImage`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncode`
- `PrimitiveNode`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`VHS_VideoCombine`、`WanVideoImageClipEncode`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoContextOptions`、`WanVideoTeaCache`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
