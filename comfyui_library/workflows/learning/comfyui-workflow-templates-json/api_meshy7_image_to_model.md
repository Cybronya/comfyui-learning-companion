---
key: comfyui-workflow-templates-json/api_meshy7_image_to_model.json
name: api_meshy7_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy7_image_to_model.json
hash: 4cee0b1f0de38974
official: true
coverage: 0.875
learned_at: 2026-10-10 22:45:01
nodes: [MeshyTextureNode, MeshyAnimateModelNode, MeshyRefineNode, MeshyRigModelNode, LoadImage, MeshyImageToModelNode, MarkdownNote, SaveGLB]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_meshy7_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy7_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `MeshyTextureNode`
- `MeshyAnimateModelNode`
- `MeshyRefineNode`
- `MeshyRigModelNode`
- `LoadImage`
- `MeshyImageToModelNode`
- `MarkdownNote`
- `SaveGLB`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`MeshyTextureNode`、`MeshyAnimateModelNode`、`MeshyRefineNode`、`MeshyRigModelNode`、`LoadImage`、`MeshyImageToModelNode`、`SaveGLB`

**用到的条目**：LoadImage、SaveGLB、MeshyAnimateModelNode、MeshyImageToModelNode、MeshyRefineNode、MeshyRigModelNode、MeshyTextureNode、sd15-t2i-basic
