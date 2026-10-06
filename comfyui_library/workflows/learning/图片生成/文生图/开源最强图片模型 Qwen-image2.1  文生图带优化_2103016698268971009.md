---
key: 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json
name: 开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json
hash: 5ffabda15585bdf0
coverage: 0.666667
learned_at: 2026-10-07 01:58:02
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, easy showAnything, CR Prompt List, String Literal, easy showAnything, Seed (rgthree), ImpactInt, ImpactInt, TextGenerateLTX2Prompt, CLIPLoader, SaveImage, CR Text]
patterns: []
missing: [CR Text, String Literal, CR Prompt List, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 539000317189143, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2103016698268971009.json`

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
- `seed` = `539000317189143`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（12/18）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`ImpactInt`、`TextGenerateLTX2Prompt`、`SaveImage`

**缺卡**（4）：`CR Text`、`String Literal`、`CR Prompt List`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、TextGenerateLTX2Prompt

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
