---
name: unknown_workflow_video_204
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7195
common_nodes: [GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop, ImageResizeKJv2, MaskBoundingBox+, MaskPreview, MaskToSEGS, SAMLoader, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SegsToCombinedMask, SetNode, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SeedVR2 视频高清放大_1973981554160611329.json, 视频生成/图生视频/2025-07-12 SeedVR2 视频放大与人脸修复_1944421864041271297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_204

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/SeedVR2 视频高清放大_1973981554160611329.json、视频生成/图生视频/2025-07-12 SeedVR2 视频放大与人脸修复_1944421864041271297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageResizeKJv2`
- `MaskBoundingBox+`
- `MaskPreview`
- `MaskToSEGS`
- `SAMLoader`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SegsToCombinedMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWFloat` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
