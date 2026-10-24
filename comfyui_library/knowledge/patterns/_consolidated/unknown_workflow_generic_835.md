---
name: unknown_workflow_generic_835
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.889
common_nodes: [LoadImage, Save3DAdvanced, TripoConversionNode, TripoRetargetNode, TripoRigNode, TripoTextureNodeV2]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json, comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json, comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_835

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json、comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json、comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `Save3DAdvanced`
- `TripoConversionNode`
- `TripoRetargetNode`
- `TripoRigNode`
- `TripoTextureNodeV2`

**可变部分**（部分 workflow 才有）：
- `TripoImageToModelNodeV2` —— 1/3 个有
- `TripoPSeriesImageToModelNode` —— 1/3 个有
- `TripoPSeriesMultiviewToModelNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
