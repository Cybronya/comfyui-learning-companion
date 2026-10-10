---
key: comfyui-workflow-templates-json/api_openai_image_1_i2i.json
name: api_openai_image_1_i2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_image_1_i2i.json
hash: c2e063ede037ac94
official: true
coverage: 0.8
learned_at: 2026-10-10 22:45:23
nodes: [LoadImage, SaveImage, MarkdownNote, OpenAIGPTImageNodeV2, ImageCompare]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_openai_image_1_i2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_image_1_i2i.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `LoadImage`
- `SaveImage`
- `MarkdownNote`
- `OpenAIGPTImageNodeV2`
- `ImageCompare`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`SaveImage`、`OpenAIGPTImageNodeV2`、`ImageCompare`

**用到的条目**：LoadImage、SaveImage、ImageCompare、OpenAIGPTImageNodeV2、sd15-t2i-basic、sd15-t2i-lora、node、v2
