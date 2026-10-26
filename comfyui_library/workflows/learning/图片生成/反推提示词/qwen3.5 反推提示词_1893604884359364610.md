---
key: 图片生成/反推提示词/qwen3.5 反推提示词_1893604884359364610.json
name: qwen3.5 反推提示词_1893604884359364610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推提示词_1893604884359364610.json
hash: 66c4516ddd0fae1f
coverage: 0.8
learned_at: 2026-10-26 01:47:00
nodes: [LoadImage, PreviewAny, llama_cpp_instruct_adv, llama_cpp_model_loader, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5 反推提示词_1893604884359364610.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5 反推提示词_1893604884359364610.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `LoadImage`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `easy saveText`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadImage`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
