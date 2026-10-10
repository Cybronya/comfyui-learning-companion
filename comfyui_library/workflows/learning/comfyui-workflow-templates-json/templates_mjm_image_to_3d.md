---
key: comfyui-workflow-templates-json/templates_mjm_image_to_3d.json
name: templates_mjm_image_to_3d
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates_mjm_image_to_3d.json
hash: 81bfc4f83bce2f02
official: true
coverage: 0.916667
learned_at: 2026-10-10 22:49:31
nodes: [BatchImagesNode, MarkdownNote, LoadImage, GeminiNanoBanana2, SaveImage, GeminiNanoBanana2, SaveImage, SaveImage, GeminiNanoBanana2, Preview3D, TripoImageToModelNode, SaveGLB]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/templates_mjm_image_to_3d.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates_mjm_image_to_3d.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `BatchImagesNode`
- `MarkdownNote`
- `LoadImage`
- `GeminiNanoBanana2`
- `SaveImage`
- `GeminiNanoBanana2`
- `SaveImage`
- `SaveImage`
- `GeminiNanoBanana2`
- `Preview3D`
- `TripoImageToModelNode`
- `SaveGLB`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`BatchImagesNode`、`LoadImage`、`GeminiNanoBanana2`、`SaveImage`、`Preview3D`、`TripoImageToModelNode`、`SaveGLB`

**用到的条目**：LoadImage、SaveImage、SaveGLB、Preview3D、BatchImagesNode、GeminiNanoBanana2、TripoImageToModelNode、sd15-t2i-basic
