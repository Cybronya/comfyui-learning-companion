---
key: comfyui-workflow-templates-json/api_seedance2_5_video_editing.json
name: api_seedance2_5_video_editing
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_5_video_editing.json
hash: e29071b36bd50723
official: true
coverage: 0.6
learned_at: 2026-10-10 22:46:10
nodes: [SaveVideo, LoadVideo, Video Slice, MarkdownNote, ByteDance2ReferenceNodeV2]
patterns: []
missing: [Video Slice]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_seedance2_5_video_editing.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_5_video_editing.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `SaveVideo`
- `LoadVideo`
- `Video Slice`
- `MarkdownNote`
- `ByteDance2ReferenceNodeV2`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`SaveVideo`、`LoadVideo`、`ByteDance2ReferenceNodeV2`

**缺卡**（1）：`Video Slice`

**用到的条目**：SaveVideo、LoadVideo、ByteDance2ReferenceNodeV2、sd15-t2i-basic、sd15-t2i-lora、node、v2、ByteDance2ReferenceNode

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
