---
key: 视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json
name: 首尾帧视频 wan2.2_2018548235928870914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json
hash: 9f4cd316d1216d90
coverage: 0.939394
learned_at: 2026-10-15 22:34:58
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, GetNode, ImageLoader, ImageLoader, ImageResize+, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoTextEncode, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018548235928870914.json`

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
- `INTConstant`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `ImageLoader`
- `ImageLoader`
- `ImageResize+`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `JWInteger`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`ImageLoader`、`ImageResize+`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
