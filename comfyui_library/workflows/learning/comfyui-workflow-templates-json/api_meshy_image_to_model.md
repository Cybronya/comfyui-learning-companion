---
key: comfyui-workflow-templates-json/api_meshy_image_to_model.json
name: api_meshy_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy_image_to_model.json
hash: 769f032d5d3005db
official: true
coverage: 0.888889
learned_at: 2026-10-10 22:45:03
nodes: [MeshyTextureNode, MeshyAnimateModelNode, MeshyRefineNode, MeshyRigModelNode, LoadImage, MarkdownNote, SaveGLB, SaveGLB, MeshyImageToModelNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_meshy_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `MeshyTextureNode`
- `MeshyAnimateModelNode`
- `MeshyRefineNode`
- `MeshyRigModelNode`
- `LoadImage`
- `MarkdownNote`
- `SaveGLB`
- `SaveGLB`
- `MeshyImageToModelNode`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`MeshyTextureNode`、`MeshyAnimateModelNode`、`MeshyRefineNode`、`MeshyRigModelNode`、`LoadImage`、`SaveGLB`、`MeshyImageToModelNode`

**用到的条目**：LoadImage、SaveGLB、MeshyAnimateModelNode、MeshyImageToModelNode、MeshyRefineNode、MeshyRigModelNode、MeshyTextureNode、sd15-t2i-basic
