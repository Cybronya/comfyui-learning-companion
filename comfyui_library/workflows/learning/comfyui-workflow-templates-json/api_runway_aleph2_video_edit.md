---
key: comfyui-workflow-templates-json/api_runway_aleph2_video_edit.json
name: api_runway_aleph2_video_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_aleph2_video_edit.json
hash: ee7590c9fe5a1580
official: true
coverage: 0.875
learned_at: 2026-10-07 21:34:43
nodes: [RunwayAleph2VideoToVideoNode, RunwayAleph2PromptImageNode, LoadImage, LoadVideo, RunwayAleph2KeyframeNode, LoadImage, SaveVideo, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_runway_aleph2_video_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_runway_aleph2_video_edit.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `RunwayAleph2VideoToVideoNode`
- `RunwayAleph2PromptImageNode`
- `LoadImage`
- `LoadVideo`
- `RunwayAleph2KeyframeNode`
- `LoadImage`
- `SaveVideo`
- `MarkdownNote`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`RunwayAleph2VideoToVideoNode`、`RunwayAleph2PromptImageNode`、`LoadImage`、`LoadVideo`、`RunwayAleph2KeyframeNode`、`SaveVideo`

**用到的条目**：LoadImage、RunwayAleph2PromptImageNode、SaveVideo、LoadVideo、RunwayAleph2KeyframeNode、RunwayAleph2VideoToVideoNode、sd15-t2i-basic、sd15-t2i-lora
