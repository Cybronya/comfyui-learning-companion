---
key: 图片生成/反推提示词/qwen3.5 反推提示词_2093708902130077698.json
name: qwen3.5 反推提示词_2093708902130077698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推提示词_2093708902130077698.json
hash: c2d1cd440cc08b7b
coverage: 0.8
learned_at: 2026-10-26 01:47:00
nodes: [LoadImage, llama_cpp_instruct_adv, llama_cpp_model_loader, easy saveText, PreviewAny]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5 反推提示词_2093708902130077698.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推提示词_2093708902130077698.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `easy saveText`
- `PreviewAny`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
