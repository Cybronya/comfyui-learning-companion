---
key: 视频生成/图生视频/Wan2.1-Scail2 单人角色替换 （高质量循环版）_2068508853481861121.json
name: Wan2.1-Scail2 单人角色替换 （高质量循环版）_2068508853481861121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068508853481861121.json
hash: bcf05bcf8eaa4c37
coverage: 0.442177
learned_at: 2026-10-15 22:40:19
nodes: [GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, SAM3_TrackToMask, EmptyImage, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, ImageCompositeMasked, ImageResizeKJv2, GetNode, VHS_VideoCombine, LoraLoaderModelOnly, MarkdownNote, CLIPVisionLoader, GetNode, GetNode, GetImageRangeFromBatch, GetNode, GetNode, ResizeImageMaskNode, ImageConcatMulti, ImageConcatMulti, GetImageRangeFromBatch, ImageConcatMulti, GetNode, SAM3_VideoTrack, CLIPTextEncode, SetNode, Reroute, SCAIL2ColoredMask, GetNode, GetNode, SamplerCustom, WanSCAILToVideo, SAM3_VideoTrack, SetNode, GetNode, SetNode, ImageConcatMulti, Reroute, PreviewAny, Reroute, ComfyMathExpression, GIMMVFI_interpolate, RunningHub Deepcleaner, VAEDecode, GetNode, GetImageRangeFromBatch, ColorTransfer, GetImageSize, GetNode, BatchImagesNode, TensorLoopClose, ComfyMathExpression, Reroute, VHS_LoadVideo, SetNode, SetNode, PrimitiveInt, PreviewImage, DownloadAndLoadGIMMVFIModel, GetImageSize, LoadImage, Reroute, CLIPLoader, ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, BasicScheduler, KSamplerSelect, CLIPTextEncode, LoraLoaderModelOnly, VAELoader, CLIPVisionEncode, DiffusionModelLoaderKJ, SetNode, SamplerCustom, CheckpointLoaderSimple, PrimitiveInt, PrimitiveInt, GetNode, VHS_VideoCombine, GetImageSize, TensorLoopOpen, GetNode, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, PreviewAny, GetNode, GetNode, GetNode, BatchImagesNode, ColorTransfer, GetImageRangeFromBatch, VHS_VideoCombine, VAEDecode, GetNode, WanSCAILToVideo, WanSCAILToVideo, SamplerCustom, Reroute, VAEDecode, GetNode, VHS_VideoCombine, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, GetNode, SizeSelector, CLIPTextEncode, SetNode, JWInteger]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.1-Scail2 单人角色替换 （高质量循环版）_2068508853481861121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068508853481861121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（147 个）：
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
- `SAM3_TrackToMask`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `GetNode`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `SetNode`
- `Reroute`
- `SCAIL2ColoredMask`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `WanSCAILToVideo`
- `SAM3_VideoTrack`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `Reroute`
- `PreviewAny`
- `Reroute`
- `ComfyMathExpression`
- `GIMMVFI_interpolate`
- `RunningHub Deepcleaner`
- `VAEDecode` ★核心
- `GetNode`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `GetImageSize`
- `GetNode`
- `BatchImagesNode`
- `TensorLoopClose`
- `ComfyMathExpression`
- `Reroute`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PreviewImage`
- `DownloadAndLoadGIMMVFIModel`
- `GetImageSize`
- `LoadImage`
- `Reroute`
- `CLIPLoader`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPVisionEncode`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `SamplerCustom` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageSize`
- `TensorLoopOpen`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `ColorTransfer`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `GetNode`
- `WanSCAILToVideo`
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `GetNode`
- `SizeSelector`
- `CLIPTextEncode` ★核心
- `SetNode`
- `JWInteger`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **44%**（65/147）

**有卡**：`SAM3_TrackToMask`、`EmptyImage`、`ImageResizeKJv2`、`ImageCompositeMasked`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`GetImageRangeFromBatch`、`ResizeImageMaskNode`、`ImageConcatMulti`、`SAM3_VideoTrack`、`CLIPTextEncode`、`SCAIL2ColoredMask`、`SamplerCustom`、`WanSCAILToVideo`、`ComfyMathExpression`、`GIMMVFI_interpolate`、`RunningHub Deepcleaner`、`VAEDecode`、`ColorTransfer`、`GetImageSize`、`BatchImagesNode`、`TensorLoopClose`、`VHS_LoadVideo`、`DownloadAndLoadGIMMVFIModel`、`LoadImage`、`CLIPLoader`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`VAELoader`、`CLIPVisionEncode`、`DiffusionModelLoaderKJ`、`CheckpointLoaderSimple`、`TensorLoopOpen`、`SizeSelector`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
