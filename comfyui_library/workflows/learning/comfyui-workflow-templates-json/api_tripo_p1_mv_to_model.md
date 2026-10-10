---
key: comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json
name: api_tripo_p1_mv_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json
hash: 0391c413fe4aa9cf
official: true
coverage: 1
learned_at: 2026-10-10 22:46:26
nodes: [SaveGLB, TripoRigNode, TripoRetargetNode, TripoConversionNode, LoadImage, TripoP1MultiviewToModelNode, LoadImage, LoadImage, TripoTextureNodeV2]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p1_mv_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `SaveGLB`
- `TripoRigNode`
- `TripoRetargetNode`
- `TripoConversionNode`
- `LoadImage`
- `TripoP1MultiviewToModelNode`
- `LoadImage`
- `LoadImage`
- `TripoTextureNodeV2`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`SaveGLB`、`TripoRigNode`、`TripoRetargetNode`、`TripoConversionNode`、`LoadImage`、`TripoP1MultiviewToModelNode`、`TripoTextureNodeV2`

**用到的条目**：LoadImage、SaveGLB、TripoConversionNode、TripoP1MultiviewToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNodeV2、sd15-t2i-basic
