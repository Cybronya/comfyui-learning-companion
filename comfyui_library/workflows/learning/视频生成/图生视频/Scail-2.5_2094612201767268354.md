---
key: 视频生成/图生视频/Scail-2.5_2094612201767268354.json
name: Scail-2.5_2094612201767268354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Scail-2.5_2094612201767268354.json
hash: 77e683f91db0d36c
coverage: 0.6
learned_at: 2026-10-17 00:02:35
nodes: [MathExpression|pysssss, VAEDecode, GetImageRangeFromBatch, SamplerCustom, LoraLoaderModelOnly, ColorTransfer, MathExpression|pysssss, SamplerCustom, MathExpression|pysssss, GetImageRangeFromBatch, SetNode, AutoCropFaces, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanSCAILToVideo, MathExpression|pysssss, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, VAELoader, MathExpression|pysssss, easy forLoopStart, Reroute, PreviewImage, SAM3_VideoTrack, GetNode, PrimitiveInt, SetNode, KSamplerSelect, GetNode, EmptyImage, SetNode, BatchImagesNode, BasicScheduler, MathExpression|pysssss, CLIPVisionEncode, PrimitiveInt, CLIPTextEncode, SetNode, SetNode, SetNode, GetNode, MathExpression|pysssss, CheckpointLoaderSimple, GetImageRangeFromBatch, VAEDecode, PrimitiveInt, GetNode, GetImageRangeFromBatch, ModelSamplingSD3, DiffusionModelLoaderKJ, ImageResizeKJv2, ImageCompositeMasked, GetImageSize, CLIPTextEncode, GetNode, GetNode, GetNode, SCAIL2ColoredMask, CLIPLoader, GetNode, Reroute, SetNode, MathExpression|pysssss, SetNode, Bjornulf_ShowInt, LoraLoaderModelOnly, CLIPVisionEncode, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, SetNode, DownloadAndLoadGIMMVFIModel, SetNode, GIMMVFI_interpolate, WanSCAILToVideo, CLIPVisionLoader, GetNode, PrimitiveInt, PrimitiveInt, GetNode, SAM3_TrackToMask, GetNode, MathExpression|pysssss, easy forLoopEnd, MathExpression|pysssss, SAM3_VideoTrack, SetNode, Reroute, MathExpression|pysssss, SetNode, GetNode, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio, GetImageSize, VHS_LoadVideo, CLIPTextEncode, VHS_VideoCombine, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/Scail-2.5_2094612201767268354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Scail-2.5_2094612201767268354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `ColorTransfer`
- `MathExpression|pysssss`
- `SamplerCustom` ★核心
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `SetNode`
- `AutoCropFaces`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanSCAILToVideo`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAELoader`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `Reroute`
- `PreviewImage`
- `SAM3_VideoTrack`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `EmptyImage`
- `SetNode`
- `BatchImagesNode`
- `BasicScheduler`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MathExpression|pysssss`
- `CheckpointLoaderSimple` ★核心
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `GetNode`
- `GetImageRangeFromBatch`
- `ModelSamplingSD3`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `ImageCompositeMasked`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SCAIL2ColoredMask`
- `CLIPLoader`
- `GetNode`
- `Reroute`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Bjornulf_ShowInt`
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `GIMMVFI_interpolate`
- `WanSCAILToVideo`
- `CLIPVisionLoader`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `SAM3_TrackToMask`
- `GetNode`
- `MathExpression|pysssss`
- `easy forLoopEnd`
- `MathExpression|pysssss`
- `SAM3_VideoTrack`
- `SetNode`
- `Reroute`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio`
- `GetImageSize`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **60%**（63/105）

**有卡**：`MathExpression|pysssss`、`VAEDecode`、`GetImageRangeFromBatch`、`SamplerCustom`、`LoraLoaderModelOnly`、`ColorTransfer`、`AutoCropFaces`、`WanSCAILToVideo`、`VAELoader`、`easy forLoopStart`、`SAM3_VideoTrack`、`KSamplerSelect`、`EmptyImage`、`BatchImagesNode`、`BasicScheduler`、`CLIPVisionEncode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`ModelSamplingSD3`、`DiffusionModelLoaderKJ`、`ImageResizeKJv2`、`ImageCompositeMasked`、`GetImageSize`、`SCAIL2ColoredMask`、`CLIPLoader`、`Bjornulf_ShowInt`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`CLIPVisionLoader`、`SAM3_TrackToMask`、`easy forLoopEnd`、`LayerUtility: ImageScaleByAspectRatio`、`VHS_LoadVideo`、`VHS_VideoCombine`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
