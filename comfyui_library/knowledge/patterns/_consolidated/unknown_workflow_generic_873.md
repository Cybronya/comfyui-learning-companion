---
name: unknown_workflow_generic_873
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.592
common_nodes: [HYPIRImageRestoration, Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/HYPIR 高清放大（央视推荐）_1951868106232811521.json, 图片生成/图生图/HYPIR-无损高清修复_1965092092236189697.json, 图片生成/图生图/RTX4k超分+HYPIR高清放大加二次修复_2038617804471017473.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_873

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/HYPIR 高清放大（央视推荐）_1951868106232811521.json、图片生成/图生图/HYPIR-无损高清修复_1965092092236189697.json、图片生成/图生图/RTX4k超分+HYPIR高清放大加二次修复_2038617804471017473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
- `HYPIRImageRestoration`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
