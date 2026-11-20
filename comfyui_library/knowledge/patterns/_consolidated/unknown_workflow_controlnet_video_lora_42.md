---
name: unknown_workflow_controlnet_video_lora_42
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.946
common_nodes: [CLIPVisionLoader, CR Text, ConvertOpenPoseKeypointsToDWPose, DWPreprocessor, DrawViTPose, EmptyImage, GetImageRangeFromBatch, GroundingDinoModelLoader_SDPose, ImageFromBatch+, ImageResizeKJv2, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LazySwitch1way, LoadImage, LoadNLFModel, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PoseDetectionVitPoseToDWPose, PrimitiveBoolean, RenderNLFPoses, SDPoseOODLoader, SDPoseOODProcessor, SimpleCalculatorKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoAddSteadyDancerEmbeds, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSamplerExtraArgs, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSamplerv2, WanVideoScheduler, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy compare, easy int]
problems: []
missing: []
members: [平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json, 视频生成/图生视频/动作迁移合集-图生视频-wan Animate、SteadyDancer、SCAIL_2017059703095824385.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/动作迁移合集-wan2.2+Animate、SteadyDancer、SCAIL_2018334020274233346.json、视频生成/图生视频/动作迁移合集-图生视频-wan Animate、SteadyDancer、SCAIL_2017059703095824385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `ConvertOpenPoseKeypointsToDWPose`
- `DWPreprocessor`
- `DrawViTPose`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GroundingDinoModelLoader_SDPose`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LazySwitch1way`
- `LoadImage`
- `LoadNLFModel`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PoseDetectionVitPoseToDWPose`
- `PrimitiveBoolean`
- `RenderNLFPoses`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SimpleCalculatorKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSamplerv2`
- `WanVideoScheduler`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy compare`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
