---
name: unknown_workflow_video_208
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [GetImageRangeFromBatch, Image Comparer (rgthree), SeedVR2BlockSwap, SeedVR2GGUF, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, easy int]
problems: []
missing: []
members: [平台全量/【GGUF版】SeedVR2_视频放大_超清放大_1960889038549004289.json, 平台全量/【GGUF版加速版全模型】SeedVR2 视频放大视频超清放大视频超分加速全模型3b到7b全模型_2011813909161844737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_208

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【GGUF版】SeedVR2_视频放大_超清放大_1960889038549004289.json、平台全量/【GGUF版加速版全模型】SeedVR2 视频放大视频超清放大视频超分加速全模型3b到7b全模型_2011813909161844737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
