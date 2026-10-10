---
key: comfyui-workflow-templates-json/api_tripo_text_to_model.json
name: api_tripo_text_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_text_to_model.json
hash: d6d00cb0b28aa2e5
official: true
coverage: 1
learned_at: 2026-10-10 22:46:30
nodes: [TripoRigNode, TripoConversionNode, TripoTextureNode, TripoRetargetNode, TripoTextToModelNode, SaveGLB, SaveGLB]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_text_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_text_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `TripoRigNode`
- `TripoConversionNode`
- `TripoTextureNode`
- `TripoRetargetNode`
- `TripoTextToModelNode`
- `SaveGLB`
- `SaveGLB`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`TripoRigNode`、`TripoConversionNode`、`TripoTextureNode`、`TripoRetargetNode`、`TripoTextToModelNode`、`SaveGLB`

**用到的条目**：SaveGLB、TripoConversionNode、TripoRetargetNode、TripoRigNode、TripoTextToModelNode、TripoTextureNode、sd15-t2i-basic、sd15-t2i-lora
