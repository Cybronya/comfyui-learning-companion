---
key: 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json
name: Krea2 Turbo Realism Engineer V2文生图_2072187241404911618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json
hash: 9c7a7ead8df2586d
coverage: 0.76
learned_at: 2026-10-19 23:41:14
nodes: [SaveImage, EmptyLatentImage, MarkdownNote, CLIPLoader, MarkdownNote, MarkdownNote, StringConcatenate, PrimitiveStringMultiline, PreviewAny, TextGenerate, ResolutionSelector, VAELoader, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, KSampler, UNETLoader, LoraLoaderModelOnly, VAEDecode, VAEDecode, ImageConcanate, PrimitiveStringMultiline, SaveImage, ConditioningZeroOut]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1039245109574526, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `SaveImage`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextGenerate`
- `ResolutionSelector`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `PrimitiveStringMultiline`
- `SaveImage`
- `ConditioningZeroOut`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1039245109574526`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`SaveImage`、`EmptyLatentImage`、`CLIPLoader`、`StringConcatenate`、`TextGenerate`、`ResolutionSelector`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageConcanate`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
