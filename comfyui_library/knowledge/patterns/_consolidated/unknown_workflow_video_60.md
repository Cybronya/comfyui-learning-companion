---
name: unknown_workflow_video_60
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7205
common_nodes: [GetImageRangeFromBatch, Image Comparer (rgthree), Int, PreviewImage, SeedVR2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/自己用：视频放大_1940780956850798593.json, 平台全量/视频放大_超清放大SeedVR2_V2_1933111775560642562.json, 平台全量/视频放大_超清放大SeedVR2_V2_2000054771467812865.json, 平台全量/视频放大_超清放大SeedVR2_V2_2014658744814145538.json, 平台全量/视频超清放大（SeedVR2）_1980142752237260802.json, 视频生成/图生视频/视频放大_超清放大SeedVR2_V2_2116654061964587010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_60

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/自己用：视频放大_1940780956850798593.json、平台全量/视频放大_超清放大SeedVR2_V2_1933111775560642562.json、平台全量/视频放大_超清放大SeedVR2_V2_2000054771467812865.json、平台全量/视频放大_超清放大SeedVR2_V2_2014658744814145538.json、平台全量/视频超清放大（SeedVR2）_1980142752237260802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `Int`
- `PreviewImage`
- `SeedVR2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `SeedVR2BlockSwap` —— 5/6 个有
- `ImageScaleBy` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
