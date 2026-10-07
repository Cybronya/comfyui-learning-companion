---
key: comfyui-workflow-templates-json/api_bfl_flux_pro_t2i.json
name: api_bfl_flux_pro_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux_pro_t2i.json
hash: 17429d8118d48531
official: true
coverage: 0.5
learned_at: 2026-10-07 21:33:21
nodes: [SaveImage, MarkdownNote, MarkdownNote, MarkdownNote, FluxProUltraImageNode, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bfl_flux_pro_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux_pro_t2i.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `FluxProUltraImageNode`
- `LoadImage`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`SaveImage`、`FluxProUltraImageNode`、`LoadImage`

**用到的条目**：LoadImage、FluxProUltraImageNode、SaveImage、sd15-t2i-basic、sd15-t2i-lora、node、CheckpointLoaderSimple、UNETLoader
