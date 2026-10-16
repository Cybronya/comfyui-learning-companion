---
key: 视频生成/图生视频/Wan2.2Animate：角色、动作、表情的三位一体！全维角色重塑，影随心动的迁移艺术_2013086174964883457.json
name: Wan2.2Animate：角色、动作、表情的三位一体！全维角色重塑，影随心动的迁移艺术_2013086174964883457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013086174964883457.json
hash: 21e0529d0a9f44b0
coverage: 0.678161
learned_at: 2026-10-15 22:34:29
nodes: [Text Concatenate, easy showAnything, RH_Captioner, INTConstant, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, PixelPerfectResolution, RMBG, PrimitiveString, GrowMask, DWPreprocessor, WanVideoSampler, ShowText|pysssss, easy cleanGpuUsed, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, easy anythingIndexSwitch, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, Reroute, WanVideoClipVisionEncode, CLIPVisionLoader, Reroute, WanVideoVAELoader, Reroute, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, SetNode, Reroute, easy anythingIndexSwitch, WanVideoTextEncodeCached, Reroute, Reroute, GetNode, SimpleMath+, Reroute, SetNode, PreviewImage, PreviewImage, RH_Translator, Florence2Run, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, Text Multiline, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, PreviewImage, ShowAnything|Mie, GetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, ShowText|pysssss, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant, INTConstant, INTConstant, VHS_LoadVideo, LoadImage, Primitive integer [Crystools], INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Animate：角色、动作、表情的三位一体！全维角色重塑，影随心动的迁移艺术_2013086174964883457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013086174964883457.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（87 个）：
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
- `Text Multiline`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
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
- `VHS_LoadVideo`
- `LoadImage`
- `Primitive integer [Crystools]`
- `INTConstant`

## 知识

覆盖率 **68%**（59/87）

**有卡**：`Text Concatenate`、`RH_Captioner`、`INTConstant`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`RMBG`、`GrowMask`、`DWPreprocessor`、`WanVideoSampler`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy anythingIndexSwitch`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`RH_Translator`、`Florence2Run`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`Text Multiline`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ShowAnything|Mie`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
