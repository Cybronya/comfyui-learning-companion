---
key: comfyui-workflow-templates-json/templates-subject_product_swap.app.json
name: templates-subject_product_swap.app
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates-subject_product_swap.app.json
hash: 589fe4d34753fe3f
official: true
coverage: 0.8
learned_at: 2026-10-10 22:49:26
nodes: [LoadImage, LoadImage, GeminiImage2Node, SaveImage, e20a7fb5-3d72-41c9-a78c-fdf287ec46ec]
patterns: []
missing: [e20a7fb5-3d72-41c9-a78c-fdf287ec46ec]
discoveries: [次要节点 `e20a7fb5-3d72-41c9-a78c-fdf287ec46ec` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/templates-subject_product_swap.app.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates-subject_product_swap.app.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `LoadImage`
- `LoadImage`
- `GeminiImage2Node`
- `SaveImage`
- `e20a7fb5-3d72-41c9-a78c-fdf287ec46ec`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`GeminiImage2Node`、`SaveImage`

**缺卡**（1）：`e20a7fb5-3d72-41c9-a78c-fdf287ec46ec`

**用到的条目**：LoadImage、SaveImage、GeminiImage2Node、sd15-t2i-basic、sd15-t2i-lora、node、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `e20a7fb5-3d72-41c9-a78c-fdf287ec46ec` 知识库中没有该节点类型的任何知识
