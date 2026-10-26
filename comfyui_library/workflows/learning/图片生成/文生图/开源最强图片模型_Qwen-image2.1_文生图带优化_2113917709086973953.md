---
key: 图片生成/文生图/开源最强图片模型_Qwen-image2.1_文生图带优化_2113917709086973953.json
name: 开源最强图片模型_Qwen-image2.1_文生图带优化_2113917709086973953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强图片模型_Qwen-image2.1_文生图带优化_2113917709086973953.json
hash: 60254ca551edecd7
coverage: 0.888889
learned_at: 2026-10-26 22:09:35
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, easy showAnything, CR Prompt List, String Literal, easy showAnything, Seed (rgthree), ImpactInt, ImpactInt, TextGenerateLTX2Prompt, CLIPLoader, SaveImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 409105136703499, "steps": 50, "width": 1024}
---

# 图片生成/文生图/开源最强图片模型_Qwen-image2.1_文生图带优化_2113917709086973953.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强图片模型_Qwen-image2.1_文生图带优化_2113917709086973953.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `CR Prompt List`
- `String Literal`
- `easy showAnything`
- `Seed (rgthree)`
- `ImpactInt`
- `ImpactInt`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `SaveImage`
- `CR Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `409105136703499`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CR Prompt List`、`String Literal`、`Seed (rgthree)`、`ImpactInt`、`TextGenerateLTX2Prompt`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、Seed (rgthree)
