---
key: 视频生成/图生视频/Wan2.2Animate：角色替换_2027913310934409217.json
name: Wan2.2Animate：角色替换_2027913310934409217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027913310934409217.json
hash: d99887db22b16c20
coverage: 0.653846
learned_at: 2026-10-15 22:35:18
nodes: [Text Concatenate, RH_Captioner, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, PixelPerfectResolution, RMBG, PrimitiveString, GrowMask, DWPreprocessor, WanVideoSampler, ShowText|pysssss, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], GetNode, SimpleMath+, Reroute, WanVideoClipVisionEncode, CLIPVisionLoader, Reroute, WanVideoVAELoader, Reroute, ImageResizeKJv2, Reroute, WanVideoTextEncodeCached, Reroute, Reroute, GetNode, SimpleMath+, Reroute, PreviewImage, PreviewImage, RH_Translator, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, WanVideoBlockSwap, Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, PreviewImage, GetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, ShowText|pysssss, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, LoadImage, SetNode, SetNode, Text Multiline, ShowAnything|Mie, easy cleanGpuUsed, easy cleanGpuUsed, Florence2Run, VHS_LoadVideo, INTConstant, INTConstant, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Animate：角色替换_2027913310934409217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027913310934409217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `Text Concatenate`
- `RH_Captioner`
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
- `Reroute`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Reroute`
- `Reroute`
- `SimpleMath+`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `GetNode`
- `SimpleMath+`
- `Reroute`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `WanVideoTextEncodeCached`
- `Reroute`
- `Reroute`
- `GetNode`
- `SimpleMath+`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `RH_Translator`
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
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `ShowText|pysssss`
- `PrimitiveString`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SetNode`
- `SetNode`
- `Text Multiline`
- `ShowAnything|Mie`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Florence2Run`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `SetNode`

## 知识

覆盖率 **65%**（51/78）

**有卡**：`Text Concatenate`、`RH_Captioner`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`RMBG`、`GrowMask`、`DWPreprocessor`、`WanVideoSampler`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`RH_Translator`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`LoadImage`、`Text Multiline`、`ShowAnything|Mie`、`easy cleanGpuUsed`、`Florence2Run`、`VHS_LoadVideo`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
