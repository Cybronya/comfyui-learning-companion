---
key: comfyui-workflow-templates-json/utility_sdpose_multi_person.json
name: utility_sdpose_multi_person
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_sdpose_multi_person.json
hash: 7c0c2da013e5a18c
official: true
coverage: 0.5
learned_at: 2026-10-10 22:49:55
nodes: [MarkdownNote, 01b6a731-fb78-4070-9a38-c87146da9604, LoadImage, SaveImage, DrawBBoxes, PreviewImage, ResizeImageMaskNode, PrimitiveInt, MarkdownNote, ImageBlend]
patterns: []
missing: [01b6a731-fb78-4070-9a38-c87146da9604]
discoveries: [次要节点 `01b6a731-fb78-4070-9a38-c87146da9604` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/utility_sdpose_multi_person.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_sdpose_multi_person.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `MarkdownNote`
- `01b6a731-fb78-4070-9a38-c87146da9604`
- `LoadImage`
- `SaveImage`
- `DrawBBoxes`
- `PreviewImage`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `MarkdownNote`
- `ImageBlend`

## 知识

覆盖率 **50%**（5/10）

**有卡**：`LoadImage`、`SaveImage`、`DrawBBoxes`、`ResizeImageMaskNode`、`ImageBlend`

**缺卡**（1）：`01b6a731-fb78-4070-9a38-c87146da9604`

**用到的条目**：LoadImage、ResizeImageMaskNode、SaveImage、ImageBlend、DrawBBoxes、sd15-t2i-basic、sd15-t2i-lora、ResizeImage

## 学习发现

- 次要节点 `01b6a731-fb78-4070-9a38-c87146da9604` 知识库中没有该节点类型的任何知识
