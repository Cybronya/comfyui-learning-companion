---
key: 视频生成/图生视频/通义万相 Wan2.1 图生视频_1894649502454710273.json
name: 通义万相 Wan2.1 图生视频_1894649502454710273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相 Wan2.1 图生视频_1894649502454710273.json
hash: fbb8fcf37299fda0
coverage: 0.777778
learned_at: 2026-10-15 22:29:16
nodes: [easy cleanGpuUsed, WanVideoDecode, WanVideoSampler, Note, WanVideoTorchCompileSettings, VHS_VideoCombine, LoadImage, Note, WanVideoBlockSwap, WanVideoModelLoader, LoadWanVideoClipTextEncoder, ImageResizeAdvanced, WanVideoImageClipEncode, Note, JjkText, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相 Wan2.1 图生视频_1894649502454710273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894649502454710273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（18 个）：
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `ImageResizeAdvanced`
- `WanVideoImageClipEncode`
- `Note`
- `JjkText`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`ImageResizeAdvanced`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
