---
key: comfyui-workflow-templates-json/image_longcat_text_to_image.json
name: image_longcat_text_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_longcat_text_to_image.json
hash: 0df9cfdf378e68b3
official: true
coverage: 0.5
learned_at: 2026-10-10 22:48:12
nodes: [ResolutionSelector, MarkdownNote, SaveImage, 4cdb8c8f-7b15-4921-a2b1-383d5c2d9105]
patterns: []
missing: [4cdb8c8f-7b15-4921-a2b1-383d5c2d9105]
discoveries: [次要节点 `4cdb8c8f-7b15-4921-a2b1-383d5c2d9105` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_longcat_text_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_longcat_text_to_image.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（4 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `SaveImage`
- `4cdb8c8f-7b15-4921-a2b1-383d5c2d9105`

## 知识

覆盖率 **50%**（2/4）

**有卡**：`ResolutionSelector`、`SaveImage`

**缺卡**（1）：`4cdb8c8f-7b15-4921-a2b1-383d5c2d9105`

**用到的条目**：ResolutionSelector、SaveImage、sd15-t2i-basic、sd15-t2i-lora、EmptyLatentImage、height 调整经验、width 调整经验、easy_imagesize

## 学习发现

- 次要节点 `4cdb8c8f-7b15-4921-a2b1-383d5c2d9105` 知识库中没有该节点类型的任何知识
