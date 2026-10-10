---
key: comfyui-workflow-templates-json/api_vidu_reference_to_video.json
name: api_vidu_reference_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_vidu_reference_to_video.json
hash: e1df24ea1dbe3b56
official: true
coverage: 0.75
learned_at: 2026-10-10 22:46:36
nodes: [LoadImage, LoadImage, LoadImage, SaveVideo, MarkdownNote, MarkdownNote, ViduReferenceVideoNode, BatchImagesNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_vidu_reference_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_vidu_reference_to_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `ViduReferenceVideoNode`
- `BatchImagesNode`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`LoadImage`、`SaveVideo`、`ViduReferenceVideoNode`、`BatchImagesNode`

**用到的条目**：LoadImage、SaveVideo、BatchImagesNode、ViduReferenceVideoNode、sd15-t2i-basic、sd15-t2i-lora、node、SaveImage
