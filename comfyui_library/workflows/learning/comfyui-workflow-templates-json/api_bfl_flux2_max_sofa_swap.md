---
key: comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json
name: api_bfl_flux2_max_sofa_swap
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json
hash: 14797288453d6005
official: true
coverage: 0.857143
learned_at: 2026-10-10 22:43:13
nodes: [LoadImage, LoadImage, LoadImage, GetImageSize, SaveImage, Flux2ImageNode, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bfl_flux2_max_sofa_swap.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetImageSize`
- `SaveImage`
- `Flux2ImageNode`
- `MarkdownNote`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`GetImageSize`、`SaveImage`、`Flux2ImageNode`

**用到的条目**：LoadImage、Flux2ImageNode、GetImageSize、GetImageSize、SaveImage、sd15-t2i-basic、sd15-t2i-lora、node
