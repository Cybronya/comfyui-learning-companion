---
key: 图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json
name: 千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json
hash: 380eb7a6daff1b6a
coverage: 0.733333
learned_at: 2026-10-10 20:59:38
nodes: [CLIPLoader, ShowText|pysssss, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, Seed (rgthree), VAEDecode, SaveImageAdvanced, KSampler, SaveImage, 忽略多组孤海, QwenPERewriteT8, Text Multiline]
patterns: []
missing: [Text Multiline, 忽略多组孤海, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json`

## 结构

**节点**（15 个）：
- `CLIPLoader`
- `ShowText|pysssss`
- `UNETLoader`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `VAEDecode`
- `SaveImageAdvanced`
- `KSampler`
- `SaveImage`
- `忽略多组孤海`
- `QwenPERewriteT8`
- `Text Multiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`CLIPLoader`、`ShowText|pysssss`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`

**缺卡**（3）：`Text Multiline`、`忽略多组孤海`、`Seed (rgthree)`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
