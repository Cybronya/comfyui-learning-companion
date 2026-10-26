---
key: 图片生成/反推提示词/Qwen3.5--图像反推_2035655088227753985.json
name: Qwen3.5--图像反推_2035655088227753985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5--图像反推_2035655088227753985.json
hash: 02018076cd7a4e76
coverage: 0.875
learned_at: 2026-10-26 01:46:07
nodes: [llama_cpp_model_loader, PreviewAny, easy cleanGpuUsed, llama_cpp_parameters, llama_cpp_instruct_adv, ShellAgentPluginOutputText, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5--图像反推_2035655088227753985.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5--图像反推_2035655088227753985.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `llama_cpp_model_loader`
- `PreviewAny`
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ShellAgentPluginOutputText`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`llama_cpp_model_loader`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ShellAgentPluginOutputText`、`LoadImage`、`SaveImage`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、easy cleanGpuUsed、sd15-t2i-basic
