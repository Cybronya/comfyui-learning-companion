---
key: 视频生成/图生视频/Wan2.2极速图生视频_1994312738337914882.json
name: Wan2.2极速图生视频_1994312738337914882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2极速图生视频_1994312738337914882.json
hash: 56f0a6721a3011ec
coverage: 0.83871
learned_at: 2026-10-15 22:33:20
nodes: [WanVideoBlockSwap, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, GetImageSizeAndCount, WanVideoLoraSelectMulti, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Note, Note, JWInteger, DF_Integer, PrimitiveNode, Note, LoadImage, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2极速图生视频_1994312738337914882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994312738337914882.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoBlockSwap`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `JWInteger`
- `DF_Integer`
- `PrimitiveNode`
- `Note`
- `LoadImage`
- `JjkText`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVideoBlockSwap`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`JWInteger`、`DF_Integer`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
