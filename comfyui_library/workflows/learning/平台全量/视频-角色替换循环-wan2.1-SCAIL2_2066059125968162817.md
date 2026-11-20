---
key: 平台全量/视频-角色替换循环-wan2.1-SCAIL2_2066059125968162817.json
name: 视频-角色替换循环-wan2.1-SCAIL2_2066059125968162817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-角色替换循环-wan2.1-SCAIL2_2066059125968162817.json
hash: 6a8869cb334c3bc6
coverage: 0.470199
learned_at: 2026-11-14 02:34:43
nodes: [CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Reroute, KSamplerSelect, SetNode, SetNode, ModelSamplingSD3, SetNode, SetNode, SetNode, SamplerCustom, GetNode, WanSCAILToVideo, SAM3_TrackToMask, EmptyImage, Reroute, SamplerCustom, PreviewAny, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, WanSCAILToVideo, Reroute, GetImageRangeFromBatch, ImageResizeKJv2, SAM3_VideoTrack, GetImageRangeFromBatch, GetImageRangeFromBatch, ImageConcatMulti, GetNode, ColorTransfer, GetImageSize, GetNode, SCAIL2ColoredMask, SetNode, GetImageSize, CLIPVisionLoader, BasicScheduler, CLIPTextEncode, SetNode, TensorLoopClose, BatchImagesNode, ComfyMathExpression, ResizeImageMaskNode, ImageConcatMulti, ImageConcatMulti, ImageConcatMulti, SetNode, GetImageRangeFromBatch, BatchImagesNode, Reroute, SamplerCustom, GetNode, GetNode, ImageCompositeMasked, ComfyMathExpression, ColorTransfer, VAEDecode, PreviewAny, VAELoader, CLIPLoader, CheckpointLoaderSimple, CLIPVisionEncode, GetImageSize, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, GetImageRangeFromBatch, Reroute, WanSCAILToVideo, PrimitiveInt, TensorLoopOpen, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, MathExpression|pysssss, CM_FloatToInt, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, VHS_VideoCombine, CLIPTextEncode, GetNode, Int, SAM3_VideoTrack, easy seed, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadImage, LoadImage, Int, Text, VHS_VideoCombine, RIFE VFI, MathExpression|pysssss, PrimitiveFloat, PrimitiveFloat]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 平台全量/视频-角色替换循环-wan2.1-SCAIL2_2066059125968162817.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-角色替换循环-wan2.1-SCAIL2_2066059125968162817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（151 个）：
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `WanSCAILToVideo`
- `SAM3_TrackToMask`
- `EmptyImage`
- `Reroute`
- `SamplerCustom` ★核心
- `PreviewAny`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetNode`
- `WanSCAILToVideo`
- `Reroute`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `SAM3_VideoTrack`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `GetNode`
- `ColorTransfer`
- `GetImageSize`
- `GetNode`
- `SCAIL2ColoredMask`
- `SetNode`
- `GetImageSize`
- `CLIPVisionLoader`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `SetNode`
- `TensorLoopClose`
- `BatchImagesNode`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `GetImageRangeFromBatch`
- `BatchImagesNode`
- `Reroute`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `ImageCompositeMasked`
- `ComfyMathExpression`
- `ColorTransfer`
- `VAEDecode` ★核心
- `PreviewAny`
- `VAELoader`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionEncode`
- `GetImageSize`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `Reroute`
- `WanSCAILToVideo`
- `PrimitiveInt`
- `TensorLoopOpen`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Int`
- `SAM3_VideoTrack`
- `easy seed`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `Int`
- `Text`
- `VHS_VideoCombine`
- `RIFE VFI`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `PrimitiveFloat`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **47%**（71/151）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`KSamplerSelect`、`ModelSamplingSD3`、`SamplerCustom`、`WanSCAILToVideo`、`SAM3_TrackToMask`、`EmptyImage`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`SAM3_VideoTrack`、`ImageConcatMulti`、`ColorTransfer`、`GetImageSize`、`SCAIL2ColoredMask`、`CLIPVisionLoader`、`BasicScheduler`、`TensorLoopClose`、`BatchImagesNode`、`ComfyMathExpression`、`ResizeImageMaskNode`、`ImageCompositeMasked`、`VAELoader`、`CLIPLoader`、`CheckpointLoaderSimple`、`CLIPVisionEncode`、`VHS_VideoCombine`、`TensorLoopOpen`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`MathExpression|pysssss`、`CM_FloatToInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`easy seed`、`VHS_LoadVideo`、`LoadImage`、`Text`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage
