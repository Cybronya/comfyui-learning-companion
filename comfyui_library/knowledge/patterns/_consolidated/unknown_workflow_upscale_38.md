---
name: unknown_workflow_upscale_38
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82475
common_nodes: [Image Comparer (rgthree), ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/图片4倍放大高清无损_2068841438854598658.json, 平台全量/图片放大VS AuraSR_1942396580274311169.json, 平台全量/图片放大VS AuraSR_1971036437309231105.json, 平台全量/图片简单放大_2025855289089597442.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/图片4倍放大高清无损_2068841438854598658.json、平台全量/图片放大VS AuraSR_1942396580274311169.json、平台全量/图片放大VS AuraSR_1971036437309231105.json、平台全量/图片简单放大_2025855289089597442.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `AuraSR.AuraSRUpscaler` —— 2/4 个有
- `easy imageScaleDownToSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
