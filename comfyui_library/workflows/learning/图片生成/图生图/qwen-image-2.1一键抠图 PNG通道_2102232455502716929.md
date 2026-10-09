---
key: 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json
name: qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json
hash: fd0c59e37a0f3bbc
coverage: 1
learned_at: 2026-10-09 22:27:10
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, SaveImage, SaveImageAdvanced, KSampler, UNETLoader, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 306436481644757, "steps": 25}
---

# 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102232455502716929.json`

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

- `seed` = `306436481644757`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
