---
key: 视频生成/图生视频/Wan2.1 FusionX Phantom 多图像转视频_1949690915247017986.json
name: Wan2.1 FusionX Phantom 多图像转视频_1949690915247017986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949690915247017986.json
hash: 39be434e06ee954b
coverage: 0.818182
learned_at: 2026-10-15 22:30:49
nodes: [LoadImage, ImageResizeKJv2, WanVideoEncode, LoadWanVideoT5TextEncoder, MarkdownNote, WanVideoBlockSwap, WanVideoTorchCompileSettings, Reroute, ImageResizeKJv2, WanVideoEncode, ImageResizeKJv2, WanVideoEncode, ImageResizeKJv2, WanVideoEncode, LoadImage, LoadImage, LoadImage, WanVideoVAELoader, WanVideoModelLoader, INTConstant, INTConstant, WanVideoTextEncode, WanVideoSampler, MarkdownNote, WanVideoDecode, WanVideoPhantomEmbeds, WanVideoLoraSelect, VHS_VideoCombine, MarkdownNote, MarkdownNote, MarkdownNote, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 FusionX Phantom 多图像转视频_1949690915247017986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949690915247017986.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `WanVideoDecode`
- `WanVideoPhantomEmbeds`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`LoadImage`、`ImageResizeKJv2`、`WanVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`INTConstant`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoPhantomEmbeds`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
