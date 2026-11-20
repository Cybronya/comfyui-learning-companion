---
name: unknown_workflow_upscale_79
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7085
common_nodes: [LoadImage, PrimitiveInt, SaveImage, SeedVR2TilingUpscaler]
problems: []
missing: []
members: [图片生成/图生图/高清放大工作流｜SeedVR2_7B_分块渲染_8K_无损放大_2098343320027230209.json, 平台全量/高清放大工作流｜SeedVR2 7B 分块渲染 8K 无损放大_2098032242214924289.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_79

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清放大工作流｜SeedVR2_7B_分块渲染_8K_无损放大_2098343320027230209.json、平台全量/高清放大工作流｜SeedVR2 7B 分块渲染 8K 无损放大_2098032242214924289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2TilingUpscaler`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
