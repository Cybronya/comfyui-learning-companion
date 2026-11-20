---
key: 图片生成/文生图/Qwen2.1文生图基础版_2114728415977889793.json
name: Qwen2.1文生图基础版_2114728415977889793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图基础版_2114728415977889793.json
hash: 434c22293e5f7870
coverage: 1
learned_at: 2026-10-30 17:55:20
nodes: [EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, VAEDecode, SaveImage, TextEncodeQwenImage21, CR Prompt Text, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 955731299973913, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图基础版_2114728415977889793.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图基础版_2114728415977889793.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `955731299973913`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`CR Prompt Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
