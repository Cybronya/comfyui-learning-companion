---
key: 平台全量/视频-动作迁移-wan2.1-SteadDancer-KJ_1996877542743322625.json
name: 视频-动作迁移-wan2.1-SteadDancer-KJ_1996877542743322625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作迁移-wan2.1-SteadDancer-KJ_1996877542743322625.json
hash: 02d27bf93c8b61a1
coverage: 0.606838
learned_at: 2026-11-14 02:34:07
nodes: [PreviewImage, PreviewImage, ImageFromBatch+, VHS_VideoInfoLoaded, SetNode, Reroute, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, SetNode, Reroute, GetImageSizeAndCount, SetNode, Florence2Run, GetNode, easy showAnything, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, ShowText|pysssss, PreviewImage, SetNode, GetNode, GetNode, GetNode, PreviewImage, GetNode, GetNode, GetImageSizeAndCount, easy seed, SetNode, StringFunction|pysssss, ImageFromBatch+, PreviewImage, ImageResizeKJ, GetNode, ImageFromBatch, SetNode, ImageFromBatch, Florence2ModelLoader, SetNode, GetImageSizeAndCount, VHS_VideoCombine, SetNode, LoadImage, easy int, easy positive, WanVideoSetBlockSwap, WanVideoEncode, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoSamplerFromSettings, PrimitiveNode, PrimitiveNode, WanVideoVAELoader, WanVideoContextOptions, WanVideoLoraSelect, Note, WanVideoClipVisionEncode, GetNode, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, WanVideoSamplerSettings, GetNode, WanVideoDecode, Reroute, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetNode, MemoryCleaner, WanVideoModelLoader, SetNode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, GetImageSizeAndCount, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, GetImageRangeFromBatch, ImageFromBatch, GetImageSizeAndCount, AIO_Preprocessor, ImageResizeKJ, GetNode, GetImageSizeAndCount, GetNode, VHS_VideoCombine, GetImageSizeAndCount, WanVideoAddSteadyDancerEmbeds, SetNode, WanVideoScheduler, easy int, easy anythingIndexSwitch, GetImageSizeAndCount, WanVideoBlockSwap, VHS_LoadVideo, CM_IntToFloat, INTConstant, MathExpression|pysssss, VHS_VideoCombine, GetImageSizeAndCount, GetImageSizeAndCount, ImageResizeKJ, GetImageSizeAndCount, GetImageSizeAndCount, easy int, PoseDetectionOneToAllAnimation, OnnxDetectionModelLoader]
patterns: []
missing: []
---

# 平台全量/视频-动作迁移-wan2.1-SteadDancer-KJ_1996877542743322625.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作迁移-wan2.1-SteadDancer-KJ_1996877542743322625.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（117 个）：
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch+`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetImageSizeAndCount`
- `SetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `SetNode`
- `Florence2Run`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `ShowText|pysssss`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy seed`
- `SetNode`
- `StringFunction|pysssss`
- `ImageFromBatch+`
- `PreviewImage`
- `ImageResizeKJ`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `ImageFromBatch`
- `Florence2ModelLoader`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `easy int`
- `easy positive`
- `WanVideoSetBlockSwap`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoSamplerFromSettings` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `WanVideoSamplerSettings` ★核心
- `GetNode`
- `WanVideoDecode`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `MemoryCleaner`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `GetImageRangeFromBatch`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoAddSteadyDancerEmbeds`
- `SetNode`
- `WanVideoScheduler`
- `easy int`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `CM_IntToFloat`
- `INTConstant`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy int`
- `PoseDetectionOneToAllAnimation`
- `OnnxDetectionModelLoader`

## 知识

覆盖率 **61%**（71/117）

**有卡**：`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ImageConcanate`、`GetImageSizeAndCount`、`Florence2Run`、`easy seed`、`StringFunction|pysssss`、`ImageResizeKJ`、`ImageFromBatch`、`Florence2ModelLoader`、`LoadImage`、`easy int`、`easy positive`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`WanVideoSamplerFromSettings`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSamplerSettings`、`WanVideoDecode`、`MemoryCleaner`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`GetImageRangeFromBatch`、`AIO_Preprocessor`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoScheduler`、`easy anythingIndexSwitch`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`CM_IntToFloat`、`INTConstant`、`MathExpression|pysssss`、`PoseDetectionOneToAllAnimation`、`OnnxDetectionModelLoader`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、easy seed、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
