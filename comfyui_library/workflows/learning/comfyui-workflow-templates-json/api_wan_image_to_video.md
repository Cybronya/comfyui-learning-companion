---
key: comfyui-workflow-templates-json/api_wan_image_to_video.json
name: api_wan_image_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_wan_image_to_video.json
hash: 042cb69775bfcca7
official: true
coverage: 0.714286
learned_at: 2026-10-10 22:46:46
nodes: [SaveVideo, RecordAudio, MarkdownNote, MarkdownNote, LoadImage, WanImageToVideoApi, LoadAudio]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_wan_image_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_wan_image_to_video.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `SaveVideo`
- `RecordAudio`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `WanImageToVideoApi`
- `LoadAudio`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`SaveVideo`、`RecordAudio`、`LoadImage`、`WanImageToVideoApi`、`LoadAudio`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、RecordAudio、WanImageToVideoApi、sd15-t2i-basic、sd15-t2i-lora、WanImageToVideo
