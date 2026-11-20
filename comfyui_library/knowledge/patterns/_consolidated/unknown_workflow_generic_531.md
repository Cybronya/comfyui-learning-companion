---
name: unknown_workflow_generic_531
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [SaveGLB, TripoConversionNode, TripoRetargetNode, TripoRigNode, TripoTextureNode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_tripo3_0_text_to_model.json, comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json, comfyui-workflow-templates-json/api_tripo3_1_text_to_model.json, comfyui-workflow-templates-json/api_tripo_multiview_to_model.json, comfyui-workflow-templates-json/api_tripo_text_to_model.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_531

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/api_tripo3_0_text_to_model.json、comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json、comfyui-workflow-templates-json/api_tripo3_1_text_to_model.json、comfyui-workflow-templates-json/api_tripo_multiview_to_model.json、comfyui-workflow-templates-json/api_tripo_text_to_model.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `SaveGLB`
- `TripoConversionNode`
- `TripoRetargetNode`
- `TripoRigNode`
- `TripoTextureNode`

**可变部分**（部分 workflow 才有）：
- `TripoTextToModelNode` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `TripoMultiviewToModelNode` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
