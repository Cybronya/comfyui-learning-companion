---
key: 视频生成/图生视频/角色重塑换脸、动作、表情 高清视频人物替换，动作迁移（支持超长时间输出）Wan2.2Animate_2012703937253609473.json
name: 角色重塑换脸、动作、表情 高清视频人物替换，动作迁移（支持超长时间输出）Wan2.2Animate_2012703937253609473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色重塑换脸、动作、表情 高清视频人物替换，动作迁移（支持超长时间输出）Wan2.2Animate_2012703937253609473.json
hash: 32d57d7d7605e79a
coverage: 0.678161
learned_at: 2026-10-15 22:34:28
nodes: [Text Concatenate, easy showAnything, RH_Captioner, INTConstant, WanVideoTeaCache, WanVideoSLG, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, Florence2toCoordinates, DownloadAndLoadSAM2Model, PixelPerfectResolution, RMBG, PrimitiveString, GrowMask, DWPreprocessor, WanVideoSampler, ShowText|pysssss, easy cleanGpuUsed, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, easy anythingIndexSwitch, SimpleMath+, WanVideoDecode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, Reroute, WanVideoClipVisionEncode, CLIPVisionLoader, Reroute, WanVideoVAELoader, Reroute, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, SetNode, Reroute, WanVideoTextEncodeCached, Reroute, Reroute, GetNode, SimpleMath+, Reroute, SetNode, PreviewImage, PreviewImage, RH_Translator, Florence2Run, Sam2Segmentation, DrawMaskOnImage, BlockifyMask, LayerUtility: PurgeVRAM V2, PreviewImage, LayerMask: MaskPreview, Text Multiline, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, PreviewImage, ShowAnything|Mie, GetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, ShowText|pysssss, PrimitiveString, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, Primitive integer [Crystools], INTConstant, easy anythingIndexSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/角色重塑换脸、动作、表情 高清视频人物替换，动作迁移（支持超长时间输出）Wan2.2Animate_2012703937253609473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012703937253609473.json`

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
- `LoadImage`
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`
- `INTConstant`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **68%**（59/87）

**有卡**：`Text Concatenate`、`RH_Captioner`、`INTConstant`、`WanVideoTeaCache`、`WanVideoSLG`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`RMBG`、`GrowMask`、`DWPreprocessor`、`WanVideoSampler`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`easy anythingIndexSwitch`、`SimpleMath+`、`WanVideoDecode`、`Primitive integer [Crystools]`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`RH_Translator`、`Florence2Run`、`Sam2Segmentation`、`DrawMaskOnImage`、`BlockifyMask`、`LayerMask: MaskPreview`、`Text Multiline`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ShowAnything|Mie`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
