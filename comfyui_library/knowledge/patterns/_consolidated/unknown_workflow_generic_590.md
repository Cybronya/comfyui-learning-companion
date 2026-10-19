---
name: unknown_workflow_generic_590
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [LoadImage, SaveGLB, TripoImageToModelNode, TripoRetargetNode, TripoRigNode, TripoTextureNode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_tripo3_0_image_to_model.json, comfyui-workflow-templates-json/api_tripo_image_to_model.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_590

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_tripo3_0_image_to_model.json、comfyui-workflow-templates-json/api_tripo_image_to_model.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveGLB`
- `TripoImageToModelNode`
- `TripoRetargetNode`
- `TripoRigNode`
- `TripoTextureNode`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `Preview3D` —— 1/2 个有
- `TripoConversionNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
