---
key: 平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json
name: wan2.1 视频人物替换换人工作流视频换人_1952207188704047105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json
hash: 3703bf6d9149c4d8
coverage: 0.576271
learned_at: 2026-11-14 01:19:05
nodes: [SetNode, Reroute, Reroute, Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), Bookmark (rgthree), WanVideoTorchCompileSettings, SetNode, GetNode, Reroute, Label (rgthree), Label (rgthree), SetNode, AddLabel, Mute / Bypass Relay (rgthree), Reroute, SetNode, PrimitiveString, StringConcatenate, PrimitiveString, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveString, StringConcatenate, Bookmark (rgthree), Note Plus (mtb), GetNode, ImageFromBatch, ImageFromBatch, SetNode, ImageResizeKJ, VHS_VideoInfo, SetNode, GetNode, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoBlockSwap, GetNode, SetNode, ImageConcatMulti, AddLabel, GetNode, ImageResize+, Mute / Bypass Repeater (rgthree), GetNode, easy cleanGpuUsed, GetNode, SetNode, Label (rgthree), easy int, VHS_VideoCombine, FaceSegment, RMBG, PreviewImage, GetNode, GetNode, InvertMask, ImageFromBatch, ClothesSegment, easy seed, MaskToImage, GetImageSizeAndCount, Fast Groups Muter (rgthree), PrimitiveStringMultiline, GrowMask, PreviewImage, GetImageSize+, VHS_VideoCombine, SetNode, Any Switch (rgthree), ResizeMask, GetNode, GetNode, SetNode, INPAINT_MaskedFill, Label (rgthree), Label (rgthree), Label (rgthree), WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, VHS_LoadVideo, GetNode, WanVideoTextEncode, WanVideoVACEEncode, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, WanVideoEnhanceAVideo, GetNode, WanVideoSampler, GetNode, WanVideoModelLoader, Fast Groups Bypasser (rgthree), MarkdownNote, LoadImage, PreviewImage]
patterns: []
missing: []
---

# 平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（118 个）：
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
- `Note Plus (mtb)`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch`
- `SetNode`
- `ImageResizeKJ`
- `VHS_VideoInfo`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `AddLabel`
- `GetNode`
- `ImageResize+`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `easy int`
- `VHS_VideoCombine`
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
- `Fast Groups Muter (rgthree)`
- `PrimitiveStringMultiline`
- `GrowMask`
- `PreviewImage`
- `GetImageSize+`
- `VHS_VideoCombine`
- `SetNode`
- `Any Switch (rgthree)`
- `ResizeMask`
- `GetNode`
- `GetNode`
- `SetNode`
- `INPAINT_MaskedFill`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `VHS_LoadVideo`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `PreviewImage`

## 知识

覆盖率 **58%**（68/118）

**有卡**：`Label (rgthree)`、`Bookmark (rgthree)`、`WanVideoTorchCompileSettings`、`AddLabel`、`Mute / Bypass Relay (rgthree)`、`StringConcatenate`、`Note Plus (mtb)`、`ImageFromBatch`、`ImageResizeKJ`、`VHS_VideoInfo`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`ImageConcatMulti`、`ImageResize+`、`Mute / Bypass Repeater (rgthree)`、`easy cleanGpuUsed`、`easy int`、`FaceSegment`、`RMBG`、`InvertMask`、`ClothesSegment`、`easy seed`、`MaskToImage`、`GetImageSizeAndCount`、`GrowMask`、`GetImageSize+`、`ResizeMask`、`INPAINT_MaskedFill`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`VHS_LoadVideo`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
