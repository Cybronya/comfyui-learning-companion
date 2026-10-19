---
name: unknown_workflow_generic_655
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6875
common_nodes: [LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/1969685223988490242.json, 图片生成/文生图/年龄修改器Face Aging_1864266312905080833.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_655

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1969685223988490242.json、图片生成/文生图/年龄修改器Face Aging_1864266312905080833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AgeTransformationNode` —— 1/2 个有
- `TutengGeminiAPI` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
