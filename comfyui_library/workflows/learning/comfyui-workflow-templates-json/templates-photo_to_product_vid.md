---
key: comfyui-workflow-templates-json/templates-photo_to_product_vid.json
name: templates-photo_to_product_vid
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates-photo_to_product_vid.json
hash: 54ab4faa727c4686
official: true
coverage: 0.909091
learned_at: 2026-10-07 21:36:33
nodes: [ByteDanceSeedreamNode, SaveImage, SaveVideo, MinimaxHailuoVideoNode, MinimaxHailuoVideoNode, MinimaxHailuoVideoNode, LoadImage, 23514ff4-69d2-461d-97d8-8b34d2981d4b, SaveVideo, SaveVideo, SaveVideo]
patterns: []
missing: [23514ff4-69d2-461d-97d8-8b34d2981d4b]
discoveries: [次要节点 `23514ff4-69d2-461d-97d8-8b34d2981d4b` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/templates-photo_to_product_vid.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates-photo_to_product_vid.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `ByteDanceSeedreamNode`
- `SaveImage`
- `SaveVideo`
- `MinimaxHailuoVideoNode`
- `MinimaxHailuoVideoNode`
- `MinimaxHailuoVideoNode`
- `LoadImage`
- `23514ff4-69d2-461d-97d8-8b34d2981d4b`
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ByteDanceSeedreamNode`、`SaveImage`、`SaveVideo`、`MinimaxHailuoVideoNode`、`LoadImage`

**缺卡**（1）：`23514ff4-69d2-461d-97d8-8b34d2981d4b`

**用到的条目**：LoadImage、ByteDanceSeedreamNode、SaveImage、SaveVideo、MinimaxHailuoVideoNode、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `23514ff4-69d2-461d-97d8-8b34d2981d4b` 知识库中没有该节点类型的任何知识
