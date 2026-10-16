---
key: 视频生成/图生视频/（贞贞版）Wan2.2 Fun Vace多参实验版V1_1966685974740807681.json
name: （贞贞版）Wan2.2 Fun Vace多参实验版V1_1966685974740807681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966685974740807681.json
hash: bfc5ee718c6be222
coverage: 0.913793
learned_at: 2026-10-15 22:31:39
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, ImageConcatMulti, WanVideoBlockSwap, WanVideoVAELoader, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoLoraSelect, INTConstant, WanVideoSigmaToStep, Float, WanVideoSampler, WanVideoTorchCompileSettings, Note, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, GetImageSizeAndCount, WanVideoExperimentalArgs, WanVideoScheduler, WanVideoScheduler, VHS_VideoCombine, WanVideoModelLoader, WanVideoExtraModelSelect, StringToFloatList, StringToFloatList, WanVideoTextEncode, WanVideoSetLoRAs, Text Concatenate, JWInteger, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, ShowText, WanVideoSampler, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, WanVideoVACEEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, ImageFromBatch+, ImageRepeat, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, LoadImage, LoadImage, CR Prompt Text, RH_Captioner, RH_Captioner, PreviewImage, RepeatImageBatch, WanVideoVACEStartToEndFrame, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/（贞贞版）Wan2.2 Fun Vace多参实验版V1_1966685974740807681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966685974740807681.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `GetImageSizeAndCount`
- `WanVideoExperimentalArgs`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `StringToFloatList`
- `StringToFloatList`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `Text Concatenate`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `ShowText`
- `WanVideoSampler` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `WanVideoVACEEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageRepeat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `RH_Captioner`
- `RH_Captioner`
- `PreviewImage`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`

## 知识

覆盖率 **91%**（53/58）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`WanVideoExperimentalArgs`、`WanVideoScheduler`、`VHS_VideoCombine`、`StringToFloatList`、`WanVideoTextEncode`、`Text Concatenate`、`JWInteger`、`ShowText`、`WanVideoVACEEncode`、`WanVideoDecode`、`ImageFromBatch+`、`ImageRepeat`、`LoadImage`、`CR Prompt Text`、`RH_Captioner`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
