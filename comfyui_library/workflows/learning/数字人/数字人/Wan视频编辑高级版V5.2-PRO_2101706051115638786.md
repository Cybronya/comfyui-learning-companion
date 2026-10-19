---
key: 数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json
name: Wan视频编辑高级版V5.2-PRO_2101706051115638786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json
hash: ac9ff738722abc0c
coverage: 0.577869
learned_at: 2026-10-19 00:19:15
nodes: [WanVideoTorchCompileSettings, GetNode, SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Reroute, SetNode, PrimitiveString, GetNode, SetNode, Label (rgthree), SetNode, Label (rgthree), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, GetNode, GetImageSize+, GrowMask, ImageFromBatch, MaskToImage, ImageFromBatch, WanVideoDecode, GetNode, SimpleMath+, easy compare, PrimitiveInt, easy ifElse, ImageFromBatch, SetNode, PrimitiveString, StringConcatenate, StringConcatenate, SetNode, SetNode, GetNode, SetNode, GetImageRangeFromBatch, GetImageSizeAndCount, Mute / Bypass Repeater (rgthree), GetNode, SetNode, PreviewImage, SetNode, Mute / Bypass Repeater (rgthree), LayerMask: ObjectDetectorMask, GetImageSize, ImageFromBatch, GetImageSizeAndCount, RepeatImageBatch, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, ImageToMask, GetNode, GetNode, GetNode, ImageResizeKJv2, LayerMask: DrawBBoxMaskV2, GetNode, ImageConcatMulti, PixelPerfectResolution, Label (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), ImageFromBatch, LayerMask: SegformerB2ClothesUltra, GetNode, easy cleanGpuUsed, GetNode, Mute / Bypass Repeater (rgthree), SimpleMath+, OnnxDetectionModelLoader, GetNode, DrawMaskOnImage, Any Switch (rgthree), GetImageSizeAndCount, PreviewImage, PreviewImage, Any Switch (rgthree), GetImageSizeAndCount, LayerMask: MaskGrow, GetNode, DrawMaskOnImage, GetImageSize, WanVideoClipVisionEncode, PreviewImage, DWPreprocessor, GetNode, ResizeMask, Bookmark (rgthree), Mute / Bypass Repeater (rgthree), WanVideoSetBlockSwap, SetNode, SetNode, SetNode, WanVideoVAELoader, CLIPVisionLoader, SetNode, MarkdownNote, Label (rgthree), WanVideoAnimateEmbeds, Label (rgthree), Label (rgthree), Any Switch (rgthree), ImageResizeKJv2, LoadWanVideoT5TextEncoder, DrawViTPose, PoseAndFaceDetection, WanVideoSetLoRAs, WanVideoModelLoader, SetNode, PowerVisionQwenModelLoader, easy showAnything, GetNode, ImageCompositeMasked, GetNode, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), PreviewImage, Mask Fill Holes, easy isMaskEmpty, Switch any [Crystools], ToBinaryMask, LayerUtility: CropByMask V2, GetNode, GetNode, Any Switch (rgthree), GetImageSize, SetNode, GetNode, Switch any [Crystools], GetNode, Label (rgthree), ImageResizeKJv2, Label (rgthree), RHHiddenNodes, SetNode, ImageBatch, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, easy showAnything, SetNode, SetNode, WanVideoTextEncode, GetImageSizeAndCount, SetNode, GetNode, SimpleMath+, GetNode, Label (rgthree), Label (rgthree), easy int, RH_Translator, easy sam3VideoSegmentation, SeCVideoSegmentation, SeCModelLoader, PowerVisionObjectDetection, Mute / Bypass Relay (rgthree), Any Switch (rgthree), easy sam3ModelLoader, GetNode, Label (rgthree), BlockifyMask, Label (rgthree), easy sam3VideoSegmentation, GetNode, SeCModelLoader, SeCVideoSegmentation, ImageFromBatch, PrimitiveString, SetNode, MarkdownNote, WanVideoBlockSwap, Bookmark (rgthree), GetImageRangeFromBatch, GetNode, MaskToImage, MaskToImage, RepeatImageBatch, RepeatImageBatch, ImageBatch, ImageBatch, ImageToMask, SetNode, ImageResizeKJv2, easy int, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, SetNode, PreviewImage, WanVideoSampler, easy framesEditor, GetNode, PointsEditor, SetNode, VHS_VideoCombine, PrimitiveBoolean, Fast Groups Muter (rgthree), easy seed, LoadImage, VHS_VideoCombine, MarkdownNote, LayerMask: SegformerB2ClothesUltra, Fast Groups Bypasser (rgthree), VHS_VideoCombine, RMBG, GetNode, ImageFromBatch, GetNode, VHS_LoadVideo, easy int, easy sam3ModelLoader, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（244 个）：
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
- `LayerMask: DrawBBoxMaskV2`
- `GetNode`
- `ImageConcatMulti`
- `PixelPerfectResolution`
- `Label (rgthree)`
- `Label (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `ImageFromBatch`
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
- `Label (rgthree)`
- `WanVideoAnimateEmbeds`
- `Label (rgthree)`
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
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
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
- `GetNode`
- `Switch any [Crystools]`
- `GetNode`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `RHHiddenNodes`
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
- `easy int`
- `RH_Translator`
- `easy sam3VideoSegmentation`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `PowerVisionObjectDetection`
- `Mute / Bypass Relay (rgthree)`
- `Any Switch (rgthree)`
- `easy sam3ModelLoader`
- `GetNode`
- `Label (rgthree)`
- `BlockifyMask`
- `Label (rgthree)`
- `easy sam3VideoSegmentation`
- `GetNode`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `PrimitiveString`
- `SetNode`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `Bookmark (rgthree)`
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
- `ImageResizeKJv2`
- `easy int`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `easy framesEditor`
- `GetNode`
- `PointsEditor`
- `SetNode`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `Fast Groups Muter (rgthree)`
- `easy seed`
- `LoadImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LayerMask: SegformerB2ClothesUltra`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `RMBG`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `VHS_LoadVideo`
- `easy int`
- `easy sam3ModelLoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **58%**（141/244）

