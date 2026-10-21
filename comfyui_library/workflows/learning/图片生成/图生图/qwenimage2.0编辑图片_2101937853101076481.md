---
key: 图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json
name: qwenimage2.0编辑图片_2101937853101076481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json
hash: 940f5f25570331a8
coverage: 1
learned_at: 2026-10-21 00:46:24
nodes: [KSampler, QwenImage21Cache, SaveImage, LoadImage, TextEncodeQwenImage21, VAEDecode, VAELoader, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 239633149664965, "steps": 25}
---

# 图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（9 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `239633149664965`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`KSampler`、`QwenImage21Cache`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
