---
key: 视频生成/图生视频/开源界的seedance最强模型daVinci-MagiHuman_2037761306891128833.json
name: 开源界的seedance最强模型daVinci-MagiHuman_2037761306891128833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/开源界的seedance最强模型daVinci-MagiHuman_2037761306891128833.json
hash: c05fe9c4f127dcac
coverage: 0.875
learned_at: 2026-10-15 22:35:58
nodes: [easy cleanGpuUsed, LoadImage, llama_cpp_model_loader, llama_cpp_instruct_adv, RH_MagiHumanModelLoader, SaveVideo, PreviewAny, RH_MagiHumanGenerate]
patterns: []
missing: []
---

# 视频生成/图生视频/开源界的seedance最强模型daVinci-MagiHuman_2037761306891128833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037761306891128833.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `easy cleanGpuUsed`
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `RH_MagiHumanModelLoader`
- `SaveVideo`
- `PreviewAny`
- `RH_MagiHumanGenerate`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`easy cleanGpuUsed`、`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`RH_MagiHumanModelLoader`、`SaveVideo`、`RH_MagiHumanGenerate`

**用到的条目**：LoadImage、SaveVideo、llama_cpp_instruct_adv、llama_cpp_model_loader、RH_MagiHumanGenerate、RH_MagiHumanModelLoader、easy cleanGpuUsed、sd15-t2i-basic
