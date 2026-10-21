---
key: 图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json
name: （Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json
hash: 4e15101d8ef1f84b
coverage: 0.857143
learned_at: 2026-10-21 00:57:11
nodes: [Note, VAELoader, VAEDecode, Note, easy cleanGpuUsed, LoadImage, QwenPERewriteT8, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, PathchSageAttentionKJ, UNETLoader, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, LoraLoaderModelOnly, KSampler, CR Prompt Text, easy showAnything, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 5, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `Note`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `easy cleanGpuUsed`
- `LoadImage`
- `QwenPERewriteT8`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CR Prompt Text`
- `easy showAnything`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`LoadImage`、`QwenPERewriteT8`、`EmptyLatentImage`、`ResolutionSelector`、`PathchSageAttentionKJ`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`CR Prompt Text`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
