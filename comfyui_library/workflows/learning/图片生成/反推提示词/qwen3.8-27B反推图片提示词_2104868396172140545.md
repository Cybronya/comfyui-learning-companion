---
key: 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
name: qwen3.8-27B反推图片提示词_2104868396172140545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
hash: 82056363be76ca31
coverage: 0.833333
learned_at: 2026-10-15 22:25:03
nodes: [llama_cpp_model_loader, SaveImage, PreviewAny, easy saveText, llama_cpp_instruct_adv, LoadImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（6 个）：
- `llama_cpp_model_loader`
- `SaveImage`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `LoadImage`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`llama_cpp_model_loader`、`SaveImage`、`easy saveText`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、SaveText
