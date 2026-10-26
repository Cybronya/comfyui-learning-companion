---
key: 图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频反推智能解析_2031700361131593729.json
name: Qwen3.5大模型，自动生成专业提示词｜视频反推智能解析_2031700361131593729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频反推智能解析_2031700361131593729.json
hash: a666aed69be31410
coverage: 0.875
learned_at: 2026-10-26 01:46:12
nodes: [llama_cpp_parameters, llama_cpp_model_loader, VHS_LoadVideo, llama_cpp_instruct_adv, SaveImage, easy saveText, PreviewAny, LoadImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频反推智能解析_2031700361131593729.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5大模型，自动生成专业提示词｜视频反推智能解析_2031700361131593729.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `VHS_LoadVideo`
- `llama_cpp_instruct_adv`
- `SaveImage`
- `easy saveText`
- `PreviewAny`
- `LoadImage`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`VHS_LoadVideo`、`llama_cpp_instruct_adv`、`SaveImage`、`easy saveText`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、sd15-t2i-basic
