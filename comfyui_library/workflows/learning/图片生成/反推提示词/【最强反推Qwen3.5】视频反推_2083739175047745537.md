---
key: 图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json
name: 【最强反推Qwen3.5】视频反推_2083739175047745537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json
hash: 076ad73da63d11c9
coverage: 0.782609
learned_at: 2026-10-26 01:47:12
nodes: [llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, GetVideoComponents, llama_cpp_parameters, LoadImage, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_model_loader, easy cleanGpuUsed, PreviewAny, easy saveText, easy saveText, easy cleanGpuUsed, easy saveText, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LoadVideo]
patterns: []
missing: []
---

# 图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（23 个）：
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `GetVideoComponents`
- `llama_cpp_parameters`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `easy cleanGpuUsed`
- `easy saveText`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoadVideo`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`GetVideoComponents`、`LoadImage`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`easy saveText`、`LoadVideo`

**用到的条目**：LoadImage、easy saveText、GetVideoComponents、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、LoadVideo、easy cleanGpuUsed
