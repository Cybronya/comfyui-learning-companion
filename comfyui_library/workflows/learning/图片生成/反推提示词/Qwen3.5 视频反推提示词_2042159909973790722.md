---
key: 图片生成/反推提示词/Qwen3.5 视频反推提示词_2042159909973790722.json
name: Qwen3.5 视频反推提示词_2042159909973790722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 视频反推提示词_2042159909973790722.json
hash: a22a12e204853337
coverage: 0.777778
learned_at: 2026-10-26 01:46:06
nodes: [PreviewAny, llama_cpp_instruct_adv, easy saveText, easy saveText, llama_cpp_parameters, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), llama_cpp_model_loader, PreviewAny, llama_cpp_model_loader, llama_cpp_parameters, easy saveText, LoadImage, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, VHS_LoadVideo, PreviewAny]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 视频反推提示词_2042159909973790722.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 视频反推提示词_2042159909973790722.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（18 个）：
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `easy saveText`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_model_loader`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy saveText`
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `VHS_LoadVideo`
- `PreviewAny`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`llama_cpp_instruct_adv`、`easy saveText`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora
