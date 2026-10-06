---
key: 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
name: qwen3.8-27B反推图片提示词_2104868396172140545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json
hash: 82056363be76ca31
coverage: 0.333333
learned_at: 2026-10-06 21:37:37
nodes: [llama_cpp_model_loader, SaveImage, PreviewAny, easy saveText, llama_cpp_instruct_adv, LoadImage]
patterns: []
missing: [llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny, easy saveText]
discoveries: [次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `llama_cpp_model_loader`
- `SaveImage`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `LoadImage`

## 知识

覆盖率 **33%**（2/6）

**有卡**：`SaveImage`、`LoadImage`

**缺卡**（4）：`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`PreviewAny`、`easy saveText`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
