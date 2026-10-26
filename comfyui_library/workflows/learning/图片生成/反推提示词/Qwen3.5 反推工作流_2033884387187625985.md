---
key: 图片生成/反推提示词/Qwen3.5 反推工作流_2033884387187625985.json
name: Qwen3.5 反推工作流_2033884387187625985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 反推工作流_2033884387187625985.json
hash: aab3d84b407f3584
coverage: 0.736842
learned_at: 2026-10-26 01:46:05
nodes: [llama_cpp_parameters, llama_cpp_parameters, llama_cpp_model_loader, easy saveText, llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_model_loader, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), Note, PreviewAny, VHS_LoadVideo, LoadImage, llama_cpp_instruct_adv, llama_cpp_instruct_adv, easy saveText, PreviewAny, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 反推工作流_2033884387187625985.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 反推工作流_2033884387187625985.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（19 个）：
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `easy saveText`
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `PreviewAny`
- `VHS_LoadVideo`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewAny`
- `easy saveText`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy saveText`、`llama_cpp_instruct_adv`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora
