---
key: comfyui-workflow-templates-json/video_wan21_scail2_character_replacement_int8.json
name: video_wan21_scail2_character_replacement_int8
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan21_scail2_character_replacement_int8.json
hash: 9336ce2e9bda2408
official: true
coverage: 0.666667
learned_at: 2026-10-07 21:37:13
nodes: [LoadVideo, SaveVideo, LoadImage, CreateVideo, GetVideoComponents, GetImageSize, ComfyMathExpression, PreviewAny, BatchImagesNode, CreateVideo, SaveVideo, MarkdownNote, d1ab1953-6167-4827-b44e-b4108cea5702, 56bf150b-bd14-4513-8e03-335e1972ba62, MarkdownNote]
patterns: []
missing: [56bf150b-bd14-4513-8e03-335e1972ba62, d1ab1953-6167-4827-b44e-b4108cea5702]
discoveries: [次要节点 `56bf150b-bd14-4513-8e03-335e1972ba62` 知识库中没有该节点类型的任何知识, 次要节点 `d1ab1953-6167-4827-b44e-b4108cea5702` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_wan21_scail2_character_replacement_int8.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan21_scail2_character_replacement_int8.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
- `LoadVideo`
- `SaveVideo`
- `LoadImage`
- `CreateVideo`
- `GetVideoComponents`
- `GetImageSize`
- `ComfyMathExpression`
- `PreviewAny`
- `BatchImagesNode`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `d1ab1953-6167-4827-b44e-b4108cea5702`
- `56bf150b-bd14-4513-8e03-335e1972ba62`
- `MarkdownNote`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`LoadVideo`、`SaveVideo`、`LoadImage`、`CreateVideo`、`GetVideoComponents`、`GetImageSize`、`ComfyMathExpression`、`BatchImagesNode`

**缺卡**（2）：`56bf150b-bd14-4513-8e03-335e1972ba62`、`d1ab1953-6167-4827-b44e-b4108cea5702`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveVideo、BatchImagesNode、ComfyMathExpression、CreateVideo、GetVideoComponents

## 学习发现

- 次要节点 `56bf150b-bd14-4513-8e03-335e1972ba62` 知识库中没有该节点类型的任何知识
- 次要节点 `d1ab1953-6167-4827-b44e-b4108cea5702` 知识库中没有该节点类型的任何知识
