---
key: 视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1950823826609348610.json
name: (KJ版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1950823826609348610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950823826609348610.json
hash: ea54f78a8284829b
coverage: 0.787234
learned_at: 2026-10-15 22:30:56
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, WanVideoLoraSelect, JWInteger, Note, Note, WanVideoModelLoader, GetImageSizeAndCount, ImageFromBatch+, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text, Note, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, WanVideoSampler, PrimitiveNode, ShowText|pysssss, TextConcat, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, easy showAnything, WanVideoLoraSelect, LoadImage, easy showAnything, JWStringConcat, WanVideoTorchCompileSettings, CR Prompt Text, WanVideoSampler, Wan22PromptSelector, INTConstant, easy showAnything, RH_Captioner, RH_LLMAPI_NODE]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1950823826609348610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950823826609348610.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoLoraSelect`
- `JWInteger`
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
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Note`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `ShowText|pysssss`
- `TextConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `easy showAnything`
- `WanVideoLoraSelect`
- `LoadImage`
- `easy showAnything`
- `JWStringConcat`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `Wan22PromptSelector`
- `INTConstant`
- `easy showAnything`
- `RH_Captioner`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`TextConcat`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`JWStringConcat`、`WanVideoTorchCompileSettings`、`Wan22PromptSelector`、`RH_Captioner`、`RH_LLMAPI_NODE`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
