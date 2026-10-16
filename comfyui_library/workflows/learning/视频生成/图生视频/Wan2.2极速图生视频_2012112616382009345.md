---
key: 视频生成/图生视频/Wan2.2极速图生视频_2012112616382009345.json
name: Wan2.2极速图生视频_2012112616382009345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2012112616382009345.json
hash: 6b67758440d3740d
coverage: 0.848485
learned_at: 2026-10-15 22:34:26
nodes: [WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CreateCFGScheduleFloatList, Note, PrimitiveNode, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, JWInteger, DF_Integer, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, VHS_VideoCombine, UpscaleModelLoader, LoadImage, JjkText, WanVideoSampler, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageUpscaleWithModel, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2极速图生视频_2012112616382009345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012112616382009345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
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
- `UpscaleModelLoader`
- `LoadImage`
- `JjkText`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModel`
- `Note`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelectMulti`、`JWInteger`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`VHS_VideoCombine`、`UpscaleModelLoader`、`LoadImage`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageUpscaleWithModel`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
