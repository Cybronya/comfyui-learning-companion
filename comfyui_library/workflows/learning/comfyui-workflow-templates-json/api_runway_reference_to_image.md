---
key: comfyui-workflow-templates-json/api_runway_reference_to_image.json
name: api_runway_reference_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_reference_to_image.json
hash: 22c4066157d1f3c1
official: true
coverage: 0.6
learned_at: 2026-10-07 21:34:44
nodes: [MarkdownNote, RunwayTextToImageNode, SaveImage, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_runway_reference_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_reference_to_image.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `MarkdownNote`
- `RunwayTextToImageNode`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`RunwayTextToImageNode`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、RunwayTextToImageNode、sd15-t2i-basic、sd15-t2i-lora、node、Text、CS_Preview_Any
