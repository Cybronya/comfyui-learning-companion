---
key: comfyui-workflow-templates-json/utility_birefnet_remove_background.json
name: utility_birefnet_remove_background
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_birefnet_remove_background.json
hash: a89e7323957cea65
official: true
coverage: 0.4
learned_at: 2026-10-10 22:49:39
nodes: [LoadImage, PreviewImage, 5b40ca21-ba1a-41d5-b403-4d2d7acdc195, MaskPreview, MarkdownNote]
patterns: []
missing: [5b40ca21-ba1a-41d5-b403-4d2d7acdc195]
discoveries: [次要节点 `5b40ca21-ba1a-41d5-b403-4d2d7acdc195` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/utility_birefnet_remove_background.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_birefnet_remove_background.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `LoadImage`
- `PreviewImage`
- `5b40ca21-ba1a-41d5-b403-4d2d7acdc195`
- `MaskPreview`
- `MarkdownNote`

## 知识

覆盖率 **40%**（2/5）

**有卡**：`LoadImage`、`MaskPreview`

**缺卡**（1）：`5b40ca21-ba1a-41d5-b403-4d2d7acdc195`

**用到的条目**：LoadImage、MaskPreview、sd15-t2i-basic、sd15-t2i-lora、SaveImage、CS_Preview_Any、easy_multitrackinfooutput、easy_multitracktaskoutput

## 学习发现

- 次要节点 `5b40ca21-ba1a-41d5-b403-4d2d7acdc195` 知识库中没有该节点类型的任何知识
