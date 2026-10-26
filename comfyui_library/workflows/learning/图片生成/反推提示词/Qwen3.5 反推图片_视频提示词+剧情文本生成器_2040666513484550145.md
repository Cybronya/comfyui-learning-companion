---
key: 图片生成/反推提示词/Qwen3.5 反推图片_视频提示词+剧情文本生成器_2040666513484550145.json
name: Qwen3.5 反推图片_视频提示词+剧情文本生成器_2040666513484550145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 反推图片_视频提示词+剧情文本生成器_2040666513484550145.json
hash: 85f3292db34b3f0c
coverage: 0.777778
learned_at: 2026-10-26 01:46:05
nodes: [llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, easy saveText, LoadImage, llama_cpp_instruct_adv, PreviewAny, llama_cpp_model_loader, llama_cpp_parameters, easy saveText, Fast Groups Bypasser (rgthree), PreviewAny, llama_cpp_instruct_adv, easy saveText, VHS_LoadVideo]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 反推图片_视频提示词+剧情文本生成器_2040666513484550145.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 反推图片_视频提示词+剧情文本生成器_2040666513484550145.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（18 个）：
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy saveText`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `VHS_LoadVideo`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveText`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora
