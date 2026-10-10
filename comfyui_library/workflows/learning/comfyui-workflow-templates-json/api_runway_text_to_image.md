---
key: comfyui-workflow-templates-json/api_runway_text_to_image.json
name: api_runway_text_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_text_to_image.json
hash: 3b379ff15e66d46b
official: true
coverage: 0.6
learned_at: 2026-10-10 22:45:57
nodes: [SaveImage, RunwayTextToImageNode, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_runway_text_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_text_to_image.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `SaveImage`
- `RunwayTextToImageNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`SaveImage`、`RunwayTextToImageNode`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、RunwayTextToImageNode、sd15-t2i-basic、sd15-t2i-lora、node、Text、CS_Preview_Any
