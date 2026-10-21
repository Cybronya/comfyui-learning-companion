---
key: 图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json
name: qwen-image-2.1图生图（三套夏装)_2107744199545278466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json
hash: e016ff5d486f52a5
coverage: 1
learned_at: 2026-10-21 00:46:07
nodes: [UNETLoader, CLIPLoader, VAEDecode, LoadImage, VAELoader, QwenImage21Cache, SaveImage, KSampler, CR Text, CR Text, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 159510016152772, "steps": 20}
---

# 图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `VAELoader`
- `QwenImage21Cache`
- `SaveImage`
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `159510016152772`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`LoadImage`、`VAELoader`、`QwenImage21Cache`、`SaveImage`、`KSampler`、`CR Text`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
