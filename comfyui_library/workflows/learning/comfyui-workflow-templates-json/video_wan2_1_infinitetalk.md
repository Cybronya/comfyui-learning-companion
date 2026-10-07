---
key: comfyui-workflow-templates-json/video_wan2_1_infinitetalk.json
name: video_wan2_1_infinitetalk
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_1_infinitetalk.json
hash: 3b7f7029adb969b5
official: true
coverage: 0.611111
learned_at: 2026-10-07 21:37:13
nodes: [CreateVideo, LoadAudio, PrimitiveInt, PrimitiveInt, AudioConcat, CreateVideo, SaveVideo, MarkdownNote, SaveVideo, LoadImage, LoadAudio, MarkdownNote, MarkdownNote, BatchImagesNode, Painter, Painter, f94665ea-d4c0-44ce-b3fb-9af101983ff5, dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55]
patterns: []
missing: [dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55, f94665ea-d4c0-44ce-b3fb-9af101983ff5]
discoveries: [次要节点 `dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55` 知识库中没有该节点类型的任何知识, 次要节点 `f94665ea-d4c0-44ce-b3fb-9af101983ff5` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_wan2_1_infinitetalk.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_1_infinitetalk.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（18 个）：
- `CreateVideo`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveInt`
- `AudioConcat`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `SaveVideo`
- `LoadImage`
- `LoadAudio`
- `MarkdownNote`
- `MarkdownNote`
- `BatchImagesNode`
- `Painter`
- `Painter`
- `f94665ea-d4c0-44ce-b3fb-9af101983ff5`
- `dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55`

## 知识

覆盖率 **61%**（11/18）

**有卡**：`CreateVideo`、`LoadAudio`、`AudioConcat`、`SaveVideo`、`LoadImage`、`BatchImagesNode`、`Painter`

**缺卡**（2）：`dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55`、`f94665ea-d4c0-44ce-b3fb-9af101983ff5`

**用到的条目**：LoadImage、SaveVideo、BatchImagesNode、CreateVideo、LoadAudio、AudioConcat、Painter、sd15-t2i-basic

## 学习发现

- 次要节点 `dbb8b58f-7b4a-479d-bfc2-9edf7fce7a55` 知识库中没有该节点类型的任何知识
- 次要节点 `f94665ea-d4c0-44ce-b3fb-9af101983ff5` 知识库中没有该节点类型的任何知识
