---
key: 图片生成/反推提示词/Qwen3.5反推工作流_2029442960357593089.json
name: Qwen3.5反推工作流_2029442960357593089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5反推工作流_2029442960357593089.json
hash: a2849e51f63de19f
coverage: 0.8
learned_at: 2026-10-26 01:46:09
nodes: [LoadImage, llama_cpp_model_loader, llama_cpp_instruct_adv, easy saveText, PreviewAny]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5反推工作流_2029442960357593089.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5反推工作流_2029442960357593089.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewAny`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
