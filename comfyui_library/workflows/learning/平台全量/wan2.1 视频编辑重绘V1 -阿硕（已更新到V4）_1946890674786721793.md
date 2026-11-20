---
key: 平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json
name: wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json
hash: 6900ac0618d9425e
coverage: 0.582734
learned_at: 2026-11-14 01:19:07
nodes: [SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), Bookmark (rgthree), WanVideoTorchCompileSettings, SetNode, GetNode, Reroute, Label (rgthree), SetNode, AddLabel, Mute / Bypass Relay (rgthree), Reroute, SetNode, PrimitiveString, StringConcatenate, PrimitiveString, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveString, StringConcatenate, Bookmark (rgthree), ImageFromBatch, SetNode, VHS_VideoInfo, WanVideoDecode, WanVideoLoraSelect, WanVideoBlockSwap, GetNode, SetNode, ImageConcatMulti, AddLabel, GetNode, Mute / Bypass Repeater (rgthree), GetNode, easy cleanGpuUsed, GetNode, SetNode, Label (rgthree), PreviewImage, FaceSegment, PreviewImage, GetNode, GetNode, InvertMask, ImageFromBatch, ClothesSegment, MaskToImage, GetImageSizeAndCount, GetImageSize+, SetNode, Any Switch (rgthree), GetNode, SetNode, INPAINT_MaskedFill, Label (rgthree), Label (rgthree), WanVideoVACEModelSelect, GetNode, WanVideoTextEncode, WanVideoVACEEncode, GetNode, SetNode, BBoxesToSAM2, Note, Note, SetNode, Mute / Bypass Repeater (rgthree), GetNode, ResizeMask, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, Label (rgthree), Label (rgthree), Label (rgthree), VHS_VideoCombine, Fast Groups Bypasser (rgthree), GetNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, ImageFromBatch, PreviewImage, ImageResize+, Label (rgthree), MarkdownNote, GetNode, GetNode, GetNode, LayerMask: ObjectDetectorMask, Sam2Segmentation, DownloadAndLoadSAM2Model, LayerMask: DrawBBoxMaskV2, Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), QwenVLDetection, ImageFromBatch, DownloadAndLoadQwenModel, WanVideoSampler, GetNode, LayerMask: SAM2VideoUltra, RMBG, GrowMask, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, easy int, ImageResizeKJv2, PrimitiveStringMultiline, PrimitiveStringMultiline, Fast Groups Muter (rgthree), easy seed, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（139 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Bookmark (rgthree)`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `Reroute`
- `Label (rgthree)`
- `SetNode`
- `AddLabel`
- `Mute / Bypass Relay (rgthree)`
- `Reroute`
- `SetNode`
- `PrimitiveString`
- `StringConcatenate`
- `PrimitiveString`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveString`
- `StringConcatenate`
- `Bookmark (rgthree)`
- `ImageFromBatch`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `AddLabel`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `PreviewImage`
- `FaceSegment`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `InvertMask`
- `ImageFromBatch`
- `ClothesSegment`
- `MaskToImage`
- `GetImageSizeAndCount`
- `GetImageSize+`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `INPAINT_MaskedFill`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoVACEModelSelect`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `GetNode`
- `SetNode`
- `BBoxesToSAM2`
- `Note`
- `Note`
- `SetNode`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `ResizeMask`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageFromBatch`
- `PreviewImage`
- `ImageResize+`
- `Label (rgthree)`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: ObjectDetectorMask`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `LayerMask: DrawBBoxMaskV2`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `QwenVLDetection`
- `ImageFromBatch`
- `DownloadAndLoadQwenModel`
- `WanVideoSampler` ★核心
- `GetNode`
- `LayerMask: SAM2VideoUltra`
- `RMBG`
- `GrowMask`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `easy int`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Fast Groups Muter (rgthree)`
- `easy seed`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **58%**（81/139）

**有卡**：`Label (rgthree)`、`Bookmark (rgthree)`、`WanVideoTorchCompileSettings`、`AddLabel`、`Mute / Bypass Relay (rgthree)`、`StringConcatenate`、`ImageFromBatch`、`VHS_VideoInfo`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`ImageConcatMulti`、`Mute / Bypass Repeater (rgthree)`、`easy cleanGpuUsed`、`FaceSegment`、`InvertMask`、`ClothesSegment`、`MaskToImage`、`GetImageSizeAndCount`、`GetImageSize+`、`INPAINT_MaskedFill`、`WanVideoVACEModelSelect`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`BBoxesToSAM2`、`ResizeMask`、`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageResize+`、`LayerMask: ObjectDetectorMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LayerMask: DrawBBoxMaskV2`、`QwenVLDetection`、`DownloadAndLoadQwenModel`、`WanVideoSampler`、`LayerMask: SAM2VideoUltra`、`RMBG`、`GrowMask`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`easy int`、`ImageResizeKJv2`、`easy seed`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
