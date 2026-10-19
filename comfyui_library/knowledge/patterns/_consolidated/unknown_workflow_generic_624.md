---
name: unknown_workflow_generic_624
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.571
common_nodes: [CR Prompt Text, CR Text Concatenate, KOOK_SaveJPGImage, LoadImage, RH_RhartImageG2ImageToImage, SaveImage, 忽略多组孤海]
problems: []
missing: [CR Text Concatenate, 忽略多组孤海, CR Prompt Text]
members: [图片生成/图生图/2087051938029457409.json, 图片生成/图生图/2092922360243511297.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_624

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2087051938029457409.json、图片生成/图生图/2092922360243511297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text Concatenate`
- `KOOK_SaveJPGImage`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageNG31FlashImageToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、忽略多组孤海、CR Prompt Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
