---
name: unknown_workflow_generic_1455
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [LoadImage, RH_SeedreamV5LiteTextToImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/02豆包_SeedreamV5Lite_文生图+全节点注释_2058541341457608706.json, 图片生成/文生图/2029812011953033217.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1455

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/02豆包_SeedreamV5Lite_文生图+全节点注释_2058541341457608706.json、图片生成/文生图/2029812011953033217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_SeedreamV5LiteTextToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DoubaoSizePreset` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
