---
key: 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json
name: 图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json
hash: b989492c57ed1cec
coverage: 0.939394
learned_at: 2026-10-15 22:37:09
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoTextEncode, ImageLoader, ImageLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048571694041800706.json`

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
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `ImageLoader`
- `ImageLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`ImageLoader`、`VHS_VideoCombine`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
