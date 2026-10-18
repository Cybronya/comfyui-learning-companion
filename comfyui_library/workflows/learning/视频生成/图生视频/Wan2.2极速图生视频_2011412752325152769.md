---
key: 视频生成/图生视频/Wan2.2极速图生视频_2011412752325152769.json
name: Wan2.2极速图生视频_2011412752325152769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2极速图生视频_2011412752325152769.json
hash: 898ba3252797acbb
coverage: 0.848485
learned_at: 2026-10-15 22:34:22
nodes: [WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CreateCFGScheduleFloatList, Note, Note, PrimitiveNode, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, JWInteger, DF_Integer, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, VHS_VideoCombine, WanVideoSampler, GetImageSizeAndCount, ImageUpscaleWithModel, UpscaleModelLoader, JjkText, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2极速图生视频_2011412752325152769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011412752325152769.json`

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
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
- `Note`
- `Note`
- `PrimitiveNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
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
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelectMulti`、`JWInteger`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`VHS_VideoCombine`、`WanVideoSampler`、`GetImageSizeAndCount`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
