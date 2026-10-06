---
key: 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
name: qwen3.8-27B反推图片提示词_2104868396172140545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
hash: 82056363be76ca31
coverage: 0.666667
learned_at: 2026-10-06 22:27:38
nodes: [llama_cpp_model_loader, SaveImage, PreviewAny, easy saveText, llama_cpp_instruct_adv, LoadImage]
patterns: []
missing: [easy saveText]
discoveries: [次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
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

覆盖率 **67%**（4/6）

**有卡**：`llama_cpp_model_loader`、`SaveImage`、`llama_cpp_instruct_adv`、`LoadImage`

**缺卡**（1）：`easy saveText`

**用到的条目**：LoadImage、SaveImage、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、SaveText、Text

## 学习发现

- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
