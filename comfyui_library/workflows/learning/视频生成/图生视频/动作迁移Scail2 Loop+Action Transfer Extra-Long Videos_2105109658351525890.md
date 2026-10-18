---
key: 视频生成/图生视频/动作迁移Scail2 Loop+Action Transfer Extra-Long Videos_2105109658351525890.json
name: 动作迁移Scail2 Loop+Action Transfer Extra-Long Videos_2105109658351525890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移Scail2 Loop+Action Transfer Extra-Long Videos_2105109658351525890.json
hash: 757dd33163170f34
coverage: 0.439189
learned_at: 2026-10-17 22:19:40
nodes: [SAM3_VideoTrack, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, SAM3_TrackToMask, EmptyImage, Reroute, SetNode, SetNode, PreviewAny, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, GetNode, Reroute, Reroute, SAM3_VideoTrack, GetImageRangeFromBatch, GetNode, GetImageSize, GetImageRangeFromBatch, ImageConcatMulti, GetNode, ColorTransfer, GetImageSize, GetNode, SetNode, GetImageSize, CLIPTextEncode, BatchImagesNode, ResizeImageMaskNode, ImageConcatMulti, ImageConcatMulti, SetNode, GetImageRangeFromBatch, SamplerCustom, ComfyMathExpression, CLIPLoader, ImageCompositeMasked, CheckpointLoaderSimple, CLIPVisionLoader, VAELoader, CLIPVisionEncode, Reroute, VHS_VideoCombine, SetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, ImageConcatMulti, ComfyMathExpression, PreviewAny, GetNode, GetImageRangeFromBatch, GetNode, ColorTransfer, BatchImagesNode, SamplerCustom, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, SamplerCustom, GetNode, VHS_VideoCombine, TensorLoopClose, TensorLoopOpen, SCAIL2ColoredMask, WanSCAILToVideo, GetNode, GetNode, WanSCAILToVideo, WanSCAILToVideo, VAEDecode, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, BasicScheduler, KSamplerSelect, SetNode, SetNode, SetNode, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, VHS_LoadVideo, PrimitiveInt, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/动作迁移Scail2 Loop+Action Transfer Extra-Long Videos_2105109658351525890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移Scail2 Loop+Action Transfer Extra-Long Videos_2105109658351525890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（148 个）：
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
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
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SAM3_TrackToMask`
- `EmptyImage`
- `Reroute`
- `SetNode`
- `SetNode`
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
- `GetImageRangeFromBatch`
- `GetNode`
- `GetImageSize`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `GetNode`
- `ColorTransfer`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `BatchImagesNode`
- `ResizeImageMaskNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `GetImageRangeFromBatch`
- `SamplerCustom` ★核心
- `ComfyMathExpression`
- `CLIPLoader`
- `ImageCompositeMasked`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `Reroute`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `ImageConcatMulti`
- `ComfyMathExpression`
- `PreviewAny`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ColorTransfer`
- `BatchImagesNode`
- `SamplerCustom` ★核心
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `SamplerCustom` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `TensorLoopClose`
- `TensorLoopOpen`
- `SCAIL2ColoredMask`
- `WanSCAILToVideo`
- `GetNode`
- `GetNode`
- `WanSCAILToVideo`
- `WanSCAILToVideo`
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `CR Text`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **44%**（65/148）

**有卡**：`SAM3_VideoTrack`、`CLIPTextEncode`、`VAEDecode`、`SAM3_TrackToMask`、`EmptyImage`、`GetImageRangeFromBatch`、`GetImageSize`、`ImageConcatMulti`、`ColorTransfer`、`BatchImagesNode`、`ResizeImageMaskNode`、`SamplerCustom`、`ComfyMathExpression`、`CLIPLoader`、`ImageCompositeMasked`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`TensorLoopClose`、`TensorLoopOpen`、`SCAIL2ColoredMask`、`WanSCAILToVideo`、`MathExpression|pysssss`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio`、`VHS_LoadVideo`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
