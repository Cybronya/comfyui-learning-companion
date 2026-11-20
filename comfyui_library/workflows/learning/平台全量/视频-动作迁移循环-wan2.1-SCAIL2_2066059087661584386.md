---
key: 平台全量/视频-动作迁移循环-wan2.1-SCAIL2_2066059087661584386.json
name: 视频-动作迁移循环-wan2.1-SCAIL2_2066059087661584386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作迁移循环-wan2.1-SCAIL2_2066059087661584386.json
hash: a23464209be7c80a
coverage: 0.450331
learned_at: 2026-11-14 02:34:13
nodes: [SAM3_VideoTrack, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Reroute, KSamplerSelect, SetNode, SetNode, ModelSamplingSD3, SetNode, SetNode, SetNode, GetNode, SAM3_TrackToMask, EmptyImage, Reroute, PreviewAny, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, GetNode, Reroute, Reroute, SAM3_VideoTrack, GetImageSize, ColorTransfer, GetImageSize, GetNode, SetNode, GetImageSize, BasicScheduler, CLIPTextEncode, BatchImagesNode, GetImageRangeFromBatch, PrimitiveInt, ComfyMathExpression, CLIPLoader, ImageCompositeMasked, CheckpointLoaderSimple, CLIPVisionLoader, VAELoader, CLIPVisionEncode, Reroute, VHS_VideoCombine, PreviewImage, GetNode, GetNode, Reroute, GetNode, GetImageRangeFromBatch, GetNode, ColorTransfer, BatchImagesNode, VAEDecode, SamplerCustom, SamplerCustom, GetNode, TensorLoopClose, SCAIL2ColoredMask, WanSCAILToVideo, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, WanSCAILToVideo, WanSCAILToVideo, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, Text, VHS_VideoCombine, TensorLoopOpen, Reroute, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, GetImageRangeFromBatch, GetImageRangeFromBatch, ImageConcatMulti, ImageConcatMulti, ImageConcatMulti, GetNode, SetNode, SetNode, GetNode, GetNode, ResizeImageMaskNode, GetNode, LoadImage, Int, Int, VHS_LoadVideo, easy seed, SamplerCustom, ComfyMathExpression, PreviewAny, GetNode, PrimitiveFloat, MathExpression|pysssss, RIFE VFI, MathExpression|pysssss, VHS_VideoCombine, CM_FloatToInt, PrimitiveFloat]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 平台全量/视频-动作迁移循环-wan2.1-SCAIL2_2066059087661584386.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作迁移循环-wan2.1-SCAIL2_2066059087661584386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（151 个）：
- `SAM3_VideoTrack`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `GetNode`
- `SAM3_TrackToMask`
- `EmptyImage`
- `Reroute`
- `PreviewAny`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetNode`
- `Reroute`
- `Reroute`
- `SAM3_VideoTrack`
- `GetImageSize`
- `ColorTransfer`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `BatchImagesNode`
- `GetImageRangeFromBatch`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CLIPLoader`
- `ImageCompositeMasked`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `Reroute`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ColorTransfer`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `GetNode`
- `TensorLoopClose`
- `SCAIL2ColoredMask`
- `WanSCAILToVideo`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `WanSCAILToVideo`
- `WanSCAILToVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `Text`
- `VHS_VideoCombine`
- `TensorLoopOpen`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `LoadImage`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `easy seed`
- `SamplerCustom` ★核心
- `ComfyMathExpression`
- `PreviewAny`
- `GetNode`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `RIFE VFI`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `CM_FloatToInt`
- `PrimitiveFloat`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **45%**（68/151）

**有卡**：`SAM3_VideoTrack`、`VAEDecode`、`KSamplerSelect`、`ModelSamplingSD3`、`SAM3_TrackToMask`、`EmptyImage`、`GetImageRangeFromBatch`、`GetImageSize`、`ColorTransfer`、`BasicScheduler`、`CLIPTextEncode`、`BatchImagesNode`、`ComfyMathExpression`、`CLIPLoader`、`ImageCompositeMasked`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`VHS_VideoCombine`、`SamplerCustom`、`TensorLoopClose`、`SCAIL2ColoredMask`、`WanSCAILToVideo`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text`、`TensorLoopOpen`、`ImageConcatMulti`、`ResizeImageMaskNode`、`LoadImage`、`Int`、`VHS_LoadVideo`、`easy seed`、`MathExpression|pysssss`、`RIFE VFI`、`CM_FloatToInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage
