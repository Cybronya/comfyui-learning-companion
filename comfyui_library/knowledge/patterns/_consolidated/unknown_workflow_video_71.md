---
name: unknown_workflow_video_71
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6875
common_nodes: [DoubaoLLMNode, LayerFilter: HDREffects, LoadImage, PreviewImage, SaveImage, Seedream4StreamingNode, SeedreamImageGeneratorNode, SeedreamVideoGeneratorNode, ShowText|pysssss, VHS_VideoCombine]
problems: []
missing: [LayerFilter: HDREffects]
members: [图片生成/文生图/1987702955442900994.json, 视频生成/文生视频/即梦4.0EDIT 反推 视频 文生图_1987702955442900994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_71

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1987702955442900994.json、视频生成/文生视频/即梦4.0EDIT 反推 视频 文生图_1987702955442900994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `DoubaoLLMNode`
- `LayerFilter: HDREffects`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Seedream4StreamingNode`
- `SeedreamImageGeneratorNode`
- `SeedreamVideoGeneratorNode`
- `ShowText|pysssss`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: HDREffects
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
