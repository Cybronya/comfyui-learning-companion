---
key: 平台全量/Wan2.2Animate_人物替换(本地部署版)_2048671243871723521.json
name: Wan2.2Animate_人物替换(本地部署版)_2048671243871723521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate_人物替换(本地部署版)_2048671243871723521.json
hash: 8f798cd14c620966
coverage: 0.685393
learned_at: 2026-11-14 01:06:11
nodes: [INTConstant, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, Florence2toCoordinates, DownloadAndLoadSAM2Model, PrimitiveString, GrowMask, easy cleanGpuUsed, Reroute, Reroute, easy anythingIndexSwitch, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, Reroute, Reroute, WanVideoVAELoader, Reroute, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, SetNode, Reroute, Reroute, Reroute, Reroute, SetNode, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, WanVideoSetLoRAs, WanVideoSetBlockSwap, PreviewImage, PreviewImage, ShowAnything|Mie, GetNode, WanVideoTorchCompileSettings, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant, INTConstant, INTConstant, WanVideoBlockSwap, RMBG, DownloadAndLoadFlorence2Model, Text Concatenate, WanVideoTextEncodeCached, WanVideoSampler, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, easy anythingIndexSwitch, ShowText|pysssss, PreviewImage, PreviewImage, DWPreprocessor, PixelPerfectResolution, Reroute, PoseAndFaceDetection, OnnxDetectionModelLoader, Text Multiline, LayerUtility: LoadJoyCaptionBeta1Model, Florence2Run, ACE_TextTranslate, GetNode, SimpleMath+, INTConstant, LoadImage, WanVideoBlockSwap, VHS_VideoCombine, Primitive integer [Crystools], VHS_LoadVideo, RH_Captioner, easy showAnything, LayerUtility: JoyCaptionBeta1, ShowText|pysssss]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate_人物替换(本地部署版)_2048671243871723521.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate_人物替换(本地部署版)_2048671243871723521.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（89 个）：
- `INTConstant`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LayerUtility: PurgeVRAM V2`
- `Florence2toCoordinates`
- `DownloadAndLoadSAM2Model`
- `PrimitiveString`
- `GrowMask`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `easy anythingIndexSwitch`
- `SimpleMath+`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `Sam2Segmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `PreviewImage`
- `PreviewImage`
- `ShowAnything|Mie`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `PrimitiveString`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `RMBG`
- `DownloadAndLoadFlorence2Model`
- `Text Concatenate`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `easy anythingIndexSwitch`
- `ShowText|pysssss`
- `PreviewImage`
- `PreviewImage`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `Reroute`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `Text Multiline`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `Florence2Run`
- `ACE_TextTranslate`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `LoadImage`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `RH_Captioner`
- `easy showAnything`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`

## 知识

覆盖率 **69%**（61/89）

**有卡**：`INTConstant`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`GrowMask`、`easy cleanGpuUsed`、`easy anythingIndexSwitch`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoVAELoader`、`ImageResizeKJv2`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ShowAnything|Mie`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`RMBG`、`DownloadAndLoadFlorence2Model`、`Text Concatenate`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`DWPreprocessor`、`PixelPerfectResolution`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`Text Multiline`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Florence2Run`、`ACE_TextTranslate`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`RH_Captioner`、`LayerUtility: JoyCaptionBeta1`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
