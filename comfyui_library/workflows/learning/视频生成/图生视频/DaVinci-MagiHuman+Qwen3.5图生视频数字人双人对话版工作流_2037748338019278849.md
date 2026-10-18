---
key: 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json
name: DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json
hash: 1156d81ff45e29b7
coverage: 0.9
learned_at: 2026-10-15 22:35:58
nodes: [llama_cpp_model_loader, easy cleanGpuUsed, RH_MagiHumanModelLoader, RH_MagiHumanGenerate, llama_cpp_instruct_adv, PreviewAny, CR Prompt Text, JWInteger, SaveVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037748338019278849.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `RH_MagiHumanModelLoader`
- `RH_MagiHumanGenerate`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `CR Prompt Text`
- `JWInteger`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`llama_cpp_model_loader`、`easy cleanGpuUsed`、`RH_MagiHumanModelLoader`、`RH_MagiHumanGenerate`、`llama_cpp_instruct_adv`、`CR Prompt Text`、`JWInteger`、`SaveVideo`、`LoadImage`

**用到的条目**：LoadImage、CR Prompt Text、SaveVideo、llama_cpp_instruct_adv、llama_cpp_model_loader、JWInteger、RH_MagiHumanGenerate、RH_MagiHumanModelLoader
