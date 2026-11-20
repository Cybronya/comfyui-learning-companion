---
key: 平台全量/Wan2.2Animate：角色、动作、表情的三位一体！动作迁移_2011416952517959682.json
name: Wan2.2Animate：角色、动作、表情的三位一体！动作迁移_2011416952517959682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate：角色、动作、表情的三位一体！动作迁移_2011416952517959682.json
hash: 83004977a15d2658
coverage: 0.674157
learned_at: 2026-11-14 01:06:12
nodes: [Text Concatenate, easy showAnything, RH_Captioner, INTConstant, DownloadAndLoadFlorence2Model, PixelPerfectResolution, RMBG, DWPreprocessor, ShowText|pysssss, easy cleanGpuUsed, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, easy anythingIndexSwitch, SimpleMath+, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, ImageResizeKJv2, SetNode, Reroute, easy anythingIndexSwitch, Reroute, Reroute, GetNode, SimpleMath+, Reroute, SetNode, PreviewImage, PreviewImage, RH_Translator, Florence2Run, Text Multiline, PreviewImage, PreviewImage, ShowAnything|Mie, VHS_VideoCombine, ShowText|pysssss, PrimitiveString, INTConstant, INTConstant, INTConstant, INTConstant, VHS_LoadVideo, INTConstant, LoadImage, LoadImage, MarkdownNote, WanVideoBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTeaCache, WanVideoSLG, WanVideoSampler, LayerUtility: PurgeVRAM V2, WanVideoDecode, GetNode, PrimitiveString, Florence2toCoordinates, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, LayerUtility: PurgeVRAM V2, Reroute, Reroute, PreviewImage, LayerMask: MaskPreview, DrawMaskOnImage, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoAnimateEmbeds, Reroute, Reroute, Reroute, LayerUtility: PurgeVRAM V2, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate：角色、动作、表情的三位一体！动作迁移_2011416952517959682.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate：角色、动作、表情的三位一体！动作迁移_2011416952517959682.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（89 个）：
- `Text Concatenate`
- `easy showAnything`
- `RH_Captioner`
- `INTConstant`
- `DownloadAndLoadFlorence2Model`
- `PixelPerfectResolution`
- `RMBG`
- `DWPreprocessor`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `Reroute`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `easy anythingIndexSwitch`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `ImageResizeKJv2`
- `SetNode`
- `Reroute`
- `easy anythingIndexSwitch`
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
- `Text Multiline`
- `PreviewImage`
- `PreviewImage`
- `ShowAnything|Mie`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `PrimitiveString`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `GetNode`
- `PrimitiveString`
- `Florence2toCoordinates`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **67%**（60/89）

**有卡**：`Text Concatenate`、`RH_Captioner`、`INTConstant`、`DownloadAndLoadFlorence2Model`、`PixelPerfectResolution`、`RMBG`、`DWPreprocessor`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy anythingIndexSwitch`、`SimpleMath+`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`RH_Translator`、`Florence2Run`、`Text Multiline`、`ShowAnything|Mie`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoSampler`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`LayerMask: MaskPreview`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
