---
key: 图片生成/反推提示词/给ComfyUI接入Qwen3.5大模型，自动生成专业提示词｜图片视频智能解析｜本地部署离线可用_2046685017111269377.json
name: 给ComfyUI接入Qwen3.5大模型，自动生成专业提示词｜图片视频智能解析｜本地部署离线可用_2046685017111269377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/给ComfyUI接入Qwen3.5大模型，自动生成专业提示词｜图片视频智能解析｜本地部署离线可用_2046685017111269377.json
hash: 96ee53b6e317bc9e
coverage: 0.8
learned_at: 2026-10-26 01:48:36
nodes: [llama_cpp_parameters, llama_cpp_parameters, llama_cpp_model_loader, easy saveText, easy saveText, llama_cpp_parameters, easy saveText, PreviewAny, Fast Groups Bypasser (rgthree), llama_cpp_model_loader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_instruct_adv, PreviewAny, llama_cpp_instruct_adv, Label (rgthree), Label (rgthree), LoadImage, VHS_LoadVideo, PreviewAny]
patterns: []
missing: []
---

# 图片生成/反推提示词/给ComfyUI接入Qwen3.5大模型，自动生成专业提示词｜图片视频智能解析｜本地部署离线可用_2046685017111269377.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/给ComfyUI接入Qwen3.5大模型，自动生成专业提示词｜图片视频智能解析｜本地部署离线可用_2046685017111269377.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（20 个）：
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `easy saveText`
- `easy saveText`
- `llama_cpp_parameters`
- `easy saveText`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `VHS_LoadVideo`
- `PreviewAny`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy saveText`、`llama_cpp_instruct_adv`、`Label (rgthree)`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、Label (rgthree)、sd15-t2i-basic
