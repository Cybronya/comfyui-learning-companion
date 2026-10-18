---
key: 视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json
name: wan2.2 图生视频工作量_1974850739472306178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json
hash: d839424ec283d36d
coverage: 0.631579
learned_at: 2026-10-15 22:32:06
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, PrimitiveNode, PrimitiveNode, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, WanVideoDecode, GetNode, GetImageSizeAndCount, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoImageToVideoEncode, WanVideoSampler, TrimVideoLatent, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974850739472306178.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `TrimVideoLatent`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **63%**（24/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoImageToVideoEncode`、`TrimVideoLatent`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、TrimVideoLatent
