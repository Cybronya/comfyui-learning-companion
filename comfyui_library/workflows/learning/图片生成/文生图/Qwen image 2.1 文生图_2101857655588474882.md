---
key: 图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json
name: Qwen image 2.1 文生图_2101857655588474882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json
hash: dd9d86d6e8ce9dbc
coverage: 1
learned_at: 2026-10-20 01:51:08
nodes: [VAEDecode, EmptyLatentImage, KSampler, TextEncodeQwenImage21, CLIPLoader, UNETLoader, VAELoader, ResolutionSelector, CR Prompt Text, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 840241061336068, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `CR Prompt Text`
- `SaveImage`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `840241061336068`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`CR Prompt Text`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
