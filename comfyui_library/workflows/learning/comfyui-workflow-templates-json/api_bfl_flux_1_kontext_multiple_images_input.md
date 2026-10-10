---
key: comfyui-workflow-templates-json/api_bfl_flux_1_kontext_multiple_images_input.json
name: api_bfl_flux_1_kontext_multiple_images_input
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux_1_kontext_multiple_images_input.json
hash: f97e800c5dabede7
official: true
coverage: 0.7
learned_at: 2026-10-10 22:43:18
nodes: [LoadImage, LoadImage, SaveImage, LoadImage, FluxKontextProImageNode, ImageStitch, ImageStitch, PreviewImage, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bfl_flux_1_kontext_multiple_images_input.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux_1_kontext_multiple_images_input.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `FluxKontextProImageNode`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`LoadImage`、`SaveImage`、`FluxKontextProImageNode`、`ImageStitch`

**用到的条目**：LoadImage、FluxKontextProImageNode、SaveImage、ImageStitch、ImageStitch、sd15-t2i-basic、sd15-t2i-lora、node
