---
key: comfyui-workflow-templates-json/template_eric_exploded_view.json
name: template_eric_exploded_view
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_eric_exploded_view.json
hash: ebd7f393a99d4fd1
official: true
coverage: 0.875
learned_at: 2026-10-10 22:49:00
nodes: [SaveImage, LoadImage, SaveImage, ByteDanceFirstLastFrameNode, SaveVideo, ByteDanceFirstLastFrameNode, SaveVideo, Note, SaveVideo, GetVideoComponents, GetVideoComponents, Note, BatchImagesNode, CreateVideo, GeminiNanoBanana2V2, GeminiNanoBanana2V2]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/template_eric_exploded_view.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_eric_exploded_view.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `ByteDanceFirstLastFrameNode`
- `SaveVideo`
- `ByteDanceFirstLastFrameNode`
- `SaveVideo`
- `Note`
- `SaveVideo`
- `GetVideoComponents`
- `GetVideoComponents`
- `Note`
- `BatchImagesNode`
- `CreateVideo`
- `GeminiNanoBanana2V2`
- `GeminiNanoBanana2V2`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`SaveImage`、`LoadImage`、`ByteDanceFirstLastFrameNode`、`SaveVideo`、`GetVideoComponents`、`BatchImagesNode`、`CreateVideo`、`GeminiNanoBanana2V2`

**用到的条目**：LoadImage、SaveImage、SaveVideo、BatchImagesNode、CreateVideo、GetVideoComponents、ByteDanceFirstLastFrameNode、GeminiNanoBanana2V2
