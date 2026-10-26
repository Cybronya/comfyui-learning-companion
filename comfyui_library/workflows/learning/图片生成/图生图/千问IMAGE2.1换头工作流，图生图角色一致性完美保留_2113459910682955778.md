---
key: 图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778.json
name: 千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778.json
hash: f1f2e2e70cafd7de
coverage: 0.911111
learned_at: 2026-10-26 22:05:30
nodes: [VAEDecode, VAELoader, CLIPLoader, GetImageSize, EmptyLatentImage, SaveImage, PrimitiveStringMultiline, StringConcatenate, CLIPLoader, TextGenerate, TextEncodeQwenImage21, LoadImage, LoadImage, UNETLoader, KSampler, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `CLIPLoader`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **91%**（41/45）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`GetImageSize`、`EmptyLatentImage`、`SaveImage`、`StringConcatenate`、`TextGenerate`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
