---
name: unknown_workflow_video_sampler_75
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [AutoCropFaces, CM_FloatToInt, ColorMatch, Float, GetVideoComponents, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadVideo, Pick From Batch (mtb), PreviewImage, PrimitiveInt, RHHiddenNodes, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, SimpleMath+, VHS_VideoCombine, 视频缩放]
problems: []
missing: []
members: [平台全量/视频换脸100%一致性最强字节DreamID-V_2086068155096584194.json, 视频生成/图生视频/视频换脸100%一致性最强字节DreamID-V_2009464356030910465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_75

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频换脸100%一致性最强字节DreamID-V_2086068155096584194.json、视频生成/图生视频/视频换脸100%一致性最强字节DreamID-V_2009464356030910465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AutoCropFaces`
- `CM_FloatToInt`
- `ColorMatch`
- `Float`
- `GetVideoComponents`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadVideo`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `PrimitiveInt`
- `RHHiddenNodes`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `SimpleMath+`
- `VHS_VideoCombine`
- `视频缩放`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
