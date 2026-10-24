---
name: unknown_workflow_generic_1464
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [RH_RhartImageGTextToImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/GSeries_TextToImage_v1.0_2033744913476624386.json, 图片生成/文生图/文生图4.2_text_to_image+全节点注释_2059600835008618498.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1464

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/GSeries_TextToImage_v1.0_2033744913476624386.json、图片生成/文生图/文生图4.2_text_to_image+全节点注释_2059600835008618498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `RH_RhartImageGTextToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
