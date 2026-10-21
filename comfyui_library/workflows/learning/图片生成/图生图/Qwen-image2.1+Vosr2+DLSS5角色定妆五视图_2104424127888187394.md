---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json
hash: 3d69ecf4c82f73bc
coverage: 0.923077
learned_at: 2026-10-21 00:43:23
nodes: [CLIPLoader, VAELoader, UNETLoader, ResolutionSelector, SaveImage, PreviewImage, TextEncodeQwenImage21, EmptyLatentImage, LoadImage, VAEDecode, KSampler, CR Prompt Text, WujiUpscaler2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 904, "sampler_name": "euler", "scheduler": "simple", "seed": 206372127852617, "steps": 8, "width": 1560}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `SaveImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CR Prompt Text`
- `WujiUpscaler2`

## 关键参数

- `width` = `1560`
- `height` = `904`
- `batch_size` = `1`
- `seed` = `206372127852617`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ResolutionSelector`、`SaveImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`VAEDecode`、`KSampler`、`CR Prompt Text`、`WujiUpscaler2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
