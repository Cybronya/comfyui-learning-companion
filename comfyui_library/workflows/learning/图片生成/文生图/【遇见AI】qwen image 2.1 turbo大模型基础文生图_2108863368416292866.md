---
key: 图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json
name: 【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json
hash: bd3c913809e79334
coverage: 0.916667
learned_at: 2026-10-21 02:58:09
nodes: [ResolutionSelector, TextEncodeQwenImage21, EmptyLatentImage, KSampler, LoadImage, MarkdownNote, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1021305256448882, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1021305256448882`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
