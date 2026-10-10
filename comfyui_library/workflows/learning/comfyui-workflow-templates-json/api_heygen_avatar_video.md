---
key: comfyui-workflow-templates-json/api_heygen_avatar_video.json
name: api_heygen_avatar_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_heygen_avatar_video.json
hash: 1e48c3fb1c035eb0
official: true
coverage: 0.666667
learned_at: 2026-10-10 22:44:20
nodes: [HeyGenCreateAvatarNode, HeyGenAvatarVideoNode, SaveText, StringConcatenate, PreviewAny, SaveVideo, MarkdownNote, ColorToRGBInt, PreviewAny]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_heygen_avatar_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_heygen_avatar_video.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `HeyGenCreateAvatarNode`
- `HeyGenAvatarVideoNode`
- `SaveText`
- `StringConcatenate`
- `PreviewAny`
- `SaveVideo`
- `MarkdownNote`
- `ColorToRGBInt`
- `PreviewAny`

## 知识

覆盖率 **67%**（6/9）

**有卡**：`HeyGenCreateAvatarNode`、`HeyGenAvatarVideoNode`、`SaveText`、`StringConcatenate`、`SaveVideo`、`ColorToRGBInt`

**用到的条目**：SaveText、SaveVideo、StringConcatenate、ColorToRGBInt、HeyGenAvatarVideoNode、HeyGenCreateAvatarNode、sd15-t2i-basic、sd15-t2i-lora
