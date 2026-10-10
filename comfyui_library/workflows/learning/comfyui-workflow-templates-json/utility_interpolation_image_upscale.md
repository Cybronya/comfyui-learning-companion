---
key: comfyui-workflow-templates-json/utility_interpolation_image_upscale.json
name: utility_interpolation_image_upscale
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_interpolation_image_upscale.json
hash: 65493061d970f172
official: true
coverage: 0.8
learned_at: 2026-10-10 22:49:47
nodes: [LoadImage, ImageScaleBy, SaveImage, ImageCompare, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/utility_interpolation_image_upscale.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_interpolation_image_upscale.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `LoadImage`
- `ImageScaleBy`
- `SaveImage`
- `ImageCompare`
- `MarkdownNote`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`ImageScaleBy`、`SaveImage`、`ImageCompare`

**用到的条目**：LoadImage、SaveImage、ImageScaleBy、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale
