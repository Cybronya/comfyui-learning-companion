---
key: 视频生成/图生视频/一键泄气特效-万相wan2.1新玩意_1899415692570181634.json
name: 一键泄气特效-万相wan2.1新玩意_1899415692570181634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一键泄气特效-万相wan2.1新玩意_1899415692570181634.json
hash: 38a35fa61a9d7ea5
coverage: 0.95
learned_at: 2026-10-15 22:29:21
nodes: [Note Plus (mtb), WanVideoTeaCache, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoEnhanceAVideo, Note, UpscaleModelLoader, Int, LoadWanVideoClipTextEncoder, WanVideoDecode, WanVideoVAELoader, ImageUpscaleWithModel, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoImageClipEncode, WanVideoTextEncode, WanVideoModelLoader, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/一键泄气特效-万相wan2.1新玩意_1899415692570181634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899415692570181634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `Note Plus (mtb)`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `Note`
- `UpscaleModelLoader`
- `Int`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageUpscaleWithModel`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`Note Plus (mtb)`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`UpscaleModelLoader`、`Int`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageUpscaleWithModel`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`WanVideoModelLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
