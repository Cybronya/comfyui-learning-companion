---
key: comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json
name: api_tripo_p2_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json
hash: a5d711d62e707de7
official: true
coverage: 0.777778
learned_at: 2026-10-07 21:35:00
nodes: [MarkdownNote, TripoRetargetNode, TripoTextureNodeV2, TripoRigNode, TripoConversionNode, Save3DAdvanced, TripoPSeriesImageToModelNode, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p2_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `MarkdownNote`
- `TripoRetargetNode`
- `TripoTextureNodeV2`
- `TripoRigNode`
- `TripoConversionNode`
- `Save3DAdvanced`
- `TripoPSeriesImageToModelNode`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`TripoRetargetNode`、`TripoTextureNodeV2`、`TripoRigNode`、`TripoConversionNode`、`Save3DAdvanced`、`TripoPSeriesImageToModelNode`、`LoadImage`

**用到的条目**：LoadImage、Save3DAdvanced、TripoConversionNode、TripoPSeriesImageToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNodeV2、sd15-t2i-basic
