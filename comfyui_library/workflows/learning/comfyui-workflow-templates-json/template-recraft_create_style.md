---
key: comfyui-workflow-templates-json/template-recraft_create_style.json
name: template-recraft_create_style
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template-recraft_create_style.json
hash: d86d3406f80ec48d
official: true
coverage: 0.666667
learned_at: 2026-10-07 21:36:19
nodes: [PreviewAny, RecraftCreateStyleNode, LoadImage, LoadImage, LoadImage, PrimitiveNode, SaveImage, RecraftStyleV3InfiniteStyleLibrary, MarkdownNote, MarkdownNote, LoadImage, LoadImage, RecraftStyleV3InfiniteStyleLibrary, PrimitiveNode, RecraftTextToImageNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/template-recraft_create_style.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template-recraft_create_style.json`

## 结构

**生成流程**：Output → Other

**节点**（15 个）：
- `PreviewAny`
- `RecraftCreateStyleNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `SaveImage`
- `RecraftStyleV3InfiniteStyleLibrary`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `RecraftStyleV3InfiniteStyleLibrary`
- `PrimitiveNode`
- `RecraftTextToImageNode`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`RecraftCreateStyleNode`、`LoadImage`、`SaveImage`、`RecraftStyleV3InfiniteStyleLibrary`、`RecraftTextToImageNode`

**用到的条目**：LoadImage、RecraftCreateStyleNode、RecraftStyleV3InfiniteStyleLibrary、SaveImage、RecraftTextToImageNode、sd15-t2i-basic、sd15-t2i-lora、node