**有卡**：`WanVideoTorchCompileSettings`、`Label (rgthree)`、`GetImageSize+`、`GrowMask`、`ImageFromBatch`、`MaskToImage`、`WanVideoDecode`、`SimpleMath+`、`easy compare`、`StringConcatenate`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`Mute / Bypass Repeater (rgthree)`、`LayerMask: ObjectDetectorMask`、`GetImageSize`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`、`ImageToMask`、`ImageResizeKJv2`、`LayerMask: DrawBBoxMaskV2`、`ImageConcatMulti`、`PixelPerfectResolution`、`Mute / Bypass Relay (rgthree)`、`LayerMask: SegformerB2ClothesUltra`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`LayerMask: MaskGrow`、`WanVideoClipVisionEncode`、`DWPreprocessor`、`ResizeMask`、`Bookmark (rgthree)`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`LoadWanVideoT5TextEncoder`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`PowerVisionQwenModelLoader`、`ImageCompositeMasked`、`Mask Fill Holes`、`easy isMaskEmpty`、`Switch any [Crystools]`、`ToBinaryMask`、`LayerUtility: CropByMask V2`、`RHHiddenNodes`、`ImageBatch`、`VHS_VideoInfo`、`WanVideoTextEncode`、`easy int`、`RH_Translator`、`easy sam3VideoSegmentation`、`SeCVideoSegmentation`、`SeCModelLoader`、`PowerVisionObjectDetection`、`easy sam3ModelLoader`、`BlockifyMask`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoSampler`、`easy framesEditor`、`PointsEditor`、`VHS_VideoCombine`、`PrimitiveBoolean`、`easy seed`、`LoadImage`、`RMBG`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
