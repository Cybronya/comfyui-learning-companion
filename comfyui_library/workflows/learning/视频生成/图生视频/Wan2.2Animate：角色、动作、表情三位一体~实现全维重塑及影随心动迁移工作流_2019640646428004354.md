---
key: 视频生成/图生视频/Wan2.2Animate：角色、动作、表情三位一体~实现全维重塑及影随心动迁移工作流_2019640646428004354.json
name: Wan2.2Animate：角色、动作、表情三位一体~实现全维重塑及影随心动迁移工作流_2019640646428004354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019640646428004354.json
hash: ba13d02bdc0f07be
coverage: 0.678161
learned_at: 2026-10-15 22:35:03
nodes: [Text Concatenate, easy showAnything, RH_Captioner, INTConstant, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, PixelPerfectResolution, RMBG, PrimitiveString, GrowMask, DWPreprocessor, WanVideoSampler, ShowText|pysssss, easy cleanGpuUsed, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, easy anythingIndexSwitch, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, Reroute, WanVideoClipVisionEncode, CLIPVisionLoader, Reroute, WanVideoVAELoader, Reroute, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, SetNode, Reroute, easy anythingIndexSwitch, WanVideoTextEncodeCached, Reroute, Reroute, GetNode, SimpleMath+, Reroute, SetNode, PreviewImage, PreviewImage, RH_Translator, Florence2Run, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, Text Multiline, WanVideoBlockSwap, Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, PreviewImage, ShowAnything|Mie, GetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, ShowText|pysssss, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Animate：角色、动作、表情三位一体~实现全维重塑及影随心动迁移工作流_2019640646428004354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019640646428004354.json`

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
- `Primitive integer [Crystools]`
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
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **68%**（59/87）

**有卡**：`Text Concatenate`、`RH_Captioner`、`INTConstant`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`RMBG`、`GrowMask`、`DWPreprocessor`、`WanVideoSampler`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy anythingIndexSwitch`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`RH_Translator`、`Florence2Run`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`Text Multiline`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ShowAnything|Mie`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
