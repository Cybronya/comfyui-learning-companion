---
key: 图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json
name: Qwen image 2.1 文生图  T8版 加速_2105327796250828801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json
hash: e461b780b2680844
coverage: 0.9
learned_at: 2026-10-10 20:58:57
nodes: [CLIPLoader, VAELoader, VAEDecode, KSampler, QwenImage21Cache, SaveImage, UNETLoader, EmptyLatentImage, CLIPLoader, TextEncodeQwenImage21, ResolutionSelector, easy showAnything, TextGenerateLTX2Prompt, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImage21Cache, CR Text, UNETLoader, SaveImageAdvanced]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 731310669110862, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json`

## 结构

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode`
- `KSampler`
- `QwenImage21Cache`
- `SaveImage`
- `UNETLoader`
- `EmptyLatentImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImage21Cache`
- `CR Text`
- `UNETLoader`
- `SaveImageAdvanced`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `731310669110862`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`UNETLoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`easy showAnything`、`TextGenerateLTX2Prompt`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`CR Text`

**缺卡**（1）：`CR Text`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
