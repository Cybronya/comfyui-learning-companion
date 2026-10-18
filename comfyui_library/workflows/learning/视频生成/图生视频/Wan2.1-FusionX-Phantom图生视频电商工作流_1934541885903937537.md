---
key: 视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json
name: Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json
hash: 2eeb5f3a3772594b
coverage: 1
learned_at: 2026-10-15 22:30:17
nodes: [LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoEncode, WanVideoEncode, WanVideoVAELoader, WanVideoModelLoader, WanVideoDecode, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, INTConstant, WanVideoPhantomEmbeds, WanVideoBlockSwap, LoadImage, LoadImage, Text Multiline, INTConstant, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934541885903937537.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoPhantomEmbeds`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`INTConstant`、`WanVideoPhantomEmbeds`、`WanVideoBlockSwap`、`LoadImage`、`Text Multiline`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、ImageResizeKJv2
