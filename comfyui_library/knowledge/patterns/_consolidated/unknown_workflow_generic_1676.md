---
name: unknown_workflow_generic_1676
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5
common_nodes: [LoadImage, LoadVideo, PrimitiveInt, RHBerniniFullReferenceVideoToVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/(满血版)Bernini-Full 参考+视频编辑V1_2067135489085366274.json, 视频生成/图生视频/Bernini-Full 参考图编辑视频_2067147092631572482.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1676

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/(满血版)Bernini-Full 参考+视频编辑V1_2067135489085366274.json、视频生成/图生视频/Bernini-Full 参考图编辑视频_2067147092631572482.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoadVideo`
- `PrimitiveInt`
- `RHBerniniFullReferenceVideoToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `JjkText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
