---
name: unknown_workflow_controlnet_video_lora_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4782
common_nodes: [BBoxYOLO, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, INTConstant, ImageResizeKJv2, ImpactConditionalBranch, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PoseJSONToPoseKeypoint, PoseKeypointPreview, PreviewImage, PrimitiveBoolean, SDPoseKeypointExtractor, Seed (rgthree), SetNode, SimpleMath+, VHS_VideoCombine, VHS_VideoInfo, WanAnimatePlus AnimateEmbeds, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TorchCompileSettings, WanAnimatePlus VAELoader, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/【咸鱼店：AI军火商】Wan2.2 Animate动作迁移 姿态对齐+Sam3.1+SDPose_2059626309025882113.json, 视频生成/图生视频/动作迁移-动物专用 Wan Animate  Plus 王炸！_2064268143333302273.json, 视频生成/图生视频/动作迁移：单人！Wan Animate  PlusV5  王炸！_2065117687663128577.json, 视频生成/文生视频/【动作迁移】工作流 V5完美升级版_2101314277561954306.json, 视频生成/文生视频/动作迁移：多人！Wan Animate  PlusV5 王炸！_2064360419841634305.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【咸鱼店：AI军火商】Wan2.2 Animate动作迁移 姿态对齐+Sam3.1+SDPose_2059626309025882113.json、视频生成/图生视频/动作迁移-动物专用 Wan Animate  Plus 王炸！_2064268143333302273.json、视频生成/图生视频/动作迁移：单人！Wan Animate  PlusV5  王炸！_2065117687663128577.json、视频生成/文生视频/【动作迁移】工作流 V5完美升级版_2101314277561954306.json、视频生成/文生视频/动作迁移：多人！Wan Animate  PlusV5 王炸！_2064360419841634305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 5 个 workflow 都包含：
- `BBoxYOLO`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PoseJSONToPoseKeypoint`
- `PoseKeypointPreview`
- `PreviewImage`
- `PrimitiveBoolean`
- `SDPoseKeypointExtractor`
- `Seed (rgthree)`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimatePlus AnimateEmbeds`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus VAELoader`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 4/5 个有
- `JjkText` —— 4/5 个有
- `VHS_LoadVideoFFmpeg` —— 4/5 个有
- `WanAnimatePlus ContextOptions` —— 4/5 个有
- `WanAnimatePlus TextEncodeCached` —— 4/5 个有
- `LoadVideoUI` —— 3/5 个有
- `DF_Float` —— 2/5 个有
- `Float to Int` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `VHS_VideoInfoLoaded` —— 2/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `VHS_LoadImagesPath` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有
- `intToFloat _O` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
