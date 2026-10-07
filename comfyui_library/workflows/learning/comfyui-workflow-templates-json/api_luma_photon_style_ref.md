---
key: comfyui-workflow-templates-json/api_luma_photon_style_ref.json
name: api_luma_photon_style_ref
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_luma_photon_style_ref.json
hash: de49fd44e7c6b99f
official: true
coverage: 0.823529
learned_at: 2026-10-07 21:34:08
nodes: [LoadImage, LoadImage, LumaReferenceNode, LumaReferenceNode, LoadImage, LoadImage, LumaReferenceNode, SaveImage, LumaReferenceNode, LoadImage, MarkdownNote, LumaImageNode, MarkdownNote, MarkdownNote, LoadImage, LoadImage, BatchImagesNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_luma_photon_style_ref.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_luma_photon_style_ref.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（17 个）：
- `LoadImage`
- `LoadImage`
- `LumaReferenceNode`
- `LumaReferenceNode`
- `LoadImage`
- `LoadImage`
- `LumaReferenceNode`
- `SaveImage`
- `LumaReferenceNode`
- `LoadImage`
- `MarkdownNote`
- `LumaImageNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`LoadImage`、`LumaReferenceNode`、`SaveImage`、`LumaImageNode`、`BatchImagesNode`

**用到的条目**：LoadImage、SaveImage、BatchImagesNode、LumaImageNode、LumaReferenceNode、sd15-t2i-basic、sd15-t2i-lora、node
