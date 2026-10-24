---
key: 图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json
name: 首尾帧-wan2.2版工作流_2033445320134238210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json
hash: a7f8b7190fcf68c8
coverage: 0.931034
learned_at: 2026-10-23 13:33:10
nodes: [WanVideoClipVisionEncode, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, JWInteger, WanVideoTextEncode, ImageLoader, ImageResize+, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoDecode, SetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoClipVisionEncode`
- `INTConstant`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoTextEncode`
- `ImageLoader`
- `ImageResize+`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `SetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`WanVideoClipVisionEncode`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`ImageLoader`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
