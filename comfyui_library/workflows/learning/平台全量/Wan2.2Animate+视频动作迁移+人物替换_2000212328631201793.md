---
key: 平台全量/Wan2.2Animate+视频动作迁移+人物替换_2000212328631201793.json
name: Wan2.2Animate+视频动作迁移+人物替换_2000212328631201793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate+视频动作迁移+人物替换_2000212328631201793.json
hash: cfb73d3501547a9c
coverage: 0.606383
learned_at: 2026-11-14 01:06:10
nodes: [Reroute, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, VHS_LoadVideo, LoadImage, SetNode, DownloadAndLoadFlorence2Model, Florence2Run, DownloadAndLoadSAM2Model, Florence2toCoordinates, Sam2Segmentation, PrimitiveString, ImageResizeKJ, PrimitiveString, ShowText|pysssss, GrowMask, BlockifyMask, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, ImageConcatMulti, GetNode, ImageConcatMulti, VHS_VideoCombine, ImageCropByMaskAndResize, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoSampler, GetNode, ImageResizeKJv2, RMBG, PreviewImage, GetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, RHHiddenNodes, SetNode, SetNode, RHHiddenNodes, GetNode, SetNode, GetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, LayerUtility: PurgeVRAM, CLIPVisionLoader, WanVideoTextEncodeCached, GetNode, GetNode, MarkdownNote, RH_Translator, DrawMaskOnImage, SimpleMath+, Primitive integer [Crystools], SimpleMath+, SimpleMath+, Primitive integer [Crystools], Text Multiline, RH_Captioner, easy showAnything, SetNode, INTConstant, Primitive integer [Crystools], GetNode, SetNode, easy anythingIndexSwitch, easy anythingIndexSwitch, INTConstant, INTConstant, INTConstant, INTConstant, easy cleanGpuUsed, ShowText|pysssss, Text Concatenate]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate+视频动作迁移+人物替换_2000212328631201793.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate+视频动作迁移+人物替换_2000212328631201793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `SetNode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `DownloadAndLoadSAM2Model`
- `Florence2toCoordinates`
- `Sam2Segmentation`
- `PrimitiveString`
- `ImageResizeKJ`
- `PrimitiveString`
- `ShowText|pysssss`
- `GrowMask`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `RMBG`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `RHHiddenNodes`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `RH_Translator`
- `DrawMaskOnImage`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `RH_Captioner`
- `easy showAnything`
- `SetNode`
- `INTConstant`
- `Primitive integer [Crystools]`
- `GetNode`
- `SetNode`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `Text Concatenate`

## 知识

覆盖率 **61%**（57/94）

**有卡**：`VHS_LoadVideo`、`LoadImage`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`DownloadAndLoadSAM2Model`、`Florence2toCoordinates`、`Sam2Segmentation`、`ImageResizeKJ`、`GrowMask`、`BlockifyMask`、`LayerUtility: PurgeVRAM V2`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoSampler`、`ImageResizeKJv2`、`RMBG`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`RHHiddenNodes`、`LayerUtility: PurgeVRAM`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`RH_Translator`、`DrawMaskOnImage`、`SimpleMath+`、`Primitive integer [Crystools]`、`Text Multiline`、`RH_Captioner`、`INTConstant`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`Text Concatenate`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
