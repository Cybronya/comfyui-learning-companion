---
name: unknown_workflow_video_237
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.625
common_nodes: [ImageBatch, ImageResizeKJ, LoadImage, PrimitiveInt, SimpleMath+, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine, VHS_VideoInfoSource, easy showAnything]
problems: []
missing: []
members: [平台全量/视频立方体转场效果_1978735163066699778.json, 平台全量/视频翻转转场效果_1978729678141853698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_237

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频立方体转场效果_1978735163066699778.json、平台全量/视频翻转转场效果_1978729678141853698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageBatch`
- `ImageResizeKJ`
- `LoadImage`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `VideoCubeTransitionNode` —— 1/2 个有
- `VideoPageTurnNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
