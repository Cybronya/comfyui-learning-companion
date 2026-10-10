---
key: comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json
name: api_tripo3_1_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json
hash: b21d27e8bb021274
official: true
coverage: 1
learned_at: 2026-10-10 22:46:22
nodes: [TripoRigNode, TripoRetargetNode, TripoConversionNode, LoadImage, TripoImageToModelNodeV2, Save3DAdvanced, TripoTextureNodeV2]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo3_1_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `TripoRigNode`
- `TripoRetargetNode`
- `TripoConversionNode`
- `LoadImage`
- `TripoImageToModelNodeV2`
- `Save3DAdvanced`
- `TripoTextureNodeV2`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`TripoRigNode`、`TripoRetargetNode`、`TripoConversionNode`、`LoadImage`、`TripoImageToModelNodeV2`、`Save3DAdvanced`、`TripoTextureNodeV2`

**用到的条目**：LoadImage、Save3DAdvanced、TripoConversionNode、TripoImageToModelNodeV2、TripoRetargetNode、TripoRigNode、TripoTextureNodeV2、sd15-t2i-basic
