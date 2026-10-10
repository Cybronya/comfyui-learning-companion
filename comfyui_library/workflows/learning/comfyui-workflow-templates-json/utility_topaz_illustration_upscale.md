---
key: comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json
name: utility_topaz_illustration_upscale
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json
hash: e2d0b770a1b9ddbd
official: true
coverage: 0.75
learned_at: 2026-10-10 22:50:00
nodes: [ImageCompare, ImageScaleBy, SaveImage, TopazImageEnhance, GetImageSize, LoadImage, MarkdownNote, PrimitiveNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `ImageCompare`
- `ImageScaleBy`
- `SaveImage`
- `TopazImageEnhance`
- `GetImageSize`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveNode`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`ImageCompare`、`ImageScaleBy`、`SaveImage`、`TopazImageEnhance`、`GetImageSize`、`LoadImage`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveImage、ImageScaleBy、ImageCompare、TopazImageEnhance、sd15-t2i-basic
