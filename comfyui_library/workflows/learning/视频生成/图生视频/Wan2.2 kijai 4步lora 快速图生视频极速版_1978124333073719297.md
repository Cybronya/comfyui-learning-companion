---
key: 视频生成/图生视频/Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json
name: Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978124333073719297.json
hash: 0e30f5dcce033c76
coverage: 0.974359
learned_at: 2026-10-15 22:32:18
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, WanVideoLoraSelect, WanVideoTorchCompileSettings, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, StringToFloatList, FloatToSigmas, INTConstant, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_VideoCombine, JWInteger, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), easy int, MathExpression|pysssss, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, Label (rgthree), WanVideoLoraSelect, LoadImage, WanVideoTextEncode, CR Prompt Text, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, GetImageSizeAndCount, ImageFromBatch+, WanVideoDecode, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978124333073719297.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `StringToFloatList`
- `FloatToSigmas`
- `INTConstant`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `JWInteger`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `easy int`
- `MathExpression|pysssss`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Label (rgthree)`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoDecode`
- `WanVideoVAELoader`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`StringToFloatList`、`FloatToSigmas`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`JWInteger`、`Label (rgthree)`、`easy int`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoDecode`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
