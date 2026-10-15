---
key: comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json
name: image_anima_lllite_any_control_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json
hash: d7ffa270eb6781da
official: true
coverage: 0.727273
learned_at: 2026-10-15 22:24:53
nodes: [MarkdownNote, SaveImage, ResizeImageMaskNode, GetImageSize, ImageCompare, 147b517e-5ea6-4fba-84f7-46851be6e4ce, Canny, LoadImage, PreviewImage, ImageInvert, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `MarkdownNote`
- `SaveImage`
- `ResizeImageMaskNode`
- `GetImageSize`
- `ImageCompare`
- `147b517e-5ea6-4fba-84f7-46851be6e4ce`
- `Canny`
- `LoadImage`
- `PreviewImage`
- `ImageInvert`
- `MarkdownNote`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`SaveImage`、`ResizeImageMaskNode`、`GetImageSize`、`ImageCompare`、`147b517e-5ea6-4fba-84f7-46851be6e4ce`、`Canny`、`LoadImage`、`ImageInvert`

**用到的条目**：LoadImage、Canny、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、ImageCompare、ImageInvert
