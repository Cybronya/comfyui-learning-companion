---
key: 图片生成/反推提示词/qwen3.5 反推、提示词助手_2033361496536784897.json
name: qwen3.5 反推、提示词助手_2033361496536784897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推、提示词助手_2033361496536784897.json
hash: 7fefccf63cfd4040
coverage: 0.714286
learned_at: 2026-10-26 01:47:00
nodes: [llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny, VHS_LoadVideo, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny, easy saveText, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, PreviewAny, llama_cpp_parameters, PrimitiveStringMultiline, LoadImage, llama_cpp_model_loader]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5 反推、提示词助手_2033361496536784897.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推、提示词助手_2033361496536784897.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（21 个）：
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `PreviewAny`
- `VHS_LoadVideo`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `PreviewAny`
- `easy saveText`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `LoadImage`
- `llama_cpp_model_loader`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`VHS_LoadVideo`、`easy saveText`、`LoadImage`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora
