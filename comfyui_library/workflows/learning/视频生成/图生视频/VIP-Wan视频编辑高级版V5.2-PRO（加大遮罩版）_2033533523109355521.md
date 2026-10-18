---
key: 视频生成/图生视频/VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json
name: VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json
hash: 31bb6953ec28ead8
coverage: 0.562264
learned_at: 2026-10-15 22:35:40
nodes: [WanVideoTorchCompileSettings, GetNode, SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Reroute, SetNode, PrimitiveString, GetNode, GetNode, GetNode, GetNode, PrimitiveString, SetNode, Label (rgthree), SetNode, Label (rgthree), Note Plus (mtb), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, GetNode, GetImageSize+, GrowMask, ImageFromBatch, MaskToImage, SetNode, ImageFromBatch, WanVideoDecode, GetNode, SimpleMath+, easy compare, PrimitiveInt, easy ifElse, ImageFromBatch, ImageBatch, MaskToImage, SetNode, PrimitiveString, StringConcatenate, StringConcatenate, SetNode, SetNode, GetNode, SetNode, GetImageRangeFromBatch, GetImageSizeAndCount, Mute / Bypass Repeater (rgthree), GetNode, SetNode, PreviewImage, SetNode, Mute / Bypass Repeater (rgthree), LayerMask: ObjectDetectorMask, GetImageSize, ImageFromBatch, GetImageSizeAndCount, RepeatImageBatch, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, ImageToMask, GetNode, GetNode, GetNode, ImageResizeKJv2, VHS_LoadVideo, LayerMask: DrawBBoxMaskV2, GetNode, ImageConcatMulti, SetNode, Bookmark (rgthree), PixelPerfectResolution, Label (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), MarkdownNote, ImageFromBatch, LayerMask: SegformerB2ClothesUltra, LayerMask: SegformerB2ClothesUltra, GetNode, easy cleanGpuUsed, GetNode, Mute / Bypass Repeater (rgthree), SimpleMath+, MarkdownNote, OnnxDetectionModelLoader, GetNode, DrawMaskOnImage, Any Switch (rgthree), GetImageSizeAndCount, PreviewImage, PreviewImage, Any Switch (rgthree), GetImageSizeAndCount, GetNode, SetNode, LayerMask: MaskGrow, GetNode, DrawMaskOnImage, GetImageRangeFromBatch, ImageBatch, GetImageSize, WanVideoClipVisionEncode, PreviewImage, DWPreprocessor, GetNode, BlockifyMask, ResizeMask, Bookmark (rgthree), Mute / Bypass Repeater (rgthree), WanVideoSetBlockSwap, SetNode, SetNode, SetNode, WanVideoVAELoader, CLIPVisionLoader, SetNode, MarkdownNote, GetNode, Label (rgthree), WanVideoAnimateEmbeds, Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, PrimitiveString, PrimitiveString, GetNode, GetNode, AddLabel, AddLabel, AddLabel, GetNode, GetNode, AddLabel, ImageConcatMulti, GetNode, ImpactIfNone, ImpactIfNone, easy ifElse, easy ifElse, GetNode, ImageConcatMulti, ImageConcatMulti, easy ifElse, easy showAnything, VHS_VideoCombine, Label (rgthree), Any Switch (rgthree), ImageResizeKJv2, LoadWanVideoT5TextEncoder, DrawViTPose, PoseAndFaceDetection, ImageToMask, MaskToImage, PrimitiveStringMultiline, WanVideoSetLoRAs, WanVideoModelLoader, SetNode, easy sam3ModelLoader, easy sam3VideoSegmentation, easy showAnything, GetNode, ImageCompositeMasked, GetNode, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), PreviewImage, Mask Fill Holes, easy isMaskEmpty, Switch any [Crystools], ToBinaryMask, LayerUtility: CropByMask V2, GetNode, GetNode, Any Switch (rgthree), GetImageSize, SetNode, easy seed, GetNode, WanVideoBlockSwap, Switch any [Crystools], GetNode, Label (rgthree), ImageResizeKJv2, Label (rgthree), RHHiddenNodes, easy int, PrimitiveBoolean, WanVideoSampler, SetNode, ImageBatch, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, easy showAnything, SetNode, SetNode, WanVideoTextEncode, GetImageSizeAndCount, SetNode, GetNode, SimpleMath+, RepeatImageBatch, RepeatImageBatch, GetNode, GetNode, Label (rgthree), Label (rgthree), PreviewImage, ImageFromBatch, easy int, RH_Translator, easy sam3VideoSegmentation, SeCVideoSegmentation, SeCModelLoader, PowerVisionObjectDetection, GetNode, ImageFromBatch, Mute / Bypass Relay (rgthree), Any Switch (rgthree), easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3ModelLoader, GetNode, easy framesEditor, PrimitiveStringMultiline, Fast Groups Muter (rgthree), PowerVisionQwenModelLoader, VHS_LoadVideo, LoadImage, LoadImage, easy int, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), RMBG]
patterns: []
missing: []
---

