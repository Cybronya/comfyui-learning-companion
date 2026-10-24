---
key: 图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json
name: Qwen image 2.1深度图-线稿-转图片_2112646802997596161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json
hash: f73ad0868e993f37
coverage: 0.833333
learned_at: 2026-10-23 11:14:11
nodes: [CLIPLoader, VAEDecode, KSampler, UNETLoader, StringToInt, StringToInt, EmptyLatentImage, VAELoader, QwenImage21UnionLoader, LoadImage, TextEncodeQwenImage21, Text, PrimitiveString, PrimitiveString, QwenImage21UnionApply, SaveImage, StringToInt, PrimitiveString]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 8, "width": 16}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `StringToInt`
- `StringToInt`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `QwenImage21UnionLoader`
- `LoadImage`
- `TextEncodeQwenImage21`
- `Text`
- `PrimitiveString`
- `PrimitiveString`
- `QwenImage21UnionApply`
- `SaveImage`
- `StringToInt`
- `PrimitiveString`

## 关键参数

- `seed` = `43`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `16`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`StringToInt`、`EmptyLatentImage`、`VAELoader`、`QwenImage21UnionLoader`、`LoadImage`、`TextEncodeQwenImage21`、`Text`、`QwenImage21UnionApply`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
