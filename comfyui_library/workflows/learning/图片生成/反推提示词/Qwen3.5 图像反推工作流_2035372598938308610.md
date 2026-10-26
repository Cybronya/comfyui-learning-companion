---
key: 图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json
name: Qwen3.5 图像反推工作流_2035372598938308610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json
hash: 645a718b962833b5
coverage: 0.875
learned_at: 2026-10-26 01:46:06
nodes: [llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, LoadImage, SaveImage, easy cleanGpuUsed, ShellAgentPluginOutputText]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `ShellAgentPluginOutputText`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`SaveImage`、`easy cleanGpuUsed`、`ShellAgentPluginOutputText`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、easy cleanGpuUsed、sd15-t2i-basic
