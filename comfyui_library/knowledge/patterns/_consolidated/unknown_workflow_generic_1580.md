---
name: unknown_workflow_generic_1580
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [LoadImage, PrimitiveStringMultiline, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/香蕉 Banan图片编辑新王【单图_多图】_1960516997396180993.json, 图片生成/文生图/全能图片V1文生图_多图编辑_1987793454732390401.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1580

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/香蕉 Banan图片编辑新王【单图_多图】_1960516997396180993.json、图片生成/文生图/全能图片V1文生图_多图编辑_1987793454732390401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
