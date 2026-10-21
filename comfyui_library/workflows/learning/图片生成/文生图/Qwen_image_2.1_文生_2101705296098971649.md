---
key: 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json
name: Qwen_image_2.1_文生_2101705296098971649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json
hash: 60289ae72d7184aa
coverage: 0.818182
learned_at: 2026-10-20 01:51:27
nodes: [UNETLoader, CLIPLoader, VAELoader, MarkdownNote, EmptyLatentImage, ResolutionSelector, VAEDecode, SaveImage, MarkdownNote, TextEncodeQwenImage21, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
