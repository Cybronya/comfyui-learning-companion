---
name: unknown_workflow_sampler_65
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944333
common_nodes: [Kimodo_ExportBVH, Kimodo_LoadModel, Kimodo_Preview, Kimodo_Preview3D, Kimodo_Sampler, Kimodo_SaveNPZ, Kimodo_TextEncode, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/kimodo-basic_2067452656217579521.json, 平台全量/Kimodo 3D姿态骨骼动画V1_2040255986887299074.json, 平台全量/kimodo-with-post-process_2068218265180135425.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/kimodo-basic_2067452656217579521.json、平台全量/Kimodo 3D姿态骨骼动画V1_2040255986887299074.json、平台全量/kimodo-with-post-process_2068218265180135425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `Kimodo_ExportBVH`
- `Kimodo_LoadModel`
- `Kimodo_Preview`
- `Kimodo_Preview3D`
- `Kimodo_Sampler`
- `Kimodo_SaveNPZ`
- `Kimodo_TextEncode`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Kimodo_PostProcess` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `FancyTimerNode` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
