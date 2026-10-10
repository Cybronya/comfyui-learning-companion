---
key: comfyui-workflow-templates-json/image_pixeldit_t2i.json
name: image_pixeldit_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_pixeldit_t2i.json
hash: ef4a37f4125b2acf
official: true
coverage: 0.4
learned_at: 2026-10-10 22:48:24
nodes: [MarkdownNote, SaveImage, ef85a5af-0944-4f72-bffd-7d6d9941f33c, ResolutionSelector, MarkdownNote]
patterns: []
missing: [ef85a5af-0944-4f72-bffd-7d6d9941f33c]
discoveries: [次要节点 `ef85a5af-0944-4f72-bffd-7d6d9941f33c` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_pixeldit_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_pixeldit_t2i.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（5 个）：
- `MarkdownNote`
- `SaveImage`
- `ef85a5af-0944-4f72-bffd-7d6d9941f33c`
- `ResolutionSelector`
- `MarkdownNote`

## 知识

覆盖率 **40%**（2/5）

**有卡**：`SaveImage`、`ResolutionSelector`

**缺卡**（1）：`ef85a5af-0944-4f72-bffd-7d6d9941f33c`

**用到的条目**：ResolutionSelector、SaveImage、sd15-t2i-basic、sd15-t2i-lora、EmptyLatentImage、height 调整经验、width 调整经验、easy_imagesize

## 学习发现

- 次要节点 `ef85a5af-0944-4f72-bffd-7d6d9941f33c` 知识库中没有该节点类型的任何知识
