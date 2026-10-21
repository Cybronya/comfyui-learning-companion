---
key: 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json
name: AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json
hash: 92cb211686aff2d5
coverage: 1
learned_at: 2026-10-20 01:50:21
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, VAEDecode, KSampler, QwenImage21Cache, SaveImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1058443119655735, "steps": 25}
---

# 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `1058443119655735`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
