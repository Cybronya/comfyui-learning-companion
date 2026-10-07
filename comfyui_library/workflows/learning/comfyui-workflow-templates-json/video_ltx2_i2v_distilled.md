---
key: comfyui-workflow-templates-json/video_ltx2_i2v_distilled.json
name: video_ltx2_i2v_distilled
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_i2v_distilled.json
hash: 93e8ffd0ee03e830
official: true
coverage: 0.5
learned_at: 2026-10-07 21:37:06
nodes: [LoadImage, ResizeImageMaskNode, MarkdownNote, SaveVideo, MarkdownNote, b7c2d337-c38d-4c04-922b-2d638449d13e]
patterns: []
missing: [b7c2d337-c38d-4c04-922b-2d638449d13e]
discoveries: [次要节点 `b7c2d337-c38d-4c04-922b-2d638449d13e` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_ltx2_i2v_distilled.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_i2v_distilled.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `LoadImage`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `SaveVideo`
- `MarkdownNote`
- `b7c2d337-c38d-4c04-922b-2d638449d13e`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`LoadImage`、`ResizeImageMaskNode`、`SaveVideo`

**缺卡**（1）：`b7c2d337-c38d-4c04-922b-2d638449d13e`

**用到的条目**：LoadImage、ResizeImageMaskNode、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、ResizeImage、node、height 调整经验

## 学习发现

- 次要节点 `b7c2d337-c38d-4c04-922b-2d638449d13e` 知识库中没有该节点类型的任何知识
