---
key: comfyui-workflow-templates-json/api_hunyuan3d_text_to_model.json
name: api_hunyuan3d_text_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_text_to_model.json
hash: c6fb65e6b3a9b825
official: true
coverage: 1
learned_at: 2026-10-10 22:44:29
nodes: [Preview3D, SaveGLB, SaveGLB, TencentTextToModelNode, SaveImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_hunyuan3d_text_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_text_to_model.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `Preview3D`
- `SaveGLB`
- `SaveGLB`
- `TencentTextToModelNode`
- `SaveImage`

## 知识

覆盖率 **100%**（5/5）

**有卡**：`Preview3D`、`SaveGLB`、`TencentTextToModelNode`、`SaveImage`

**用到的条目**：SaveImage、SaveGLB、Preview3D、TencentTextToModelNode、sd15-t2i-basic、sd15-t2i-lora、node、Text
