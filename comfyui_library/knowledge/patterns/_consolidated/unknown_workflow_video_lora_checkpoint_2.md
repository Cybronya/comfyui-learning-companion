---
name: unknown_workflow_video_lora_checkpoint_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7226
common_nodes: [BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SDPoseKeypointExtractor, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json, 平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json, 平台全量/电商 宠物 跳舞打窝 短视频带货_2057837373005844482.json, 视频生成/图生视频/Wan2.2-Animate长视频分段队列，丝滑换装换人_2061297116642893825.json, 视频生成/图生视频/wan-Animate全能工作流_2055488451797110785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/wan2.2-Aniamate-最强动作迁移_2054912816318042113.json、平台全量/wan2.2-Aniamate-最强多人动作迁移_2055553242943238146.json、平台全量/电商 宠物 跳舞打窝 短视频带货_2057837373005844482.json、视频生成/图生视频/Wan2.2-Animate长视频分段队列，丝滑换装换人_2061297116642893825.json、视频生成/图生视频/wan-Animate全能工作流_2055488451797110785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SDPoseKeypointExtractor`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `YOLOModelLoader` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `Int` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `VHS_VideoInfoLoaded` —— 3/5 个有
- `WanVideoSampler` —— 3/5 个有
- `WanVideoSetBlockSwap` —— 3/5 个有
- `WanVideoSetLoRAs` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `WanVideoSamplerFromSettings` —— 2/5 个有
- `WanVideoSamplerSettings` —— 2/5 个有
- `DrawViTPose` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `SegmentQueueRunner` —— 1/5 个有
- `WanVideoTeaCache` —— 1/5 个有
- `ZML_AnyTypeSwitchFive` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
