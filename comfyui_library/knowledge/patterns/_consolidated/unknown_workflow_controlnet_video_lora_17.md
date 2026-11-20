---
name: unknown_workflow_controlnet_video_lora_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.571143
common_nodes: [BBoxYOLO, BatchCount+, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RepeatImageBatch, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimatePlus AnimateEmbeds, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus Encode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus Sampler, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus Uni3C ControlnetLoader, WanAnimatePlus Uni3C Embeds, WanAnimatePlus VAELoader, YOLOModelLoader, easy compare, easy float, easy int, easy mathInt]
problems: []
missing: []
members: [平台全量/Animate动作迁移V9（多参考图）_2061660674434101250.json, 平台全量/动作迁移PLUS多参版_2099363885118738434.json, 平台全量/动作迁移PLUS多参版_2101498269846302722.json, 平台全量/动作迁移PLUS多参版_2102661616935456769.json, 视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json, 视频生成/图生视频/仔仔动作迁移V9（多参考图）工作流_2072698338717294593.json, 视频生成/图生视频/小陆动作迁移V9（多参考图）工作流_2075957594660888578.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Animate动作迁移V9（多参考图）_2061660674434101250.json、平台全量/动作迁移PLUS多参版_2099363885118738434.json、平台全量/动作迁移PLUS多参版_2101498269846302722.json、平台全量/动作迁移PLUS多参版_2102661616935456769.json、视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
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
- `easy compare`
- `easy float`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 6/7 个有
- `BodyRatioMapperProportionTransfer` —— 6/7 个有
- `BodyRatioMapperSDPoseRender` —— 6/7 个有
- `DrawViTPose` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LayerUtility: ColorImage V2` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `PreviewImage` —— 4/7 个有
- `RHHiddenNodes` —— 4/7 个有
- `easy boolean` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `AnyBooleanSwitch` —— 3/7 个有
- `CM_IntBinaryOperation` —— 3/7 个有
- `GoohaiUniversalSlider` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `VRAM_Debug` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `布尔孤海` —— 3/7 个有
- `忽略多组孤海` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSize+` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
