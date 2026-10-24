---
key: 图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json
name: 首尾帧-wan2.2-kj版_1988497426770214913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json
hash: 8ce06edc0e042b0a
coverage: 1
learned_at: 2026-10-23 13:33:09
nodes: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, ImageLoader, ImageResize+, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageLoader`
- `ImageResize+`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `WanVideoLoraSelect`
- `INTConstant`
- `JWInteger`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`ImageLoader`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`INTConstant`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
