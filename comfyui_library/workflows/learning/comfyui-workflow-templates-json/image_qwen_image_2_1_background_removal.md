---
key: comfyui-workflow-templates-json/image_qwen_image_2_1_background_removal.json
name: image_qwen_image_2_1_background_removal
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_background_removal.json
hash: 2fca0a2581fd428f
official: true
coverage: 0.5
learned_at: 2026-10-07 21:35:57
nodes: [bc1c967a-7f6a-4be9-a372-dad16e4f28e3, SaveImageAdvanced, MarkdownNote, LoadImage, ImageCompare, MarkdownNote]
patterns: []
missing: [bc1c967a-7f6a-4be9-a372-dad16e4f28e3]
discoveries: [次要节点 `bc1c967a-7f6a-4be9-a372-dad16e4f28e3` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_2_1_background_removal.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_background_removal.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `bc1c967a-7f6a-4be9-a372-dad16e4f28e3`
- `SaveImageAdvanced`
- `MarkdownNote`
- `LoadImage`
- `ImageCompare`
- `MarkdownNote`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`SaveImageAdvanced`、`LoadImage`、`ImageCompare`

**缺卡**（1）：`bc1c967a-7f6a-4be9-a372-dad16e4f28e3`

**用到的条目**：LoadImage、SaveImageAdvanced、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、SaveImage、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `bc1c967a-7f6a-4be9-a372-dad16e4f28e3` 知识库中没有该节点类型的任何知识
