---
key: 平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json
name: 多人提示词替换工作流wan2.2 mm_1975819490330021889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json
hash: 404d3c1bd1398405
coverage: 0.627119
learned_at: 2026-11-14 01:57:28
nodes: [ImageConcatMulti, CLIPVisionLoader, GetImageSizeAndCount, WanVideoTextEncodeCached, SimpleMath+, Primitive integer [Crystools], Primitive integer [Crystools], ImpactSwitch, GetNode, ImageConcatMulti, GetNode, SimpleMath+, GetNode, GetNode, GetNode, SimpleMath+, SimpleMath+, SetNode, SetNode, ImageResizeKJv2, Primitive integer [Crystools], RMBG, WanVideoSetBlockSwap, RHHiddenNodes, Primitive integer [Crystools], GetNode, SetNode, easy anythingIndexSwitch, INTConstant, PreviewImage, SetNode, easy cleanGpuUsed, easy showAnything, RH_Captioner, Text Concatenate, ShowText|pysssss, GetNode, GetNode, Note, GetNode, RH_Translator, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Florence2toCoordinates, BlockifyMask, DrawMaskOnImage, Florence2Run, ImageResizeKJ, Sam2Segmentation, GrowMask, ShowText|pysssss, GrowMask, DownloadAndLoadSAM2Model, INTConstant, INTConstant, INTConstant, SetNode, easy anythingIndexSwitch, INTConstant, INTConstant, PrimitiveString, Primitive integer [Crystools], GetNode, GetNode, WanVideoClipVisionEncode, GrowMask, GetNode, GetNode, PointsEditor, Sam2Segmentation, SetNode, Text Multiline, PrimitiveString, Note, BBoxesToSAM2, Note, Note, Note, Note, LayerUtility: PurgeVRAM V2, LayerMask: SAM2VideoUltra, DrawMaskOnImage, WanVideoContextOptions, SetNode, SetNode, easy anythingIndexSwitch, QwenVLDetection, easy anythingIndexSwitch, BlockifyMask, GetNode, GetNode, GrowMask, Int, BlockifyMask, VHS_VideoCombine, ImageBatchGet, DrawMaskOnImage, LayerUtility: PurgeVRAM V2, GetNode, PixelPerfectResolution, DownloadAndLoadQwenModel, PreviewImage, WanVideoDecode, GetNode, DWPreprocessor, FaceMaskFromPoseKeypoints, VHS_VideoCombine, ImageCropByMaskAndResize, WanVideoSampler, WanVideoAnimateEmbeds, Reroute, GetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, CR Text, LoadImage]
patterns: []
missing: []
---

# 平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json

> 来源文件 `comfyui_library/workflows/平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（118 个）：
- `ImageConcatMulti`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Primitive integer [Crystools]`
- `RMBG`
- `WanVideoSetBlockSwap`
- `RHHiddenNodes`
- `Primitive integer [Crystools]`
- `GetNode`
- `SetNode`
- `easy anythingIndexSwitch`
- `INTConstant`
- `PreviewImage`
- `SetNode`
- `easy cleanGpuUsed`
- `easy showAnything`
- `RH_Captioner`
- `Text Concatenate`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `RH_Translator`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Florence2toCoordinates`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Florence2Run`
- `ImageResizeKJ`
- `Sam2Segmentation`
- `GrowMask`
- `ShowText|pysssss`
- `GrowMask`
- `DownloadAndLoadSAM2Model`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `easy anythingIndexSwitch`
- `INTConstant`
- `INTConstant`
- `PrimitiveString`
- `Primitive integer [Crystools]`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GrowMask`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `Sam2Segmentation`
- `SetNode`
- `Text Multiline`
- `PrimitiveString`
- `Note`
- `BBoxesToSAM2`
- `Note`
- `Note`
- `Note`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: SAM2VideoUltra`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `SetNode`
- `SetNode`
- `easy anythingIndexSwitch`
- `QwenVLDetection`
- `easy anythingIndexSwitch`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GrowMask`
- `Int`
- `BlockifyMask`
- `VHS_VideoCombine`
- `ImageBatchGet`
- `DrawMaskOnImage`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `PixelPerfectResolution`
- `DownloadAndLoadQwenModel`
- `PreviewImage`
- `WanVideoDecode`
- `GetNode`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `VHS_VideoCombine`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **63%**（74/118）

**有卡**：`ImageConcatMulti`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`SimpleMath+`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`RMBG`、`WanVideoSetBlockSwap`、`RHHiddenNodes`、`easy anythingIndexSwitch`、`INTConstant`、`easy cleanGpuUsed`、`RH_Captioner`、`Text Concatenate`、`RH_Translator`、`DownloadAndLoadFlorence2Model`、`DownloadAndLoadSAM2Model`、`Florence2toCoordinates`、`BlockifyMask`、`DrawMaskOnImage`、`Florence2Run`、`ImageResizeKJ`、`Sam2Segmentation`、`GrowMask`、`WanVideoClipVisionEncode`、`PointsEditor`、`Text Multiline`、`BBoxesToSAM2`、`LayerUtility: PurgeVRAM V2`、`LayerMask: SAM2VideoUltra`、`WanVideoContextOptions`、`QwenVLDetection`、`Int`、`VHS_VideoCombine`、`ImageBatchGet`、`PixelPerfectResolution`、`DownloadAndLoadQwenModel`、`WanVideoDecode`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、CLIPVisionLoader、GetImageSizeAndCount、ImageCropByMaskAndResize
