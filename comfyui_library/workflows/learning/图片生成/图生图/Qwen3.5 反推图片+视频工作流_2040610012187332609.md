---
key: 图片生成/图生图/Qwen3.5 反推图片+视频工作流_2040610012187332609.json
name: Qwen3.5 反推图片+视频工作流_2040610012187332609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3.5 反推图片+视频工作流_2040610012187332609.json
hash: c888b1c0d9301944
coverage: 0.736842
learned_at: 2026-10-23 11:19:47
nodes: [llama_cpp_parameters, llama_cpp_parameters, llama_cpp_model_loader, easy saveText, llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_model_loader, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), Note, PreviewAny, VHS_LoadVideo, llama_cpp_instruct_adv, llama_cpp_instruct_adv, easy saveText, easy saveText, LoadImage, PreviewAny]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen3.5 反推图片+视频工作流_2040610012187332609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3.5 反推图片+视频工作流_2040610012187332609.json`

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
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `easy saveText`
- `LoadImage`
- `PreviewAny`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy saveText`、`llama_cpp_instruct_adv`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora
