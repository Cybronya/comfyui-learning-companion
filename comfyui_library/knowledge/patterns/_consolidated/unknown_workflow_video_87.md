---
name: unknown_workflow_video_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.552
common_nodes: [ImageScaleToTotalPixels, Int, PreviewImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource]
problems: []
missing: []
members: [视频生成/图生视频/2007103726170939394.json, 视频生成/文生视频/视频高清放大合集(RTX+SeedVR2)_2100222072508211201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2007103726170939394.json、视频生成/文生视频/视频高清放大合集(RTX+SeedVR2)_2100222072508211201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `Int`
- `PreviewImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
