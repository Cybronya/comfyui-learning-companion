---
key: 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037446558546927617.json
name: DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037446558546927617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037446558546927617.json
hash: cb18ceca6e3d5faa
coverage: 0.9
learned_at: 2026-10-15 22:35:57
nodes: [llama_cpp_model_loader, LoadImage, easy cleanGpuUsed, SaveVideo, RH_MagiHumanModelLoader, PreviewAny, RH_MagiHumanGenerate, JWInteger, llama_cpp_instruct_adv, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037446558546927617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037446558546927617.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `llama_cpp_model_loader`
- `LoadImage`
- `easy cleanGpuUsed`
- `SaveVideo`
- `RH_MagiHumanModelLoader`
- `PreviewAny`
- `RH_MagiHumanGenerate`
- `JWInteger`
- `llama_cpp_instruct_adv`
- `CR Prompt Text`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`llama_cpp_model_loader`、`LoadImage`、`easy cleanGpuUsed`、`SaveVideo`、`RH_MagiHumanModelLoader`、`RH_MagiHumanGenerate`、`JWInteger`、`llama_cpp_instruct_adv`、`CR Prompt Text`

**用到的条目**：LoadImage、CR Prompt Text、SaveVideo、llama_cpp_instruct_adv、llama_cpp_model_loader、JWInteger、RH_MagiHumanGenerate、RH_MagiHumanModelLoader
