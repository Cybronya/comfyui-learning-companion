---
key: 视频生成/图生视频/首尾帧-图生视频-Wan2.2_1962385933666488322.json
name: 首尾帧-图生视频-Wan2.2_1962385933666488322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962385933666488322.json
hash: 26e30d5ee7de6b57
coverage: 0.84375
learned_at: 2026-10-15 22:31:30
nodes: [WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, PrimitiveNode, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoSampler, LoadWanVideoT5TextEncoder, SimpleMath+, WanVideoSampler, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, Anything Everywhere, Anything Everywhere, WanVideoImageToVideoEncode, Anything Everywhere, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, JjkText, DF_Integer, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-图生视频-Wan2.2_1962385933666488322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962385933666488322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoImageToVideoEncode`
- `Anything Everywhere`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `JjkText`
- `DF_Integer`
- `WanVideoDecode`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`DF_Integer`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
