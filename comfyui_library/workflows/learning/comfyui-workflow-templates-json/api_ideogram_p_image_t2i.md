---
key: comfyui-workflow-templates-json/api_ideogram_p_image_t2i.json
name: api_ideogram_p_image_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_p_image_t2i.json
hash: fd20cd8b658e08a3
official: true
coverage: 0.8
learned_at: 2026-10-10 22:44:30
nodes: [PreviewAny, CreateBoundingBoxes, IdeogramPImage, BuildJsonPromptIdeogram, SaveImageAdvanced]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_ideogram_p_image_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_p_image_t2i.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `PreviewAny`
- `CreateBoundingBoxes`
- `IdeogramPImage`
- `BuildJsonPromptIdeogram`
- `SaveImageAdvanced`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`CreateBoundingBoxes`、`IdeogramPImage`、`BuildJsonPromptIdeogram`、`SaveImageAdvanced`

**用到的条目**：BuildJsonPromptIdeogram、SaveImageAdvanced、CreateBoundingBoxes、IdeogramPImage、sd15-t2i-basic、sd15-t2i-lora、SaveImage、CLIPTextEncode
