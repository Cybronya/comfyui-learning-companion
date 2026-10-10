---
key: comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json
name: api_tripo3_1_multiview_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json
hash: 057605bd9ae9a91f
official: true
coverage: 1
learned_at: 2026-10-10 22:46:23
nodes: [TripoRetargetNode, TripoTextureNode, SaveGLB, LoadImage, LoadImage, LoadImage, TripoMultiviewToModelNode, TripoRigNode, TripoConversionNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo3_1_multiview_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `TripoRetargetNode`
- `TripoTextureNode`
- `SaveGLB`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TripoMultiviewToModelNode`
- `TripoRigNode`
- `TripoConversionNode`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`TripoRetargetNode`、`TripoTextureNode`、`SaveGLB`、`LoadImage`、`TripoMultiviewToModelNode`、`TripoRigNode`、`TripoConversionNode`

**用到的条目**：LoadImage、SaveGLB、TripoConversionNode、TripoMultiviewToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNode、sd15-t2i-basic
