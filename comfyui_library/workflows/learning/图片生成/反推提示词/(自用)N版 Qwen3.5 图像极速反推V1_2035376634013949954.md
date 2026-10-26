---
key: 图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json
name: (自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json
hash: 9d2982236e202e44
coverage: 0.888889
learned_at: 2026-10-26 01:43:55
nodes: [llama_cpp_parameters, llama_cpp_model_loader, SaveImage, LoadImage, LoadImage, llama_cpp_instruct_adv, PreviewAny, easy cleanGpuUsed, ShellAgentPluginOutputText]
patterns: []
missing: []
---

# 图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `easy cleanGpuUsed`
- `ShellAgentPluginOutputText`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`SaveImage`、`LoadImage`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`ShellAgentPluginOutputText`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、easy cleanGpuUsed、sd15-t2i-basic
