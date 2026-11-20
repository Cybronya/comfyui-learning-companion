---
key: 平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json
name: wan2.2 animate动作迁移V2_2054755232294416386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json
hash: c02785c5e795dff8
coverage: 0.541872
learned_at: 2026-11-14 01:19:20
nodes: [DrawViTPose, NLFPredict, WanVideoSetLoRAs, PoseDetectionVitPoseToDWPose, WanVideoModelLoader, WanVideoUni3C_ControlnetLoader, RenderNLFPoses, WanVideoSetBlockSwap, SetNode, SetNode, easy showAnything, easy showAnything, ImageFromBatch, CLIPVisionLoader, SetNode, SetNode, GetImageSize, GetNode, GetNode, SetNode, LayerUtility: ColorImage, RepeatImageBatch, GetNode, GetNode, GetNode, MaskToImage, GetNode, GetNode, Note, SetNode, GetNode, GetNode, SDPoseFaceBBoxes, SDPoseKeypointExtractor, WanVideoVAELoader, GetNode, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, GetNode, YOLOModelLoader, SDPoseOODProcessor, SetNode, VHS_VideoInfo, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, OnnxDetectionModelLoader, OnnxDetectionModelLoader, SDPoseOODLoader, VHS_VideoCombine, GetNode, easy cleanGpuUsed, easy clearCacheAll, YOLOModelLoader, GetNode, GroundingDinoModelLoader_SDPose, GetNode, GetNode, BodyRatioMapperSDPoseRender, YOLOModelLoader, BBoxYOLO, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseOODLoader, ImageCompositeMasked, ImageResizeKJv2, SetNode, SAM3_Detect, CheckpointLoaderSimple, PreviewImage, PreviewImage, LoadImage, ImageResizeKJv2, WanVideoClipVisionEncode, ImageResize+, Any Switch (rgthree), GetNode, GetNode, BlockifyMask, GrowMask, GetNode, GetImageSizeAndCount, RepeatImageBatch, SetNode, easy showAnything, Any Switch (rgthree), OnnxDetectionModelLoader, GetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, GetNode, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, SetNode, Note, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadNLFModel, GetNode, PoseDetectionVitPoseToDWPose, GetNode, GetNode, Note, OnnxDetectionModelLoader, GetNode, VHS_VideoCombine, SetNode, SetNode, SetNode, PoseAndFaceDetection, VHS_VideoCombine, Mute / Bypass Repeater (rgthree), Note, SetNode, LayerUtility: PurgeVRAM V2, GetNode, SetNode, LayerUtility: PurgeVRAM V2, WanVideoTorchCompileSettings, WanVideoBlockSwap, CheckpointLoaderSimple, GetNode, GetNode, Any Switch (rgthree), CropByBBoxes, SetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), VHS_VideoCombine, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Any Switch (rgthree), VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, SDPoseOODProcessor, BodyRatioMapperSDPoseRender, GetNode, SetNode, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncodeCached, VHS_VideoCombine, GetNode, GetNode, WanVideoEncode, WanVideoDecode, Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), Note, PreviewImage, ImageResizeKJv2, SetNode, SetNode, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, WanVideoContextOptions, WanVideoAnimateEmbeds, Int, easy int, easy int, VHS_LoadVideo, VHS_LoadVideo, SetNode, MuyeTextEditOutput, Fast Groups Muter (rgthree), Note, GroundingDinoModelLoader_SDPose, WanVideoSampler, GetNode, GetNode, PoseDetectionOneToAllAnimation, BodyRatioMapperProportionTransfer, Any Switch (rgthree), Fast Groups Muter (rgthree), CLIPTextEncode, Note, easy int, easy int, Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, WanVideoLoraSelectMulti, WanVideoUni3C_embeds]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（203 个）：
- `DrawViTPose`
- `NLFPredict`
- `WanVideoSetLoRAs`
- `PoseDetectionVitPoseToDWPose`
- `WanVideoModelLoader`
- `WanVideoUni3C_ControlnetLoader`
- `RenderNLFPoses`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `ImageFromBatch`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ColorImage`
- `RepeatImageBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `SDPoseFaceBBoxes`
- `SDPoseKeypointExtractor`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_VideoInfo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `OnnxDetectionModelLoader`
- `OnnxDetectionModelLoader`
- `SDPoseOODLoader`
- `VHS_VideoCombine`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `YOLOModelLoader`
- `GetNode`
- `GroundingDinoModelLoader_SDPose`
- `GetNode`
- `GetNode`
- `BodyRatioMapperSDPoseRender`
- `YOLOModelLoader`
- `BBoxYOLO`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseOODLoader`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `SetNode`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `GrowMask`
- `GetNode`
- `GetImageSizeAndCount`
- `RepeatImageBatch`
- `SetNode`
- `easy showAnything`
- `Any Switch (rgthree)`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadNLFModel`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `GetNode`
- `Note`
- `OnnxDetectionModelLoader`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `Mute / Bypass Repeater (rgthree)`
- `Note`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `CropByBBoxes`
- `SetNode`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SDPoseOODProcessor`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `SetNode`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoDecode`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `Note`
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `Int`
- `easy int`
- `easy int`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SetNode`
- `MuyeTextEditOutput`
- `Fast Groups Muter (rgthree)`
- `Note`
- `GroundingDinoModelLoader_SDPose`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `BodyRatioMapperProportionTransfer`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `easy int`
- `easy int`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `WanVideoUni3C_embeds`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **54%**（110/203）

**有卡**：`DrawViTPose`、`NLFPredict`、`WanVideoSetLoRAs`、`PoseDetectionVitPoseToDWPose`、`WanVideoModelLoader`、`WanVideoUni3C_ControlnetLoader`、`RenderNLFPoses`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`CLIPVisionLoader`、`GetImageSize`、`LayerUtility: ColorImage`、`RepeatImageBatch`、`MaskToImage`、`SDPoseFaceBBoxes`、`SDPoseKeypointExtractor`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`YOLOModelLoader`、`SDPoseOODProcessor`、`VHS_VideoInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`OnnxDetectionModelLoader`、`SDPoseOODLoader`、`easy cleanGpuUsed`、`easy clearCacheAll`、`GroundingDinoModelLoader_SDPose`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`CheckpointLoaderSimple`、`ImageCompositeMasked`、`ImageResizeKJv2`、`SAM3_Detect`、`LoadImage`、`WanVideoClipVisionEncode`、`ImageResize+`、`BlockifyMask`、`GrowMask`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadNLFModel`、`Mute / Bypass Repeater (rgthree)`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CropByBBoxes`、`Mute / Bypass Relay (rgthree)`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`Int`、`easy int`、`VHS_LoadVideo`、`MuyeTextEditOutput`、`WanVideoSampler`、`PoseDetectionOneToAllAnimation`、`BodyRatioMapperProportionTransfer`、`CLIPTextEncode`、`WanVideoUni3C_embeds`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode
