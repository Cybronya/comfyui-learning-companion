---
key: comfyui-workflow-templates-json/utility_image_segment_sam3.json
name: utility_image_segment_sam3
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_image_segment_sam3.json
hash: d2f0fe6189767934
official: true
coverage: 0.428571
learned_at: 2026-10-10 22:49:45
nodes: [PreviewImage, LoadImage, JoinImageWithAlpha, 6e7ab3ea-96aa-470f-9b94-3d9d0e01f481, MaskPreview, MarkdownNote, MarkdownNote]
patterns: []
missing: [6e7ab3ea-96aa-470f-9b94-3d9d0e01f481]
discoveries: [次要节点 `6e7ab3ea-96aa-470f-9b94-3d9d0e01f481` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/utility_image_segment_sam3.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_image_segment_sam3.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `PreviewImage`
- `LoadImage`
- `JoinImageWithAlpha`
- `6e7ab3ea-96aa-470f-9b94-3d9d0e01f481`
- `MaskPreview`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **43%**（3/7）

**有卡**：`LoadImage`、`JoinImageWithAlpha`、`MaskPreview`

**缺卡**（1）：`6e7ab3ea-96aa-470f-9b94-3d9d0e01f481`

**用到的条目**：LoadImage、MaskPreview、JoinImageWithAlpha、sd15-t2i-basic、sd15-t2i-lora、SaveImage、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `6e7ab3ea-96aa-470f-9b94-3d9d0e01f481` 知识库中没有该节点类型的任何知识
