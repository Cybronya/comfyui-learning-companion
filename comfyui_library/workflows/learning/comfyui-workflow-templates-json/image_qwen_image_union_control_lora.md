---
key: comfyui-workflow-templates-json/image_qwen_image_union_control_lora.json
name: image_qwen_image_union_control_lora
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_union_control_lora.json
hash: 192d65f74ff0d82a
official: true
coverage: 0.5
learned_at: 2026-10-07 21:36:03
nodes: [PreviewImage, ImageScaleToTotalPixels, MarkdownNote, LoadImage, Canny, MarkdownNote, SaveImage, 7db92ebb-840a-4c81-927e-6929224c69b5]
patterns: []
missing: [7db92ebb-840a-4c81-927e-6929224c69b5]
discoveries: [次要节点 `7db92ebb-840a-4c81-927e-6929224c69b5` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_union_control_lora.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_union_control_lora.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `LoadImage`
- `Canny`
- `MarkdownNote`
- `SaveImage`
- `7db92ebb-840a-4c81-927e-6929224c69b5`

## 知识

覆盖率 **50%**（4/8）

**有卡**：`ImageScaleToTotalPixels`、`LoadImage`、`Canny`、`SaveImage`

**缺卡**（1）：`7db92ebb-840a-4c81-927e-6929224c69b5`

**用到的条目**：LoadImage、Canny、SaveImage、ImageScaleToTotalPixels、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale

## 学习发现

- 次要节点 `7db92ebb-840a-4c81-927e-6929224c69b5` 知识库中没有该节点类型的任何知识
