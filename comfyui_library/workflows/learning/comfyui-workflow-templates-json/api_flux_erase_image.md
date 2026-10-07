---
key: comfyui-workflow-templates-json/api_flux_erase_image.json
name: api_flux_erase_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_flux_erase_image.json
hash: f026370a5b1a3756
official: true
coverage: 0.8
learned_at: 2026-10-07 21:33:37
nodes: [SaveImage, ImageCompare, MarkdownNote, FluxEraseNode, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_flux_erase_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_flux_erase_image.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `SaveImage`
- `ImageCompare`
- `MarkdownNote`
- `FluxEraseNode`
- `LoadImage`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`SaveImage`、`ImageCompare`、`FluxEraseNode`、`LoadImage`

**用到的条目**：LoadImage、FluxEraseNode、SaveImage、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、node、CheckpointLoaderSimple
