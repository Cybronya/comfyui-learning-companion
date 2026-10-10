---
key: comfyui-workflow-templates-json/image_qwen_image_edit_2509_relight.json
name: image_qwen_image_edit_2509_relight
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_edit_2509_relight.json
hash: bf17a8412db73407
official: true
coverage: 0.5
learned_at: 2026-10-10 22:48:33
nodes: [LoadImage, MarkdownNote, StringConcatenate, SaveImage, PrimitiveStringMultiline, 3a756f48-801b-48eb-80dd-279f32d09b12]
patterns: []
missing: [3a756f48-801b-48eb-80dd-279f32d09b12]
discoveries: [次要节点 `3a756f48-801b-48eb-80dd-279f32d09b12` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_edit_2509_relight.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_edit_2509_relight.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `LoadImage`
- `MarkdownNote`
- `StringConcatenate`
- `SaveImage`
- `PrimitiveStringMultiline`
- `3a756f48-801b-48eb-80dd-279f32d09b12`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`LoadImage`、`StringConcatenate`、`SaveImage`

**缺卡**（1）：`3a756f48-801b-48eb-80dd-279f32d09b12`

**用到的条目**：LoadImage、SaveImage、StringConcatenate、sd15-t2i-basic、sd15-t2i-lora、String、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `3a756f48-801b-48eb-80dd-279f32d09b12` 知识库中没有该节点类型的任何知识
