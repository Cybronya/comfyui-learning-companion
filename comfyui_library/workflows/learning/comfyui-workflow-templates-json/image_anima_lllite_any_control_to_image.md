---
key: comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json
name: image_anima_lllite_any_control_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json
hash: d7ffa270eb6781da
official: true
coverage: 0.636364
learned_at: 2026-10-10 22:47:23
nodes: [MarkdownNote, SaveImage, ResizeImageMaskNode, GetImageSize, ImageCompare, 147b517e-5ea6-4fba-84f7-46851be6e4ce, Canny, LoadImage, PreviewImage, ImageInvert, MarkdownNote]
patterns: []
missing: [147b517e-5ea6-4fba-84f7-46851be6e4ce]
discoveries: [次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识]
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

覆盖率 **64%**（7/11）

**有卡**：`SaveImage`、`ResizeImageMaskNode`、`GetImageSize`、`ImageCompare`、`Canny`、`LoadImage`、`ImageInvert`

**缺卡**（1）：`147b517e-5ea6-4fba-84f7-46851be6e4ce`

**用到的条目**：LoadImage、Canny、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、ImageCompare、ImageInvert

## 学习发现

- 次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识
