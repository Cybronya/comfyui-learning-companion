---
key: comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json
name: api_beeble_switchx_video_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json
hash: 337d004a1cc32779
official: true
coverage: 0.7
learned_at: 2026-10-07 21:33:17
nodes: [LoadImage, MarkdownNote, BeebleSwitchXVideoEdit, LoadVideo, SaveVideo, SaveVideo, GetVideoComponents, Video Slice, GetImageSize, PreviewAny]
patterns: []
missing: [Video Slice]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LoadImage`
- `MarkdownNote`
- `BeebleSwitchXVideoEdit`
- `LoadVideo`
- `SaveVideo`
- `SaveVideo`
- `GetVideoComponents`
- `Video Slice`
- `GetImageSize`
- `PreviewAny`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`LoadImage`、`BeebleSwitchXVideoEdit`、`LoadVideo`、`SaveVideo`、`GetVideoComponents`、`GetImageSize`

**缺卡**（1）：`Video Slice`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveVideo、GetVideoComponents、LoadVideo、BeebleSwitchXVideoEdit、sd15-t2i-basic

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
