---
key: comfyui-workflow-templates-json/api_anthropic_claude_sonnet5.json
name: api_anthropic_claude_sonnet5
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_anthropic_claude_sonnet5.json
hash: a1fc38a914274dd8
official: true
coverage: 0.5
learned_at: 2026-10-07 21:33:16
nodes: [ClaudeNode, LoadImage, SaveText, PrimitiveStringMultiline, PreviewAny, 1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5]
patterns: []
missing: [1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5]
discoveries: [次要节点 `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/api_anthropic_claude_sonnet5.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_anthropic_claude_sonnet5.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `ClaudeNode`
- `LoadImage`
- `SaveText`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`ClaudeNode`、`LoadImage`、`SaveText`

**缺卡**（1）：`1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5`

**用到的条目**：LoadImage、SaveText、ClaudeNode、sd15-t2i-basic、sd15-t2i-lora、node、Text、String

## 学习发现

- 次要节点 `1d28f9d1-7c68-4b3b-99f5-2bf7fe0615c5` 知识库中没有该节点类型的任何知识
