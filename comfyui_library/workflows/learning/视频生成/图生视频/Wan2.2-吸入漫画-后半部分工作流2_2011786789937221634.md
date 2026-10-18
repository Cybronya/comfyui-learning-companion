---
key: 视频生成/图生视频/Wan2.2-吸入漫画-后半部分工作流2_2011786789937221634.json
name: Wan2.2-吸入漫画-后半部分工作流2_2011786789937221634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-吸入漫画-后半部分工作流2_2011786789937221634.json
hash: 36c709390a21a6d8
coverage: 0.712121
learned_at: 2026-10-15 22:34:25
nodes: [FaceMaskFromPoseKeypoints, OnnxDetectionModelLoader, RMBG, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, PrimitiveString, Sam2Segmentation, RH_Translator, SetNode, LayerUtility: PurgeVRAM V2, SetNode, ShowText|pysssss, GetNode, ImageResizeKJ, GetNode, Reroute, LayerUtility: PurgeVRAM V2, GetNode, SetNode, easy anythingIndexSwitch, SetNode, easy anythingIndexSwitch, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, LoadImage, GetNode, LoadImage, SetNode, Florence2Run, PrimitiveString, WanVideoAnimateEmbeds, Primitive integer [Crystools], WanVideoSLG, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoTeaCache, WanVideoTextEncodeCached, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSetBlockSwap, RHHiddenNodes, WanVideoSampler, Text Concatenate, SetNode, RH_Captioner, Text Multiline, easy cleanGpuUsed, GetNode, GetNode, VHS_LoadVideo, PixelPerfectResolution, ImageResizeKJv2, GetNode, VHS_VideoCombine, DWPreprocessor, PoseAndFaceDetection, ImageCropByMaskAndResize]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-吸入漫画-后半部分工作流2_2011786789937221634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011786789937221634.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `FaceMaskFromPoseKeypoints`
- `OnnxDetectionModelLoader`
- `RMBG`
- `DownloadAndLoadFlorence2Model`
- `Florence2toCoordinates`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `PrimitiveString`
- `Sam2Segmentation`
- `RH_Translator`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `ShowText|pysssss`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `SetNode`
- `easy anythingIndexSwitch`
- `SetNode`
- `easy anythingIndexSwitch`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `LoadImage`
- `SetNode`
- `Florence2Run`
- `PrimitiveString`
- `WanVideoAnimateEmbeds`
- `Primitive integer [Crystools]`
- `WanVideoSLG`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `Text Concatenate`
- `SetNode`
- `RH_Captioner`
- `Text Multiline`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PixelPerfectResolution`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `PoseAndFaceDetection`
- `ImageCropByMaskAndResize`

## 知识

覆盖率 **71%**（47/66）

**有卡**：`FaceMaskFromPoseKeypoints`、`OnnxDetectionModelLoader`、`RMBG`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`RH_Translator`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJ`、`easy anythingIndexSwitch`、`INTConstant`、`LoadImage`、`Florence2Run`、`WanVideoAnimateEmbeds`、`Primitive integer [Crystools]`、`WanVideoSLG`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`RHHiddenNodes`、`WanVideoSampler`、`Text Concatenate`、`RH_Captioner`、`Text Multiline`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`PixelPerfectResolution`、`ImageResizeKJv2`、`VHS_VideoCombine`、`DWPreprocessor`、`PoseAndFaceDetection`、`ImageCropByMaskAndResize`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoClipVisionEncode、WanVideoTextEncodeCached、CLIPVisionLoader、ImageResizeKJ、ImageResizeKJv2
