---
key: comfyui-workflow-templates-json/templates-all_in_one-image_edit_models.json
name: templates-all_in_one-image_edit_models
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates-all_in_one-image_edit_models.json
hash: d91afab745d6cd73
official: true
coverage: 0.631579
learned_at: 2026-10-07 21:36:31
nodes: [GrokImageEditNode, GeminiImage2Node, ByteDanceSeedreamNode, SaveImage, OpenAIGPTImage1, SaveImage, PrimitiveStringMultiline, 84c2d189-ef35-4317-b56d-3bed5045314c, 4bef21c6-ad90-465c-b6db-791064306e5c, Reroute, Reroute, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, LoadImage, fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88, MarkdownNote]
patterns: []
missing: [4bef21c6-ad90-465c-b6db-791064306e5c, 84c2d189-ef35-4317-b56d-3bed5045314c, fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88]
discoveries: [次要节点 `4bef21c6-ad90-465c-b6db-791064306e5c` 知识库中没有该节点类型的任何知识, 次要节点 `84c2d189-ef35-4317-b56d-3bed5045314c` 知识库中没有该节点类型的任何知识, 次要节点 `fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/templates-all_in_one-image_edit_models.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates-all_in_one-image_edit_models.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `GrokImageEditNode`
- `GeminiImage2Node`
- `ByteDanceSeedreamNode`
- `SaveImage`
- `OpenAIGPTImage1`
- `SaveImage`
- `PrimitiveStringMultiline`
- `84c2d189-ef35-4317-b56d-3bed5045314c`
- `4bef21c6-ad90-465c-b6db-791064306e5c`
- `Reroute`
- `Reroute`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88`
- `MarkdownNote`

## 知识

覆盖率 **63%**（12/19）

**有卡**：`GrokImageEditNode`、`GeminiImage2Node`、`ByteDanceSeedreamNode`、`SaveImage`、`OpenAIGPTImage1`、`LoadImage`

**缺卡**（3）：`4bef21c6-ad90-465c-b6db-791064306e5c`、`84c2d189-ef35-4317-b56d-3bed5045314c`、`fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88`

**用到的条目**：LoadImage、ByteDanceSeedreamNode、SaveImage、GeminiImage2Node、GrokImageEditNode、OpenAIGPTImage1、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `4bef21c6-ad90-465c-b6db-791064306e5c` 知识库中没有该节点类型的任何知识
- 次要节点 `84c2d189-ef35-4317-b56d-3bed5045314c` 知识库中没有该节点类型的任何知识
- 次要节点 `fc6d7b70-f58e-4eeb-8e52-b390a2d5fd88` 知识库中没有该节点类型的任何知识
