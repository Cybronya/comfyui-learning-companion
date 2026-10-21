---
key: 图片生成/文生图/Qwen-Image-2.1透明图层（文生图）_2109536947332014082.json
name: Qwen-Image-2.1透明图层（文生图）_2109536947332014082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1透明图层（文生图）_2109536947332014082.json
hash: 9906b2561dd1439f
coverage: 0.9
learned_at: 2026-10-21 02:54:29
nodes: [CLIPLoader, SaveImage, JjkText, UNETLoader, VAELoader, ResolutionSelector, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 768443443158330, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1透明图层（文生图）_2109536947332014082.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1透明图层（文生图）_2109536947332014082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `SaveImage`
- `JjkText`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `768443443158330`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`SaveImage`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
