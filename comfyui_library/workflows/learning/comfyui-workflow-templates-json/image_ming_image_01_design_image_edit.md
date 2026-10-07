---
key: comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json
name: image_ming_image_01_design_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_ming_image_01_design_image_edit.json
hash: 843ee90b638d843f
official: true
coverage: 0.421053
learned_at: 2026-10-07 21:35:52
nodes: [LoadImage, 4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1, GetImageSize, ResizeImageMaskNode, MarkdownNote, MarkdownNote, MarkdownNote, CreateBoundingBoxes, PreviewAny, BuildJsonPromptIdeogram, PreviewAny, PreviewImage, MarkdownNote, PreviewAny, ae951efd-07f6-49cb-bfdb-0b8e3eee4cda, ImageStitch, ImageStitch, PreviewImage, SaveImageAdvanced]
patterns: []
missing: [4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1, ae951efd-07f6-49cb-bfdb-0b8e3eee4cda]
discoveries: [次要节点 `4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1` 知识库中没有该节点类型的任何知识, 次要节点 `ae951efd-07f6-49cb-bfdb-0b8e3eee4cda` 知识库中没有该节点类型的任何知识]
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

覆盖率 **42%**（8/19）

**有卡**：`LoadImage`、`GetImageSize`、`ResizeImageMaskNode`、`CreateBoundingBoxes`、`BuildJsonPromptIdeogram`、`ImageStitch`、`SaveImageAdvanced`

**缺卡**（2）：`4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1`、`ae951efd-07f6-49cb-bfdb-0b8e3eee4cda`

**用到的条目**：LoadImage、BuildJsonPromptIdeogram、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImageAdvanced、ImageStitch、CreateBoundingBoxes

## 学习发现

- 次要节点 `4522b5d6-7f71-4b60-8fab-1e6ffbd5f1c1` 知识库中没有该节点类型的任何知识
- 次要节点 `ae951efd-07f6-49cb-bfdb-0b8e3eee4cda` 知识库中没有该节点类型的任何知识
