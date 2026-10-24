---
key: 图片生成/图生图/qwen3.8-27B反推图片提示词_2108738295046959106.json
name: qwen3.8-27B反推图片提示词_2108738295046959106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen3.8-27B反推图片提示词_2108738295046959106.json
hash: e655ef3d3a93b5fd
coverage: 0.714286
learned_at: 2026-10-23 11:43:36
nodes: [llama_cpp_model_loader, SaveImage, PreviewAny, easy saveText, LoadImage, llama_cpp_instruct_adv, JjkText]
patterns: []
missing: []
---

# 图片生成/图生图/qwen3.8-27B反推图片提示词_2108738295046959106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen3.8-27B反推图片提示词_2108738295046959106.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `llama_cpp_model_loader`
- `SaveImage`
- `PreviewAny`
- `easy saveText`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `JjkText`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`llama_cpp_model_loader`、`SaveImage`、`easy saveText`、`LoadImage`、`llama_cpp_instruct_adv`

**用到的条目**：LoadImage、SaveImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
