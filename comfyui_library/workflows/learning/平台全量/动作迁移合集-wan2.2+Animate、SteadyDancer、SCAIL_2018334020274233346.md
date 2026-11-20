---
key: 平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json
name: 动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json
hash: 0f241167ddafdaf8
coverage: 0.942149
learned_at: 2026-11-14 01:45:53
nodes: [WanVideoScheduler, WanVideoTextEncode, WanVideoSamplerExtraArgs, easy compare, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SDPoseOODLoader, GroundingDinoModelLoader_SDPose, WanVideoTextEncode, WanVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetImageRangeFromBatch, WanVideoAddSteadyDancerEmbeds, PoseDetectionVitPoseToDWPose, SimpleCalculatorKJ, RenderNLFPoses, WanVideoSamplerv2, WanVideoEmptyEmbeds, easy int, WanVideoModelLoader, WanVideoModelLoader, Note, CR Text, easy int, easy int, easy compare, WanVideoDecode, PoseDetectionVitPoseToDWPose, WanVideoContextOptions, ImageFromBatch+, DWPreprocessor, WanVideoDecode, WanVideoClipVisionEncode, GetImageRangeFromBatch, LazySwitch1way, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, WanVideoTextEncode, SimpleCalculatorKJ, CLIPVisionLoader, SDPoseOODProcessor, WanVideoAnimateEmbeds, DrawViTPose, easy compare, easy compare, LazySwitch1way, EmptyImage, LazySwitch1way, LazySwitch1way, easy int, easy int, WanVideoClipVisionEncode, SDPoseOODProcessor, ImageResizeKJv2, WanVideoContextOptions, VHS_VideoInfoLoaded, ImageResizeKJv2, WanVideoLoraSelect, WanVideoUni3C_ControlnetLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoUni3C_embeds, WanVideoEncode, WanVideoUni3C_embeds, WanVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoSamplerFromSettings, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, NLFPredict, PoseDetectionOneToAllAnimation, Note, easy int, Note, Note, PrimitiveBoolean, WanVideoBlockSwap, WanVideoSamplerSettings, WanVideoSchedulerv2, ImageFromBatch+, ImageFromBatch+, LayerUtility: PurgeVRAM V2, LazySwitch1way, VHS_VideoCombine, WanVideoClipVisionEncode, ImpactSwitch, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, easy int, easy int, easy int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, easy int, LayerUtility: PurgeVRAM V2, easy int, easy compare, LazySwitch1way, LayerUtility: PurgeVRAM V2, Note, VHS_LoadVideo, LoadImage, LoadNLFModel, LayerUtility: ImageScaleByAspectRatio V2, easy compare, LazySwitch1way, easy int, ConvertOpenPoseKeypointsToDWPose, ImpactSwitch, LazySwitch1way, easy compare, easy int]
patterns: []
missing: []
---

# 平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（121 个）：
- `WanVideoScheduler`
- `WanVideoTextEncode`
- `WanVideoSamplerExtraArgs` ★核心
- `easy compare`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SDPoseOODLoader`
- `GroundingDinoModelLoader_SDPose`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetImageRangeFromBatch`
- `WanVideoAddSteadyDancerEmbeds`
- `PoseDetectionVitPoseToDWPose`
- `SimpleCalculatorKJ`
- `RenderNLFPoses`
- `WanVideoSamplerv2` ★核心
- `WanVideoEmptyEmbeds`
- `easy int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `CR Text`
- `easy int`
- `easy int`
- `easy compare`
- `WanVideoDecode`
- `PoseDetectionVitPoseToDWPose`
- `WanVideoContextOptions`
- `ImageFromBatch+`
- `DWPreprocessor`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `LazySwitch1way`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `WanVideoTextEncode`
- `SimpleCalculatorKJ`
- `CLIPVisionLoader`
- `SDPoseOODProcessor`
- `WanVideoAnimateEmbeds`
- `DrawViTPose`
- `easy compare`
- `easy compare`
- `LazySwitch1way`
- `EmptyImage`
- `LazySwitch1way`
- `LazySwitch1way`
- `easy int`
- `easy int`
- `WanVideoClipVisionEncode`
- `SDPoseOODProcessor`
- `ImageResizeKJv2`
- `WanVideoContextOptions`
- `VHS_VideoInfoLoaded`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `NLFPredict`
- `PoseDetectionOneToAllAnimation`
- `Note`
- `easy int`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `WanVideoBlockSwap`
- `WanVideoSamplerSettings` ★核心
- `WanVideoSchedulerv2`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM V2`
- `LazySwitch1way`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `ImpactSwitch`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `easy int`
- `easy int`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `easy int`
- `LayerUtility: PurgeVRAM V2`
- `easy int`
- `easy compare`
- `LazySwitch1way`
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadNLFModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy compare`
- `LazySwitch1way`
- `easy int`
- `ConvertOpenPoseKeypointsToDWPose`
- `ImpactSwitch`
- `LazySwitch1way`
- `easy compare`
- `easy int`

## 知识

覆盖率 **94%**（114/121）

**有卡**：`WanVideoScheduler`、`WanVideoTextEncode`、`WanVideoSamplerExtraArgs`、`easy compare`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`SDPoseOODLoader`、`GroundingDinoModelLoader_SDPose`、`WanVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageRangeFromBatch`、`WanVideoAddSteadyDancerEmbeds`、`PoseDetectionVitPoseToDWPose`、`SimpleCalculatorKJ`、`RenderNLFPoses`、`WanVideoSamplerv2`、`WanVideoEmptyEmbeds`、`easy int`、`CR Text`、`WanVideoDecode`、`WanVideoContextOptions`、`ImageFromBatch+`、`DWPreprocessor`、`WanVideoClipVisionEncode`、`LazySwitch1way`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`SDPoseOODProcessor`、`WanVideoAnimateEmbeds`、`DrawViTPose`、`EmptyImage`、`VHS_VideoInfoLoaded`、`WanVideoLoraSelect`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSamplerFromSettings`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoAddSCAILReferenceEmbeds`、`NLFPredict`、`PoseDetectionOneToAllAnimation`、`PrimitiveBoolean`、`WanVideoSamplerSettings`、`WanVideoSchedulerv2`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`VHS_LoadVideo`、`LoadImage`、`LoadNLFModel`、`ConvertOpenPoseKeypointsToDWPose`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、ConvertOpenPoseKeypointsToDWPose、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoSamplerExtraArgs、WanVideoSamplerFromSettings、WanVideoSamplerSettings
