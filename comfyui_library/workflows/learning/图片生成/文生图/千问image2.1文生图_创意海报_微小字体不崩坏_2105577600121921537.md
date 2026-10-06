---
key: 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json
name: 千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json
hash: 3c170b22da59f3da
coverage: 0.733333
learned_at: 2026-10-07 02:37:01
nodes: [CLIPLoader, ShowText|pysssss, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, Seed (rgthree), VAEDecode, SaveImageAdvanced, KSampler, SaveImage, 忽略多组孤海, QwenPERewriteT8, Text Multiline]
patterns: []
missing: [Text Multiline, 忽略多组孤海, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json`

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

覆盖率 **73%**（11/15）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`SaveImage`、`QwenPERewriteT8`

**缺卡**（3）：`Text Multiline`、`忽略多组孤海`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
