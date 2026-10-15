---
key: 图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json
name: 千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json
hash: 6c3c4d6e6a6d91f5
coverage: 0.542373
learned_at: 2026-10-15 22:25:47
nodes: [LoadImage, LoadImage, SaveImage, PreviewImage, VAELoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, TextEncodeQwenImage21, KSampler, JjkText, 孤海注释, 孤海注释, JjkText, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, UNETLoader, QwenImage21Cache, PlaySound|pysssss, ComfySwitchNode, UNETLoader, ResolutionSelector, 孤海注释, TextEncodeQwenImage21, VAEDecode, 孤海注释, easy int, easy int, 孤海注释, 孤海注释, LoadImage, Note, 孤海注释, JjkText, JjkText, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, 孤海注释, PreviewImage, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 588419230546023, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `JjkText`
- `孤海注释`
- `孤海注释`
- `JjkText`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `PlaySound|pysssss`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `孤海注释`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `孤海注释`
- `easy int`
- `easy int`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `Note`
- `孤海注释`
- `JjkText`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `588419230546023`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（32/59）

**有卡**：`LoadImage`、`SaveImage`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`PlaySound|pysssss`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`easy int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
