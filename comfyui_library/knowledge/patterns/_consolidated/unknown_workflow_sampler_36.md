---
name: unknown_workflow_sampler_36
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78925
common_nodes: [LoadImage, SaveImage, SenseNova_SM_Model, SenseNova_SM_Sampler]
problems: []
missing: []
members: [图片生成/图生图/SenseNova U1-图像编辑-商汤-日日新_2091321728873099266.json, 图片生成/图生图/SenseNova 单图编辑_2053113135225163778.json, 图片生成/文生图/商汤SenseNova-U1_2052931963757051905.json, 图片生成/文生图/商汤SenseNova-U1_2056611909402714114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_36

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SenseNova U1-图像编辑-商汤-日日新_2091321728873099266.json、图片生成/图生图/SenseNova 单图编辑_2053113135225163778.json、图片生成/文生图/商汤SenseNova-U1_2052931963757051905.json、图片生成/文生图/商汤SenseNova-U1_2056611909402714114.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SenseNova_SM_Model`
- `SenseNova_SM_Sampler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
