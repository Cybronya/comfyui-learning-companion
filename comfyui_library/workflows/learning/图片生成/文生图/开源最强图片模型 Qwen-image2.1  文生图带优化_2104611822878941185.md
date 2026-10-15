---
key: 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json
name: 开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json
hash: 75381f88a2be61a4
coverage: 0.75
learned_at: 2026-10-10 20:59:43
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, easy showAnything, Seed (rgthree), ImpactInt, ImpactInt, TextGenerateLTX2Prompt, CLIPLoader, SaveImage, 孤海注释, CR Text]
patterns: []
missing: [CR Text, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 761864581797680, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104611822878941185.json`

## 结构

**节点**（16 个）：
- `UNETLoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `easy showAnything`
- `Seed (rgthree)`
- `ImpactInt`
- `ImpactInt`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `SaveImage`
- `孤海注释`
- `CR Text`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `761864581797680`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`easy showAnything`、`Seed (rgthree)`、`ImpactInt`、`TextGenerateLTX2Prompt`

**缺卡**（2）：`CR Text`、`Seed (rgthree)`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
