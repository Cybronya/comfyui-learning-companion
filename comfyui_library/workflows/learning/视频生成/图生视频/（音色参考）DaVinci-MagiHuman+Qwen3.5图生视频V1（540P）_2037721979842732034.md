---
key: 视频生成/图生视频/（音色参考）DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037721979842732034.json
name: （音色参考）DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037721979842732034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037721979842732034.json
hash: f066d6cfc275ba84
coverage: 0.909091
learned_at: 2026-10-15 22:35:58
nodes: [llama_cpp_model_loader, easy cleanGpuUsed, SaveVideo, RH_MagiHumanModelLoader, PreviewAny, JWInteger, llama_cpp_instruct_adv, CR Prompt Text, RH_MagiHumanGenerate, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/（音色参考）DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037721979842732034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037721979842732034.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（11 个）：
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `SaveVideo`
- `RH_MagiHumanModelLoader`
- `PreviewAny`
- `JWInteger`
- `llama_cpp_instruct_adv`
- `CR Prompt Text`
- `RH_MagiHumanGenerate`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`llama_cpp_model_loader`、`easy cleanGpuUsed`、`SaveVideo`、`RH_MagiHumanModelLoader`、`JWInteger`、`llama_cpp_instruct_adv`、`CR Prompt Text`、`RH_MagiHumanGenerate`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、CR Prompt Text、SaveVideo、llama_cpp_instruct_adv、llama_cpp_model_loader、LoadAudio、JWInteger、RH_MagiHumanGenerate
