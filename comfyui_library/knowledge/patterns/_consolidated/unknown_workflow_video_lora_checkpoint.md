---
name: unknown_workflow_video_lora_checkpoint
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.446923
common_nodes: [BBoxYOLO, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PreviewImage, SDPoseKeypointExtractor, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2063268215194742785.json, 视频生成/图生视频/2069239719984189441.json, 视频生成/图生视频/2061263344446828545.json, 视频生成/图生视频/2063811846200713218.json, 视频生成/图生视频/2064236484089171969.json, 视频生成/图生视频/2064605018237530113.json, 视频生成/图生视频/2062733771589373954.json, 视频生成/图生视频/2069037364332294145.json, 视频生成/图生视频/2062892652022030338.json, 视频生成/图生视频/2063193185219858434.json, 视频生成/图生视频/2066425187536564226.json, 视频生成/图生视频/顶级视频换人（变装跳舞专用）_2099576921075052545.json, 视频生成/图生视频/2063449521627160577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_checkpoint

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2063268215194742785.json、视频生成/图生视频/2069239719984189441.json、视频生成/图生视频/2061263344446828545.json、视频生成/图生视频/2063811846200713218.json、视频生成/图生视频/2064236484089171969.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 13 个 workflow 都包含：
- `BBoxYOLO`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 12/13 个有
- `WanVideoEncode` —— 12/13 个有
- `WanVideoSamplerFromSettings` —— 12/13 个有
- `WanVideoSamplerSettings` —— 12/13 个有
- `WanVideoUni3C_ControlnetLoader` —— 12/13 个有
- `WanVideoUni3C_embeds` —— 12/13 个有
- `BlockifyMask` —— 11/13 个有
- `CLIPTextEncode` —— 11/13 个有
- `DrawMaskOnImage` —— 11/13 个有
- `GrowMaskWithBlur` —— 11/13 个有
- `ImageBlend` —— 11/13 个有
- `MaskToImage` —— 11/13 个有
- `SAM3_Detect` —— 11/13 个有
- `SegmentQueueRunner` —— 11/13 个有
- `SimpleMath+` —— 3/13 个有
- `BodyRatioMapperProportionTransfer` —— 2/13 个有
- `ImpactConditionalBranch` —— 2/13 个有
- `ImpactSwitch` —— 2/13 个有
- `PoseJSONToPoseKeypoint` —— 2/13 个有
- `PoseKeypointPreview` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `Any Switch (rgthree)` —— 1/13 个有
- `BatchCount+` —— 1/13 个有
- `Bjornulf_ShowInt` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `ChangeImageBatchSize //Inspire` —— 1/13 个有
- `ComfySwitchNode` —— 1/13 个有
- `DF_Float` —— 1/13 个有
- `Image Blank` —— 1/13 个有
- `ImageBatchMulti` —— 1/13 个有
- `ImageCompositeMasked` —— 1/13 个有
- `ImpactImageInfo` —— 1/13 个有
- `Int` —— 1/13 个有
- `JjkText` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `PointsEditor` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `RepeatImageBatch` —— 1/13 个有
- `ReverseImageBatch` —— 1/13 个有
- `Text` —— 1/13 个有
- `WanVideoSampler` —— 1/13 个有
- `easy int` —— 1/13 个有
- `easy mathInt` —— 1/13 个有
- `easy showAnything` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
