---
key: 视频生成/图生视频/Wan2.2极速图生视频_1993142430524440578.json
name: Wan2.2极速图生视频_1993142430524440578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2极速图生视频_1993142430524440578.json
hash: b686288025447c16
coverage: 0.823529
learned_at: 2026-10-15 22:33:17
nodes: [WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CreateCFGScheduleFloatList, JjkText, Note, Note, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, WanVideoSampler, GetImageSizeAndCount, ImageUpscaleWithModel, UpscaleModelLoader, PrimitiveNode, JWInteger, DF_Integer, VHS_VideoCombine, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2极速图生视频_1993142430524440578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993142430524440578.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
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
- `JjkText`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PrimitiveNode`
- `JWInteger`
- `DF_Integer`
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`GetImageSizeAndCount`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`JWInteger`、`DF_Integer`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
