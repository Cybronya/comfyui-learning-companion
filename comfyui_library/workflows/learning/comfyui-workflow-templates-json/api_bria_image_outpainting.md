---
key: comfyui-workflow-templates-json/api_bria_image_outpainting.json
name: api_bria_image_outpainting
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bria_image_outpainting.json
hash: eb12f8faaec98a90
official: true
coverage: 0.8
learned_at: 2026-10-10 22:43:24
nodes: [SaveImage, LoadImage, ImagePadForOutpaint, BriaImageEditNode, PreviewImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bria_image_outpainting.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bria_image_outpainting.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `SaveImage`
- `LoadImage`
- `ImagePadForOutpaint`
- `BriaImageEditNode`
- `PreviewImage`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`SaveImage`、`LoadImage`、`ImagePadForOutpaint`、`BriaImageEditNode`

**用到的条目**：LoadImage、SaveImage、ImagePadForOutpaint、BriaImageEditNode、sd15-t2i-basic、sd15-t2i-lora、Int、node
