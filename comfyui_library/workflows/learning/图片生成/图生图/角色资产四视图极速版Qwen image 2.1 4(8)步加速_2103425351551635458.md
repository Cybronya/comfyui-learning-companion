---
key: 图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json
name: 角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json
hash: c5e09aa955b3042f
coverage: 0.647059
learned_at: 2026-10-21 00:56:24
nodes: [CLIPLoader, SetNode, VAELoader, SetNode, SetNode, EmptyLatentImage, SaveImage, GetNode, GetNode, GetNode, VAEDecode, TextEncodeQwenImage21, QwenImage21Cache, UNETLoader, KSampler, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 473812199824826, "steps": 8, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `2048`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `473812199824826`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（11/17）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`UNETLoader`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
