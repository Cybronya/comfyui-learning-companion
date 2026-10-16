---
key: 视频生成/图生视频/(KJ版4步版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1953756753928355841.json
name: (KJ版4步版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1953756753928355841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953756753928355841.json
hash: 5aa0f784130eeae9
coverage: 0.795918
learned_at: 2026-10-15 22:31:05
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, JWInteger, Note, Note, WanVideoModelLoader, GetImageSizeAndCount, ImageFromBatch+, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoTextEncode, CR Prompt Text, Note, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, WanVideoSampler, PrimitiveNode, ShowText|pysssss, TextConcat, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, easy showAnything, LoadImage, easy showAnything, JWStringConcat, WanVideoTorchCompileSettings, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_Captioner, RH_LLMAPI_NODE, CreateCFGScheduleFloatList, StringToFloatList, FloatToSigmas, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, INTConstant, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版4步版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1953756753928355841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953756753928355841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
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
- `LoadImage`
- `easy showAnything`
- `JWStringConcat`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `CreateCFGScheduleFloatList`
- `StringToFloatList`
- `FloatToSigmas`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **80%**（39/49）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`TextConcat`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`JWStringConcat`、`WanVideoTorchCompileSettings`、`Wan22PromptSelector`、`RH_Captioner`、`RH_LLMAPI_NODE`、`CreateCFGScheduleFloatList`、`StringToFloatList`、`FloatToSigmas`、`WanVideoLoraSelect`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
