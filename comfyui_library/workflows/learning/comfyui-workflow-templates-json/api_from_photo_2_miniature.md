---
key: comfyui-workflow-templates-json/api_from_photo_2_miniature.json
name: api_from_photo_2_miniature
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_from_photo_2_miniature.json
hash: 97971ab26e5f952f
official: true
coverage: 1
learned_at: 2026-10-10 22:43:53
nodes: [GeminiImage2Node, LoadImage, SaveImage, GeminiImage2Node, SaveImage, BatchImagesNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_from_photo_2_miniature.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_from_photo_2_miniature.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `GeminiImage2Node`
- `LoadImage`
- `SaveImage`
- `GeminiImage2Node`
- `SaveImage`
- `BatchImagesNode`

## 知识

覆盖率 **100%**（6/6）

**有卡**：`GeminiImage2Node`、`LoadImage`、`SaveImage`、`BatchImagesNode`

**用到的条目**：LoadImage、SaveImage、BatchImagesNode、GeminiImage2Node、sd15-t2i-basic、sd15-t2i-lora、node、CS_Preview_Any
