---
name: unknown_workflow_video_lora_sampler_392
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.568
common_nodes: [Any Switch (rgthree), BlockifyMask, Bookmark (rgthree), CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, DrawViTPose, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetImageRangeFromBatch, GetImageSize, GetImageSize+, GetImageSizeAndCount, GetNode, GrowMask, ImageBatch, ImageCompositeMasked, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImageToMask, Label (rgthree), LayerMask: DrawBBoxMaskV2, LayerMask: MaskGrow, LayerMask: ObjectDetectorMask, LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, LoadImage, LoadWanVideoT5TextEncoder, Mask Fill Holes, MaskToImage, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, PowerVisionObjectDetection, PowerVisionQwenModelLoader, PreviewImage, PrimitiveBoolean, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, RHHiddenNodes, RH_Translator, RMBG, RepeatImageBatch, ResizeMask, SeCModelLoader, SeCVideoSegmentation, SetNode, SimpleMath+, StringConcatenate, Switch any [Crystools], ToBinaryMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy compare, easy ifElse, easy int, easy isMaskEmpty, easy sam3ModelLoader, easy sam3VideoSegmentation, easy seed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/V5.2-PRO（遮罩20 开启人脸检测）_2034257190483140609.json, 数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json, 视频生成/图生视频/VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json, 视频生成/图生视频/Wan视频编辑高级版V5.2-PRO_2031919124909137922.json, 视频生成/文生视频/VIP-Wan视频编辑高级版V5.2-PRO_2011701676641619970.json, 视频生成/文生视频/菠萝仔专用工作流_2022698322439442433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_392

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/V5.2-PRO（遮罩20 开启人脸检测）_2034257190483140609.json、数字人/数字人/Wan视频编辑高级版V5.2-PRO_2101706051115638786.json、视频生成/图生视频/VIP-Wan视频编辑高级版V5.2-PRO（加大遮罩版）_2033533523109355521.json、视频生成/图生视频/Wan视频编辑高级版V5.2-PRO_2031919124909137922.json、视频生成/文生视频/VIP-Wan视频编辑高级版V5.2-PRO_2011701676641619970.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BlockifyMask`
- `Bookmark (rgthree)`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageBatch`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageToMask`
- `Label (rgthree)`
- `LayerMask: DrawBBoxMaskV2`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorMask`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Mask Fill Holes`
- `MaskToImage`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `PowerVisionObjectDetection`
- `PowerVisionQwenModelLoader`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RH_Translator`
- `RMBG`
- `RepeatImageBatch`
- `ResizeMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SimpleMath+`
- `StringConcatenate`
- `Switch any [Crystools]`
- `ToBinaryMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy isMaskEmpty`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 4/6 个有
- `ImpactIfNone` —— 4/6 个有
- `Note Plus (mtb)` —— 4/6 个有
- `PointsEditor` —— 4/6 个有
- `easy framesEditor` —— 4/6 个有
- `DownloadAndLoadSAM2Model` —— 2/6 个有
- `Sam2Segmentation` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
