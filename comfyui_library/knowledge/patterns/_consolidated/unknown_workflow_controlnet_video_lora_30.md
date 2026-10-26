---
name: unknown_workflow_controlnet_video_lora_30
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.582
common_nodes: [BBoxYOLO, BatchCount+, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimatePlus AnimateEmbeds, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus Encode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus Sampler, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus Uni3C ControlnetLoader, WanAnimatePlus Uni3C Embeds, WanAnimatePlus VAELoader, YOLOModelLoader, easy boolean, easy cleanGpuUsed, easy compare, easy float, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json, 视频生成/图生视频/仔仔动作迁移V9（多参考图）工作流_2072698338717294593.json, 视频生成/图生视频/小陆动作迁移V9（多参考图）工作流_2075957594660888578.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json、视频生成/图生视频/仔仔动作迁移V9（多参考图）工作流_2072698338717294593.json、视频生成/图生视频/小陆动作迁移V9（多参考图）工作流_2075957594660888578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxYOLO`
- `BatchCount+`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LazySwitch2way`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimatePlus AnimateEmbeds`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus Encode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus Uni3C ControlnetLoader`
- `WanAnimatePlus Uni3C Embeds`
- `WanAnimatePlus VAELoader`
- `YOLOModelLoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy compare`
- `easy float`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `AnyBooleanSwitch` —— 2/3 个有
- `BatchImagesNode` —— 2/3 个有
- `BodyRatioMapperProportionTransfer` —— 2/3 个有
- `BodyRatioMapperSDPoseRender` —— 2/3 个有
- `DrawViTPose` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LayerUtility: ColorImage V2` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
