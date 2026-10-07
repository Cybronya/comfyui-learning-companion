---
key: comfyui-workflow-templates-json/api_hunyuan3d_image_to_model.json
name: api_hunyuan3d_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_image_to_model.json
hash: 5f4d9e4f3cef77fe
official: true
coverage: 1
learned_at: 2026-10-07 21:33:55
nodes: [LoadImage, LoadImage, SaveGLB, TencentImageToModelNode, SaveGLB, Preview3D, SaveImage, SaveImage, SaveImage, SaveImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_hunyuan3d_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_hunyuan3d_image_to_model.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LoadImage`
- `LoadImage`
- `SaveGLB`
- `TencentImageToModelNode`
- `SaveGLB`
- `Preview3D`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`LoadImage`、`SaveGLB`、`TencentImageToModelNode`、`Preview3D`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、SaveGLB、Preview3D、TencentImageToModelNode、sd15-t2i-basic、sd15-t2i-lora、node
