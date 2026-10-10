---
key: comfyui-workflow-templates-json/image_qwen_image_2_1_image_edit.json
name: image_qwen_image_2_1_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_image_edit.json
hash: c1e6551759de131f
official: true
coverage: 0.5
learned_at: 2026-10-10 22:48:29
nodes: [bc1c967a-7f6a-4be9-a372-dad16e4f28e3, SaveImageAdvanced, MarkdownNote, LoadImage, ImageCompare, LoadImage, MarkdownNote, MarkdownNote]
patterns: []
missing: [bc1c967a-7f6a-4be9-a372-dad16e4f28e3]
discoveries: [次要节点 `bc1c967a-7f6a-4be9-a372-dad16e4f28e3` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_2_1_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `bc1c967a-7f6a-4be9-a372-dad16e4f28e3`
- `SaveImageAdvanced`
- `MarkdownNote`
- `LoadImage`
- `ImageCompare`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **50%**（4/8）

**有卡**：`SaveImageAdvanced`、`LoadImage`、`ImageCompare`

**缺卡**（1）：`bc1c967a-7f6a-4be9-a372-dad16e4f28e3`

**用到的条目**：LoadImage、SaveImageAdvanced、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、SaveImage、Compare、CS_Preview_Any

## 学习发现

- 次要节点 `bc1c967a-7f6a-4be9-a372-dad16e4f28e3` 知识库中没有该节点类型的任何知识
