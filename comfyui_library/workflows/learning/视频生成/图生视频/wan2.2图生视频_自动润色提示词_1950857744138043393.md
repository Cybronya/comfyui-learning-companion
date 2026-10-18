---
key: 视频生成/图生视频/wan2.2图生视频_自动润色提示词_1950857744138043393.json
name: wan2.2图生视频_自动润色提示词_1950857744138043393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_自动润色提示词_1950857744138043393.json
hash: 475c197408d5093f
coverage: 0.947368
learned_at: 2026-10-15 22:30:56
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, JWInteger, PrimitiveNode, WanVideoSampler, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ImageFromBatch+, GetImageSizeAndCount, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, ShowText|pysssss, CR Text, CR Text Concatenate, RH_Captioner, CR Text, WanVideoImageToVideoEncode, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoScheduler, WanVideoScheduler, CreateCFGScheduleFloatList, INTConstant, Float, WanVideoSigmaToStep]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频_自动润色提示词_1950857744138043393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950857744138043393.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `JWInteger`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `CR Text`
- `CR Text Concatenate`
- `RH_Captioner`
- `CR Text`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `Float`
- `WanVideoSigmaToStep`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoSampler`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`ImageFromBatch+`、`GetImageSizeAndCount`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`CR Text`、`CR Text Concatenate`、`RH_Captioner`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`INTConstant`、`Float`、`WanVideoSigmaToStep`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
