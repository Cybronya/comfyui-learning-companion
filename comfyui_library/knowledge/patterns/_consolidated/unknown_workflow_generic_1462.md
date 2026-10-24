---
name: unknown_workflow_generic_1462
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [RH_RhartImageG3TextToImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/G3_TextToImage_v3.0_2033739292979236866.json, 图片生成/文生图/文生图1r_次 3_text_to_image+全节点注释_2059599731541762050.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1462

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/G3_TextToImage_v3.0_2033739292979236866.json、图片生成/文生图/文生图1r_次 3_text_to_image+全节点注释_2059599731541762050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `RH_RhartImageG3TextToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
