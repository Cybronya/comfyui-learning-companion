---
key: comfyui-workflow-templates-json/api_flux2.json
name: api_flux2
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_flux2.json
hash: b7f0a5d09b1a603a
official: true
coverage: 0.857143
learned_at: 2026-10-07 21:33:37
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, Flux2ImageNode, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_flux2.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_flux2.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Flux2ImageNode`
- `MarkdownNote`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`SaveImage`、`Flux2ImageNode`

**用到的条目**：LoadImage、Flux2ImageNode、SaveImage、sd15-t2i-basic、sd15-t2i-lora、node、CheckpointLoaderSimple、UNETLoader
