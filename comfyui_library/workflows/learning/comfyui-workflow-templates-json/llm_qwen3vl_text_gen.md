---
key: comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json
name: llm_qwen3vl_text_gen
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json
hash: 212f5608ff9049a5
official: true
coverage: 0.6
learned_at: 2026-10-07 21:36:14
nodes: [CLIPLoader, TextGenerate, PreviewAny, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json`

## 结构

**生成流程**：Model → Other

**节点**（5 个）：
- `CLIPLoader`
- `TextGenerate`
- `PreviewAny`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`CLIPLoader`、`TextGenerate`、`LoadImage`

**用到的条目**：CLIPLoader、LoadImage、TextGenerate、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、ConditioningZeroOut
