---
key: comfyui-workflow-templates-json/api_google_gemini_image.json
name: api_google_gemini_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_image.json
hash: 0c15fa06fd1eaf95
official: true
coverage: 0.666667
learned_at: 2026-10-07 21:33:39
nodes: [GeminiInputFiles, GeminiInputFiles, MarkdownNote, PreviewAny, LoadImage, SaveImage, GeminiImageNode, MarkdownNote, BatchImagesNode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_google_gemini_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_google_gemini_image.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `GeminiInputFiles`
- `GeminiInputFiles`
- `MarkdownNote`
- `PreviewAny`
- `LoadImage`
- `SaveImage`
- `GeminiImageNode`
- `MarkdownNote`
- `BatchImagesNode`

## 知识

覆盖率 **67%**（6/9）

**有卡**：`GeminiInputFiles`、`LoadImage`、`SaveImage`、`GeminiImageNode`、`BatchImagesNode`

**用到的条目**：LoadImage、SaveImage、BatchImagesNode、GeminiImageNode、GeminiInputFiles、sd15-t2i-basic、sd15-t2i-lora、node
