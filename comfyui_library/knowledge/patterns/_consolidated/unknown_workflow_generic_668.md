---
name: unknown_workflow_generic_668
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [InspyrenetRembg, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键去背景+遮罩生成 Inspyrenet Rembg_1937460712161886209.json, 图片生成/图生图/一键抠图_2026831606878572545.json, 图片生成/图生图/一键抠图_2070166368229609474.json, 图片生成/图生图/快速抠像_2052668485251149826.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_668

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键去背景+遮罩生成 Inspyrenet Rembg_1937460712161886209.json、图片生成/图生图/一键抠图_2026831606878572545.json、图片生成/图生图/一键抠图_2070166368229609474.json、图片生成/图生图/快速抠像_2052668485251149826.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `InspyrenetRembg`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageCombineAlpha` —— 2/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