# 视频生成/图生视频/VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033533523109355521.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（265 个）：
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
- `PrimitiveString`
- `SetNode`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `Note Plus (mtb)`
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
- `ImageBatch`
- `MaskToImage`
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
- `SetNode`
- `Bookmark (rgthree)`
- `PixelPerfectResolution`
- `Label (rgthree)`
- `Label (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `MarkdownNote`
- `ImageFromBatch`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `SimpleMath+`
- `MarkdownNote`
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
- `GetImageRangeFromBatch`
- `ImageBatch`
- `GetImageSize`
- `WanVideoClipVisionEncode`
- `PreviewImage`
- `DWPreprocessor`
- `GetNode`
- `BlockifyMask`
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
- `GetNode`
- `GetNode`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `GetNode`
- `GetNode`
- `AddLabel`
- `ImageConcatMulti`
- `GetNode`
- `ImpactIfNone`
- `ImpactIfNone`
- `easy ifElse`
- `easy ifElse`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `easy ifElse`
- `easy showAnything`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `ImageToMask`
- `MaskToImage`
- `PrimitiveStringMultiline`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `SetNode`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy showAnything`
- `GetNode`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `GetNode`
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
- `easy seed`
- `GetNode`
- `WanVideoBlockSwap`
- `Switch any [Crystools]`
- `GetNode`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `RHHiddenNodes`
- `easy int`
- `PrimitiveBoolean`
- `WanVideoSampler` ★核心
- `SetNode`
- `ImageBatch`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `PreviewImage`
- `ImageFromBatch`
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
- `easy sam3VideoSegmentation`
- `easy sam3ModelLoader`
- `GetNode`
- `easy framesEditor`
- `PrimitiveStringMultiline`
- `Fast Groups Muter (rgthree)`
- `PowerVisionQwenModelLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `easy int`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `RMBG`

## 知识

覆盖率 **56%**（149/265）

**有卡**：`WanVideoTorchCompileSettings`、`Label (rgthree)`、`Note Plus (mtb)`、`GetImageSize+`、`GrowMask`、`ImageFromBatch`、`MaskToImage`、`WanVideoDecode`、`SimpleMath+`、`easy compare`、`ImageBatch`、`StringConcatenate`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`Mute / Bypass Repeater (rgthree)`、`LayerMask: ObjectDetectorMask`、`GetImageSize`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`、`ImageToMask`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LayerMask: DrawBBoxMaskV2`、`ImageConcatMulti`、`Bookmark (rgthree)`、`PixelPerfectResolution`、`Mute / Bypass Relay (rgthree)`、`LayerMask: SegformerB2ClothesUltra`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`LayerMask: MaskGrow`、`WanVideoClipVisionEncode`、`DWPreprocessor`、`BlockifyMask`、`ResizeMask`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`AddLabel`、`ImpactIfNone`、`LoadWanVideoT5TextEncoder`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`easy sam3ModelLoader`、`easy sam3VideoSegmentation`、`ImageCompositeMasked`、`Mask Fill Holes`、`easy isMaskEmpty`、`Switch any [Crystools]`、`ToBinaryMask`、`LayerUtility: CropByMask V2`、`easy seed`、`WanVideoBlockSwap`、`RHHiddenNodes`、`easy int`、`PrimitiveBoolean`、`WanVideoSampler`、`VHS_VideoInfo`、`WanVideoTextEncode`、`RH_Translator`、`SeCVideoSegmentation`、`SeCModelLoader`、`PowerVisionObjectDetection`、`easy framesEditor`、`PowerVisionQwenModelLoader`、`LoadImage`、`RMBG`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
