---
key: 图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2104117775550734338.json
name: 千问image2.1文生图 （创意海报 微小字体不崩坏）_2104117775550734338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2104117775550734338.json
hash: 6d43f6b569b0e58e
coverage: 0.928571
learned_at: 2026-10-15 22:28:16
nodes: [CLIPLoader, UNETLoader, VAELoader, TextEncodeQwenImage21, Seed (rgthree), VAEDecode, 忽略多组孤海, Text Multiline, StringConcatenate, KSampler, EmptySD3LatentImage, SaveImage, easy showAnything, RH_Captioner_Pro]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25}
---

# 图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2104117775550734338.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2104117775550734338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `忽略多组孤海`
- `Text Multiline`
- `StringConcatenate`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `easy showAnything`
- `RH_Captioner_Pro`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`VAEDecode`、`忽略多组孤海`、`Text Multiline`、`StringConcatenate`、`KSampler`、`EmptySD3LatentImage`、`SaveImage`、`RH_Captioner_Pro`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、UNETLoader、Seed (rgthree)、SaveImage
