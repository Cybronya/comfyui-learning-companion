---
key: 平台全量/qwen-image-2.1一键抠图 PNG通道_2102019029182537730.json
name: qwen-image-2.1一键抠图 PNG通道_2102019029182537730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image-2.1一键抠图 PNG通道_2102019029182537730.json
hash: 4593350971805c32
coverage: 1
learned_at: 2026-11-14 01:16:16
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, SaveImage, SaveImageAdvanced, KSampler, UNETLoader, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 691802214833894, "steps": 25}
---

# 平台全量/qwen-image-2.1一键抠图 PNG通道_2102019029182537730.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image-2.1一键抠图 PNG通道_2102019029182537730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `691802214833894`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
