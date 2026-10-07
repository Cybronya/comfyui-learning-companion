---
key: comfyui-workflow-templates-json/llm_gemma4_text_gen.json
name: llm_gemma4_text_gen
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/llm_gemma4_text_gen.json
hash: 2ffe86d2b809f2a2
official: true
coverage: 0.666667
learned_at: 2026-10-07 21:36:13
nodes: [CLIPLoader, LoadAudio, LoadImage, PreviewAny, TextGenerate, LoadVideo, GetVideoComponents, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/llm_gemma4_text_gen.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/llm_gemma4_text_gen.json`

## 结构

**生成流程**：Model → Other

**节点**（9 个）：
- `CLIPLoader`
- `LoadAudio`
- `LoadImage`
- `PreviewAny`
- `TextGenerate`
- `LoadVideo`
- `GetVideoComponents`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **67%**（6/9）

**有卡**：`CLIPLoader`、`LoadAudio`、`LoadImage`、`TextGenerate`、`LoadVideo`、`GetVideoComponents`

**用到的条目**：CLIPLoader、LoadImage、GetVideoComponents、LoadAudio、LoadVideo、TextGenerate、sd15-t2i-basic、sd15-t2i-lora
