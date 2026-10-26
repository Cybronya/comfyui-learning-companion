---
key: 图片生成/反推提示词/Qwen3.5 强悍的图像反推工作流_2035648568308015105.json
name: Qwen3.5 强悍的图像反推工作流_2035648568308015105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 强悍的图像反推工作流_2035648568308015105.json
hash: 7ab03eeddec7afc0
coverage: 0.727273
learned_at: 2026-10-26 01:46:06
nodes: [llama_cpp_model_loader, easy cleanGpuUsed, llama_cpp_parameters, SaveImage, ShellAgentPluginOutputText, PreviewAny, llama_cpp_instruct_adv, LoadImage, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 强悍的图像反推工作流_2035648568308015105.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 强悍的图像反推工作流_2035648568308015105.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（11 个）：
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`llama_cpp_model_loader`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`SaveImage`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、easy cleanGpuUsed、sd15-t2i-basic
