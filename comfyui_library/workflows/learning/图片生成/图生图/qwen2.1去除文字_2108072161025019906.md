---
key: 图片生成/图生图/qwen2.1去除文字_2108072161025019906.json
name: qwen2.1去除文字_2108072161025019906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1去除文字_2108072161025019906.json
hash: 55bb00a89b24742d
coverage: 0.9
learned_at: 2026-10-21 00:46:10
nodes: [Anything Everywhere3, UNETLoader, CLIPLoader, KSampler, TextEncodeQwenImage21, VAEDecode, LoadImage, Text, SaveImage, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 433112160729119, "steps": 25}
---

# 图片生成/图生图/qwen2.1去除文字_2108072161025019906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1去除文字_2108072161025019906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `Text`
- `SaveImage`
- `VAELoader`

## 关键参数

- `seed` = `433112160729119`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`UNETLoader`、`CLIPLoader`、`KSampler`、`TextEncodeQwenImage21`、`VAEDecode`、`LoadImage`、`Text`、`SaveImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage
