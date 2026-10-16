---
key: 视频生成/图生视频/解压神器，一起来切水晶--万相WAN2.1_1899288956402356225.json
name: 解压神器，一起来切水晶--万相WAN2.1_1899288956402356225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1899288956402356225.json
hash: 5dbcc76a956147ae
coverage: 0.909091
learned_at: 2026-10-15 22:29:21
nodes: [ImageUpscaleWithModel, Note Plus (mtb), UpscaleModelLoader, LayerUtility: PurgeVRAM, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, RHHiddenNodes, PrimitiveStringMultiline, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoImageClipEncode, LoadImage, WanVideoDecode, Int, MarkdownNote, VHS_VideoCombine, WanVideoTextEncode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/解压神器，一起来切水晶--万相WAN2.1_1899288956402356225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899288956402356225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（22 个）：
- `ImageUpscaleWithModel`
- `Note Plus (mtb)`
- `UpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `RHHiddenNodes`
- `PrimitiveStringMultiline`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageClipEncode`
- `LoadImage`
- `WanVideoDecode`
- `Int`
- `MarkdownNote`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ImageUpscaleWithModel`、`Note Plus (mtb)`、`UpscaleModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`RHHiddenNodes`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoImageClipEncode`、`LoadImage`、`WanVideoDecode`、`Int`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
