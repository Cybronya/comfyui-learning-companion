---
key: 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1911140460969062401.json
name: 万相WAN2.1，美女一键跳舞！_1911140460969062401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1911140460969062401.json
hash: c9d4bdda710db8d6
coverage: 1
learned_at: 2026-10-15 22:29:30
nodes: [LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, LoadImage, LayerUtility: PurgeVRAM, WanVideoImageClipEncode, Note Plus (mtb), ImageUpscaleWithModel, WanVideoTextEncode, UpscaleModelLoader, WanVideoTeaCache]
patterns: []
missing: []
---

# 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1911140460969062401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911140460969062401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（18 个）：
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `WanVideoImageClipEncode`
- `Note Plus (mtb)`
- `ImageUpscaleWithModel`
- `WanVideoTextEncode`
- `UpscaleModelLoader`
- `WanVideoTeaCache`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadImage`、`LayerUtility: PurgeVRAM`、`WanVideoImageClipEncode`、`Note Plus (mtb)`、`ImageUpscaleWithModel`、`WanVideoTextEncode`、`UpscaleModelLoader`、`WanVideoTeaCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
