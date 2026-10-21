---
key: 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json
name: 微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json
hash: 98bfc2839323fd8e
coverage: 0.857143
learned_at: 2026-10-20 01:52:30
nodes: [CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, Seed (rgthree), UNETLoader, VAELoader, KSampler, VAEDecode, ResolutionSelector, QwenPERewriteT8, ShowText|pysssss, SaveImage, SaveImageAdvanced, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 543544505961982, "steps": 25, "width": 1024}
---

# 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImageAdvanced`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `543544505961982`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`Seed (rgthree)`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
