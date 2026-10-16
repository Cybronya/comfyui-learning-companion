---
key: 视频生成/图生视频/图生视频（Wan2.2-V2）高动态加速版_1956567836586070018.json
name: 图生视频（Wan2.2-V2）高动态加速版_1956567836586070018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956567836586070018.json
hash: 6b591998f408773b
coverage: 0.888889
learned_at: 2026-10-15 22:31:14
nodes: [JWInteger, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_Captioner, CR Prompt Text, easy showAnything, TextConcat, ShowText|pysssss, JWStringConcat, RH_LLMAPI_NODE, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoVAELoader, JWInteger, WanVideoImageToVideoEncode, PrimitiveNode, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, GetImageSizeAndCount, WanVideoSetLoRAs, ImageFromBatch+, CR Prompt Text, LoadImage, VHS_VideoCombine, WanVideoSampler, FloatToSigmas, StringToFloatList, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频（Wan2.2-V2）高动态加速版_1956567836586070018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956567836586070018.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `JWInteger`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `RH_Captioner`
- `CR Prompt Text`
- `easy showAnything`
- `TextConcat`
- `ShowText|pysssss`
- `JWStringConcat`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `CR Prompt Text`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `FloatToSigmas`
- `StringToFloatList`
- `CR Prompt Text`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`JWInteger`、`CR Prompt Text`、`Wan22PromptSelector`、`RH_Captioner`、`TextConcat`、`JWStringConcat`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`INTConstant`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageFromBatch+`、`LoadImage`、`VHS_VideoCombine`、`FloatToSigmas`、`StringToFloatList`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
