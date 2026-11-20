---
key: 平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json
name: Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json
hash: 32de5e24064b402c
coverage: 0.724138
learned_at: 2026-11-14 01:06:06
nodes: [Primitive integer [Crystools], WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoSetBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, SetNode, AIO_Preprocessor, GetNode, GetNode, AddLabel, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, WanVideoSampler, GetNode, WanVideoTextEncodeCached, GetNode, SetNode, WanVideoVACEEncode, PreviewImage, WanVideoSampler, WanVideoScheduler, WanVideoModelLoader, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, VHS_VideoCombine, ImpactSwitch, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, GetImageSizeAndCount, SetNode, SetNode, JWInteger, CR Text, JWInteger, LoadImage, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `Primitive integer [Crystools]`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `WanVideoVACEEncode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `JWInteger`
- `CR Text`
- `JWInteger`
- `LoadImage`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **72%**（42/58）

**有卡**：`Primitive integer [Crystools]`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`AIO_Preprocessor`、`AddLabel`、`EmptyImage`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`WanVideoDecode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`VHS_VideoCombine`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`JWInteger`、`CR Text`、`LoadImage`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached
