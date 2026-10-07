---
key: comfyui-workflow-templates-json/api_tripo_image_to_model.json
name: api_tripo_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_image_to_model.json
hash: 25162db9df71a63c
official: true
coverage: 0.875
learned_at: 2026-10-07 21:34:58
nodes: [TripoRetargetNode, TripoRigNode, TripoTextureNode, TripoImageToModelNode, SaveGLB, LoadImage, MarkdownNote, SaveGLB]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `TripoRetargetNode`
- `TripoRigNode`
- `TripoTextureNode`
- `TripoImageToModelNode`
- `SaveGLB`
- `LoadImage`
- `MarkdownNote`
- `SaveGLB`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`TripoRetargetNode`、`TripoRigNode`、`TripoTextureNode`、`TripoImageToModelNode`、`SaveGLB`、`LoadImage`

**用到的条目**：LoadImage、SaveGLB、TripoImageToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNode、sd15-t2i-basic、sd15-t2i-lora
