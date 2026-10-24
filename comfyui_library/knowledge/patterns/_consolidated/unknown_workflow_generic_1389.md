---
name: unknown_workflow_generic_1389
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, LoadImage, RH_RhartImageG2OfficialImageToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/批量+改色(G-2.0)_2045144708422307842.json, 图片生成/文生图/Image2.0文生图_2046782365061615618.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1389

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量+改色(G-2.0)_2045144708422307842.json、图片生成/文生图/Image2.0文生图_2046782365061615618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LoadImage`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextJoin` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
