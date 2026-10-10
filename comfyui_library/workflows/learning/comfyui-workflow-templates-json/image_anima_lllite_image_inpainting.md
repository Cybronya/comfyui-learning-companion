---
key: comfyui-workflow-templates-json/image_anima_lllite_image_inpainting.json
name: image_anima_lllite_image_inpainting
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_image_inpainting.json
hash: 3707099547db43e7
official: true
coverage: 0.6
learned_at: 2026-10-10 22:47:24
nodes: [MarkdownNote, SaveImage, ImageCompare, 147b517e-5ea6-4fba-84f7-46851be6e4ce, LoadImage, Painter, MaskPreview, ResizeImageMaskNode, MarkdownNote, MarkdownNote]
patterns: []
missing: [147b517e-5ea6-4fba-84f7-46851be6e4ce]
discoveries: [次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_anima_lllite_image_inpainting.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_image_inpainting.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `MarkdownNote`
- `SaveImage`
- `ImageCompare`
- `147b517e-5ea6-4fba-84f7-46851be6e4ce`
- `LoadImage`
- `Painter`
- `MaskPreview`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **60%**（6/10）

**有卡**：`SaveImage`、`ImageCompare`、`LoadImage`、`Painter`、`MaskPreview`、`ResizeImageMaskNode`

**缺卡**（1）：`147b517e-5ea6-4fba-84f7-46851be6e4ce`

**用到的条目**：LoadImage、ResizeImageMaskNode、SaveImage、MaskPreview、ImageCompare、Painter、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识
