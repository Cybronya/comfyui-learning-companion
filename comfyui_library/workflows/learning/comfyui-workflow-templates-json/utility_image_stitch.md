---
key: comfyui-workflow-templates-json/utility_image_stitch.json
name: utility_image_stitch
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_image_stitch.json
hash: d00b088bdba0d456
official: true
coverage: 0.9
learned_at: 2026-10-07 21:36:46
nodes: [LoadImage, LoadImage, ImageStitch, ResizeImageMaskNode, ImageStitch, ImageStitch, SaveImage, LoadImage, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/utility_image_stitch.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_image_stitch.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LoadImage`
- `LoadImage`
- `ImageStitch`
- `ResizeImageMaskNode`
- `ImageStitch`
- `ImageStitch`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`LoadImage`、`ImageStitch`、`ResizeImageMaskNode`、`SaveImage`

**用到的条目**：LoadImage、ResizeImageMaskNode、SaveImage、ImageStitch、sd15-t2i-basic、sd15-t2i-lora、ResizeImage、node
