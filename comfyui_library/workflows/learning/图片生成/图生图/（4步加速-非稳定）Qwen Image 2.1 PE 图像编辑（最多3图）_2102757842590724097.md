---
key: 图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json
name: （4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json
hash: bf023149b2e56cac
coverage: 0.857143
learned_at: 2026-10-21 00:57:11
nodes: [Note, CLIPLoader, VAELoader, VAEDecode, Note, easy cleanGpuUsed, LoadImage, CR Prompt Text, QwenPERewriteT8, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, QwenImage21Cache, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `easy cleanGpuUsed`
- `LoadImage`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`

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

覆盖率 **86%**（24/28）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`LoadImage`、`CR Prompt Text`、`QwenPERewriteT8`、`EmptyLatentImage`、`ResolutionSelector`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
