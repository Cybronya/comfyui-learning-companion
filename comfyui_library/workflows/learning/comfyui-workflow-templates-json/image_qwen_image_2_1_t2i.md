---
key: comfyui-workflow-templates-json/image_qwen_image_2_1_t2i.json
name: image_qwen_image_2_1_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_t2i.json
hash: 5f2b50eeaf27e56a
official: true
coverage: 0.333333
learned_at: 2026-10-07 21:35:58
nodes: [ResolutionSelector, c291ceec-b98f-4751-9d0b-7bc288f27b30, SaveImageAdvanced, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: [c291ceec-b98f-4751-9d0b-7bc288f27b30]
discoveries: [次要节点 `c291ceec-b98f-4751-9d0b-7bc288f27b30` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_2_1_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_2_1_t2i.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（6 个）：
- `ResolutionSelector`
- `c291ceec-b98f-4751-9d0b-7bc288f27b30`
- `SaveImageAdvanced`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **33%**（2/6）

**有卡**：`ResolutionSelector`、`SaveImageAdvanced`

**缺卡**（1）：`c291ceec-b98f-4751-9d0b-7bc288f27b30`

**用到的条目**：ResolutionSelector、SaveImageAdvanced、sd15-t2i-basic、sd15-t2i-lora、SaveImage、EmptyLatentImage、height 调整经验、width 调整经验

## 学习发现

- 次要节点 `c291ceec-b98f-4751-9d0b-7bc288f27b30` 知识库中没有该节点类型的任何知识
