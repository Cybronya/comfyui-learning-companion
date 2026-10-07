---
key: comfyui-workflow-templates-json/api_tripo_multiview_to_model.json
name: api_tripo_multiview_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_multiview_to_model.json
hash: d1d94f664907dce8
official: true
coverage: 1
learned_at: 2026-10-07 21:34:59
nodes: [LoadImage, LoadImage, TripoRigNode, TripoRetargetNode, TripoConversionNode, TripoTextureNode, SaveGLB, TripoMultiviewToModelNode, SaveGLB]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_multiview_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_multiview_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `LoadImage`
- `LoadImage`
- `TripoRigNode`
- `TripoRetargetNode`
- `TripoConversionNode`
- `TripoTextureNode`
- `SaveGLB`
- `TripoMultiviewToModelNode`
- `SaveGLB`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`LoadImage`、`TripoRigNode`、`TripoRetargetNode`、`TripoConversionNode`、`TripoTextureNode`、`SaveGLB`、`TripoMultiviewToModelNode`

**用到的条目**：LoadImage、SaveGLB、TripoConversionNode、TripoMultiviewToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNode、sd15-t2i-basic
