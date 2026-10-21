---
key: 图片生成/文生图/qwen2.1洗图_2107694512381456385.json
name: qwen2.1洗图_2107694512381456385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1洗图_2107694512381456385.json
hash: 9e3afd710f6207e4
coverage: 0.761905
learned_at: 2026-10-20 01:51:59
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, EmptyLatentImage, CLIPLoader, ResolutionSelector, QwenImage21Cache, VAELoader, LoadImage, ImageScaleToTotalPixels, KSampler, VAEEncode, VAEDecode, SaveImage, TextGenerate, SeedGenerator, PrimitiveStringMultiline, PreviewAny, TextEncodeQwenImage21]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 796516852314732, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen2.1洗图_2107694512381456385.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1洗图_2107694512381456385.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `QwenImage21Cache`
- `VAELoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TextGenerate`
- `SeedGenerator`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextEncodeQwenImage21`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `796516852314732`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`ResolutionSelector`、`QwenImage21Cache`、`VAELoader`、`LoadImage`、`ImageScaleToTotalPixels`、`KSampler`、`VAEEncode`、`VAEDecode`、`SaveImage`、`TextGenerate`、`SeedGenerator`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
