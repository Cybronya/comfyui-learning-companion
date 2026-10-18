---
key: 视频生成/图生视频/Wan2.2极速图生视频_1996499644534366210.json
name: Wan2.2极速图生视频_1996499644534366210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2极速图生视频_1996499644534366210.json
hash: 344d9af973b3675c
coverage: 0.848485
learned_at: 2026-10-15 22:33:26
nodes: [WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CreateCFGScheduleFloatList, Note, Note, PrimitiveNode, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, JWInteger, DF_Integer, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, VHS_VideoCombine, WanVideoSampler, GetImageSizeAndCount, ImageUpscaleWithModel, UpscaleModelLoader, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2极速图生视频_1996499644534366210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996499644534366210.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
- `Note`
- `Note`
- `PrimitiveNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `JWInteger`
- `DF_Integer`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `JjkText`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`JWInteger`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageUpscaleWithModel`、`UpscaleModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
