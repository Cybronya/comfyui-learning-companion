---
key: comfyui-workflow-templates-json/api_openai_gpt6_astra.json
name: api_openai_gpt6_astra
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_gpt6_astra.json
hash: 6c13d4560ab3ef54
official: true
coverage: 0.5
learned_at: 2026-10-10 22:45:18
nodes: [LoadImage, SaveText, PrimitiveStringMultiline, PreviewAny, 1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5, OpenAIChatNode]
patterns: []
missing: [1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5]
discoveries: [次要节点 `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_openai_gpt6_astra.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_openai_gpt6_astra.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `LoadImage`
- `SaveText`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5`
- `OpenAIChatNode`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`LoadImage`、`SaveText`、`OpenAIChatNode`

**缺卡**（1）：`1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5`

**用到的条目**：LoadImage、SaveText、OpenAIChatNode、sd15-t2i-basic、sd15-t2i-lora、node、Text、String

## 学习发现

- 次要节点 `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5` 知识库中没有该节点类型的任何知识
