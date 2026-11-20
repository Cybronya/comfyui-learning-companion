---
key: 平台全量/Wan2.2Animate+视频表情动作迁移+人物替换_1999522541179895810.json
name: Wan2.2Animate+视频表情动作迁移+人物替换_1999522541179895810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate+视频表情动作迁移+人物替换_1999522541179895810.json
hash: 3f95e659fa8616f4
coverage: 0.626087
learned_at: 2026-11-14 01:06:11
nodes: [Reroute, GetNode, SimpleMath+, WanVideoVAELoader, DownloadAndLoadSAM2Model, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, LoadImage, GrowMask, GrowMask, BlockifyMask, BlockifyMask, Sam2Segmentation, DrawMaskOnImage, WanVideoContextOptions, SetNode, Primitive integer [Crystools], ImpactSwitch, SimpleMath+, RH_Captioner, INTConstant, Text Concatenate, ShowText|pysssss, easy cleanGpuUsed, SetNode, INTConstant, INTConstant, INTConstant, INTConstant, easy anythingIndexSwitch, easy anythingIndexSwitch, SetNode, SetNode, easy showAnything, DownloadAndLoadFlorence2Model, Florence2Run, DownloadAndLoadSAM2Model, Florence2toCoordinates, Sam2Segmentation, PrimitiveString, ImageResizeKJ, PrimitiveString, RH_Translator, DrawMaskOnImage, ShowText|pysssss, GrowMask, BlockifyMask, LayerUtility: PurgeVRAM V2, PointsEditor, GetImageSizeAndCount, ImageConcatMulti, GetNode, ImageConcatMulti, VHS_VideoCombine, ImageCropByMaskAndResize, GetNode, PixelPerfectResolution, DWPreprocessor, FaceMaskFromPoseKeypoints, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, GetNode, ImageResizeKJv2, RMBG, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, RHHiddenNodes, Text Multiline, easy anythingIndexSwitch, easy anythingIndexSwitch, SetNode, VHS_VideoCombine, SimpleMath+, Primitive integer [Crystools], SimpleMath+, SetNode, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], VHS_VideoCombine, INTConstant, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate+视频表情动作迁移+人物替换_1999522541179895810.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate+视频表情动作迁移+人物替换_1999522541179895810.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（115 个）：
- `Reroute`
- `GetNode`
- `SimpleMath+`
- `WanVideoVAELoader`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `GrowMask`
- `GrowMask`
- `BlockifyMask`
- `BlockifyMask`
- `Sam2Segmentation`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `SetNode`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `SimpleMath+`
- `RH_Captioner`
- `INTConstant`
- `Text Concatenate`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `DownloadAndLoadSAM2Model`
- `Florence2toCoordinates`
- `Sam2Segmentation`
- `PrimitiveString`
- `ImageResizeKJ`
- `PrimitiveString`
- `RH_Translator`
- `DrawMaskOnImage`
- `ShowText|pysssss`
- `GrowMask`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `PointsEditor`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageCropByMaskAndResize`
- `GetNode`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `GetNode`
- `ImageResizeKJv2`
- `RMBG`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `RHHiddenNodes`
- `Text Multiline`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `SetNode`
- `VHS_VideoCombine`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `SetNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `INTConstant`
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **63%**（72/115）

**有卡**：`SimpleMath+`、`WanVideoVAELoader`、`DownloadAndLoadSAM2Model`、`VHS_LoadVideo`、`LoadImage`、`GrowMask`、`BlockifyMask`、`Sam2Segmentation`、`DrawMaskOnImage`、`WanVideoContextOptions`、`Primitive integer [Crystools]`、`RH_Captioner`、`INTConstant`、`Text Concatenate`、`easy cleanGpuUsed`、`easy anythingIndexSwitch`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`Florence2toCoordinates`、`ImageResizeKJ`、`RH_Translator`、`LayerUtility: PurgeVRAM V2`、`PointsEditor`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`RMBG`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`RHHiddenNodes`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
