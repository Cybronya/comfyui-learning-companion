---
key: comfyui-workflow-templates-json/api_recraft_style_reference.json
name: api_recraft_style_reference
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_recraft_style_reference.json
hash: 4e730b1f641a1436
official: true
coverage: 0.818182
learned_at: 2026-10-07 21:34:38
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, RecraftCreateStyleNode, RecraftStyleV3InfiniteStyleLibrary, PreviewAny, RecraftStyleV3InfiniteStyleLibrary, RecraftTextToImageNode, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_recraft_style_reference.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_recraft_style_reference.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RecraftCreateStyleNode`
- `RecraftStyleV3InfiniteStyleLibrary`
- `PreviewAny`
- `RecraftStyleV3InfiniteStyleLibrary`
- `RecraftTextToImageNode`
- `MarkdownNote`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`LoadImage`、`SaveImage`、`RecraftCreateStyleNode`、`RecraftStyleV3InfiniteStyleLibrary`、`RecraftTextToImageNode`

**用到的条目**：LoadImage、RecraftCreateStyleNode、RecraftStyleV3InfiniteStyleLibrary、SaveImage、RecraftTextToImageNode、sd15-t2i-basic、sd15-t2i-lora、node
