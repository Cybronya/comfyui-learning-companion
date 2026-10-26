---
key: 图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json
name: QWEN 3.5图像反推打标 lora训练助手_2044732074195689473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json
hash: bd589e59a1417534
coverage: 0.875
learned_at: 2026-10-26 01:45:48
nodes: [easy cleanGpuUsed, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, LoadImage, TextInput_, llama_cpp_instruct_adv, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `LoadImage`
- `TextInput_`
- `llama_cpp_instruct_adv`
- `easy saveText`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`TextInput_`、`llama_cpp_instruct_adv`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、TextInput_、easy cleanGpuUsed、sd15-t2i-basic
