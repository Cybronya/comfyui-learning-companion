---
key: comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json
name: utility_sdpose_multi_person_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json
hash: 83c66c8fa40a778e
official: true
coverage: 0.583333
learned_at: 2026-10-07 21:36:51
nodes: [MarkdownNote, 01b6a731-fb78-4070-9a38-c87146da9604, DrawBBoxes, ResizeImageMaskNode, PrimitiveInt, MarkdownNote, ImageBlend, LoadVideo, CreateVideo, SaveVideo, GetVideoComponents, PreviewImage]
patterns: []
missing: [01b6a731-fb78-4070-9a38-c87146da9604]
discoveries: [次要节点 `01b6a731-fb78-4070-9a38-c87146da9604` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `MarkdownNote`
- `01b6a731-fb78-4070-9a38-c87146da9604`
- `DrawBBoxes`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `MarkdownNote`
- `ImageBlend`
- `LoadVideo`
- `CreateVideo`
- `SaveVideo`
- `GetVideoComponents`
- `PreviewImage`

## 知识

覆盖率 **58%**（7/12）

**有卡**：`DrawBBoxes`、`ResizeImageMaskNode`、`ImageBlend`、`LoadVideo`、`CreateVideo`、`SaveVideo`、`GetVideoComponents`

**缺卡**（1）：`01b6a731-fb78-4070-9a38-c87146da9604`

**用到的条目**：ResizeImageMaskNode、SaveVideo、CreateVideo、GetVideoComponents、ImageBlend、LoadVideo、DrawBBoxes、sd15-t2i-basic

## 学习发现

- 次要节点 `01b6a731-fb78-4070-9a38-c87146da9604` 知识库中没有该节点类型的任何知识
