---
name: unknown_workflow_generic_1207
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [GetImageSize+, ImageCompositeMasked, InspyrenetRembg, LayerUtility: ColorImage, SaveImage, SplitImageWithAlpha]
problems: []
missing: []
members: [图片生成/图生图/抠白底图（适合产品）_1907655582273138689.json, 平台全量/电商产品抠白底图（一键快速输出）_1990263221057712129.json, 平台全量/电商产品抠白底图（一键快速输出）_1990333623750545410.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/抠白底图（适合产品）_1907655582273138689.json、平台全量/电商产品抠白底图（一键快速输出）_1990263221057712129.json、平台全量/电商产品抠白底图（一键快速输出）_1990333623750545410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize+`
- `ImageCompositeMasked`
- `InspyrenetRembg`
- `LayerUtility: ColorImage`
- `SaveImage`
- `SplitImageWithAlpha`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `LoadImagesFromURL` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
