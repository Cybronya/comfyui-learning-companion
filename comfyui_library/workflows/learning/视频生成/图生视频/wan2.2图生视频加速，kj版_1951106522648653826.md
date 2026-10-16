---
key: 视频生成/图生视频/wan2.2图生视频加速，kj版_1951106522648653826.json
name: wan2.2图生视频加速，kj版_1951106522648653826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951106522648653826.json
hash: 0841c3c0f9a7226f
coverage: 0.857143
learned_at: 2026-10-15 22:30:57
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, Note, Note, Note, WanVideoModelLoader, GetImageSizeAndCount, ImageFromBatch+, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, PrimitiveNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncode, INTConstant, CreateCFGScheduleFloatList, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频加速，kj版_1951106522648653826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951106522648653826.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoModelLoader`
- `Note`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
