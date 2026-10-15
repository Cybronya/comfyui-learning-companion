---
key: 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json
name: 首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json
hash: e483cdb6cf7e19fd
coverage: 0.967742
learned_at: 2026-10-15 22:49:07
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, ImageLoader, ImageLoader, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, SetNode, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
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
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `ImageLoader`
- `ImageLoader`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `SetNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`ImageLoader`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
