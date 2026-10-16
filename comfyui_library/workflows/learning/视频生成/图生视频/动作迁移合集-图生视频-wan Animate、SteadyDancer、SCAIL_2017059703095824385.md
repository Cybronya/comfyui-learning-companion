---
key: 视频生成/图生视频/动作迁移合集-图生视频-wan Animate、SteadyDancer、SCAIL_2017059703095824385.json
name: 动作迁移合集-图生视频-wan Animate、SteadyDancer、SCAIL_2017059703095824385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017059703095824385.json
hash: b936b29701f74957
coverage: 0.950413
learned_at: 2026-10-15 22:34:44
nodes: [WanVideoScheduler, WanVideoTextEncode, WanVideoSamplerExtraArgs, easy compare, easy compare, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SDPoseOODLoader, GroundingDinoModelLoader_SDPose, WanVideoTextEncode, WanVideoEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetImageRangeFromBatch, WanVideoClipVisionEncode, WanVideoAddSteadyDancerEmbeds, PoseDetectionVitPoseToDWPose, SimpleCalculatorKJ, RenderNLFPoses, WanVideoSamplerv2, WanVideoEmptyEmbeds, WanVideoSchedulerv2, easy int, WanVideoModelLoader, WanVideoModelLoader, LoadNLFModel, VHS_VideoCombine, Note, WanVideoBlockSwap, PrimitiveBoolean, CR Text, easy int, VHS_LoadVideo, easy int, easy compare, ImageFromBatch+, WanVideoDecode, WanVideoClipVisionEncode, PoseDetectionVitPoseToDWPose, WanVideoContextOptions, ImageFromBatch+, LoadImage, ImpactSwitch, easy int, easy int, DWPreprocessor, LazySwitch1way, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetImageRangeFromBatch, LazySwitch1way, ImageResizeKJv2, easy int, ImpactSwitch, easy compare, LazySwitch1way, OnnxDetectionModelLoader, LazySwitch1way, LazySwitch1way, PoseAndFaceDetection, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageFromBatch+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleCalculatorKJ, easy compare, CLIPVisionLoader, SDPoseOODProcessor, LayerUtility: ImageScaleByAspectRatio V2, easy int, DrawViTPose, easy compare, easy compare, LazySwitch1way, EmptyImage, LazySwitch1way, LazySwitch1way, easy int, easy int, WanVideoClipVisionEncode, SDPoseOODProcessor, ImageResizeKJv2, easy int, WanVideoContextOptions, ImageResizeKJv2, WanVideoLoraSelect, WanVideoUni3C_ControlnetLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoUni3C_embeds, WanVideoEncode, WanVideoUni3C_embeds, LayerUtility: ImageScaleByAspectRatio V2, WanVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSamplerSettings, WanVideoDecode, WanVideoSamplerFromSettings, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, NLFPredict, ConvertOpenPoseKeypointsToDWPose, PoseDetectionOneToAllAnimation, Note, Note, VHS_VideoInfoLoaded, WanVideoDecode, WanVideoSampler, WanVideoContextOptions, WanVideoAnimateEmbeds, easy int, easy int, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移合集-图生视频-wan Animate、SteadyDancer、SCAIL_2017059703095824385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017059703095824385.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（121 个）：
- `WanVideoScheduler`
- `WanVideoTextEncode`
- `WanVideoSamplerExtraArgs` ★核心
- `easy compare`
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
- `WanVideoClipVisionEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `PoseDetectionVitPoseToDWPose`
- `SimpleCalculatorKJ`
- `RenderNLFPoses`
- `WanVideoSamplerv2` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSchedulerv2`
- `easy int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadNLFModel`
- `VHS_VideoCombine`
- `Note`
- `WanVideoBlockSwap`
- `PrimitiveBoolean`
- `CR Text`
- `easy int`
- `VHS_LoadVideo`
- `easy int`
- `easy compare`
- `ImageFromBatch+`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `PoseDetectionVitPoseToDWPose`
- `WanVideoContextOptions`
- `ImageFromBatch+`
- `LoadImage`
- `ImpactSwitch`
- `easy int`
- `easy int`
- `DWPreprocessor`
- `LazySwitch1way`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `LazySwitch1way`
- `ImageResizeKJv2`
- `easy int`
- `ImpactSwitch`
- `easy compare`
- `LazySwitch1way`
- `OnnxDetectionModelLoader`
- `LazySwitch1way`
- `LazySwitch1way`
- `PoseAndFaceDetection`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SimpleCalculatorKJ`
- `easy compare`
- `CLIPVisionLoader`
- `SDPoseOODProcessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
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
- `easy int`
- `WanVideoContextOptions`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `NLFPredict`
- `ConvertOpenPoseKeypointsToDWPose`
- `PoseDetectionOneToAllAnimation`
- `Note`
- `Note`
- `VHS_VideoInfoLoaded`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `easy int`
- `easy int`
- `easy int`

## 知识

覆盖率 **95%**（115/121）

**有卡**：`WanVideoScheduler`、`WanVideoTextEncode`、`WanVideoSamplerExtraArgs`、`easy compare`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`SDPoseOODLoader`、`GroundingDinoModelLoader_SDPose`、`WanVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoAddSteadyDancerEmbeds`、`PoseDetectionVitPoseToDWPose`、`SimpleCalculatorKJ`、`RenderNLFPoses`、`WanVideoSamplerv2`、`WanVideoEmptyEmbeds`、`WanVideoSchedulerv2`、`easy int`、`LoadNLFModel`、`VHS_VideoCombine`、`PrimitiveBoolean`、`CR Text`、`VHS_LoadVideo`、`ImageFromBatch+`、`WanVideoDecode`、`WanVideoContextOptions`、`LoadImage`、`DWPreprocessor`、`LazySwitch1way`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`LayerUtility: PurgeVRAM V2`、`CLIPVisionLoader`、`SDPoseOODProcessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawViTPose`、`EmptyImage`、`WanVideoLoraSelect`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoSamplerSettings`、`WanVideoSamplerFromSettings`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoAddSCAILReferenceEmbeds`、`NLFPredict`、`ConvertOpenPoseKeypointsToDWPose`、`PoseDetectionOneToAllAnimation`、`VHS_VideoInfoLoaded`、`WanVideoSampler`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、ConvertOpenPoseKeypointsToDWPose、WanVideoSampler、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoSamplerFromSettings
