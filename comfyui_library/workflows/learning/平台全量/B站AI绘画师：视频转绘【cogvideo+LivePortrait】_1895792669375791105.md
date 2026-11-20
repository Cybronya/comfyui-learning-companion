---
key: 平台全量/B站AI绘画师：视频转绘【cogvideo+LivePortrait】_1895792669375791105.json
name: B站AI绘画师：视频转绘【cogvideo+LivePortrait】_1895792669375791105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/B站AI绘画师：视频转绘【cogvideo+LivePortrait】_1895792669375791105.json
hash: 0c3912960216fdd4
coverage: 0.754098
learned_at: 2026-11-14 00:21:27
nodes: [easy cleanGpuUsed, LayerUtility: PurgeVRAM, CogVideoImageEncode, PreviewImage, easy showAnything, easy showAnything, GetImageSizeAndCount, easy showAnything, easy cleanGpuUsed, PreviewImage, CM_IntToFloat, easy showAnything, easy showAnything, easy showAnything, VHS_VideoInfoLoaded, CogVideoDecode, CogVideoTextEncode, CogVideoSampler, LayerUtility: PurgeVRAM, VHS_VideoCombine, INTConstant, Int Literal, ImageResizeKJ, ImageResizeKJ, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, easy showAnything, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, easy showAnything, ImageConcatMulti, INTConstant, CM_IntToFloat, CR Upscale Image, ImageResizeKJ, VHS_LoadVideo, DownloadAndLoadCogVideoModel, CLIPLoader, AIO_Preprocessor, CogVideoTextEncode, VHS_VideoCombine, CogVideoLoraSelect, TeaCacheForCogVideoX, Int Literal, CogVideoContextOptions, PreviewImage, INTConstant, VHS_VideoCombine, FaceRestoreModelLoader, VHS_LoadVideo, Int Literal, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, FaceRestoreCFWithModel, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: []
---

# 平台全量/B站AI绘画师：视频转绘【cogvideo+LivePortrait】_1895792669375791105.json

> 来源文件 `comfyui_library/workflows/平台全量/B站AI绘画师：视频转绘【cogvideo+LivePortrait】_1895792669375791105.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `CogVideoImageEncode`
- `PreviewImage`
- `easy showAnything`
- `easy showAnything`
- `GetImageSizeAndCount`
- `easy showAnything`
- `easy cleanGpuUsed`
- `PreviewImage`
- `CM_IntToFloat`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `CogVideoDecode`
- `CogVideoTextEncode`
- `CogVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `INTConstant`
- `Int Literal`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ImageConcatMulti`
- `INTConstant`
- `CM_IntToFloat`
- `CR Upscale Image`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `DownloadAndLoadCogVideoModel`
- `CLIPLoader`
- `AIO_Preprocessor`
- `CogVideoTextEncode`
- `VHS_VideoCombine`
- `CogVideoLoraSelect`
- `TeaCacheForCogVideoX`
- `Int Literal`
- `CogVideoContextOptions`
- `PreviewImage`
- `INTConstant`
- `VHS_VideoCombine`
- `FaceRestoreModelLoader`
- `VHS_LoadVideo`
- `Int Literal`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FaceRestoreCFWithModel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`

## 知识

覆盖率 **75%**（46/61）

**有卡**：`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`CogVideoImageEncode`、`GetImageSizeAndCount`、`CM_IntToFloat`、`VHS_VideoInfoLoaded`、`CogVideoDecode`、`CogVideoTextEncode`、`CogVideoSampler`、`VHS_VideoCombine`、`INTConstant`、`Int Literal`、`ImageResizeKJ`、`ImageConcatMulti`、`CR Upscale Image`、`VHS_LoadVideo`、`DownloadAndLoadCogVideoModel`、`CLIPLoader`、`AIO_Preprocessor`、`CogVideoLoraSelect`、`TeaCacheForCogVideoX`、`CogVideoContextOptions`、`FaceRestoreModelLoader`、`FaceRestoreCFWithModel`、`RHHiddenNodes`

**用到的条目**：CLIPLoader、CogVideoSampler、CogVideoDecode、CogVideoImageEncode、CogVideoTextEncode、CogVideoLoraSelect、CR Upscale Image、GetImageSizeAndCount
