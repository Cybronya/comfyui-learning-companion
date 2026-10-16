---
key: 视频生成/图生视频/Wan2.2 Fun VACE 姿势深度参考转绘_1966804556082556930.json
name: Wan2.2 Fun VACE 姿势深度参考转绘_1966804556082556930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966804556082556930.json
hash: b134fb1b3f6f7b9f
coverage: 0.724138
learned_at: 2026-10-15 22:31:39
nodes: [LayerUtility: ImageScaleByAspectRatio V2, JWInteger, Primitive integer [Crystools], WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, SetNode, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, AIO_Preprocessor, SetNode, SetNode, GetNode, GetNode, AddLabel, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, WanVideoSampler, JWInteger, GetNode, WanVideoTextEncodeCached, GetNode, SetNode, CR Text, VHS_VideoCombine, WanVideoVACEEncode, LoadImage, PreviewImage, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, ImpactSwitch, VHS_VideoCombine, ImageResizeKJ, WanVideoScheduler, VHS_VideoInfo, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun VACE 姿势深度参考转绘_1966804556082556930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966804556082556930.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
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
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `AIO_Preprocessor`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `JWInteger`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `CR Text`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `LoadImage`
- `PreviewImage`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoScheduler`
- `VHS_VideoInfo`
- `VHS_LoadVideo`

## 知识

覆盖率 **72%**（42/58）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`Primitive integer [Crystools]`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`AIO_Preprocessor`、`AddLabel`、`EmptyImage`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`CR Text`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`LoadImage`、`ImageResizeKJ`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader
