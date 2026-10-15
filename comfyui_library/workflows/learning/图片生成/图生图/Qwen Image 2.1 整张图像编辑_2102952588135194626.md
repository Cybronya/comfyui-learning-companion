---
key: 图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json
name: Qwen Image 2.1 整张图像编辑_2102952588135194626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json
hash: e1e836ae176c978e
coverage: 0.894737
learned_at: 2026-10-15 22:25:11
nodes: [VAELoader, QwenPERewriteT8, easy showAnything, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, VAEDecode, easy cleanGpuUsed, EmptyLatentImage, ComfySwitchNode, LoadImage, ResolutionSelector, CR Prompt Text, SaveImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `QwenPERewriteT8`
- `easy showAnything`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `SaveImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`VAELoader`、`QwenPERewriteT8`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAEDecode`、`easy cleanGpuUsed`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`、`SaveImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
