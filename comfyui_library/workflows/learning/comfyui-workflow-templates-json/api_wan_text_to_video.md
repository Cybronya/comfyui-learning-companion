---
key: comfyui-workflow-templates-json/api_wan_text_to_video.json
name: api_wan_text_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_wan_text_to_video.json
hash: 2a72e1ef0bf99c85
official: true
coverage: 0.666667
learned_at: 2026-10-10 22:46:48
nodes: [SaveVideo, RecordAudio, MarkdownNote, WanTextToVideoApi, MarkdownNote, LoadAudio]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_wan_text_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_wan_text_to_video.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `SaveVideo`
- `RecordAudio`
- `MarkdownNote`
- `WanTextToVideoApi`
- `MarkdownNote`
- `LoadAudio`

## 知识

覆盖率 **67%**（4/6）

**有卡**：`SaveVideo`、`RecordAudio`、`WanTextToVideoApi`、`LoadAudio`

**用到的条目**：SaveVideo、LoadAudio、RecordAudio、WanTextToVideoApi、sd15-t2i-basic、sd15-t2i-lora、Text、SaveImage
