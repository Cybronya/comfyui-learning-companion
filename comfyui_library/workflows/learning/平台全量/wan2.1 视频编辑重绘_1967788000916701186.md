---
key: 平台全量/wan2.1 视频编辑重绘_1967788000916701186.json
name: wan2.1 视频编辑重绘_1967788000916701186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 视频编辑重绘_1967788000916701186.json
hash: 49aa554535a51a0a
coverage: 0.53913
learned_at: 2026-11-14 01:19:08
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), WanVideoTorchCompileSettings, GetNode, SetNode, AddLabel, Mute / Bypass Relay (rgthree), Reroute, PrimitiveString, StringConcatenate, PrimitiveString, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, StringConcatenate, ImageFromBatch, SetNode, ImageResizeKJ, VHS_VideoInfo, WanVideoDecode, WanVideoLoraSelect, WanVideoBlockSwap, GetNode, SetNode, ImageConcatMulti, AddLabel, GetNode, Mute / Bypass Repeater (rgthree), GetNode, easy cleanGpuUsed, GetNode, SetNode, PreviewImage, FaceSegment, RMBG, PreviewImage, GetNode, GetNode, InvertMask, ImageFromBatch, ClothesSegment, MaskToImage, GetImageSizeAndCount, GrowMask, GetImageSize+, SetNode, Any Switch (rgthree), GetNode, SetNode, INPAINT_MaskedFill, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, GetNode, WanVideoTextEncode, WanVideoVACEEncode, GetNode, WanVideoModelLoader, BBoxesToSAM2, Note, Note, SetNode, Mute / Bypass Repeater (rgthree), GetNode, ResizeMask, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_LoadVideo, easy int, WanVideoSampler, GetNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, ImageFromBatch, PreviewImage, ImageResize+, GetNode, GetNode, GetNode, LayerMask: ObjectDetectorMask, Sam2Segmentation, DownloadAndLoadSAM2Model, LayerMask: SAM2VideoUltra, LayerMask: DrawBBoxMaskV2, GetNode, Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), GrowMaskWithBlur, QwenVLDetection, ImageFromBatch, DownloadAndLoadQwenModel, Fast Groups Muter (rgthree), easy seed, SetNode, PrimitiveStringMultiline, SetNode, PrimitiveStringMultiline, SetNode, PrimitiveString, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/wan2.1 视频编辑重绘_1967788000916701186.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 视频编辑重绘_1967788000916701186.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（115 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `SetNode`
- `AddLabel`
- `Mute / Bypass Relay (rgthree)`
- `Reroute`
- `PrimitiveString`
- `StringConcatenate`
- `PrimitiveString`
- `GetNode`
- `SetNode`
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
- `PreviewImage`
- `FaceSegment`
- `RMBG`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `InvertMask`
- `ImageFromBatch`
- `ClothesSegment`
- `MaskToImage`
- `GetImageSizeAndCount`
- `GrowMask`
- `GetImageSize+`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `INPAINT_MaskedFill`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `GetNode`
- `WanVideoModelLoader`
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
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `easy int`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageFromBatch`
- `PreviewImage`
- `ImageResize+`
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
- `Mute / Bypass Relay (rgthree)`
- `GrowMaskWithBlur`
- `QwenVLDetection`
- `ImageFromBatch`
- `DownloadAndLoadQwenModel`
- `Fast Groups Muter (rgthree)`
- `easy seed`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `PrimitiveString`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **54%**（62/115）

**有卡**：`Label (rgthree)`、`WanVideoTorchCompileSettings`、`AddLabel`、`Mute / Bypass Relay (rgthree)`、`StringConcatenate`、`ImageFromBatch`、`ImageResizeKJ`、`VHS_VideoInfo`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`ImageConcatMulti`、`Mute / Bypass Repeater (rgthree)`、`easy cleanGpuUsed`、`FaceSegment`、`RMBG`、`InvertMask`、`ClothesSegment`、`MaskToImage`、`GetImageSizeAndCount`、`GrowMask`、`GetImageSize+`、`INPAINT_MaskedFill`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoModelLoader`、`BBoxesToSAM2`、`ResizeMask`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`easy int`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageResize+`、`LayerMask: ObjectDetectorMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LayerMask: SAM2VideoUltra`、`LayerMask: DrawBBoxMaskV2`、`GrowMaskWithBlur`、`QwenVLDetection`、`DownloadAndLoadQwenModel`、`easy seed`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
