---
key: 图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json
name: Qwen image 2.1 文生图_2101866858684174338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json
hash: 7a955cef13bb68d8
coverage: 0.928571
learned_at: 2026-10-20 01:51:08
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CLIPLoader, VAELoader, CLIPLoader, easy showAnything, UNETLoader, SaveImage, KSampler, SeedGeneratorMira, TextGenerateLTX2Prompt, Int, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `UNETLoader` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SeedGeneratorMira`
- `TextGenerateLTX2Prompt`
- `Int`
- `Int`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`KSampler`、`SeedGeneratorMira`、`TextGenerateLTX2Prompt`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SeedGeneratorMira
