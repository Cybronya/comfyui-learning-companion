---
name: unknown_workflow_generic_1223
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.755667
common_nodes: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/移除产品背景+建立透明背景图+全节点注释_2057763002581078017.json, 平台全量/安-抠图王，细致到发丝_1935726958787686402.json, 平台全量/电商产品抠图_1928091323943763970.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1223

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/移除产品背景+建立透明背景图+全节点注释_2057763002581078017.json、平台全量/安-抠图王，细致到发丝_1935726958787686402.json、平台全量/电商产品抠图_1928091323943763970.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
