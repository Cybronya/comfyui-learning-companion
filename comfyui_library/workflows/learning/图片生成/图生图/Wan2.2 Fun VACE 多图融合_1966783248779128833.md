---
key: 图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json
name: Wan2.2 Fun VACE 多图融合_1966783248779128833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json
hash: 21c8f18a5fa3562b
coverage: 0.783333
learned_at: 2026-10-23 11:27:59
nodes: [LoadImage, JWInteger, LoadImage, ImageConcanate, LayerUtility: ImageRemoveAlpha, InspyrenetRembg, JWInteger, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, CR Text, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoVACEModelSelect, ImpactSwitch, Note, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, PrimitiveNode, PrimitiveNode, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSampler, CR Text, WanVideoTextEncodeCached, RH_LLMAPI_NODE, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, ImageConcanate, WanVideoVACEEncode, GetNode, JWInteger, MathExpression|pysssss, WanVideoScheduler, WanVideoSigmaToStep, GetNode, GetImageSizeAndCount, EmptyImage, WanVideoDecode, WanVideoSampler, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, SetNode, WanVideoBlockSwap, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, PreviewImage, JWInteger]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（60 个）：
- `LoadImage`
- `JWInteger`
- `LoadImage`
- `ImageConcanate`
- `LayerUtility: ImageRemoveAlpha`
- `InspyrenetRembg`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `CR Text`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `ImpactSwitch`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `CR Text`
- `WanVideoTextEncodeCached`
- `RH_LLMAPI_NODE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `ImageConcanate`
- `WanVideoVACEEncode`
- `GetNode`
- `JWInteger`
- `MathExpression|pysssss`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `GetNode`
- `GetImageSizeAndCount`
- `EmptyImage`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoBlockSwap`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `JWInteger`

## 知识

覆盖率 **78%**（47/60）

**有卡**：`LoadImage`、`JWInteger`、`ImageConcanate`、`LayerUtility: ImageRemoveAlpha`、`InspyrenetRembg`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`CR Text`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`WanVideoVACEEncode`、`MathExpression|pysssss`、`WanVideoSigmaToStep`、`GetImageSizeAndCount`、`EmptyImage`、`WanVideoDecode`、`AddLabel`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`ImageResizeKJv2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
