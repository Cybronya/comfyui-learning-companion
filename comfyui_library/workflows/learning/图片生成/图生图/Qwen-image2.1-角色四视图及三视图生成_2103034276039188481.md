---
key: 图片生成/图生图/Qwen-image2.1-角色四视图及三视图生成_2103034276039188481.json
name: Qwen-image2.1-角色四视图及三视图生成_2103034276039188481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-角色四视图及三视图生成_2103034276039188481.json
hash: 17356b708c3e6d1c
coverage: 0.846154
learned_at: 2026-10-21 00:43:28
nodes: [CLIPLoader, SaveImage, VAEDecode, UNETLoader, LoraLoaderModelOnly, VAELoader, TextEncodeQwenImage21, KSampler, LoadImage, PreviewImage, Note, EmptyLatentImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 904, "sampler_name": "euler", "scheduler": "simple", "seed": 318096561589914, "steps": 6, "width": 1560}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1-角色四视图及三视图生成_2103034276039188481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-角色四视图及三视图生成_2103034276039188481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoadImage`
- `PreviewImage`
- `Note`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `318096561589914`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1560`
- `height` = `904`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPLoader`、`SaveImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`LoadImage`、`EmptyLatentImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
