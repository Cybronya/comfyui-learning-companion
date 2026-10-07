---
key: comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json
name: api_meshy_multi_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json
hash: de24bef14e5ebabb
official: true
coverage: 0.916667
learned_at: 2026-10-07 21:34:15
nodes: [MeshyAnimateModelNode, MeshyRefineNode, MeshyRigModelNode, LoadImage, LoadImage, LoadImage, MeshyTextureNode, Preview3D, MarkdownNote, SaveGLB, SaveGLB, MeshyMultiImageToModelNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy_multi_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `MeshyAnimateModelNode`
- `MeshyRefineNode`
- `MeshyRigModelNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MeshyTextureNode`
- `Preview3D`
- `MarkdownNote`
- `SaveGLB`
- `SaveGLB`
- `MeshyMultiImageToModelNode`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`MeshyAnimateModelNode`、`MeshyRefineNode`、`MeshyRigModelNode`、`LoadImage`、`MeshyTextureNode`、`Preview3D`、`SaveGLB`、`MeshyMultiImageToModelNode`

**用到的条目**：LoadImage、SaveGLB、Preview3D、MeshyAnimateModelNode、MeshyMultiImageToModelNode、MeshyRefineNode、MeshyRigModelNode、MeshyTextureNode
