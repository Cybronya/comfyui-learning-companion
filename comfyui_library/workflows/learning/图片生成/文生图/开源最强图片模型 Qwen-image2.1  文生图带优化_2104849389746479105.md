---
key: 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json
name: 开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json
hash: 299ead2726554018
coverage: 0.571429
learned_at: 2026-10-10 20:59:43
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, easy showAnything, CR Prompt List, String Literal, easy showAnything, Seed (rgthree), MarkdownNote, Note Plus (mtb), 孤海注释, ImpactInt, ImpactInt, TextGenerateLTX2Prompt, CLIPLoader, SaveImage, CR Text]
patterns: []
missing: [CR Text, Note Plus (mtb), String Literal, CR Prompt List, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 279496845159360, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2104849389746479105.json`

## 结构

**节点**（21 个）：
- `UNETLoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `easy showAnything`
- `CR Prompt List`
- `String Literal`
- `easy showAnything`
- `Seed (rgthree)`
- `MarkdownNote`
- `Note Plus (mtb)`
- `孤海注释`
- `ImpactInt`
- `ImpactInt`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `SaveImage`
- `CR Text`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `279496845159360`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **57%**（12/21）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`easy showAnything`、`CR Prompt List`、`String Literal`、`Seed (rgthree)`

**缺卡**（5）：`CR Text`、`Note Plus (mtb)`、`String Literal`、`CR Prompt List`、`Seed (rgthree)`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
