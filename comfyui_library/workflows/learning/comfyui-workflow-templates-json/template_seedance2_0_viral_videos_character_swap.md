---
key: comfyui-workflow-templates-json/template_seedance2_0_viral_videos_character_swap.json
name: template_seedance2_0_viral_videos_character_swap
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_seedance2_0_viral_videos_character_swap.json
hash: f9a7baf356457704
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:36:26
nodes: [LoadVideo, PreviewAny, Video Slice, OpenAIGPTImageNodeV2, ImageFromBatch, GetVideoComponents, LoadImage, SaveVideo, SaveImage, StringConcatenate, ByteDance2ReferenceNodeV2, GeminiNodeV3]
patterns: []
missing: [Video Slice]
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/template_seedance2_0_viral_videos_character_swap.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_seedance2_0_viral_videos_character_swap.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `LoadVideo`
- `PreviewAny`
- `Video Slice`
- `OpenAIGPTImageNodeV2`
- `ImageFromBatch`
- `GetVideoComponents`
- `LoadImage`
- `SaveVideo`
- `SaveImage`
- `StringConcatenate`
- `ByteDance2ReferenceNodeV2`
- `GeminiNodeV3`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`LoadVideo`、`OpenAIGPTImageNodeV2`、`ImageFromBatch`、`GetVideoComponents`、`LoadImage`、`SaveVideo`、`SaveImage`、`StringConcatenate`、`ByteDance2ReferenceNodeV2`、`GeminiNodeV3`

**缺卡**（1）：`Video Slice`

**用到的条目**：LoadImage、SaveImage、SaveVideo、GetVideoComponents、ImageFromBatch、LoadVideo、StringConcatenate、ByteDance2ReferenceNodeV2

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
