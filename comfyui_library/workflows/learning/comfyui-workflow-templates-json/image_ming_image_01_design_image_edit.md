---
key: comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json
name: image_ming_image_01_design_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json
hash: 843ee90b638d843f
official: true
coverage: 0.526316
learned_at: 2026-10-15 22:24:54
nodes: [LoadImage, 4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1, GetImageSize, ResizeImageMaskNode, MarkdownNote, MarkdownNote, MarkdownNote, CreateBoundingBoxes, PreviewAny, BuildJsonPromptIdeogram, PreviewAny, PreviewImage, MarkdownNote, PreviewAny, ae951efd-07f6-49cb-bfdb-0b8e3eee4cda, ImageStitch, ImageStitch, PreviewImage, SaveImageAdvanced]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `LoadImage`
- `4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1`
- `GetImageSize`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CreateBoundingBoxes`
- `PreviewAny`
- `BuildJsonPromptIdeogram`
- `PreviewAny`
- `PreviewImage`
- `MarkdownNote`
- `PreviewAny`
- `ae951efd-07f6-49cb-bfdb-0b8e3eee4cda`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `SaveImageAdvanced`

## 知识

覆盖率 **53%**（10/19）

**有卡**：`LoadImage`、`4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1`、`GetImageSize`、`ResizeImageMaskNode`、`CreateBoundingBoxes`、`BuildJsonPromptIdeogram`、`ae951efd-07f6-49cb-bfdb-0b8e3eee4cda`、`ImageStitch`、`SaveImageAdvanced`

**用到的条目**：LoadImage、BuildJsonPromptIdeogram、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImageAdvanced、ImageStitch、ImageStitch
