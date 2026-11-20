---
key: 平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json
name: Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json
hash: 7dfb1a4d1e52397e
coverage: 0.888889
learned_at: 2026-11-14 01:06:39
nodes: [LoadImage, WanVideoBlockSwap, MarkdownNote, WanVideoDecode, INTConstant, WanVideoTorchCompileSettings, LoadImage, LoadImage, WanVideoPhantomEmbeds, WanVideoSampler, VHS_VideoCombine, INTConstant, Reroute, WanVideoTextEncode, ImageResizeKJv2, WanVideoEncode, ImageResizeKJv2, WanVideoEncode, ImageResizeKJv2, WanVideoEncode, ImageResizeKJv2, WanVideoEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, MarkdownNote, LoadImage, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `LoadImage`
- `WanVideoBlockSwap`
- `MarkdownNote`
- `WanVideoDecode`
- `INTConstant`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `LoadImage`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `Reroute`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `MarkdownNote`
- `LoadImage`
- `WanVideoModelLoader`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`LoadImage`、`WanVideoBlockSwap`、`WanVideoDecode`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoPhantomEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJv2
