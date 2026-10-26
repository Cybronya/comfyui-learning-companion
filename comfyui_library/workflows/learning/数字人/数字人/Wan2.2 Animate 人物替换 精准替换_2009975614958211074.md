---
key: 数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json
name: Wan2.2 Animate 人物替换 精准替换_2009975614958211074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json
hash: c91bc1cacea1eae1
coverage: 0.512
learned_at: 2026-10-26 01:57:49
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, ImageResizeKJv2, ImageConcatMulti, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Bookmark (rgthree), Reroute, SetNode, PrimitiveString, PrimitiveString, GetNode, GetNode, GetNode, GetNode, PrimitiveString, GetNode, SetNode, Label (rgthree), SetNode, SetNode, VHS_VideoInfo, Note Plus (mtb), Label (rgthree), SetNode, SetNode, Label (rgthree), StringConcatenate, StringConcatenate, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), GetNode, SetNode, GetNode, GetNode, GetNode, PreviewImage, ImageFromBatch, GetNode, GetNode, GetImageSize+, easy cleanGpuUsed, ResizeMask, OnnxDetectionModelLoader, Sam2Segmentation, BlockifyMask, GetNode, DrawMaskOnImage, GetImageSize, SetNode, PreviewImage, GetNode, easy clearCacheAll, WanVideoVAELoader, GetImageSizeAndCount, SetNode, VHS_VideoCombine, DrawViTPose, SetNode, GetImageSize, PoseAndFaceDetection, SetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, MarkdownNote, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, SetNode, GrowMask, GetNode, WanVideoTextEncode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, Label (rgthree), Label (rgthree), ImageResizeKJ, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), SetNode, Fast Groups Bypasser (rgthree), GetImageSize, easy seed, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, PreviewAny, SetNode, PrimitiveStringMultiline, easy int, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoBlockSwap, DownloadAndLoadSAM2Model, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（125 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
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
- `Label (rgthree)`
- `SetNode`
- `Bookmark (rgthree)`
- `Reroute`
- `SetNode`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveString`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `Note Plus (mtb)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `ResizeMask`
- `OnnxDetectionModelLoader`
- `Sam2Segmentation`
- `BlockifyMask`
- `GetNode`
- `DrawMaskOnImage`
- `GetImageSize`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `easy clearCacheAll`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `SetNode`
- `GetImageSize`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GrowMask`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `ImageResizeKJ`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `easy seed`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PreviewAny`
- `SetNode`
- `PrimitiveStringMultiline`
- `easy int`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `DownloadAndLoadSAM2Model`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **51%**（64/125）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`ImageConcatMulti`、`Label (rgthree)`、`Bookmark (rgthree)`、`VHS_VideoInfo`、`Note Plus (mtb)`、`StringConcatenate`、`ImageFromBatch`、`GetImageSize+`、`easy cleanGpuUsed`、`ResizeMask`、`OnnxDetectionModelLoader`、`Sam2Segmentation`、`BlockifyMask`、`DrawMaskOnImage`、`GetImageSize`、`easy clearCacheAll`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`GrowMask`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`ImageResizeKJ`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`easy seed`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy int`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`DownloadAndLoadSAM2Model`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
