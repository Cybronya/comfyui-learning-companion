---
key: 视频生成/图生视频/被压扁特效-万相wan2.1新玩意_1899672945285877762.json
name: 被压扁特效-万相wan2.1新玩意_1899672945285877762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/被压扁特效-万相wan2.1新玩意_1899672945285877762.json
hash: 6cfe0b487a05c555
coverage: 0.95
learned_at: 2026-10-15 22:29:21
nodes: [WanVideoTeaCache, ImageUpscaleWithModel, Note Plus (mtb), Note, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoDecode, Int, WanVideoTextEncode, LayerUtility: PurgeVRAM, VHS_VideoCombine, LoadImage, UpscaleModelLoader, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/被压扁特效-万相wan2.1新玩意_1899672945285877762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899672945285877762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoTeaCache`
- `ImageUpscaleWithModel`
- `Note Plus (mtb)`
- `Note`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `Int`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LoadImage`
- `UpscaleModelLoader`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **95%**（19/20）

**有卡**：`WanVideoTeaCache`、`ImageUpscaleWithModel`、`Note Plus (mtb)`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`Int`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`LoadImage`、`UpscaleModelLoader`、`WanVideoImageClipEncode`、`WanVideoLoraSelect`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
