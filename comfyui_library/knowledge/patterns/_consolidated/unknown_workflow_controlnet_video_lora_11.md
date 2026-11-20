---
name: unknown_workflow_controlnet_video_lora_11
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.439444
common_nodes: [BBoxYOLO, BlockifyMask, BodyRatioMapperSDPoseRender, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, INTConstant, ImageBlend, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PreviewImage, SAM3_Detect, SDPoseKeypointExtractor, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json, 视频生成/图生视频/720p 四图直出！效果炸裂-wan animate最新动作迁移_2063268215194742785.json, 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2061263344446828545.json, 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2063811846200713218.json, 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064236484089171969.json, 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064605018237530113.json, 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+_2062733771589373954.json, 视频生成/图生视频/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2069037364332294145.json, 视频生成/图生视频/高质量人物替换_2063449521627160577.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json、视频生成/图生视频/720p 四图直出！效果炸裂-wan animate最新动作迁移_2063268215194742785.json、视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2061263344446828545.json、视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2063811846200713218.json、视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064236484089171969.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 9 个 workflow 都包含：
- `BBoxYOLO`
- `BlockifyMask`
- `BodyRatioMapperSDPoseRender`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageBlend`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SAM3_Detect`
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
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSamplerFromSettings` —— 8/9 个有
- `WanVideoSamplerSettings` —— 8/9 个有
- `SegmentQueueRunner` —— 7/9 个有
- `ImpactSwitch` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `BatchCount+` —— 2/9 个有
- `BodyRatioMapperProportionTransfer` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `ChangeImageBatchSize //Inspire` —— 2/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `Image Blank` —— 2/9 个有
- `ImageBatchMulti` —— 2/9 个有
- `ImageCompositeMasked` —— 2/9 个有
- `ImpactConditionalBranch` —— 2/9 个有
- `ImpactImageInfo` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `PointsEditor` —— 2/9 个有
- `PoseJSONToPoseKeypoint` —— 2/9 个有
- `PoseKeypointPreview` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `RepeatImageBatch` —— 2/9 个有
- `ReverseImageBatch` —— 2/9 个有
- `easy int` —— 2/9 个有
- `easy mathInt` —— 2/9 个有
- `Bjornulf_ShowInt` —— 1/9 个有
- `DF_Float` —— 1/9 个有
- `Int` —— 1/9 个有
- `WanVideoSampler` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
