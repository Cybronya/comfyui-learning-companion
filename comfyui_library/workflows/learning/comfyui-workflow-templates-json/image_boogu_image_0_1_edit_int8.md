---
key: comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json
name: image_boogu_image_0_1_edit_int8
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json
hash: dee31a93378a6645
official: true
coverage: 0.555556
learned_at: 2026-10-07 21:35:34
nodes: [LoadImage, fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb, GetImageSize, ResizeImageMaskNode, MarkdownNote, ImageCompare, MarkdownNote, SaveImageAdvanced, MarkdownNote]
patterns: []
missing: [fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb]
discoveries: [次要节点 `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LoadImage`
- `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb`
- `GetImageSize`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `ImageCompare`
- `MarkdownNote`
- `SaveImageAdvanced`
- `MarkdownNote`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`LoadImage`、`GetImageSize`、`ResizeImageMaskNode`、`ImageCompare`、`SaveImageAdvanced`

**缺卡**（1）：`fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb`

**用到的条目**：LoadImage、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImageAdvanced、ImageCompare、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb` 知识库中没有该节点类型的任何知识
