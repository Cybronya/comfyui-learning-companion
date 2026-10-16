---
key: 视频生成/图生视频/af_scail.json_2074789088183537665.json
name: af_scail.json_2074789088183537665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2074789088183537665.json
hash: da3d3d0df49ca4de
coverage: 0.438538
learned_at: 2026-10-15 22:41:18
nodes: [SAM3_VideoTrack, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, SetNode, SetNode, SetNode, GetNode, SAM3_TrackToMask, EmptyImage, Reroute, SetNode, SetNode, PreviewAny, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, Reroute, Reroute, SAM3_VideoTrack, GetImageRangeFromBatch, GetImageSize, ColorTransfer, GetImageSize, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, ImageConcatMulti, ImageConcatMulti, GetImageRangeFromBatch, ComfyMathExpression, CLIPLoader, ImageCompositeMasked, CheckpointLoaderSimple, CLIPVisionLoader, VAELoader, CLIPVisionEncode, Reroute, SetNode, GetNode, GetNode, ImageConcatMulti, Reroute, GetImageRangeFromBatch, GetNode, ColorTransfer, SamplerCustom, GetNode, TensorLoopClose, TensorLoopOpen, SCAIL2ColoredMask, GetNode, GetNode, VAEDecode, SetNode, SetNode, PrimitiveInt, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, BasicScheduler, KSamplerSelect, SetNode, SetNode, SetNode, ImageResizeKJv2, PrimitiveInt, SAM3_VideoTrack, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, SAM3_TrackToMask, EmptyImage, Reroute, SetNode, SetNode, PreviewAny, Reroute, GetNode, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, GetNode, Reroute, Reroute, SAM3_VideoTrack, GetImageRangeFromBatch, GetNode, GetImageSize, GetImageRangeFromBatch, ImageConcatMulti, GetNode, ColorTransfer, GetImageSize, GetNode, SetNode, GetImageSize, CLIPTextEncode, BatchImagesNode, ResizeImageMaskNode, ImageConcatMulti, ImageConcatMulti, SetNode, GetImageRangeFromBatch, SamplerCustom, ComfyMathExpression, CLIPLoader, ImageCompositeMasked, CheckpointLoaderSimple, CLIPVisionLoader, VAELoader, CLIPVisionEncode, Reroute, VHS_VideoCombine, SetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, ImageConcatMulti, Reroute, ComfyMathExpression, PreviewAny, GetNode, GetImageRangeFromBatch, GetNode, ColorTransfer, BatchImagesNode, GIMMVFI_interpolate, SamplerCustom, GetNode, TensorLoopClose, TensorLoopOpen, SCAIL2ColoredMask, WanSCAILToVideo, GetNode, GetNode, WanSCAILToVideo, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, CR Text, PrimitiveInt, PrimitiveInt, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, PrimitiveInt, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, BasicScheduler, KSamplerSelect, SetNode, SetNode, SetNode, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio, VHS_LoadVideo, LoadImage, VAEDecode, WanSCAILToVideo, SamplerCustom, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio, PrimitiveInt, Bjornulf_ShowInt, PrimitiveInt, SetNode, CLIPTextEncode, BatchImagesNode, GetNode, VHS_VideoCombine, VAEDecode, ImageConcatMulti, GetNode, GetImageRangeFromBatch, DownloadAndLoadGIMMVFIModel, GetNode, GetImageRangeFromBatch, ComfyMathExpression, PreviewAny, BatchImagesNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SamplerCustom, WanSCAILToVideo, CLIPTextEncode, WanSCAILToVideo, Wav2Lip, GIMMVFI_interpolate, ImageResizeKJv2, WanSCAILToVideo, SamplerCustom, VHS_VideoCombine, CR Text, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, MathExpression|pysssss, SetNode, PrimitiveInt, LoadImage, PrimitiveInt]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/af_scail.json_2074789088183537665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074789088183537665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（301 个）：
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
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `Reroute`
- `Reroute`
- `SAM3_VideoTrack`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ColorTransfer`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageRangeFromBatch`
- `ComfyMathExpression`
- `CLIPLoader`
- `ImageCompositeMasked`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `Reroute`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `Reroute`
- `GetImageRangeFromBatch`
- `GetNode`
- `ColorTransfer`
- `SamplerCustom` ★核心
- `GetNode`
- `TensorLoopClose`
- `TensorLoopOpen`
- `SCAIL2ColoredMask`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveInt`
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
- `Reroute`
- `ComfyMathExpression`
- `PreviewAny`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ColorTransfer`
- `BatchImagesNode`
- `GIMMVFI_interpolate`
- `SamplerCustom` ★核心
- `GetNode`
- `TensorLoopClose`
- `TensorLoopOpen`
- `SCAIL2ColoredMask`
- `WanSCAILToVideo`
- `GetNode`
- `GetNode`
- `WanSCAILToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
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
- `VHS_LoadVideo`
- `LoadImage`
- `VAEDecode` ★核心
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio`
- `PrimitiveInt`
- `Bjornulf_ShowInt`
- `PrimitiveInt`
- `SetNode`
- `CLIPTextEncode` ★核心
- `BatchImagesNode`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `GetNode`
- `GetImageRangeFromBatch`
- `DownloadAndLoadGIMMVFIModel`
- `GetNode`
- `GetImageRangeFromBatch`
- `ComfyMathExpression`
- `PreviewAny`
- `BatchImagesNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `WanSCAILToVideo`
- `CLIPTextEncode` ★核心
- `WanSCAILToVideo`
- `Wav2Lip`
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `SetNode`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **44%**（132/301）

**有卡**：`SAM3_VideoTrack`、`CLIPTextEncode`、`SAM3_TrackToMask`、`EmptyImage`、`VAEDecode`、`GetImageRangeFromBatch`、`GetImageSize`、`ColorTransfer`、`ResizeImageMaskNode`、`ImageConcatMulti`、`ComfyMathExpression`、`CLIPLoader`、`ImageCompositeMasked`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`SamplerCustom`、`TensorLoopClose`、`TensorLoopOpen`、`SCAIL2ColoredMask`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`ImageResizeKJv2`、`BatchImagesNode`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`WanSCAILToVideo`、`CR Text`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio`、`VHS_LoadVideo`、`LoadImage`、`DownloadAndLoadGIMMVFIModel`、`Wav2Lip`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
