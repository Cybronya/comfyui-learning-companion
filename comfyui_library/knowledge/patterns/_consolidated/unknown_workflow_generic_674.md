---
name: unknown_workflow_generic_674
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.889
common_nodes: [LoadImage, MeshyAnimateModelNode, MeshyRefineNode, MeshyRigModelNode, MeshyTextureNode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json, comfyui-workflow-templates-json/api_meshy7_image_to_model.json, comfyui-workflow-templates-json/api_meshy_image_to_model.json, comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_674

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json、comfyui-workflow-templates-json/api_meshy7_image_to_model.json、comfyui-workflow-templates-json/api_meshy_image_to_model.json、comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `MeshyAnimateModelNode`
- `MeshyRefineNode`
- `MeshyRigModelNode`
- `MeshyTextureNode`

**可变部分**（部分 workflow 才有）：
- `MeshyImageToModelNode` —— 3/4 个有
- `SaveGLB` —— 3/4 个有
- `MeshyMultiImageToModelNode` —— 1/4 个有
- `Preview3D` —— 1/4 个有
- `Save3DAdvanced` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
