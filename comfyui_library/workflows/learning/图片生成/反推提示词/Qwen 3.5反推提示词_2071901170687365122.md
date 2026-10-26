---
key: 图片生成/反推提示词/Qwen 3.5反推提示词_2071901170687365122.json
name: Qwen 3.5反推提示词_2071901170687365122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen 3.5反推提示词_2071901170687365122.json
hash: 9cbd1eb97b3ab4a4
coverage: 0.833333
learned_at: 2026-10-26 01:45:49
nodes: [llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, PreviewAny, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen 3.5反推提示词_2071901170687365122.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen 3.5反推提示词_2071901170687365122.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（6 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
