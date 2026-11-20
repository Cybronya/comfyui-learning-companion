---
name: unknown_workflow_controlnet_video_lora_5
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.4524
common_nodes: [BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SDPoseKeypointExtractor, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/+一致性分段穿搭换衣+变装++动作迁移++动作模仿+_2063573536182198274.json, 平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json, 平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json, 平台全量/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062012284179935234.json, 平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json, 平台全量/【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058.json, 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153.json, 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138.json, 平台全量/一致性分段穿搭换衣 变装 +动作迁移 +动作模仿_2063430169309835265.json, 平台全量/二创神器：【替换视频人物】Wan Animate 新王炸！分段队列_2062182820365299714.json, 平台全量/人物替换+动作模仿+视频背景替换+运镜 视频编辑合集_2077263036775231489.json, 平台全量/人物替换+动作模仿+视频背景替换+运镜_2070471646825242626.json, 平台全量/人物替换+动作模仿+视频背景替换+运镜_2076544592090066946.json, 数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json, 视频生成/图生视频/高质量人物替换_2063449521627160577.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_5

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/+一致性分段穿搭换衣+变装++动作迁移++动作模仿+_2063573536182198274.json、平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json、平台全量/Wan2.2_Animate_单人动作迁移_姿态自动对齐_三视图一致性_2058141806164013058.json、平台全量/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062012284179935234.json、平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 15 个 workflow 都包含：
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SDPoseKeypointExtractor`
- `Seed (rgthree)`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 14/15 个有
- `INTConstant` —— 14/15 个有
- `PlaySound|pysssss` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `YOLOModelLoader` —— 14/15 个有
- `BlockifyMask` —— 13/15 个有
- `CLIPTextEncode` —— 13/15 个有
- `DrawMaskOnImage` —— 13/15 个有
- `GrowMaskWithBlur` —— 13/15 个有
- `ImageBlend` —— 13/15 个有
- `MaskToImage` —— 13/15 个有
- `SAM3_Detect` —— 13/15 个有
- `WanVideoSamplerFromSettings` —— 11/15 个有
- `WanVideoSamplerSettings` —— 11/15 个有
- `SegmentQueueRunner` —— 8/15 个有
- `SimpleMath+` —— 8/15 个有
- `BodyRatioMapperProportionTransfer` —— 7/15 个有
- `Label (rgthree)` —— 7/15 个有
- `PrimitiveBoolean` —— 7/15 个有
- `CR Text` —— 6/15 个有
- `ComfySwitchNode` —— 6/15 个有
- `ImpactConditionalBranch` —— 6/15 个有
- `PoseJSONToPoseKeypoint` —— 6/15 个有
- `PoseKeypointPreview` —— 6/15 个有
- `Primitive integer [Crystools]` —— 6/15 个有
- `easy mathInt` —— 6/15 个有
- `Any Switch (rgthree)` —— 5/15 个有
- `BatchCount+` —— 5/15 个有
- `ChangeImageBatchSize //Inspire` —— 5/15 个有
- `Image Blank` —— 5/15 个有
- `ImageBatchMulti` —— 5/15 个有
- `ImageCompositeMasked` —— 5/15 个有
- `ImpactImageInfo` —— 5/15 个有
- `ImpactSwitch` —— 5/15 个有
- `PointsEditor` —— 5/15 个有
- `PreviewAny` —— 5/15 个有
- `RepeatImageBatch` —— 5/15 个有
- `ReverseImageBatch` —— 5/15 个有
- `easy int` —— 5/15 个有
- `WanVideoSampler` —— 4/15 个有
- `Int` —— 2/15 个有
- `PrimitiveFloat` —— 2/15 个有
- `DuckHideNode` —— 1/15 个有
- `MuteSwitch` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `workflow>15` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
