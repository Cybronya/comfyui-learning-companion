---
key: comfyui-workflow-templates-json/api_ideogram_v4_5_image_edit.json
name: api_ideogram_v4_5_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_v4_5_image_edit.json
hash: a7e4ebe6936b76b3
official: true
coverage: 0.666667
learned_at: 2026-10-10 22:44:30
nodes: [IdeogramEditApi, LoadImage, BuildJsonPromptIdeogram, CreateBoundingBoxes, PreviewAny, SaveImageAdvanced, ImageCompare, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_ideogram_v4_5_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_v4_5_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `IdeogramEditApi`
- `LoadImage`
- `BuildJsonPromptIdeogram`
- `CreateBoundingBoxes`
- `PreviewAny`
- `SaveImageAdvanced`
- `ImageCompare`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **67%**（6/9）

**有卡**：`IdeogramEditApi`、`LoadImage`、`BuildJsonPromptIdeogram`、`CreateBoundingBoxes`、`SaveImageAdvanced`、`ImageCompare`

**用到的条目**：LoadImage、BuildJsonPromptIdeogram、SaveImageAdvanced、CreateBoundingBoxes、IdeogramEditApi、ImageCompare、sd15-t2i-basic、sd15-t2i-lora
