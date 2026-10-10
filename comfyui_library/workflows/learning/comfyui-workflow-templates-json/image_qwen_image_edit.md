---
key: comfyui-workflow-templates-json/image_qwen_image_edit.json
name: image_qwen_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_edit.json
hash: 177d260f8fdd686a
official: true
coverage: 0.5
learned_at: 2026-10-10 22:48:31
nodes: [ImageScaleToTotalPixels, MarkdownNote, LoadImage, SaveImage, MarkdownNote, 74a8e1e2-9cb8-4112-978e-06ce1b5793f1]
patterns: []
missing: [74a8e1e2-9cb8-4112-978e-06ce1b5793f1]
discoveries: [次要节点 `74a8e1e2-9cb8-4112-978e-06ce1b5793f1` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `MarkdownNote`
- `74a8e1e2-9cb8-4112-978e-06ce1b5793f1`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`

**缺卡**（1）：`74a8e1e2-9cb8-4112-978e-06ce1b5793f1`

**用到的条目**：LoadImage、SaveImage、ImageScaleToTotalPixels、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale、CS_Preview_Any

## 学习发现

- 次要节点 `74a8e1e2-9cb8-4112-978e-06ce1b5793f1` 知识库中没有该节点类型的任何知识
