---
key: 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json
name: 千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json
hash: 2418c59b8de54585
coverage: 0.933333
learned_at: 2026-10-20 01:52:21
nodes: [CLIPLoader, ShowText|pysssss, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, Seed (rgthree), VAEDecode, SaveImageAdvanced, KSampler, SaveImage, 忽略多组孤海, QwenPERewriteT8, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `KSampler` ★核心
- `SaveImage`
- `忽略多组孤海`
- `QwenPERewriteT8`
- `Text Multiline`

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

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`SaveImage`、`忽略多组孤海`、`QwenPERewriteT8`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
