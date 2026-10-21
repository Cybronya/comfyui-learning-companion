---
key: 图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json
name: Qwen Image 2.1透明图层+文生图！_2101836586576072706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json
hash: 20310b3e233caa4c
coverage: 0.818182
learned_at: 2026-10-20 01:51:03
nodes: [VAELoader, CLIPLoader, MarkdownNote, VAEDecode, EmptyLatentImage, TextEncodeQwenImage21, SaveImage, JjkText, UNETLoader, KSampler, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1090734849071299, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAELoader`
- `CLIPLoader`
- `MarkdownNote`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `JjkText`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1090734849071299`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImage`、`UNETLoader`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
