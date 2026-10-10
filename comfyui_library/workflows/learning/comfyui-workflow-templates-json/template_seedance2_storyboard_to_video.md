---
key: comfyui-workflow-templates-json/template_seedance2_storyboard_to_video.json
name: template_seedance2_storyboard_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_seedance2_storyboard_to_video.json
hash: 3303408db5ad7fcf
official: true
coverage: 0.769231
learned_at: 2026-10-10 22:49:10
nodes: [OpenAIGPTImageNodeV2, SaveImage, LoadImage, SaveVideo, LoadImage, PreviewAny, MarkdownNote, MarkdownNote, ImageStitch, StringConcatenate, ByteDance2ReferenceNodeV2, GeminiNodeV3, GeminiNodeV3]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/template_seedance2_storyboard_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_seedance2_storyboard_to_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `OpenAIGPTImageNodeV2`
- `SaveImage`
- `LoadImage`
- `SaveVideo`
- `LoadImage`
- `PreviewAny`
- `MarkdownNote`
- `MarkdownNote`
- `ImageStitch`
- `StringConcatenate`
- `ByteDance2ReferenceNodeV2`
- `GeminiNodeV3`
- `GeminiNodeV3`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`OpenAIGPTImageNodeV2`、`SaveImage`、`LoadImage`、`SaveVideo`、`ImageStitch`、`StringConcatenate`、`ByteDance2ReferenceNodeV2`、`GeminiNodeV3`

**用到的条目**：LoadImage、SaveImage、SaveVideo、ImageStitch、ImageStitch、StringConcatenate、ByteDance2ReferenceNodeV2、GeminiNodeV3
