---
name: unknown_workflow_controlnet_video_lora_30
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.54375
common_nodes: [Any Switch (rgthree), BBoxYOLO, BlockifyMask, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, CropByBBoxes, DownloadAndLoadNLFModel, DrawViTPose, Fast Groups Muter (rgthree), GetImageSize, GetImageSizeAndCount, GetNode, GroundingDinoModelLoader_SDPose, GrowMask, ImageCompositeMasked, ImageFromBatch, ImageResize+, ImageResizeKJv2, Int, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), MuyeTextEditOutput, NLFPredict, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, RepeatImageBatch, SAM3_Detect, SDPoseFaceBBoxes, SDPoseKeypointExtractor, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader, easy cleanGpuUsed, easy clearCacheAll, easy int, easy showAnything]
problems: []
missing: []
members: [平台全量/animate动作迁移-上下文窗口方式_2060925061581856769.json, 平台全量/animate动作迁移-首帧+内循环方式_2061007357307609089.json, 平台全量/animate动作迁移-首帧方式_2060995809738575874.json, 平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/animate动作迁移-上下文窗口方式_2060925061581856769.json、平台全量/animate动作迁移-首帧+内循环方式_2061007357307609089.json、平台全量/animate动作迁移-首帧方式_2060995809738575874.json、平台全量/wan2.2 animate动作迁移V2_2054755232294416386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BBoxYOLO`
- `BlockifyMask`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `CropByBBoxes`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader_SDPose`
- `GrowMask`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `MuyeTextEditOutput`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RenderNLFPoses`
- `RepeatImageBatch`
- `SAM3_Detect`
- `SDPoseFaceBBoxes`
- `SDPoseKeypointExtractor`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy int`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
