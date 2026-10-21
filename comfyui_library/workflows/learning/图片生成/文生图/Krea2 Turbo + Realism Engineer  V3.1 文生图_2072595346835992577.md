---
key: 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json
name: Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json
hash: 4d3bdcf208e8304a
coverage: 0.645833
learned_at: 2026-10-19 23:41:14
nodes: [MarkdownNote, KSampler, KSampler, VAEDecode, VAELoader, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, Reroute, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, LoadImage, CLIPTextEncode, ConditioningZeroOut, ResolutionSelector, EmptyLatentImage, SaveImage, VAEDecode, PrimitiveStringMultiline, SaveImage, PreviewImage, VAEDecode, KSampler, LoraLoaderModelOnly, ImageConcanate, PreviewImage, SaveImage, LoraLoaderModelOnly, PreviewImage, ImageConcanate, UNETLoader, PrimitiveStringMultiline, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 550094786376036, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `MarkdownNote`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Reroute`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ImageConcanate`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `550094786376036`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（31/48）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`ImageConcanate`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
