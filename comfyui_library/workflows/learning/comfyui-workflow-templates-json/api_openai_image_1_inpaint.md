---
key: comfyui-workflow-templates-json/api_openai_image_1_inpaint.json
name: api_openai_image_1_inpaint
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_image_1_inpaint.json
hash: 692d7a34b5edb752
official: true
coverage: 0.8
learned_at: 2026-10-10 22:45:24
nodes: [SaveImage, MarkdownNote, LoadImage, OpenAIGPTImageNodeV2, ImageCompare]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_openai_image_1_inpaint.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_image_1_inpaint.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `OpenAIGPTImageNodeV2`
- `ImageCompare`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`SaveImage`、`LoadImage`、`OpenAIGPTImageNodeV2`、`ImageCompare`

**用到的条目**：LoadImage、SaveImage、ImageCompare、OpenAIGPTImageNodeV2、sd15-t2i-basic、sd15-t2i-lora、node、v2
