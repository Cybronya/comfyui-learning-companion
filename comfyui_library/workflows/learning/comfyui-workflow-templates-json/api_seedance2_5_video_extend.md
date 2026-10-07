---
key: comfyui-workflow-templates-json/api_seedance2_5_video_extend.json
name: api_seedance2_5_video_extend
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_5_video_extend.json
hash: 4fd2a20e1a89a513
official: true
coverage: 0.571429
learned_at: 2026-10-07 21:34:51
nodes: [SaveVideo, LoadVideo, Video Slice, ByteDance2ReferenceNodeV2, d9aa59a4-3784-4796-9f1b-5b467fb41fa1, SaveVideo, MarkdownNote]
patterns: []
missing: [Video Slice, d9aa59a4-3784-4796-9f1b-5b467fb41fa1]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识, 次要节点 `d9aa59a4-3784-4796-9f1b-5b467fb41fa1` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_seedance2_5_video_extend.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_seedance2_5_video_extend.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `SaveVideo`
- `LoadVideo`
- `Video Slice`
- `ByteDance2ReferenceNodeV2`
- `d9aa59a4-3784-4796-9f1b-5b467fb41fa1`
- `SaveVideo`
- `MarkdownNote`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`SaveVideo`、`LoadVideo`、`ByteDance2ReferenceNodeV2`

**缺卡**（2）：`Video Slice`、`d9aa59a4-3784-4796-9f1b-5b467fb41fa1`

**用到的条目**：SaveVideo、LoadVideo、ByteDance2ReferenceNodeV2、sd15-t2i-basic、sd15-t2i-lora、node、v2、ByteDance2ReferenceNode

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
- 次要节点 `d9aa59a4-3784-4796-9f1b-5b467fb41fa1` 知识库中没有该节点类型的任何知识
