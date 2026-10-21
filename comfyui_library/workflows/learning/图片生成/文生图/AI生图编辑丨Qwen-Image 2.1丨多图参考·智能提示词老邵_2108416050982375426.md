---
key: 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json
name: AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json
hash: 1ce32e5ffbde6dd0
coverage: 1
learned_at: 2026-10-20 01:50:21
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, VAEDecode, KSampler, QwenImage21Cache, CR Text, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 321063687819527, "steps": 25}
---

# 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `321063687819527`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`CR Text`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
