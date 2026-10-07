---
key: comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json
name: api_tripo_p2_multiview_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json
hash: 7a78f14909664142
official: true
coverage: 0.888889
learned_at: 2026-10-07 21:35:01
nodes: [TripoRetargetNode, TripoTextureNodeV2, TripoRigNode, TripoConversionNode, LoadImage, MarkdownNote, TripoPSeriesMultiviewToModelNode, LoadImage, Save3DAdvanced]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_tripo_p2_multiview_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `TripoRetargetNode`
- `TripoTextureNodeV2`
- `TripoRigNode`
- `TripoConversionNode`
- `LoadImage`
- `MarkdownNote`
- `TripoPSeriesMultiviewToModelNode`
- `LoadImage`
- `Save3DAdvanced`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`TripoRetargetNode`、`TripoTextureNodeV2`、`TripoRigNode`、`TripoConversionNode`、`LoadImage`、`TripoPSeriesMultiviewToModelNode`、`Save3DAdvanced`

**用到的条目**：LoadImage、Save3DAdvanced、TripoConversionNode、TripoPSeriesMultiviewToModelNode、TripoRetargetNode、TripoRigNode、TripoTextureNodeV2、sd15-t2i-basic
