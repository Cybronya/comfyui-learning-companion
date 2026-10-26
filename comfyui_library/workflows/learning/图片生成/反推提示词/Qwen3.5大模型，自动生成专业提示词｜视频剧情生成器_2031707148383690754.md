---
key: 图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频剧情生成器_2031707148383690754.json
name: Qwen3.5大模型，自动生成专业提示词｜视频剧情生成器_2031707148383690754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频剧情生成器_2031707148383690754.json
hash: 6e550dbd5afdcdc8
coverage: 0.75
learned_at: 2026-10-26 01:46:11
nodes: [SaveImage, LoadImage, PreviewAny, easy saveText, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, JjkText]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频剧情生成器_2031707148383690754.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频剧情生成器_2031707148383690754.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `JjkText`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`SaveImage`、`LoadImage`、`easy saveText`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`

**用到的条目**：LoadImage、SaveImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、sd15-t2i-basic、sd15-t2i-lora
