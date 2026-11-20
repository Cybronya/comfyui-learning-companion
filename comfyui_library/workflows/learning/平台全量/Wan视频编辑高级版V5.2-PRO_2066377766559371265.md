---
key: 平台全量/Wan视频编辑高级版V5.2-PRO_2066377766559371265.json
name: Wan视频编辑高级版V5.2-PRO_2066377766559371265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan视频编辑高级版V5.2-PRO_2066377766559371265.json
hash: 7455973ee7e9f5ec
coverage: 0.579592
learned_at: 2026-11-14 01:07:19
nodes: [WanVideoTorchCompileSettings, GetNode, SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Reroute, SetNode, PrimitiveString, GetNode, GetNode, GetNode, GetNode, SetNode, Label (rgthree), SetNode, Label (rgthree), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, GetNode, GetImageSize+, GrowMask, ImageFromBatch, MaskToImage, SetNode, ImageFromBatch, WanVideoDecode, GetNode, SimpleMath+, easy compare, PrimitiveInt, easy ifElse, ImageFromBatch, SetNode, PrimitiveString, StringConcatenate, StringConcatenate, SetNode, SetNode, GetNode, SetNode, GetImageRangeFromBatch, GetImageSizeAndCount, Mute / Bypass Repeater (rgthree), GetNode, SetNode, PreviewImage, SetNode, Mute / Bypass Repeater (rgthree), LayerMask: ObjectDetectorMask, GetImageSize, ImageFromBatch, GetImageSizeAndCount, RepeatImageBatch, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, ImageToMask, GetNode, GetNode, GetNode, ImageResizeKJv2, VHS_LoadVideo, LayerMask: DrawBBoxMaskV2, GetNode, ImageConcatMulti, PixelPerfectResolution, Label (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), ImageFromBatch, LayerMask: SegformerB2ClothesUltra, LayerMask: SegformerB2ClothesUltra, GetNode, easy cleanGpuUsed, GetNode, Mute / Bypass Repeater (rgthree), SimpleMath+, OnnxDetectionModelLoader, GetNode, DrawMaskOnImage, Any Switch (rgthree), GetImageSizeAndCount, PreviewImage, PreviewImage, Any Switch (rgthree), GetImageSizeAndCount, GetNode, SetNode, LayerMask: MaskGrow, GetNode, DrawMaskOnImage, GetImageSize, WanVideoClipVisionEncode, PreviewImage, DWPreprocessor, GetNode, ResizeMask, Bookmark (rgthree), Mute / Bypass Repeater (rgthree), WanVideoSetBlockSwap, SetNode, SetNode, SetNode, WanVideoVAELoader, CLIPVisionLoader, SetNode, MarkdownNote, GetNode, Label (rgthree), WanVideoAnimateEmbeds, Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, Label (rgthree), Any Switch (rgthree), ImageResizeKJv2, LoadWanVideoT5TextEncoder, DrawViTPose, PoseAndFaceDetection, WanVideoSetLoRAs, WanVideoModelLoader, SetNode, PowerVisionQwenModelLoader, easy showAnything, GetNode, ImageCompositeMasked, GetNode, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), GetNode, VHS_VideoCombine, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), RMBG, PreviewImage, Mask Fill Holes, easy isMaskEmpty, Switch any [Crystools], ToBinaryMask, LayerUtility: CropByMask V2, GetNode, GetNode, Any Switch (rgthree), GetImageSize, SetNode, easy seed, GetNode, Switch any [Crystools], GetNode, Label (rgthree), ImageResizeKJv2, Label (rgthree), RHHiddenNodes, Fast Groups Muter (rgthree), WanVideoSampler, SetNode, ImageBatch, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, easy showAnything, SetNode, SetNode, WanVideoTextEncode, GetImageSizeAndCount, SetNode, GetNode, SimpleMath+, GetNode, Label (rgthree), Label (rgthree), PreviewImage, easy int, RH_Translator, easy sam3VideoSegmentation, SeCVideoSegmentation, SeCModelLoader, PowerVisionObjectDetection, GetNode, ImageFromBatch, Mute / Bypass Relay (rgthree), Any Switch (rgthree), easy sam3ModelLoader, easy sam3ModelLoader, GetNode, Label (rgthree), BlockifyMask, Label (rgthree), easy sam3VideoSegmentation, GetNode, easy framesEditor, SeCModelLoader, SeCVideoSegmentation, ImageFromBatch, LoadImage, MarkdownNote, Fast Groups Muter (rgthree), PrimitiveString, SetNode, MarkdownNote, WanVideoBlockSwap, PointsEditor, Bookmark (rgthree), LoadImage, GetImageRangeFromBatch, GetNode, MaskToImage, MaskToImage, RepeatImageBatch, RepeatImageBatch, ImageBatch, ImageBatch, ImageToMask, SetNode, Fast Groups Bypasser (rgthree), LoadImage, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveStringMultiline, ImageResizeKJv2, VHS_LoadVideo, easy int, easy int]
patterns: []
missing: []
---

# 平台全量/Wan视频编辑高级版V5.2-PRO_2066377766559371265.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan视频编辑高级版V5.2-PRO_2066377766559371265.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（245 个）：
- `WanVideoTorchCompileSettings`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `Label (rgthree)`
- `Reroute`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `Reroute`
- `SetNode`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize+`
- `GrowMask`
- `ImageFromBatch`
- `MaskToImage`
- `SetNode`
- `ImageFromBatch`
- `WanVideoDecode`
- `GetNode`
- `SimpleMath+`
- `easy compare`
- `PrimitiveInt`
- `easy ifElse`
- `ImageFromBatch`
- `SetNode`
- `PrimitiveString`
- `StringConcatenate`
- `StringConcatenate`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `Mute / Bypass Repeater (rgthree)`
- `LayerMask: ObjectDetectorMask`
- `GetImageSize`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `ImageToMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LayerMask: DrawBBoxMaskV2`
- `GetNode`
- `ImageConcatMulti`
- `PixelPerfectResolution`
- `Label (rgthree)`
- `Label (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `ImageFromBatch`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `SimpleMath+`
- `OnnxDetectionModelLoader`
- `GetNode`
- `DrawMaskOnImage`
- `Any Switch (rgthree)`
- `GetImageSizeAndCount`
- `PreviewImage`
- `PreviewImage`
- `Any Switch (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `DrawMaskOnImage`
- `GetImageSize`
- `WanVideoClipVisionEncode`
- `PreviewImage`
- `DWPreprocessor`
- `GetNode`
- `ResizeMask`
- `Bookmark (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `Label (rgthree)`
- `WanVideoAnimateEmbeds`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `SetNode`
- `PowerVisionQwenModelLoader`
- `easy showAnything`
- `GetNode`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `RMBG`
- `PreviewImage`
- `Mask Fill Holes`
- `easy isMaskEmpty`
- `Switch any [Crystools]`
- `ToBinaryMask`
- `LayerUtility: CropByMask V2`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetImageSize`
- `SetNode`
- `easy seed`
- `GetNode`
- `Switch any [Crystools]`
- `GetNode`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `RHHiddenNodes`
- `Fast Groups Muter (rgthree)`
- `WanVideoSampler` ★核心
- `SetNode`
- `ImageBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `PreviewImage`
- `easy int`
- `RH_Translator`
- `easy sam3VideoSegmentation`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `PowerVisionObjectDetection`
- `GetNode`
- `ImageFromBatch`
- `Mute / Bypass Relay (rgthree)`
- `Any Switch (rgthree)`
- `easy sam3ModelLoader`
- `easy sam3ModelLoader`
- `GetNode`
- `Label (rgthree)`
- `BlockifyMask`
- `Label (rgthree)`
- `easy sam3VideoSegmentation`
- `GetNode`
- `easy framesEditor`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `LoadImage`
- `MarkdownNote`
- `Fast Groups Muter (rgthree)`
- `PrimitiveString`
- `SetNode`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `PointsEditor`
- `Bookmark (rgthree)`
- `LoadImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `MaskToImage`
- `MaskToImage`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageToMask`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `easy int`
- `easy int`

## 知识

覆盖率 **58%**（142/245）

**有卡**：`WanVideoTorchCompileSettings`、`Label (rgthree)`、`GetImageSize+`、`GrowMask`、`ImageFromBatch`、`MaskToImage`、`WanVideoDecode`、`SimpleMath+`、`easy compare`、`StringConcatenate`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`Mute / Bypass Repeater (rgthree)`、`LayerMask: ObjectDetectorMask`、`GetImageSize`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`、`ImageToMask`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LayerMask: DrawBBoxMaskV2`、`ImageConcatMulti`、`PixelPerfectResolution`、`Mute / Bypass Relay (rgthree)`、`LayerMask: SegformerB2ClothesUltra`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`LayerMask: MaskGrow`、`WanVideoClipVisionEncode`、`DWPreprocessor`、`ResizeMask`、`Bookmark (rgthree)`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`PowerVisionQwenModelLoader`、`ImageCompositeMasked`、`RMBG`、`Mask Fill Holes`、`easy isMaskEmpty`、`Switch any [Crystools]`、`ToBinaryMask`、`LayerUtility: CropByMask V2`、`easy seed`、`RHHiddenNodes`、`WanVideoSampler`、`ImageBatch`、`VHS_VideoInfo`、`WanVideoTextEncode`、`easy int`、`RH_Translator`、`easy sam3VideoSegmentation`、`SeCVideoSegmentation`、`SeCModelLoader`、`PowerVisionObjectDetection`、`easy sam3ModelLoader`、`BlockifyMask`、`easy framesEditor`、`LoadImage`、`WanVideoBlockSwap`、`PointsEditor`、`PrimitiveBoolean`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
