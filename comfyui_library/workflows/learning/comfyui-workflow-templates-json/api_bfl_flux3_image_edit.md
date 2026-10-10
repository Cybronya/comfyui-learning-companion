---
key: comfyui-workflow-templates-json/api_bfl_flux3_image_edit.json
name: api_bfl_flux3_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux3_image_edit.json
hash: 37f2f0fb579c4292
official: true
coverage: 0.8
learned_at: 2026-10-10 22:43:15
nodes: [SaveImageAdvanced, Flux3ImageNode, LoadImage, ImageCompare, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bfl_flux3_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux3_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `SaveImageAdvanced`
- `Flux3ImageNode`
- `LoadImage`
- `ImageCompare`
- `MarkdownNote`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`SaveImageAdvanced`、`Flux3ImageNode`、`LoadImage`、`ImageCompare`

**用到的条目**：LoadImage、Flux3ImageNode、SaveImageAdvanced、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、SaveImage、node
