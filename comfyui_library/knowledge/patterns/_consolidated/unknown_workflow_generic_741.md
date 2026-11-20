---
name: unknown_workflow_generic_741
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9056
common_nodes: [LoadImage, Preview3D, RunningHubPixal3DImageTo3D, RunningHubPixal3DModelLoader, RunningHubPixal3DSaveGLB, easy saveText]
problems: []
missing: []
members: [平台全量/Pixal3D 图像生成3D_2055311140476989441.json, 平台全量/Pixal3D 图像生成3D_2055478344984080386.json, 平台全量/Pixal3D 图像生成3D_2056375491925471233.json, 平台全量/Pixal3D 图像生成3D_2057418953923850241.json, 平台全量/Pixal3D_图转3D_2057070083079499778.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_741

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Pixal3D 图像生成3D_2055311140476989441.json、平台全量/Pixal3D 图像生成3D_2055478344984080386.json、平台全量/Pixal3D 图像生成3D_2056375491925471233.json、平台全量/Pixal3D 图像生成3D_2057418953923850241.json、平台全量/Pixal3D_图转3D_2057070083079499778.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `Preview3D`
- `RunningHubPixal3DImageTo3D`
- `RunningHubPixal3DModelLoader`
- `RunningHubPixal3DSaveGLB`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
