---
key: comfyui-workflow-templates-json/api_flux_vto.json
name: api_flux_vto
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_flux_vto.json
hash: 3872d6205eb3ae10
official: true
coverage: 0.857143
learned_at: 2026-10-07 21:33:38
nodes: [LoadImage, SaveImage, LoadImage, ImageCompare, FluxVTONode, MarkdownNote, ImageStitch]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_flux_vto.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_flux_vto.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `ImageCompare`
- `FluxVTONode`
- `MarkdownNote`
- `ImageStitch`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`SaveImage`、`ImageCompare`、`FluxVTONode`、`ImageStitch`

**用到的条目**：LoadImage、FluxVTONode、SaveImage、ImageStitch、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、node
