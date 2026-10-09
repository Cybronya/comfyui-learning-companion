---
key: 图片生成/图生图/qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json
name: qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json
hash: f85e0bbb7675c42e
coverage: 0.916667
learned_at: 2026-10-09 22:27:11
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, SaveImageAdvanced, KSampler, UNETLoader, TextEncodeQwenImage21, LoadImage, SaveImage, VAEDecode, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 914604142516591, "steps": 25}
---

# 图片生成/图生图/qwen-image-2.1一键抠图_PNG通道_2102319407006572545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102319407006572545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `914604142516591`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`SaveImageAdvanced`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`VAEDecode`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
