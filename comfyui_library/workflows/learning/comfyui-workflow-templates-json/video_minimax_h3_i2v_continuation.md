---
key: comfyui-workflow-templates-json/video_minimax_h3_i2v_continuation.json
name: video_minimax_h3_i2v_continuation
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_i2v_continuation.json
hash: 332184c45587d70c
official: true
coverage: 0.5
learned_at: 2026-10-07 21:37:09
nodes: [SaveVideo, LoadImage, ResolutionSelector, 4c314f31-ecda-4b08-ae98-faaba1bf613f, MarkdownNote, MarkdownNote]
patterns: []
missing: [4c314f31-ecda-4b08-ae98-faaba1bf613f]
discoveries: [次要节点 `4c314f31-ecda-4b08-ae98-faaba1bf613f` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_minimax_h3_i2v_continuation.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_i2v_continuation.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（6 个）：
- `SaveVideo`
- `LoadImage`
- `ResolutionSelector`
- `4c314f31-ecda-4b08-ae98-faaba1bf613f`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`SaveVideo`、`LoadImage`、`ResolutionSelector`

**缺卡**（1）：`4c314f31-ecda-4b08-ae98-faaba1bf613f`

**用到的条目**：ResolutionSelector、LoadImage、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、EmptyLatentImage、height 调整经验、width 调整经验

## 学习发现

- 次要节点 `4c314f31-ecda-4b08-ae98-faaba1bf613f` 知识库中没有该节点类型的任何知识
