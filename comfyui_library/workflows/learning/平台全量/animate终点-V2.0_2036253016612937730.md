---
key: 平台全量/animate终点-V2.0_2036253016612937730.json
name: animate终点-V2.0_2036253016612937730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/animate终点-V2.0_2036253016612937730.json
hash: 2b40bb347b75da6e
coverage: 0.38835
learned_at: 2026-11-14 01:09:25
nodes: [GetNode, Note, Note, GetNode, GetNode, Note, Note, YOLOModelLoader, PoseDetectionVitPoseToDWPose, NLFPredict, RenderNLFPoses, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, PoseDetectionVitPoseToDWPose, GrowMask, SeCModelLoader, SeCVideoSegmentation, GetNode, GetNode, GetNode, GrowMask, SeCModelLoader, SeCVideoSegmentation, SeCModelLoader, Any Switch (rgthree), BlockifyMask, DrawMaskOnImage, Any Switch (rgthree), GetNode, GetNode, SetNode, SetNode, BlockifyMask, DrawMaskOnImage, SetNode, SetNode, Int, ImageFromBatch, SeCVideoSegmentation, GrowMask, DrawMaskOnImage, SetNode, ImageFromBatch, easy sam3ModelLoader, DownloadAndLoadNLFModel, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, GetNode, easy framesEditor, VHS_VideoCombine, DrawViTPose, SDPoseOODLoader, VHS_VideoCombine, PoseDetectionOneToAllAnimation, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SDPoseOODProcessor, GroundingDinoModelLoader_SDPose, Note, Note, Note, Note, SetNode, GetNode, SetNode, GetNode, Any Switch (rgthree), SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SimpleMath+, GetNode, GetNode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Int, VHS_VideoCombine, Note, Fast Groups Bypasser (rgthree), Note, Note, Note, Note, Int, SetNode, SetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), PoseAndFaceDetection, easy sam3ImageSegmentation, Int, PointsEditor, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, BlockifyMask, SetNode, PreviewImage, Note, OnnxDetectionModelLoader, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, GetNode, VHS_VideoInfo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, GetNode, ImageFromBatch, GetNode, SetNode, GetNode, BatchCount+, SetNode, SetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoEncode, WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, ImageFromBatch, RepeatImageBatch, ImageBatch, BatchCount+, GetNode, WanVideoSampler, Fast Groups Bypasser (rgthree), WanVideoAnimateEmbeds, WanVideoDecode, SetNode, GetNode, GetNode, GetNode, ImpactConditionalBranch, easy compare, Note, easy showAnything, WanVideoClipVisionEncode, VHS_LoadVideo, Int, WanVideoContextOptions, LoadImage, CR Text, GetNode, WanVideoTextEncodeCached, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, GetImageSizeAndCount, RepeatImageBatch, easy anythingIndexSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 平台全量/animate终点-V2.0_2036253016612937730.json

> 来源文件 `comfyui_library/workflows/平台全量/animate终点-V2.0_2036253016612937730.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（206 个）：
- `GetNode`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `YOLOModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `NLFPredict`
- `RenderNLFPoses`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PoseDetectionVitPoseToDWPose`
- `GrowMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `Any Switch (rgthree)`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `Int`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `GrowMask`
- `DrawMaskOnImage`
- `SetNode`
- `ImageFromBatch`
- `easy sam3ModelLoader`
- `DownloadAndLoadNLFModel`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy framesEditor`
- `VHS_VideoCombine`
- `DrawViTPose`
- `SDPoseOODLoader`
- `VHS_VideoCombine`
- `PoseDetectionOneToAllAnimation`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODProcessor`
- `GroundingDinoModelLoader_SDPose`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `Int`
- `VHS_VideoCombine`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `PoseAndFaceDetection`
- `easy sam3ImageSegmentation`
- `Int`
- `PointsEditor`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `PreviewImage`
- `Note`
- `OnnxDetectionModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `BatchCount+`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `ImageFromBatch`
- `RepeatImageBatch`
- `ImageBatch`
- `BatchCount+`
- `GetNode`
- `WanVideoSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `easy compare`
- `Note`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `Int`
- `WanVideoContextOptions`
- `LoadImage`
- `CR Text`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `RepeatImageBatch`
- `easy anythingIndexSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **39%**（80/206）

**有卡**：`YOLOModelLoader`、`PoseDetectionVitPoseToDWPose`、`NLFPredict`、`RenderNLFPoses`、`GrowMask`、`SeCModelLoader`、`SeCVideoSegmentation`、`BlockifyMask`、`DrawMaskOnImage`、`Int`、`ImageFromBatch`、`easy sam3ModelLoader`、`DownloadAndLoadNLFModel`、`ImageResizeKJv2`、`easy framesEditor`、`VHS_VideoCombine`、`DrawViTPose`、`SDPoseOODLoader`、`PoseDetectionOneToAllAnimation`、`SDPoseOODProcessor`、`GroundingDinoModelLoader_SDPose`、`SimpleMath+`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`PoseAndFaceDetection`、`easy sam3ImageSegmentation`、`PointsEditor`、`OnnxDetectionModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`BatchCount+`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`RepeatImageBatch`、`ImageBatch`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`ImpactConditionalBranch`、`easy compare`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`WanVideoContextOptions`、`LoadImage`、`CR Text`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`easy anythingIndexSwitch`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
