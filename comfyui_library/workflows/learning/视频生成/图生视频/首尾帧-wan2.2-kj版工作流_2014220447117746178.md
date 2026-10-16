---
key: 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2014220447117746178.json
name: 首尾帧-wan2.2-kj版工作流_2014220447117746178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014220447117746178.json
hash: 598f8534a6da8adf
coverage: 0.911765
learned_at: 2026-10-15 22:34:34
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, GetNode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, Note, WanVideoTextEncode, ImageLoader, ImageLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2014220447117746178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014220447117746178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（34 个）：
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
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `Note`
- `WanVideoTextEncode`
- `ImageLoader`
- `ImageLoader`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`ImageLoader`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
