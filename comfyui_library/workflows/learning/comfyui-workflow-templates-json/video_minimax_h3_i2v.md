---
key: comfyui-workflow-templates-json/video_minimax_h3_i2v.json
name: video_minimax_h3_i2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_i2v.json
hash: 34ee39544808fd3b
official: true
coverage: 0.555556
learned_at: 2026-10-07 21:37:09
nodes: [SaveVideo, LoadImage, ResolutionSelector, 4c314f31-ecda-4b08-ae98-faaba1bf613f, MarkdownNote, MarkdownNote, MarkdownNote, ImageScaleToTotalPixels, GetImageSize]
patterns: []
missing: [4c314f31-ecda-4b08-ae98-faaba1bf613f]
discoveries: [次要节点 `4c314f31-ecda-4b08-ae98-faaba1bf613f` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_minimax_h3_i2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_i2v.json`

## 结构

**生成流程**：Latent → Process → Output → Other

**节点**（9 个）：
- `SaveVideo`
- `LoadImage`
- `ResolutionSelector`
- `4c314f31-ecda-4b08-ae98-faaba1bf613f`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `GetImageSize`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`SaveVideo`、`LoadImage`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`GetImageSize`

**缺卡**（1）：`4c314f31-ecda-4b08-ae98-faaba1bf613f`

**用到的条目**：ResolutionSelector、LoadImage、GetImageSize、GetImageSize、SaveVideo、ImageScaleToTotalPixels、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `4c314f31-ecda-4b08-ae98-faaba1bf613f` 知识库中没有该节点类型的任何知识
