---
key: 图片生成/文生图/qwen2.1文生图_2104275580962304002.json
name: qwen2.1文生图_2104275580962304002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1文生图_2104275580962304002.json
hash: 03e2c7ce7617bebc
coverage: 0.909091
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, VAELoader, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 331652005049054, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen2.1文生图_2104275580962304002.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1文生图_2104275580962304002.json`

## 结构

**节点**（11 个）：
- `ResolutionSelector`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `331652005049054`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`ComfySwitchNode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`VAELoader`、`CLIPLoader`
