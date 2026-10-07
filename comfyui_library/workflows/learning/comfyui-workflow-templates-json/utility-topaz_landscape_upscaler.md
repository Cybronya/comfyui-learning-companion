---
key: comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json
name: utility-topaz_landscape_upscaler
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json
hash: a5ed767a09af0aee
official: true
coverage: 0.857143
learned_at: 2026-10-07 21:36:42
nodes: [LoadImage, ImageScaleBy, GetImageSize, SaveImage, TopazImageEnhanceV2, MarkdownNote, ImageCompare]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `LoadImage`
- `ImageScaleBy`
- `GetImageSize`
- `SaveImage`
- `TopazImageEnhanceV2`
- `MarkdownNote`
- `ImageCompare`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`ImageScaleBy`、`GetImageSize`、`SaveImage`、`TopazImageEnhanceV2`、`ImageCompare`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveImage、ImageScaleBy、ImageCompare、TopazImageEnhanceV2、sd15-t2i-basic
