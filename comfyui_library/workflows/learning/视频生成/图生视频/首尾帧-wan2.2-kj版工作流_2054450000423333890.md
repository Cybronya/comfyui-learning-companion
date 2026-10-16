---
key: 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2054450000423333890.json
name: 首尾帧-wan2.2-kj版工作流_2054450000423333890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054450000423333890.json
hash: 6553263c6292aaab
coverage: 0.911765
learned_at: 2026-10-15 22:37:47
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, GetNode, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, Note, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, WanVideoLoraSelect, JWInteger, ImageLoader, ImageLoader, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2054450000423333890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054450000423333890.json`

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
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `WanVideoLoraSelect`
- `JWInteger`
- `ImageLoader`
- `ImageLoader`
- `WanVideoTextEncode`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`ImageLoader`、`WanVideoTextEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
