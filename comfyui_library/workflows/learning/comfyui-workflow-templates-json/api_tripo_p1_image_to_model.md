---
key: comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json
name: api_tripo_p1_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json
hash: d4658e25ccaf1888
official: true
coverage: 1
learned_at: 2026-10-07 21:34:59
nodes: [SaveGLB, TripoRigNode, TripoRetargetNode, TripoConversionNode, LoadImage, TripoP1ImageToModelNode, TripoTextureNodeV2]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p1_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `SaveGLB`
- `TripoRigNode`
- `TripoRetargetNode`
- `TripoConversionNode`
- `LoadImage`
- `TripoP1ImageToModelNode`
- `TripoTextureNodeV2`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`SaveGLB`、`TripoRigNode`、`TripoRetargetNode`、`TripoConversionNode`、`LoadImage`、`TripoP1ImageToModelNode`、`TripoTextureNodeV2`

**用到的条目**：LoadImage、SaveGLB、TripoConversionNode、TripoP1ImageToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNodeV2、sd15-t2i-basic
