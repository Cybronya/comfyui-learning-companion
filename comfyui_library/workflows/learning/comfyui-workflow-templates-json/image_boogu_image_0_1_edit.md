---
key: comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json
name: image_boogu_image_0_1_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json
hash: 9fd2141c9bdfecbf
official: true
coverage: 0.555556
learned_at: 2026-10-10 22:47:26
nodes: [LoadImage, SaveImage, fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb, GetImageSize, ResizeImageMaskNode, MarkdownNote, ImageCompare, MarkdownNote, MarkdownNote]
patterns: []
missing: [fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb]
discoveries: [次要节点 `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LoadImage`
- `SaveImage`
- `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb`
- `GetImageSize`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `ImageCompare`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`LoadImage`、`SaveImage`、`GetImageSize`、`ResizeImageMaskNode`、`ImageCompare`

**缺卡**（1）：`fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb`

**用到的条目**：LoadImage、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、ImageCompare、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb` 知识库中没有该节点类型的任何知识
