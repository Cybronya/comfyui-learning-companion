---
key: 图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json
name: 千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json
hash: fdb062dd9cf9e398
coverage: 0.823529
learned_at: 2026-10-15 22:28:16
nodes: [ResolutionSelector, SaveImageAdvanced, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, SaveImage, VAEDecode, TextEncodeQwenImage21, Seed (rgthree), Note, Text Multiline, ShowText|pysssss, ShowText|pysssss, 忽略多组孤海, QwenPERewriteT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ResolutionSelector`
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `Note`
- `Text Multiline`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `忽略多组孤海`
- `QwenPERewriteT8`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ResolutionSelector`、`SaveImageAdvanced`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`Text Multiline`、`忽略多组孤海`、`QwenPERewriteT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
