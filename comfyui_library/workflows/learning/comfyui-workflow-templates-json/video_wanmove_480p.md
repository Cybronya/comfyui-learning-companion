---
key: comfyui-workflow-templates-json/video_wanmove_480p.json
name: video_wanmove_480p
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wanmove_480p.json
hash: f940baa64b76e110
official: true
coverage: 0.75
learned_at: 2026-10-10 22:50:53
nodes: [CreateVideo, SaveVideo, WanMoveVisualizeTracks, GenerateTracks, GenerateTracks, GenerateTracks, WanMoveConcatTrack, WanMoveConcatTrack, ImageScale, SaveVideo, MarkdownNote, LoadImage, PreviewImage, MarkdownNote, WanMoveTracksFromCoords, 0ad975d5-38e9-46ed-a943-85b7c5594051]
patterns: []
missing: [0ad975d5-38e9-46ed-a943-85b7c5594051]
discoveries: [次要节点 `0ad975d5-38e9-46ed-a943-85b7c5594051` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_wanmove_480p.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wanmove_480p.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（16 个）：
- `CreateVideo`
- `SaveVideo`
- `WanMoveVisualizeTracks`
- `GenerateTracks`
- `GenerateTracks`
- `GenerateTracks`
- `WanMoveConcatTrack`
- `WanMoveConcatTrack`
- `ImageScale`
- `SaveVideo`
- `MarkdownNote`
- `LoadImage`
- `PreviewImage`
- `MarkdownNote`
- `WanMoveTracksFromCoords`
- `0ad975d5-38e9-46ed-a943-85b7c5594051`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`CreateVideo`、`SaveVideo`、`WanMoveVisualizeTracks`、`GenerateTracks`、`WanMoveConcatTrack`、`ImageScale`、`LoadImage`、`WanMoveTracksFromCoords`

**缺卡**（1）：`0ad975d5-38e9-46ed-a943-85b7c5594051`

**用到的条目**：LoadImage、SaveVideo、CreateVideo、ImageScale、GenerateTracks、WanMoveConcatTrack、WanMoveTracksFromCoords、WanMoveVisualizeTracks

## 学习发现

- 次要节点 `0ad975d5-38e9-46ed-a943-85b7c5594051` 知识库中没有该节点类型的任何知识
