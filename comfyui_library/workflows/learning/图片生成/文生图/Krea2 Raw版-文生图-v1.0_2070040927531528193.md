---
key: 图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json
name: Krea2 Raw版-文生图-v1.0_2070040927531528193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json
hash: e633c65624ffe5b1
coverage: 0.5
learned_at: 2026-10-19 23:41:13
nodes: [VAEDecode, PrimitiveStringMultiline, UNETLoader, CLIPLoader, CLIPTextEncode, KSampler, VAELoader, StringConcatenate, easy showAnything, CLIPTextEncode, PreviewAny, SaveImage, EmptyLatentImage, 孤海注释, MarkdownNote, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, TextGenerate, 孤海注释, MarkdownNote, 孤海注释, MarkdownNote, PrimitiveStringMultiline, ResolutionSelector]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 545388956008555, "steps": 28, "width": 1024}
---

# 图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `StringConcatenate`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `孤海注释`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextGenerate`
- `孤海注释`
- `MarkdownNote`
- `孤海注释`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `ResolutionSelector`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `545388956008555`
- `steps` = `28`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（13/26）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`StringConcatenate`、`SaveImage`、`EmptyLatentImage`、`LoadImage`、`TextGenerate`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
