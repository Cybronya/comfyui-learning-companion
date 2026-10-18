---
key: 视频生成/图生视频/Wan2.2 6步差异模型Sigma调度3迭代图生视频动态加速版V3_1956010463471566849.json
name: Wan2.2 6步差异模型Sigma调度3迭代图生视频动态加速版V3_1956010463471566849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 6步差异模型Sigma调度3迭代图生视频动态加速版V3_1956010463471566849.json
hash: 328d221ed11b9cc9
coverage: 0.813559
learned_at: 2026-10-15 22:31:11
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, JWInteger, Note, Note, WanVideoModelLoader, ImageFromBatch+, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoTextEncode, CR Prompt Text, Note, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, TextConcat, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, easy showAnything, LoadImage, easy showAnything, JWStringConcat, WanVideoTorchCompileSettings, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_Captioner, RH_LLMAPI_NODE, FloatToSigmas, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, INTConstant, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, PrimitiveNode, ImageFromBatch+, WanVideoSetLoRAs, GetImageSizeAndCount, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, LoadVideo, ShowText|pysssss, WanVideoSetBlockSwap, WanVideoSetLoRAs, StringToFloatList, Note, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 6步差异模型Sigma调度3迭代图生视频动态加速版V3_1956010463471566849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956010463471566849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `JWInteger`
- `Note`
- `Note`
- `WanVideoModelLoader`
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
- `FloatToSigmas`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `ImageFromBatch+`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadVideo`
- `ShowText|pysssss`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `StringToFloatList`
- `Note`
- `CR Prompt Text`

## 知识

覆盖率 **81%**（48/59）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoModelLoader`、`ImageFromBatch+`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`TextConcat`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`JWStringConcat`、`WanVideoTorchCompileSettings`、`Wan22PromptSelector`、`RH_Captioner`、`RH_LLMAPI_NODE`、`FloatToSigmas`、`WanVideoDecode`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadVideo`、`StringToFloatList`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
