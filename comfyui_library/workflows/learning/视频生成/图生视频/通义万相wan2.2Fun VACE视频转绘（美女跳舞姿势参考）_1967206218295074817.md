---
key: 视频生成/图生视频/通义万相wan2.2Fun VACE视频转绘（美女跳舞姿势参考）_1967206218295074817.json
name: 通义万相wan2.2Fun VACE视频转绘（美女跳舞姿势参考）_1967206218295074817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相wan2.2Fun VACE视频转绘（美女跳舞姿势参考）_1967206218295074817.json
hash: 3afd8864504da6c3
coverage: 0.719298
learned_at: 2026-10-15 22:31:40
nodes: [JWInteger, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, AIO_Preprocessor, SetNode, GetNode, GetNode, AddLabel, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, SetNode, WanVideoSampler, ImpactSwitch, VHS_VideoCombine, WanVideoScheduler, VHS_LoadVideo, VHS_VideoInfo, JWInteger, CR Text, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncodeCached, WanVideoVACEEncode, GetNode, SetNode, GetImageSizeAndCount, ImageResizeKJ, GetNode, WanVideoSampler, GetNode, SetNode, WanVideoVACEModelSelect, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相wan2.2Fun VACE视频转绘（美女跳舞姿势参考）_1967206218295074817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967206218295074817.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（57 个）：
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `AIO_Preprocessor`
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
- `SetNode`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `JWInteger`
- `CR Text`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **72%**（41/57）

**有卡**：`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`AIO_Preprocessor`、`AddLabel`、`EmptyImage`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`VHS_VideoInfo`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`ImageResizeKJ`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader
