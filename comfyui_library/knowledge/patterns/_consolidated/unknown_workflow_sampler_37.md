---
name: unknown_workflow_sampler_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3665
common_nodes: [CR Text, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RunningHub USO Loader, RunningHub USO Sampler, SaveImage, easy int]
problems: []
missing: [CR Text, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, RunningHub USO Loader, easy int, RunningHub USO Sampler]
members: [图片生成/文生图/1968119490942763009.json, 图片生成/文生图/1968132053638217730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1968119490942763009.json、图片生成/文生图/1968132053638217730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：37%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ColorImage、LayerUtility: ImageScaleByAspectRatio V2、RunningHub USO Loader、easy int
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
