---
name: unknown_workflow_generic_1137
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [Flux2ImageNode, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json, comfyui-workflow-templates-json/api_flux2.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1137

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json、comfyui-workflow-templates-json/api_flux2.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Flux2ImageNode`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
