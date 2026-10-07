---
key: comfyui-workflow-templates-json/llm_qwen3_text_gen.json
name: llm_qwen3_text_gen
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/llm_qwen3_text_gen.json
hash: a63fe6fb7583ed0c
official: true
coverage: 0.4
learned_at: 2026-10-07 21:36:13
nodes: [TextGenerate, PreviewAny, MarkdownNote, CLIPLoader, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/llm_qwen3_text_gen.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/llm_qwen3_text_gen.json`

## 结构

**生成流程**：Model → Other

**节点**（5 个）：
- `TextGenerate`
- `PreviewAny`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`

## 知识

覆盖率 **40%**（2/5）

**有卡**：`TextGenerate`、`CLIPLoader`

**用到的条目**：CLIPLoader、TextGenerate、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、ConditioningZeroOut、CLIPLoaderGGUF
