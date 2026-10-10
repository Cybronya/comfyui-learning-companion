---
key: comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json
name: api_meshy7_1_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json
hash: f8ac869569c3847e
official: true
coverage: 0.875
learned_at: 2026-10-10 22:45:00
nodes: [MeshyTextureNode, MeshyAnimateModelNode, MeshyRefineNode, MeshyRigModelNode, LoadImage, MeshyImageToModelNode, MarkdownNote, Save3DAdvanced]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_meshy7_1_image_to_model.json`

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
- `Save3DAdvanced`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`MeshyTextureNode`、`MeshyAnimateModelNode`、`MeshyRefineNode`、`MeshyRigModelNode`、`LoadImage`、`MeshyImageToModelNode`、`Save3DAdvanced`

**用到的条目**：LoadImage、Save3DAdvanced、MeshyAnimateModelNode、MeshyImageToModelNode、MeshyRefineNode、MeshyRigModelNode、MeshyTextureNode、sd15-t2i-basic
