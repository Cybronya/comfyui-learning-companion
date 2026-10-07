---
key: comfyui-workflow-templates-json/api_kling_omni_edit_video.json
name: api_kling_omni_edit_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_kling_omni_edit_video.json
hash: 9a7768393e54fe55
official: true
coverage: 0.714286
learned_at: 2026-10-07 21:34:03
nodes: [SaveVideo, Note, LoadVideo, LoadImage, KlingOmniProEditVideoNode, Video Slice, BatchImagesNode]
patterns: []
missing: [Video Slice]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_kling_omni_edit_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_kling_omni_edit_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `SaveVideo`
- `Note`
- `LoadVideo`
- `LoadImage`
- `KlingOmniProEditVideoNode`
- `Video Slice`
- `BatchImagesNode`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`SaveVideo`、`LoadVideo`、`LoadImage`、`KlingOmniProEditVideoNode`、`BatchImagesNode`

**缺卡**（1）：`Video Slice`

**用到的条目**：LoadImage、SaveVideo、BatchImagesNode、LoadVideo、KlingOmniProEditVideoNode、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
