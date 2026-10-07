---
key: comfyui-workflow-templates-json/api_ideogram_v4_5_precise_image_edit.json
name: api_ideogram_v4_5_precise_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_v4_5_precise_image_edit.json
hash: 170cc8b1fb2c82cf
official: true
coverage: 0.666667
learned_at: 2026-10-07 21:33:58
nodes: [LoadImage, BuildJsonPromptIdeogram, CreateBoundingBoxes, PreviewAny, SaveImageAdvanced, ImageCompare, MarkdownNote, MarkdownNote, IdeogramPreciseEditApi]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_ideogram_v4_5_precise_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_ideogram_v4_5_precise_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LoadImage`
- `BuildJsonPromptIdeogram`
- `CreateBoundingBoxes`
- `PreviewAny`
- `SaveImageAdvanced`
- `ImageCompare`
- `MarkdownNote`
- `MarkdownNote`
- `IdeogramPreciseEditApi`

## 知识

覆盖率 **67%**（6/9）

**有卡**：`LoadImage`、`BuildJsonPromptIdeogram`、`CreateBoundingBoxes`、`SaveImageAdvanced`、`ImageCompare`、`IdeogramPreciseEditApi`

**用到的条目**：LoadImage、IdeogramPreciseEditApi、BuildJsonPromptIdeogram、SaveImageAdvanced、CreateBoundingBoxes、ImageCompare、sd15-t2i-basic、sd15-t2i-lora
