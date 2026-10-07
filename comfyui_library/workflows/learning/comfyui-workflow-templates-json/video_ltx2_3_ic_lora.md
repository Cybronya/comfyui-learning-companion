---
key: comfyui-workflow-templates-json/video_ltx2_3_ic_lora.json
name: video_ltx2_3_ic_lora
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_3_ic_lora.json
hash: e0338ea7c9046b18
official: true
coverage: 0.333333
learned_at: 2026-10-07 21:37:02
nodes: [SaveVideo, MarkdownNote, f9f61b10-b689-4d67-b4fa-0acc1d9b5390, LoadVideo, LoadImage, Video Slice, ed545fa5-009c-4ccc-b318-4c00dd239751, MarkdownNote, PreviewImage]
patterns: []
missing: [Video Slice, ed545fa5-009c-4ccc-b318-4c00dd239751, f9f61b10-b689-4d67-b4fa-0acc1d9b5390]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识, 次要节点 `ed545fa5-009c-4ccc-b318-4c00dd239751` 知识库中没有该节点类型的任何知识, 次要节点 `f9f61b10-b689-4d67-b4fa-0acc1d9b5390` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_ltx2_3_ic_lora.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_3_ic_lora.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `SaveVideo`
- `MarkdownNote`
- `f9f61b10-b689-4d67-b4fa-0acc1d9b5390`
- `LoadVideo`
- `LoadImage`
- `Video Slice`
- `ed545fa5-009c-4ccc-b318-4c00dd239751`
- `MarkdownNote`
- `PreviewImage`

## 知识

覆盖率 **33%**（3/9）

**有卡**：`SaveVideo`、`LoadVideo`、`LoadImage`

**缺卡**（3）：`Video Slice`、`ed545fa5-009c-4ccc-b318-4c00dd239751`、`f9f61b10-b689-4d67-b4fa-0acc1d9b5390`

**用到的条目**：LoadImage、SaveVideo、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、SaveImage、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
- 次要节点 `ed545fa5-009c-4ccc-b318-4c00dd239751` 知识库中没有该节点类型的任何知识
- 次要节点 `f9f61b10-b689-4d67-b4fa-0acc1d9b5390` 知识库中没有该节点类型的任何知识
