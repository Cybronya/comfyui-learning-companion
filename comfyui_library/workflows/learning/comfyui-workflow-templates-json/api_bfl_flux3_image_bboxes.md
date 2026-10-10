---
key: comfyui-workflow-templates-json/api_bfl_flux3_image_bboxes.json
name: api_bfl_flux3_image_bboxes
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux3_image_bboxes.json
hash: 90d015a970ea6c32
official: true
coverage: 0.714286
learned_at: 2026-10-10 22:43:14
nodes: [Flux3ImageNode, LoadImage, CreateBoundingBoxes, PreviewAny, SaveImageAdvanced, ImageCompare, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bfl_flux3_image_bboxes.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux3_image_bboxes.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `Flux3ImageNode`
- `LoadImage`
- `CreateBoundingBoxes`
- `PreviewAny`
- `SaveImageAdvanced`
- `ImageCompare`
- `MarkdownNote`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`Flux3ImageNode`、`LoadImage`、`CreateBoundingBoxes`、`SaveImageAdvanced`、`ImageCompare`

**用到的条目**：LoadImage、Flux3ImageNode、SaveImageAdvanced、CreateBoundingBoxes、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、SaveImage
