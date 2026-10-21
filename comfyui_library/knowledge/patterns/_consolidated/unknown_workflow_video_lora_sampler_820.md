---
name: unknown_workflow_video_lora_sampler_820
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5515
common_nodes: [BBoxYOLO, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SDPoseKeypointExtractor, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2061297116642893825.json, 视频生成/图生视频/2055488451797110785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_820

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2061297116642893825.json、视频生成/图生视频/2055488451797110785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxYOLO`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SDPoseKeypointExtractor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `SegmentQueueRunner` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `ZML_AnyTypeSwitchFive` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
