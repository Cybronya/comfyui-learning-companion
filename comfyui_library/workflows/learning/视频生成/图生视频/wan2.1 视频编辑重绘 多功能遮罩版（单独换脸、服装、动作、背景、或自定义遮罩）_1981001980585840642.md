---
key: 视频生成/图生视频/wan2.1 视频编辑重绘 多功能遮罩版（单独换脸、服装、动作、背景、或自定义遮罩）_1981001980585840642.json
name: wan2.1 视频编辑重绘 多功能遮罩版（单独换脸、服装、动作、背景、或自定义遮罩）_1981001980585840642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981001980585840642.json
hash: ff4e396d58d560ba
coverage: 0.58156
learned_at: 2026-10-15 22:32:36
nodes: [SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), Bookmark (rgthree), WanVideoTorchCompileSettings, SetNode, GetNode, Reroute, Label (rgthree), SetNode, AddLabel, Mute / Bypass Relay (rgthree), Reroute, SetNode, PrimitiveString, StringConcatenate, PrimitiveString, GetNode, GetNode, GetNode, GetNode, SetNode, StringConcatenate, ImageFromBatch, SetNode, ImageResizeKJ, VHS_VideoInfo, WanVideoDecode, GetNode, SetNode, ImageConcatMulti, AddLabel, GetNode, Mute / Bypass Repeater (rgthree), GetNode, easy cleanGpuUsed, GetNode, SetNode, Label (rgthree), PreviewImage, FaceSegment, RMBG, PreviewImage, GetNode, GetNode, InvertMask, ImageFromBatch, ClothesSegment, easy seed, MaskToImage, GetImageSizeAndCount, GrowMask, GetImageSize+, SetNode, Any Switch (rgthree), GetNode, SetNode, INPAINT_MaskedFill, Label (rgthree), Label (rgthree), WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, GetNode, WanVideoTextEncode, WanVideoVACEEncode, GetNode, WanVideoModelLoader, SetNode, BBoxesToSAM2, Note, Note, SetNode, GetNode, ResizeMask, SetNode, GetNode, VHS_VideoCombine, Label (rgthree), Label (rgthree), Label (rgthree), VHS_VideoCombine, Fast Groups Bypasser (rgthree), WanVideoSampler, GetNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, ImageFromBatch, PreviewImage, ImageResize+, Label (rgthree), GetNode, GetNode, GetNode, LayerMask: ObjectDetectorMask, Sam2Segmentation, DownloadAndLoadSAM2Model, LayerMask: SAM2VideoUltra, LayerMask: DrawBBoxMaskV2, GetNode, Mute / Bypass Repeater (rgthree), GrowMaskWithBlur, QwenVLDetection, ImageFromBatch, DownloadAndLoadQwenModel, Fast Groups Muter (rgthree), Bookmark (rgthree), SetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), WanVideoLoraSelect, PrimitiveString, VHS_LoadVideo, easy int, VHS_VideoCombine, MarkdownNote, MarkdownNote, WanVideoBlockSwap, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 视频编辑重绘 多功能遮罩版（单独换脸、服装、动作、背景、或自定义遮罩）_1981001980585840642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981001980585840642.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（141 个）：
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
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `StringConcatenate`
- `ImageFromBatch`
- `SetNode`
- `ImageResizeKJ`
- `VHS_VideoInfo`
- `WanVideoDecode`
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
- `RMBG`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `InvertMask`
- `ImageFromBatch`
- `ClothesSegment`
- `easy seed`
- `MaskToImage`
- `GetImageSizeAndCount`
- `GrowMask`
- `GetImageSize+`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `INPAINT_MaskedFill`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `GetNode`
- `WanVideoModelLoader`
- `SetNode`
- `BBoxesToSAM2`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `ResizeMask`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageFromBatch`
- `PreviewImage`
- `ImageResize+`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: ObjectDetectorMask`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: DrawBBoxMaskV2`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `GrowMaskWithBlur`
- `QwenVLDetection`
- `ImageFromBatch`
- `DownloadAndLoadQwenModel`
- `Fast Groups Muter (rgthree)`
- `Bookmark (rgthree)`
- `SetNode`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoLoraSelect`
- `PrimitiveString`
- `VHS_LoadVideo`
- `easy int`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **58%**（82/141）

**有卡**：`Label (rgthree)`、`Bookmark (rgthree)`、`WanVideoTorchCompileSettings`、`AddLabel`、`Mute / Bypass Relay (rgthree)`、`StringConcatenate`、`ImageFromBatch`、`ImageResizeKJ`、`VHS_VideoInfo`、`WanVideoDecode`、`ImageConcatMulti`、`Mute / Bypass Repeater (rgthree)`、`easy cleanGpuUsed`、`FaceSegment`、`RMBG`、`InvertMask`、`ClothesSegment`、`easy seed`、`MaskToImage`、`GetImageSizeAndCount`、`GrowMask`、`GetImageSize+`、`INPAINT_MaskedFill`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoModelLoader`、`BBoxesToSAM2`、`ResizeMask`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageResize+`、`LayerMask: ObjectDetectorMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LayerMask: SAM2VideoUltra`、`LayerMask: DrawBBoxMaskV2`、`GrowMaskWithBlur`、`QwenVLDetection`、`DownloadAndLoadQwenModel`、`VHS_LoadVideo`、`easy int`、`WanVideoBlockSwap`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
