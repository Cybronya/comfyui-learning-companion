---
name: unknown_workflow_generic_1503
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [Florence2ModelLoader, Florence2Run, LoadImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/文生图/反推-图提示词-Florence_1972214705517424642.json, 图片生成/文生图/提示词反推  图片提取 文本生图_1930817149471010818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1503

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/反推-图提示词-Florence_1972214705517424642.json、图片生成/文生图/提示词反推  图片提取 文本生图_1930817149471010818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Florence2ModelLoader`
- `Florence2Run`
- `LoadImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
