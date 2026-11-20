---
key: 平台全量/Wan2.2Animate：角色、动作、表情的保持一致_2018686755846754306.json
name: Wan2.2Animate：角色、动作、表情的保持一致_2018686755846754306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate：角色、动作、表情的保持一致_2018686755846754306.json
hash: 756142f01cac2ce4
coverage: 0.674157
learned_at: 2026-11-14 01:06:12
nodes: [Text Concatenate, easy showAnything, RH_Captioner, INTConstant, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, PixelPerfectResolution, RMBG, PrimitiveString, GrowMask, DWPreprocessor, WanVideoSampler, ShowText|pysssss, easy cleanGpuUsed, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, easy anythingIndexSwitch, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, Reroute, WanVideoClipVisionEncode, CLIPVisionLoader, Reroute, WanVideoVAELoader, Reroute, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, SetNode, Reroute, easy anythingIndexSwitch, WanVideoTextEncodeCached, Reroute, Reroute, GetNode, SimpleMath+, Reroute, SetNode, PreviewImage, PreviewImage, RH_Translator, Florence2Run, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, WanVideoBlockSwap, Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, INTConstant, PreviewImage, PreviewImage, ShowAnything|Mie, GetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, ShowText|pysssss, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant, INTConstant, INTConstant, LoadImage, Text Multiline, LoadImage, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate：角色、动作、表情的保持一致_2018686755846754306.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate：角色、动作、表情的保持一致_2018686755846754306.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（89 个）：
- `Text Concatenate`
- `easy showAnything`
- `RH_Captioner`
- `INTConstant`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadFlorence2Model`
- `Florence2toCoordinates`
- `DownloadAndLoadSAM2Model`
- `PixelPerfectResolution`
- `RMBG`
- `PrimitiveString`
- `GrowMask`
- `DWPreprocessor`
- `WanVideoSampler` ★核心
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `Reroute`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `WanVideoAnimateEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `SetNode`
- `Reroute`
- `easy anythingIndexSwitch`
- `WanVideoTextEncodeCached`
- `Reroute`
- `Reroute`
- `GetNode`
- `SimpleMath+`
- `Reroute`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `RH_Translator`
- `Florence2Run`
- `Sam2Segmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `WanVideoBlockSwap`
- `Primitive integer [Crystools]`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `PreviewImage`
- `PreviewImage`
- `ShowAnything|Mie`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `ShowText|pysssss`
- `PrimitiveString`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `Text Multiline`
- `LoadImage`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **67%**（60/89）

**有卡**：`Text Concatenate`、`RH_Captioner`、`INTConstant`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`RMBG`、`GrowMask`、`DWPreprocessor`、`WanVideoSampler`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy anythingIndexSwitch`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`RH_Translator`、`Florence2Run`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ShowAnything|Mie`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`Text Multiline`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
