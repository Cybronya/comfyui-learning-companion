---
key: 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json
name: 首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json
hash: 32410ca284c4797e
coverage: 0.939394
learned_at: 2026-10-26 02:06:02
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoTextEncode, GetNode, VHS_VideoCombine, ImageLoader, ImageLoader]
patterns: []
missing: []
---

# 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageLoader`
- `ImageLoader`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`ImageLoader`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
