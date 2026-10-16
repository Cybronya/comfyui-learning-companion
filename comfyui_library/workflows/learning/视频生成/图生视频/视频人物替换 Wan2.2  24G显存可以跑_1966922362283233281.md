---
key: 视频生成/图生视频/视频人物替换 Wan2.2  24G显存可以跑_1966922362283233281.json
name: 视频人物替换 Wan2.2  24G显存可以跑_1966922362283233281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966922362283233281.json
hash: 600c4de2cc51026e
coverage: 0.703704
learned_at: 2026-10-15 22:31:40
nodes: [JWInteger, Primitive integer [Crystools], WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, SetNode, DepthAnything_V2, SetNode, SetNode, SetNode, GetImageSizeAndCount, ImageResizeKJ, WanVideoScheduler, VHS_VideoInfo, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, WanVideoTextEncodeCached, easy cleanGpuUsed, WanVideoVACEEncode, CreateCFGScheduleFloatList, WanVideoScheduler, ImpactSwitch, AIO_Preprocessor, WanVideoSampler, WanVideoDecode, GetNode, LoadImage, PreviewImage, CR Text, VHS_VideoCombine, JWInteger, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, GetNode, DownloadAndLoadDepthAnythingV2Model, WanVideoModelLoader, GetNode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, VHS_VideoCombine, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/视频人物替换 Wan2.2  24G显存可以跑_1966922362283233281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966922362283233281.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `JWInteger`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `DepthAnything_V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `WanVideoScheduler`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoTextEncodeCached`
- `easy cleanGpuUsed`
- `WanVideoVACEEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoScheduler`
- `ImpactSwitch`
- `AIO_Preprocessor`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `CR Text`
- `VHS_VideoCombine`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `DownloadAndLoadDepthAnythingV2Model`
- `WanVideoModelLoader`
- `GetNode`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **70%**（38/54）

**有卡**：`JWInteger`、`Primitive integer [Crystools]`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoSigmaToStep`、`DepthAnything_V2`、`GetImageSizeAndCount`、`ImageResizeKJ`、`WanVideoScheduler`、`VHS_VideoInfo`、`easy cleanGpuUsed`、`WanVideoTextEncodeCached`、`WanVideoVACEEncode`、`CreateCFGScheduleFloatList`、`AIO_Preprocessor`、`WanVideoSampler`、`WanVideoDecode`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`DownloadAndLoadDepthAnythingV2Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader
