---
name: unknown_workflow_generic_591
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, SaveGLB, TripoConversionNode, TripoRetargetNode, TripoRigNode, TripoTextureNodeV2]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json, comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_591

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json、comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveGLB`
- `TripoConversionNode`
- `TripoRetargetNode`
- `TripoRigNode`
- `TripoTextureNodeV2`

**可变部分**（部分 workflow 才有）：
- `TripoP1ImageToModelNode` —— 1/2 个有
- `TripoP1MultiviewToModelNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
