---
key: comfyui-workflow-templates-json/image_qwen_image_layered_control.json
name: image_qwen_image_layered_control
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_layered_control.json
hash: 9c77e0518359cd88
official: true
coverage: 0.5
learned_at: 2026-10-07 21:36:03
nodes: [LoadImage, ImageScaleToMaxDimension, MarkdownNote, SaveImage, MarkdownNote, f754a936-daaf-4b6e-9658-41fdc54d301d]
patterns: []
missing: [f754a936-daaf-4b6e-9658-41fdc54d301d]
discoveries: [次要节点 `f754a936-daaf-4b6e-9658-41fdc54d301d` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_layered_control.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_layered_control.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `LoadImage`
- `ImageScaleToMaxDimension`
- `MarkdownNote`
- `SaveImage`
- `MarkdownNote`
- `f754a936-daaf-4b6e-9658-41fdc54d301d`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`LoadImage`、`ImageScaleToMaxDimension`、`SaveImage`

**缺卡**（1）：`f754a936-daaf-4b6e-9658-41fdc54d301d`

**用到的条目**：LoadImage、SaveImage、ImageScaleToMaxDimension、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale、CS_Preview_Any

## 学习发现

- 次要节点 `f754a936-daaf-4b6e-9658-41fdc54d301d` 知识库中没有该节点类型的任何知识
