---
key: 视频生成/图生视频/FusionX Phantom MagCache加速实验版V1(视频编辑融合)_1934292137033031682.json
name: FusionX Phantom MagCache加速实验版V1(视频编辑融合)_1934292137033031682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/FusionX Phantom MagCache加速实验版V1(视频编辑融合)_1934292137033031682.json
hash: 1483420702db75e0
coverage: 0.818182
learned_at: 2026-10-15 22:30:17
nodes: [VHS_Unbatch, WanVideoEncode, WanVideoVAELoader, WanVideoDecode, AddLabel, ImageConcatMulti, WanVideoEncode, Reroute, ImageResizeKJv2, AddLabel, ImageConcatMulti, WanVideoTextEncode, EmptyImage, LoadWanVideoT5TextEncoder, LoadImage, ImageResizeKJv2, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoModelLoader, JWInteger, Note, Note, Note, Note, SetNode, LoadImage, VHS_VideoCombine, WanVideoPhantomEmbeds, WanVideoMagCache, WanVideoSampler, WanVideoSLG, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/FusionX Phantom MagCache加速实验版V1(视频编辑融合)_1934292137033031682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934292137033031682.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `VHS_Unbatch`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `AddLabel`
- `ImageConcatMulti`
- `WanVideoEncode`
- `Reroute`
- `ImageResizeKJv2`
- `AddLabel`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `EmptyImage`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoPhantomEmbeds`
- `WanVideoMagCache`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `VHS_VideoCombine`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`VHS_Unbatch`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`AddLabel`、`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoTextEncode`、`EmptyImage`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`JWInteger`、`VHS_VideoCombine`、`WanVideoPhantomEmbeds`、`WanVideoMagCache`、`WanVideoSampler`、`WanVideoSLG`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、ImageResizeKJv2
