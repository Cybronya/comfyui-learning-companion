---
key: comfyui-workflow-templates-json/image_lens_t2i.json
name: image_lens_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_lens_t2i.json
hash: d9626a9a6627b146
official: true
coverage: 0.5
learned_at: 2026-10-10 22:48:09
nodes: [ec44c008-5f23-4498-a682-eb96a8598475, ResolutionSelector, SaveImage, MarkdownNote]
patterns: []
missing: [ec44c008-5f23-4498-a682-eb96a8598475]
discoveries: [次要节点 `ec44c008-5f23-4498-a682-eb96a8598475` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_lens_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_lens_t2i.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（4 个）：
- `ec44c008-5f23-4498-a682-eb96a8598475`
- `ResolutionSelector`
- `SaveImage`
- `MarkdownNote`

## 知识

覆盖率 **50%**（2/4）

**有卡**：`ResolutionSelector`、`SaveImage`

**缺卡**（1）：`ec44c008-5f23-4498-a682-eb96a8598475`

**用到的条目**：ResolutionSelector、SaveImage、sd15-t2i-basic、sd15-t2i-lora、EmptyLatentImage、height 调整经验、width 调整经验、easy_imagesize

## 学习发现

- 次要节点 `ec44c008-5f23-4498-a682-eb96a8598475` 知识库中没有该节点类型的任何知识
