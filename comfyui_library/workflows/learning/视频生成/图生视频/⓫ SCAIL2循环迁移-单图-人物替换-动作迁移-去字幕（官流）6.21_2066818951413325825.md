---
key: 视频生成/图生视频/⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json
name: ⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json
hash: 61cb890e444284c8
coverage: 0.385593
learned_at: 2026-10-15 22:39:53
nodes: [GetNode, GetNode, SetNode, SetNode, SAM3_TrackToMask, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, ImageResizeKJv2, GetNode, GetImageRangeFromBatch, GetImageSize, ComfyMathExpression, TensorLoopClose, GetImageSize, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DiffusionModelLoaderKJ, ComfySwitchNode, SetNode, GetNode, GetNode, easy int, PrimitiveBoolean, CheckpointLoaderSimple, GetNode, SCAIL2ColoredMask, CLIPTextEncode, GetNode, GetNode, Reroute, GetNode, GetNode, SetNode, PreviewImage, CLIPTextEncode, GetNode, GetNode, SetNode, ImageCompositeMasked, EmptyImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanSCAILToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BatchImagesNode, GetImageRangeFromBatch, ColorTransfer, SetNode, GetNode, GetNode, SAM3_VideoTrack, ColorTransfer, GetNode, SetNode, BatchImagesNode, GetNode, GetImageSize, VAEDecodeTiled, VAEDecodeTiled, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VAEDecode, easy showAnything, Reroute, WanSCAILToVideo, VAEDecodeTiled, GetNode, GetNode, SAM3_TrackToMask, PreviewImage, GetNode, SetNode, Any Switch (rgthree), VHS_VideoCombine, LoadImage, ImageResizeKJv2, MarkdownNote, GetNode, GetNode, Reroute, SetNode, SetNode, GetNode, ResizeImageMaskNode, ImageConcatMulti, GetNode, ImageConcatMulti, GetNode, GetNode, FL_VideoTrim, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, FL_RIFE, GetImageRangeFromBatch, ImageConcatMulti, FL_RIFE, ImageConcatMulti, SetNode, VHS_LoadVideo, SaveImage, easy showAnything, PreviewImage, PlaySound|pysssss, LayerUtility: ImageScaleByAspectRatio V2, FL_VideoTrim, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, SamplerCustom, SamplerCustom, SamplerCustom, VHS_LoadVideo, SetNode, CLIPLoader, GetNode, GetNode, SetNode, SetNode, CLIPVisionLoader, CLIPVisionEncode, GetNode, SetNode, MarkdownNote, GetNode, SAM3_VideoTrack, GetNode, GetNode, GetNode, GetNode, SetNode, ModelSamplingSD3, KSamplerSelect, SetNode, SetNode, VAELoader, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, SetNode, LoadImage, SaveImage, ImageFlip+, Fast Groups Bypasser (rgthree), VHS_VideoCombine, GetNode, SetNode, SetNode, TensorLoopOpen, GetNode, WanSCAILToVideo, SAM3_TrackPreview, MarkdownNote, SetNode, SetNode, easy int, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MarkdownNote, easy int, SetNode, TextInput_, CLIPTextEncode, CLIPTextEncode, easy int, easy int, Fast Groups Bypasser (rgthree), ImageCompositeMasked, SAM3_VideoTrack, Convert Masks to Images, InvertMask, GetNode, ComfyMathExpression, ComfySwitchNode, easy showAnything, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066818951413325825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（236 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SAM3_TrackToMask`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ComfyMathExpression`
- `TensorLoopClose`
- `GetImageSize`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetNode`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `DiffusionModelLoaderKJ`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `PrimitiveBoolean`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `SCAIL2ColoredMask`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCompositeMasked`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanSCAILToVideo`
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
- `BatchImagesNode`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `SetNode`
- `GetNode`
- `GetNode`
- `SAM3_VideoTrack`
- `ColorTransfer`
- `GetNode`
- `SetNode`
- `BatchImagesNode`
- `GetNode`
- `GetImageSize`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `easy showAnything`
- `Reroute`
- `WanSCAILToVideo`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SAM3_TrackToMask`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `FL_VideoTrim`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `FL_RIFE`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `FL_RIFE`
- `ImageConcatMulti`
- `SetNode`
- `VHS_LoadVideo`
- `SaveImage`
- `easy showAnything`
- `PreviewImage`
- `PlaySound|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FL_VideoTrim`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `SAM3_VideoTrack`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SetNode`
- `LoadImage`
- `SaveImage`
- `ImageFlip+`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `TensorLoopOpen`
- `GetNode`
- `WanSCAILToVideo`
- `SAM3_TrackPreview`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `easy int`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `easy int`
- `SetNode`
- `TextInput_`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `ImageCompositeMasked`
- `SAM3_VideoTrack`
- `Convert Masks to Images`
- `InvertMask`
- `GetNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **39%**（91/236）

**有卡**：`SAM3_TrackToMask`、`VAEDecode`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`GetImageSize`、`ComfyMathExpression`、`TensorLoopClose`、`LayerUtility: ImageScaleByAspectRatio V2`、`DiffusionModelLoaderKJ`、`easy int`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`SCAIL2ColoredMask`、`CLIPTextEncode`、`ImageCompositeMasked`、`EmptyImage`、`WanSCAILToVideo`、`BatchImagesNode`、`ColorTransfer`、`SAM3_VideoTrack`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoadImage`、`ResizeImageMaskNode`、`ImageConcatMulti`、`FL_VideoTrim`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`FL_RIFE`、`VHS_LoadVideo`、`SaveImage`、`PlaySound|pysssss`、`SamplerCustom`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ModelSamplingSD3`、`KSamplerSelect`、`VAELoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`ImageFlip+`、`TensorLoopOpen`、`SAM3_TrackPreview`、`TextInput_`、`Convert Masks to Images`、`InvertMask`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
