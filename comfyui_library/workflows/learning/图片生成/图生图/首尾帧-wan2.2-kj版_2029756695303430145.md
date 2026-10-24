---
key: 图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json
name: 首尾帧-wan2.2-kj版_2029756695303430145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json
hash: f95d9ad2fa787973
coverage: 1
learned_at: 2026-10-23 13:33:10
nodes: [LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, ImageLoader, ImageLoader, JWInteger, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
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
- `ImageLoader`
- `JWInteger`
- `WanVideoLoraSelect`
- `INTConstant`
- `JWInteger`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`ImageLoader`、`JWInteger`、`INTConstant`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`WanVideoTextEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
