---
key: comfyui-workflow-templates-json/video_bernini_r_video_editing.json
name: video_bernini_r_video_editing
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_bernini_r_video_editing.json
hash: ef0644e39739b408
official: true
coverage: 0.5
learned_at: 2026-10-10 22:50:05
nodes: [LoadVideo, SaveVideo, MarkdownNote, MarkdownNote, BatchImagesNode, MarkdownNote, LoadImage, Video Slice, GetVideoComponents, GetImageSize, PreviewAny, 69c3c422-bcfe-4955-bc23-8bac307287a8]
patterns: []
missing: [69c3c422-bcfe-4955-bc23-8bac307287a8, Video Slice]
discoveries: [次要节点 `69c3c422-bcfe-4955-bc23-8bac307287a8` 知识库中没有该节点类型的任何知识, 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_bernini_r_video_editing.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_bernini_r_video_editing.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `LoadVideo`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `BatchImagesNode`
- `MarkdownNote`
- `LoadImage`
- `Video Slice`
- `GetVideoComponents`
- `GetImageSize`
- `PreviewAny`
- `69c3c422-bcfe-4955-bc23-8bac307287a8`

## 知识

覆盖率 **50%**（6/12）

**有卡**：`LoadVideo`、`SaveVideo`、`BatchImagesNode`、`LoadImage`、`GetVideoComponents`、`GetImageSize`

**缺卡**（2）：`69c3c422-bcfe-4955-bc23-8bac307287a8`、`Video Slice`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveVideo、BatchImagesNode、GetVideoComponents、LoadVideo、sd15-t2i-basic

## 学习发现

- 次要节点 `69c3c422-bcfe-4955-bc23-8bac307287a8` 知识库中没有该节点类型的任何知识
- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
